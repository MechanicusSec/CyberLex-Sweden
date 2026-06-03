from pathlib import Path
from datetime import datetime
import re


# Project folders
# ROOT_DIR points to the main CyberLex Sweden project folder.
# DATA_DIR is where the trusted Markdown knowledge files are stored.
# DOCS_DIR is where documentation and generated reports are stored.
ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
DOCS_DIR = ROOT_DIR / "docs"
REPORT_FILE = DOCS_DIR / "source_audit_report.md"


def read_markdown_file(file_path):
    """Read a Markdown file safely."""
    return file_path.read_text(encoding="utf-8")


def clean_markdown_label(text):
    """
    Remove common Markdown formatting from labels.

    Example:
    **Source date:** becomes Source date:
    """
    text = text.replace("**", "")
    text = text.replace("__", "")
    text = text.strip()
    return text


def extract_section(content, heading):
    """
    Extract a Markdown section by heading.

    This supports headings such as:
    ## Source metadata
    ### Source metadata
    #### Source metadata
    """
    pattern = rf"^#{{2,6}}\s+{re.escape(heading)}\s*$([\s\S]*?)(?=^#{{2,6}}\s+|\Z)"
    match = re.search(pattern, content, flags=re.IGNORECASE | re.MULTILINE)

    if not match:
        return ""

    return match.group(1).strip()


def extract_source_date(metadata_section):
    """
    Extract the source date line from the Source metadata section.

    Supported examples:
    Source date: Last checked: 2026-05-31
    **Source date:** Last checked: 2026-05-31
    - Source date: Last checked: 2026-05-31
    """
    for line in metadata_section.splitlines():
        cleaned = clean_markdown_label(line)
        cleaned = cleaned.lstrip("-").strip()

        if cleaned.lower().startswith("source date"):
            return cleaned

    return ""


def extract_version_notes(metadata_section):
    """
    Extract version notes from the Source metadata section.

    Supported examples:
    Version notes: Initial educational summary added for CyberLex Sweden.
    **Version notes:** Initial educational summary added for CyberLex Sweden.
    - Version notes: Initial educational summary added for CyberLex Sweden.
    """
    for line in metadata_section.splitlines():
        cleaned = clean_markdown_label(line)
        cleaned = cleaned.lstrip("-").strip()

        if cleaned.lower().startswith("version notes"):
            return cleaned

    return ""


def count_links(text):
    """
    Count Markdown links and raw URLs in a text block.

    Markdown link example:
    [MSB: Example](https://www.msb.se/)

    Raw URL example:
    https://www.msb.se/
    """
    markdown_links = re.findall(r"\[[^\]]+\]\([^)]+\)", text)
    raw_links = re.findall(r"https?://[^\s)]+", text)

    return len(set(markdown_links + raw_links))


def get_freshness_label(source_date):
    """
    Give a simple freshness label based on the stored source date.

    This does not check the internet.
    It only checks the date written in the local Markdown file.
    """
    if not source_date:
        return "No review date stored"

    if "2026" in source_date:
        return "Recently checked"

    return "Review recommended"


def audit_file(file_path):
    """
    Audit one Markdown source file and return a dictionary with results.
    """
    content = read_markdown_file(file_path)

    official_source_section = extract_section(content, "Official source")
    metadata_section = extract_section(content, "Source metadata")

    source_date = extract_source_date(metadata_section)
    version_notes = extract_version_notes(metadata_section)

    # Fallback:
    # If metadata was not found inside a Source metadata section,
    # scan the whole file. This makes the audit more tolerant of older source file formats.
    if not source_date:
        source_date = extract_source_date(content)

    if not version_notes:
        version_notes = extract_version_notes(content)

    official_link_count = count_links(official_source_section)
    freshness_label = get_freshness_label(source_date)

    has_official_source_section = bool(official_source_section)
    has_metadata_section = bool(metadata_section)
    has_source_date = bool(source_date)
    has_version_notes = bool(version_notes)

    issues = []

    if not has_official_source_section:
        issues.append("Missing Official source section")

    if official_link_count == 0:
        issues.append("No official source links found")

    if not has_metadata_section:
        issues.append("Missing Source metadata section")

    if not has_source_date:
        issues.append("Missing source date")

    if not has_version_notes:
        issues.append("Missing version notes")

    if freshness_label != "Recently checked":
        issues.append(f"Freshness status: {freshness_label}")

    status = "OK" if not issues else "Needs review"

    return {
        "filename": file_path.name,
        "status": status,
        "official_link_count": official_link_count,
        "source_date": source_date if source_date else "Not found",
        "version_notes": version_notes if version_notes else "Not found",
        "freshness": freshness_label,
        "issues": issues,
    }


def build_report(results):
    """
    Build the Markdown audit report.
    """
    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    total_files = len(results)
    ok_files = sum(1 for result in results if result["status"] == "OK")
    review_files = total_files - ok_files

    lines = []

    lines.append("# CyberLex Sweden Source Audit Report")
    lines.append("")
    lines.append("## Purpose")
    lines.append("")
    lines.append(
        "This report checks the local CyberLex Sweden Markdown knowledge files for source metadata, official source links, review dates, and version notes."
    )
    lines.append("")
    lines.append(
        "This audit does not browse the web and does not confirm whether the law is currently up to date. It only checks the local project files."
    )
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Audit Summary")
    lines.append("")
    lines.append(f"- Generated at: `{generated_at}`")
    lines.append(f"- Total source files checked: `{total_files}`")
    lines.append(f"- Files marked OK: `{ok_files}`")
    lines.append(f"- Files needing review: `{review_files}`")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## File Results")
    lines.append("")

    for result in results:
        lines.append(f"### {result['filename']}")
        lines.append("")
        lines.append(f"- Status: `{result['status']}`")
        lines.append(f"- Official source links found: `{result['official_link_count']}`")
        lines.append(f"- Source date: `{result['source_date']}`")
        lines.append(f"- Source freshness: `{result['freshness']}`")
        lines.append(f"- Version notes: `{result['version_notes']}`")
        lines.append("")

        if result["issues"]:
            lines.append("#### Issues")
            lines.append("")
            for issue in result["issues"]:
                lines.append(f"- {issue}")
            lines.append("")
        else:
            lines.append("No issues found.")
            lines.append("")

        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def main():
    """
    Main program entry point.

    This finds Markdown files in the data folder, audits them, and writes a report.
    """
    DOCS_DIR.mkdir(exist_ok=True)

    if not DATA_DIR.exists():
        raise FileNotFoundError(f"Data folder not found: {DATA_DIR}")

    markdown_files = sorted(DATA_DIR.glob("*.md"))

    if not markdown_files:
        raise FileNotFoundError(f"No Markdown files found in: {DATA_DIR}")

    results = [audit_file(file_path) for file_path in markdown_files]
    report = build_report(results)

    REPORT_FILE.write_text(report, encoding="utf-8")

    print("Source audit completed.")
    print(f"Files checked: {len(results)}")
    print(f"Report written to: {REPORT_FILE}")


if __name__ == "__main__":
    main()