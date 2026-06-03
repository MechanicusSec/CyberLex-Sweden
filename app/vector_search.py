from pathlib import Path
import re
from collections import Counter


ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"


def clean_text(text):
    """
    Convert text into searchable lowercase words.

    This removes punctuation and splits the text into simple word tokens.
    """
    text = text.lower()
    text = re.sub(r"[^a-zåäö0-9\s]", " ", text)
    words = text.split()
    return words


def load_markdown_files(data_dir=DATA_DIR):
    """
    Load all Markdown files from the data folder.

    Returns a list of dictionaries containing filename and content.
    """
    files = []

    for file_path in sorted(data_dir.glob("*.md")):
        content = file_path.read_text(encoding="utf-8")
        files.append(
            {
                "filename": file_path.name,
                "content": content,
            }
        )

    return files


def split_into_chunks(markdown_file):
    """
    Split one Markdown file into chunks based on headings.

    Each chunk keeps:
    - filename
    - section title
    - chunk text
    """
    filename = markdown_file["filename"]
    content = markdown_file["content"]

    chunks = []
    current_section = "Introduction"
    current_lines = []

    for line in content.splitlines():
        if line.startswith("## "):
            if current_lines:
                chunks.append(
                    {
                        "filename": filename,
                        "section": current_section,
                        "text": "\n".join(current_lines).strip(),
                    }
                )

            current_section = line.replace("##", "").strip()
            current_lines = []
        else:
            current_lines.append(line)

    if current_lines:
        chunks.append(
            {
                "filename": filename,
                "section": current_section,
                "text": "\n".join(current_lines).strip(),
            }
        )

    return chunks


def build_chunk_index(data_dir=DATA_DIR):
    """
    Build a searchable chunk index from all Markdown source files.

    This is the first experimental search index.
    Later, this can be replaced or extended with real vector embeddings.
    """
    markdown_files = load_markdown_files(data_dir)
    all_chunks = []

    for markdown_file in markdown_files:
        chunks = split_into_chunks(markdown_file)
        all_chunks.extend(chunks)

    return all_chunks


def score_chunk(question_words, chunk):
    """
    Score a chunk against a user question.

    This is still a simple lexical similarity score.
    It is placed here so it can later be replaced with vector similarity.
    """
    chunk_words = clean_text(chunk["text"])
    section_words = clean_text(chunk["section"])
    filename_words = clean_text(chunk["filename"].replace("_", " "))

    chunk_counter = Counter(chunk_words)
    score = 0

    for word in question_words:
        if len(word) <= 2:
            continue

        score += chunk_counter.get(word, 0)

        if word in section_words:
            score += 5

        if word in filename_words:
            score += 3

    return score


def search_chunks(question, chunks, limit=5):
    """
    Search the chunk index and return the best matches.

    This function returns ranked source chunks.
    """
    question_words = clean_text(question)
    results = []

    for chunk in chunks:
        score = score_chunk(question_words, chunk)

        if score > 0:
            results.append(
                {
                    "filename": chunk["filename"],
                    "section": chunk["section"],
                    "text": chunk["text"],
                    "score": score,
                }
            )

    results.sort(key=lambda item: item["score"], reverse=True)

    return results[:limit]


def format_result(result):
    """
    Format one result for terminal testing.
    """
    excerpt = result["text"].replace("\n", " ").strip()

    if len(excerpt) > 300:
        excerpt = excerpt[:300] + "..."

    return (
        f"File: {result['filename']}\n"
        f"Section: {result['section']}\n"
        f"Score: {result['score']}\n"
        f"Excerpt: {excerpt}\n"
    )


def main():
    """
    Manual test entry point.

    This lets us test the experimental search module from the terminal.
    """
    chunks = build_chunk_index()

    print("CyberLex experimental vector search module")
    print("-----------------------------------------")
    print(f"Loaded chunks: {len(chunks)}")
    print("")

    question = input("Ask a test question: ").strip()

    if not question:
        print("No question entered.")
        return

    results = search_chunks(question, chunks)

    if not results:
        print("No matching chunks found.")
        return

    print("")
    print("Top matches:")
    print("")

    for index, result in enumerate(results, start=1):
        print(f"Result {index}")
        print(format_result(result))


if __name__ == "__main__":
    main()