"""
Markdown source loading helpers for CyberLex Sweden.

This module handles the local trusted source files in data/.
It extracts official links, metadata, and searchable chunks so main.py can
focus on Streamlit UI and answer flow instead of archive duty.
"""

from config import DATA_DIR
from text_utils import clean_words

def extract_official_sources(content):
    # Extracts official source links from the "## Official source" section.
    # Supports:
    # https://example.com
    # [Source name](https://example.com)
    # - [Source name](https://example.com)
    # - https://example.com

    lines = content.splitlines()
    sources = []
    in_official_source_section = False
    previous_label = ""

    for line in lines:
        stripped_line = line.strip()

        heading_lower = stripped_line.lower()

        if heading_lower.startswith("## official source"):
            in_official_source_section = True
            continue

        if in_official_source_section and stripped_line.startswith("## "):
            break

        if not in_official_source_section or not stripped_line:
            continue

        # Remove common Markdown bullet prefixes before parsing links.
        cleaned_line = stripped_line
        while cleaned_line.startswith(("-", "*")):
            cleaned_line = cleaned_line[1:].strip()

        # Markdown link format:
        # [Source name](https://example.com)
        if cleaned_line.startswith("[") and "](" in cleaned_line and ")" in cleaned_line:
            label = cleaned_line.split("](", 1)[0].replace("[", "").strip()
            url = cleaned_line.split("](", 1)[1].split(")", 1)[0].strip()

            if label and url.startswith("http"):
                sources.append(
                    {
                        "label": label,
                        "url": url
                    }
                )
                previous_label = ""
                continue

        # Raw URL format:
        # https://example.com
        if cleaned_line.startswith("http"):
            label = previous_label if previous_label else cleaned_line

            sources.append(
                {
                    "label": label,
                    "url": cleaned_line
                }
            )
            previous_label = ""
            continue

        # Label on one line followed by URL on next line.
        # Example:
        # EUR-Lex - Directive 2013/40/EU
        # https://eur-lex.europa.eu/...
        previous_label = cleaned_line.rstrip(":")

    return sources

def extract_section_text(content, heading):
    # Extracts text from a specific Markdown heading section.
    lines = content.splitlines()
    section_lines = []
    in_section = False

    for line in lines:
        stripped_line = line.strip()

        if stripped_line.lower() == heading.lower():
            in_section = True
            continue

        if in_section and stripped_line.startswith("## "):
            break

        if in_section:
            section_lines.append(line)

    return "\n".join(section_lines).strip()

def extract_source_metadata(content):
    # Extracts source date and version notes from a Markdown knowledge file.
    # Supports both the older layout:
    # ## Source date
    # ## Version notes
    #
    # and the newer combined layout:
    # ## Source metadata
    # Source date: Last checked: 2026-06-03
    # Version notes: Source reviewed...

    source_date = extract_section_text(content, "## Source date")
    version_notes = extract_section_text(content, "## Version notes")

    metadata_section = extract_section_text(content, "## Source metadata")

    if metadata_section:
        metadata_lines = metadata_section.splitlines()

        for index, line in enumerate(metadata_lines):
            stripped_line = line.strip()
            lower_line = stripped_line.lower()

            if lower_line.startswith("source date:"):
                source_date = stripped_line.split(":", 1)[1].strip()

            elif lower_line.startswith("version notes:"):
                version_text = stripped_line.split(":", 1)[1].strip()

                # Include following non-empty lines until another metadata field appears.
                extra_lines = []
                for following_line in metadata_lines[index + 1:]:
                    following_stripped = following_line.strip()
                    following_lower = following_stripped.lower()

                    if following_lower.startswith("source date:") or following_lower.startswith("version notes:"):
                        break

                    if following_stripped:
                        extra_lines.append(following_stripped)

                if extra_lines:
                    version_text = " ".join([version_text] + extra_lines).strip()

                version_notes = version_text

    if not source_date:
        source_date = "No source date stored for this document yet."

    if not version_notes:
        version_notes = "No version notes stored for this document yet."

    return {
        "source_date": source_date,
        "version_notes": version_notes
    }

def load_documents():
    # Loads all Markdown files from the data folder.
    documents = []

    for file_path in DATA_DIR.glob("*.md"):
        content = file_path.read_text(encoding="utf-8")
        metadata = extract_source_metadata(content)

        documents.append(
            {
                "filename": file_path.name,
                "content": content,
                "official_sources": extract_official_sources(content),
                "source_date": metadata["source_date"],
                "version_notes": metadata["version_notes"]
            }
        )

    return documents

def split_into_chunks(document):
    # Splits a Markdown document into smaller searchable chunks based on headings.
    filename = document["filename"]
    content = document["content"]
    official_sources = document["official_sources"]
    source_date = document["source_date"]
    version_notes = document["version_notes"]

    chunks = []
    current_title = "Introduction"
    current_lines = []

    def save_chunk(title, lines):
        chunk_content = "\n".join(lines).strip()
        plain_words = clean_words(chunk_content)

        if len(plain_words) < 8:
            return

        chunks.append(
            {
                "filename": filename,
                "section": title,
                "content": chunk_content,
                "official_sources": official_sources,
                "source_date": source_date,
                "version_notes": version_notes
            }
        )

    for line in content.splitlines():
        if line.startswith("#"):
            if current_lines:
                save_chunk(current_title, current_lines)

            current_title = line.replace("#", "").strip()
            current_lines = [line]
        else:
            current_lines.append(line)

    if current_lines:
        save_chunk(current_title, current_lines)

    return chunks

def load_chunks():
    # Loads all documents and splits them into searchable chunks.
    documents = load_documents()
    all_chunks = []

    for document in documents:
        all_chunks.extend(split_into_chunks(document))

    return documents, all_chunks

