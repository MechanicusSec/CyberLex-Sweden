from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"

METADATA_BLOCK = """

## Source metadata

Source date: Last checked: 2026-06-03

Version notes: Source reviewed for CyberLex Sweden educational prototype.
"""


def file_has_source_metadata(content):
    return "## Source metadata" in content or "### Source metadata" in content


def add_metadata_to_file(file_path):
    content = file_path.read_text(encoding="utf-8")

    if file_has_source_metadata(content):
        print(f"Skipped, metadata already exists: {file_path.name}")
        return False

    updated_content = content.rstrip() + METADATA_BLOCK + "\n"
    file_path.write_text(updated_content, encoding="utf-8")

    print(f"Added metadata: {file_path.name}")
    return True


def main():
    if not DATA_DIR.exists():
        raise FileNotFoundError(f"Data folder not found: {DATA_DIR}")

    markdown_files = sorted(DATA_DIR.glob("*.md"))

    if not markdown_files:
        raise FileNotFoundError(f"No Markdown files found in: {DATA_DIR}")

    changed_count = 0

    for file_path in markdown_files:
        changed = add_metadata_to_file(file_path)
        if changed:
            changed_count += 1

    print("")
    print(f"Metadata update completed.")
    print(f"Files checked: {len(markdown_files)}")
    print(f"Files updated: {changed_count}")


if __name__ == "__main__":
    main()