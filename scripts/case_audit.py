from pathlib import Path
from datetime import datetime

CASES_DIR = Path("cases")
REPORT_PATH = Path("docs/case_library/case_audit_report.md")

REQUIRED_SECTIONS = [
    "## Case type",
    "## Jurisdiction",
    "## Year",
    "## Authority or court",
    "## Topic",
    "## Short summary",
    "## What happened",
    "## Legal issue",
    "## Decision or outcome",
    "## Fine or cost",
    "## Why it matters for CyberLex",
    "## Similar CyberLex questions",
    "## Related CyberLex topics",
    "## Official source",
    "## Case metadata",
    "## Disclaimer",
]


def read_file(path):
    return path.read_text(encoding="utf-8")


def extract_section(content, heading):
    lines = content.splitlines()
    in_section = False
    section_lines = []

    for line in lines:
        stripped = line.strip()

        if stripped.lower() == heading.lower():
            in_section = True
            continue

        if in_section and stripped.startswith("## "):
            break

        if in_section:
            section_lines.append(line)

    return "\n".join(section_lines).strip()


def has_official_link(content):
    official_section = extract_section(content, "## Official source")

    if not official_section:
        return False

    return "http://" in official_section or "https://" in official_section


def audit_case_file(path):
    content = read_file(path)
    issues = []

    for section in REQUIRED_SECTIONS:
        if section.lower() not in content.lower():
            issues.append(f"Missing section: `{section}`")

    if not has_official_link(content):
        issues.append("Missing official source link")

    metadata = extract_section(content, "## Case metadata")

    if "source date:" not in metadata.lower():
        issues.append("Missing case source date")

    if "version notes:" not in metadata.lower():
        issues.append("Missing case version notes")

    status = "OK" if not issues else "Needs review"

    return {
        "filename": path.name,
        "status": status,
        "issues": issues,
    }


def build_report(results):
    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    total_files = len(results)
    ok_files = sum(1 for result in results if result["status"] == "OK")
    review_files = total_files - ok_files

    lines = [
        "# CyberLex Sweden Case Audit Report",
        "",
        "## Purpose",
        "",
        "This report checks the local CyberLex Sweden case-library Markdown files for required sections, official source links, source dates, and version notes.",
        "",
        "This audit does not browse the web and does not confirm whether a case summary is legally complete or currently updated. It only checks the local project files.",
        "",
        "---",
        "",
        "## Audit Summary",
        "",
        f"- Generated at: `{generated_at}`",
        f"- Total case files checked: `{total_files}`",
        f"- Case files marked OK: `{ok_files}`",
        f"- Case files needing review: `{review_files}`",
        "",
        "---",
        "",
        "## File Results",
        "",
    ]

    for result in results:
        lines.append(f"### {result['filename']}")
        lines.append("")
        lines.append(f"- Status: `{result['status']}`")
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
    if not CASES_DIR.exists():
        print(f"Cases folder not found: {CASES_DIR}")
        return

    case_files = sorted(
        path for path in CASES_DIR.glob("*.md")
        if path.name.upper() not in {"CASE_TEMPLATE.MD", "CASE_INDEX.MD"}
    )

    results = [audit_case_file(path) for path in case_files]

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(build_report(results), encoding="utf-8")

    print("Case audit completed.")
    print(f"Case files checked: {len(results)}")
    print(f"Report written to: {REPORT_PATH}")


if __name__ == "__main__":
    main()