from pathlib import Path
from datetime import datetime
import hashlib
import json
import re
import sys

import requests
from bs4 import BeautifulSoup


# Project folders
ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
DOCS_DIR = ROOT_DIR / "docs"
SNAPSHOT_DIR = ROOT_DIR / "source_snapshots"

REPORT_FILE = DOCS_DIR / "source_watch_report.md"
STATE_FILE = SNAPSHOT_DIR / "source_watch_state.json"

REQUEST_TIMEOUT_SECONDS = 20

USER_AGENT = (
    "CyberLex-Sweden-Source-Watch/1.0 "
    "(educational source monitoring prototype)"
)


def read_markdown_file(file_path):
    """Read a Markdown file safely."""
    return file_path.read_text(encoding="utf-8")


def clean_url(url):
    """
    Clean a URL extracted from Markdown.

    This removes common trailing characters from Markdown or punctuation.
    """
    return str(url or "").strip().rstrip(").,;]")


def extract_section(content, heading):
    """
    Extract a Markdown section by heading.

    This supports headings such as:
    ## Official source
    ### Official source
    #### Official source
    """
    pattern = rf"^#{{2,6}}\s+{re.escape(heading)}\s*$([\s\S]*?)(?=^#{{2,6}}\s+|\Z)"
    match = re.search(pattern, content, flags=re.IGNORECASE | re.MULTILINE)

    if not match:
        return ""

    return match.group(1).strip()


def extract_urls_from_text(text):
    """
    Extract URLs from Markdown links and raw URLs.

    Supported examples:
    [IMY: Example](https://www.imy.se/)
    https://www.imy.se/
    """
    urls = []

    markdown_links = re.findall(r"\[[^\]]+\]\((https?://[^)]+)\)", text)
    raw_links = re.findall(r"https?://[^\s)]+", text)

    urls.extend(markdown_links)
    urls.extend(raw_links)

    cleaned_urls = []
    seen = set()

    for url in urls:
        cleaned = clean_url(url)

        if cleaned and cleaned not in seen:
            cleaned_urls.append(cleaned)
            seen.add(cleaned)

    return cleaned_urls


def extract_official_source_urls(file_path):
    """
    Extract official source URLs from the Official source section.

    If no Official source section exists, this returns an empty list.
    """
    content = read_markdown_file(file_path)
    official_source_section = extract_section(content, "Official source")

    if not official_source_section:
        return []

    return extract_urls_from_text(official_source_section)


def load_previous_state():
    """
    Load previous source watch state.

    If no previous state exists, return an empty state.
    """
    if not STATE_FILE.exists():
        return {
            "version": 1,
            "sources": {},
        }

    try:
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {
            "version": 1,
            "sources": {},
            "state_warning": "Previous state file existed but could not be decoded.",
        }


def save_state(state):
    """Save source watch state as formatted JSON."""
    SNAPSHOT_DIR.mkdir(exist_ok=True)
    STATE_FILE.write_text(
        json.dumps(state, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def normalize_page_text(html_text):
    """
    Convert HTML into normalized readable text for hashing.

    This intentionally removes script, style, and navigation noise where possible.
    The goal is not perfect legal parsing. The goal is detecting meaningful page changes.
    """
    soup = BeautifulSoup(html_text, "html.parser")

    for tag in soup(["script", "style", "noscript", "svg"]):
        tag.decompose()

    text = soup.get_text(separator=" ")
    text = re.sub(r"\s+", " ", text)
    text = text.strip()

    return text


def hash_text(text):
    """Create a SHA-256 hash from normalized text."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def fetch_url(url):
    """
    Fetch a URL and return a result dictionary.

    This function does not raise for normal HTTP errors.
    It returns a structured result instead so the report can explain what happened.
    """
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=REQUEST_TIMEOUT_SECONDS,
            allow_redirects=True,
        )

        status_code = response.status_code
        final_url = response.url

        if status_code >= 400:
            return {
                "ok": False,
                "url": url,
                "final_url": final_url,
                "status_code": status_code,
                "error": f"HTTP error {status_code}",
                "content_hash": "",
                "content_length": 0,
            }

        content_type = response.headers.get("Content-Type", "")

        if "text/html" in content_type or "application/xhtml+xml" in content_type:
            normalized_text = normalize_page_text(response.text)
        else:
            # For PDFs and other source types, hash raw bytes.
            # This allows change detection even when text extraction is not available.
            normalized_text = response.content.decode("utf-8", errors="ignore")

        content_hash = hash_text(normalized_text)

        return {
            "ok": True,
            "url": url,
            "final_url": final_url,
            "status_code": status_code,
            "error": "",
            "content_hash": content_hash,
            "content_length": len(normalized_text),
        }

    except requests.RequestException as error:
        return {
            "ok": False,
            "url": url,
            "final_url": "",
            "status_code": "",
            "error": str(error),
            "content_hash": "",
            "content_length": 0,
        }


def classify_source_status(previous_entry, current_result):
    """
    Compare previous and current source result.

    Possible statuses:
    - First snapshot
    - Unchanged
    - Changed
    - Failed
    """
    if not current_result["ok"]:
        return "Failed"

    if not previous_entry:
        return "First snapshot"

    previous_hash = previous_entry.get("content_hash", "")

    if not previous_hash:
        return "First snapshot"

    if previous_hash == current_result["content_hash"]:
        return "Unchanged"

    return "Changed"


def collect_source_urls():
    """
    Collect official source URLs from all Markdown files in data/.
    """
    if not DATA_DIR.exists():
        raise FileNotFoundError(f"Data folder not found: {DATA_DIR}")

    markdown_files = sorted(DATA_DIR.glob("*.md"))

    if not markdown_files:
        raise FileNotFoundError(f"No Markdown files found in: {DATA_DIR}")

    collected = []

    for file_path in markdown_files:
        urls = extract_official_source_urls(file_path)

        for url in urls:
            collected.append(
                {
                    "source_file": file_path.name,
                    "source_path": str(file_path.relative_to(ROOT_DIR)),
                    "url": url,
                }
            )

    return collected


def run_source_watch():
    """
    Check official source URLs online and detect possible changes.

    This does not update CyberLex knowledge files.
    It only creates a monitoring report and a local hash state.
    """
    DOCS_DIR.mkdir(exist_ok=True)
    SNAPSHOT_DIR.mkdir(exist_ok=True)

    previous_state = load_previous_state()
    previous_sources = previous_state.get("sources", {})

    collected_sources = collect_source_urls()

    results = []
    new_sources_state = {}

    checked_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for item in collected_sources:
        source_file = item["source_file"]
        source_path = item["source_path"]
        url = item["url"]

        current_result = fetch_url(url)
        previous_entry = previous_sources.get(url, {})

        status = classify_source_status(previous_entry, current_result)

        result = {
            "source_file": source_file,
            "source_path": source_path,
            "url": url,
            "final_url": current_result.get("final_url", ""),
            "status": status,
            "http_status": current_result.get("status_code", ""),
            "content_hash": current_result.get("content_hash", ""),
            "previous_hash": previous_entry.get("content_hash", ""),
            "content_length": current_result.get("content_length", 0),
            "error": current_result.get("error", ""),
            "checked_at": checked_at,
        }

        results.append(result)

        if current_result["ok"]:
            new_sources_state[url] = {
                "source_file": source_file,
                "source_path": source_path,
                "url": url,
                "final_url": current_result.get("final_url", ""),
                "content_hash": current_result.get("content_hash", ""),
                "content_length": current_result.get("content_length", 0),
                "last_successful_check": checked_at,
                "last_status": status,
                "http_status": current_result.get("status_code", ""),
            }
        else:
            # Keep previous successful state if a source temporarily fails.
            if previous_entry:
                new_sources_state[url] = previous_entry
                new_sources_state[url]["last_failed_check"] = checked_at
                new_sources_state[url]["last_error"] = current_result.get("error", "")

    new_state = {
        "version": 1,
        "generated_at": checked_at,
        "description": (
            "CyberLex Sweden source watch state. This stores URL hashes for detecting "
            "possible official source changes. It does not store full webpage contents."
        ),
        "sources": new_sources_state,
    }

    save_state(new_state)

    report = build_report(results, previous_state)
    REPORT_FILE.write_text(report, encoding="utf-8")

    return results


def build_result_block(result):
    """
    Build a Markdown block for one source-watch result.
    """
    lines = []

    lines.append(f"### {result['source_file']}")
    lines.append("")
    lines.append(f"- Local file: `{result['source_path']}`")
    lines.append(f"- Official source URL: `{result['url']}`")

    if result.get("final_url") and result["final_url"] != result["url"]:
        lines.append(f"- Final URL after redirects: `{result['final_url']}`")

    lines.append(f"- Status: `{result['status']}`")
    lines.append(f"- HTTP status: `{result['http_status']}`")
    lines.append(f"- Content length: `{result['content_length']}`")
    lines.append(f"- Checked at: `{result['checked_at']}`")

    if result.get("error"):
        lines.append(f"- Error: `{result['error']}`")

    if result.get("previous_hash") and result.get("content_hash"):
        lines.append(f"- Previous hash: `{result['previous_hash'][:16]}...`")
        lines.append(f"- Current hash: `{result['content_hash'][:16]}...`")
    elif result.get("content_hash"):
        lines.append(f"- Current hash: `{result['content_hash'][:16]}...`")

    lines.append("")

    return lines


def build_report(results, previous_state):
    """
    Build the Markdown source watch report.
    """
    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    total_checked = len(results)
    first_snapshot_count = sum(1 for result in results if result["status"] == "First snapshot")
    unchanged_count = sum(1 for result in results if result["status"] == "Unchanged")
    changed_count = sum(1 for result in results if result["status"] == "Changed")
    failed_count = sum(1 for result in results if result["status"] == "Failed")

    lines = []

    lines.append("# CyberLex Sweden Source Watch Report")
    lines.append("")
    lines.append("## Purpose")
    lines.append("")
    lines.append(
        "This report checks official online source URLs referenced by the local CyberLex Sweden Markdown knowledge files."
    )
    lines.append("")
    lines.append(
        "The purpose is to detect whether an official source page may have changed since the last source watch run."
    )
    lines.append("")
    lines.append(
        "This report does not automatically update CyberLex source summaries and does not confirm legal currentness. Any changed source must be reviewed manually."
    )
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Watch Summary")
    lines.append("")
    lines.append(f"- Generated at: `{generated_at}`")
    lines.append(f"- Total official source URLs checked: `{total_checked}`")
    lines.append(f"- First snapshots created: `{first_snapshot_count}`")
    lines.append(f"- Unchanged sources: `{unchanged_count}`")
    lines.append(f"- Changed sources: `{changed_count}`")
    lines.append(f"- Failed checks: `{failed_count}`")
    lines.append("")
    lines.append("---")
    lines.append("")

    state_warning = previous_state.get("state_warning")

    if state_warning:
        lines.append("## State Warning")
        lines.append("")
        lines.append(f"- {state_warning}")
        lines.append("")
        lines.append("---")
        lines.append("")

    changed_results = [result for result in results if result["status"] == "Changed"]
    failed_results = [result for result in results if result["status"] == "Failed"]
    first_results = [result for result in results if result["status"] == "First snapshot"]
    unchanged_results = [result for result in results if result["status"] == "Unchanged"]

    lines.append("## Sources Needing Manual Review")
    lines.append("")

    if not changed_results and not failed_results:
        lines.append("No changed or failed official sources were detected.")
        lines.append("")
    else:
        if changed_results:
            lines.append("### Changed Sources")
            lines.append("")
            for result in changed_results:
                lines.extend(build_result_block(result))
                lines.append(
                    "Recommended action: Review the official source manually and update the local Markdown summary if needed."
                )
                lines.append("")

        if failed_results:
            lines.append("### Failed Checks")
            lines.append("")
            for result in failed_results:
                lines.extend(build_result_block(result))
                lines.append(
                    "Recommended action: Check whether the URL is still correct, temporarily unavailable, blocked, redirected, or moved."
                )
                lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## First Snapshots")
    lines.append("")

    if not first_results:
        lines.append("No first snapshots were created in this run.")
        lines.append("")
    else:
        lines.append(
            "These sources were seen for the first time by the source watcher. Future runs can compare against these hashes."
        )
        lines.append("")
        for result in first_results:
            lines.extend(build_result_block(result))
            lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Unchanged Sources")
    lines.append("")

    if not unchanged_results:
        lines.append("No unchanged sources were detected in this run.")
        lines.append("")
    else:
        for result in unchanged_results:
            lines.extend(build_result_block(result))
            lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Important Limitations")
    lines.append("")
    lines.append("- This script checks whether fetched source content appears to have changed.")
    lines.append("- It does not decide whether the law has changed.")
    lines.append("- It does not decide whether CyberLex summaries are still legally correct.")
    lines.append("- It does not automatically rewrite local source files.")
    lines.append("- Some official websites may change navigation, cookies, footers, timestamps, or layout without changing the legal substance.")
    lines.append("- Some official websites may block automated requests or serve different content over time.")
    lines.append("- Changed sources should always be reviewed manually.")
    lines.append("")

    return "\n".join(lines)


def main():
    """
    Main program entry point.
    """
    results = run_source_watch()

    changed_count = sum(1 for result in results if result["status"] == "Changed")
    failed_count = sum(1 for result in results if result["status"] == "Failed")

    print("Source watch completed.")
    print(f"URLs checked: {len(results)}")
    print(f"Changed sources: {changed_count}")
    print(f"Failed checks: {failed_count}")
    print(f"Report written to: {REPORT_FILE}")
    print(f"State written to: {STATE_FILE}")

    # Exit code 0 because changed sources are not script failures.
    # They are review signals.
    return 0


if __name__ == "__main__":
    sys.exit(main())
