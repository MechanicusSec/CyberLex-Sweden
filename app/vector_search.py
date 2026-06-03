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
    It is designed to behave like an experimental retrieval engine before
    real vector embeddings are added.
    """
    chunk_words = clean_text(chunk["text"])
    section_words = clean_text(chunk["section"])
    filename_words = clean_text(chunk["filename"].replace("_", " "))

    chunk_text = chunk["text"].lower()
    section_text = chunk["section"].lower()
    filename_text = chunk["filename"].lower()

    chunk_counter = Counter(chunk_words)
    score = 0

    useful_sections = {
        "incident assessment checklist": 35,
        "data breach assessment checklist": 35,
        "swedish summary": 30,
        "key idea": 25,
        "important points": 20,
        "main authority": 18,
        "reporting to imy": 18,
        "incident reporting": 18,
        "affected individuals": 18,
        "cybersecurity connection": 15,
        "swedish connection": 15,
        "practical explanation": 15,
        "relationship with gdpr breach reporting": 15,
        "third-party ict risk": 15,
        "legal reference": 15,
    }

    weak_sections = {
        "useful questions": -35,
        "official source": -30,
        "source metadata": -30,
        "source date": -30,
        "version notes": -30,
        "disclaimer": -25,
        "topic": -15,
        "introduction": -10,
    }

    for section_name, boost in useful_sections.items():
        if section_name in section_text:
            score += boost

    for section_name, penalty in weak_sections.items():
        if section_name in section_text:
            score += penalty

    for word in question_words:
        if len(word) <= 2:
            continue

        # Main text match.
        score += chunk_counter.get(word, 0) * 3

        # Section title match.
        if word in section_words:
            score += 8

        # Filename match.
        if word in filename_words:
            score += 6

        # Broader text match.
        if word in chunk_text:
            score += 1

    # Topic-specific boosts.
    question_joined = " ".join(question_words)

    # DORA / digital operational resilience questions.
    if (
        "dora" in question_joined
        or "digital operational resilience" in question_joined
        or "operational resilience" in question_joined
        or "ict risk" in question_joined
        or "financial sector" in question_joined
        or "finansiella sektorn" in question_joined
        or "digital operativ motståndskraft" in question_joined
    ):
        if "dora" in filename_text:
            score += 40
        if "key idea" in section_text:
            score += 30
        if "important points" in section_text:
            score += 25
        if "third-party ict risk" in section_text:
            score += 20
        if "swedish summary" in section_text:
            score += 20
        if "official source" in section_text or "useful questions" in section_text:
            score -= 30

    # Ransomware, malware, cyber attack, and general cyber incident questions.
    if (
        "ransomware" in question_joined
        or "ransomwareattack" in question_joined
        or "malware" in question_joined
        or "skadlig kod" in question_joined
        or "cyber incident" in question_joined
        or "cybersäkerhetsincident" in question_joined
        or "cyber attack" in question_joined
        or "cyberattack" in question_joined
        or "attack" in question_joined
        or "incident" in question_joined
    ):
        if "nis2_incident_reporting" in filename_text:
            score += 120
        if "gdpr_personal_data_breach" in filename_text:
            score += 35
        if "nis2_cybersecurity_law" in filename_text:
            score += 25
        if "eu_dora" in filename_text:
            score -= 100

        if "incident assessment checklist" in section_text:
            score += 80
        if "swedish summary" in section_text:
            score += 40
        if "incident reporting" in section_text:
            score += 35
        if "relationship with gdpr breach reporting" in section_text:
            score += 20
        if "cybersecurity connection" in section_text:
            score += 20
        if "practical explanation" in section_text:
            score += 20
        if "key idea" in section_text:
            score += 15
        if "official source" in section_text or "useful questions" in section_text:
            score -= 30

    # Unauthorized access / dataintrång questions.
    if (
        "unauthorized" in question_joined
        or "access" in question_joined
        or "dataintrång" in question_joined
        or "obehörig åtkomst" in question_joined
        or "illegal access" in question_joined
        or "olaglig åtkomst" in question_joined
    ):
        if "cybercrime_dataintrang" in filename_text:
            score += 70
        if "key idea" in section_text:
            score += 25
        if "legal reference" in section_text:
            score += 25
        if "practical explanation" in section_text:
            score += 20
        if "swedish summary" in section_text:
            score += 20
        if "official source" in section_text or "useful questions" in section_text:
            score -= 30

        # IMY / Swedish GDPR supervision authority questions.
    if (
        "imy" in question_joined
        or "integritetsskyddsmyndigheten" in question_joined
        or "tillsynsmyndighet" in question_joined
        or "tillsyn" in question_joined
        or "gdpr myndighet" in question_joined
        or "myndighet ansvarar" in question_joined
        or "dataskyddsmyndighet" in question_joined
        or "personuppgiftsskydd" in question_joined
    ):
        if "imy_gdpr_supervision" in filename_text:
            score += 180
        if "gdpr_personal_data_breach" in filename_text:
            score -= 60

        if "swedish summary" in section_text:
            score += 80
        if "main authority" in section_text:
            score += 70
        if "key idea" in section_text:
            score += 40
        if "important points" in section_text:
            score += 30
        if "cybersecurity connection" in section_text:
            score += 20
        if "official source" in section_text or "useful questions" in section_text:
            score -= 30

    # GDPR / personal data breach questions.
    if (
        "breach" in question_joined
        or "gdpr" in question_joined
        or "personal data" in question_joined
        or "data breach" in question_joined
        or "personuppgiftsincident" in question_joined
        or "personuppgifter" in question_joined
        or "personuppgift" in question_joined
        or "imy" in question_joined
        or "72" in question_joined
        or "72 timmarsregeln" in question_joined
        or "72-timmarsregeln" in question_joined
        or "anmälas" in question_joined
        or "anmäla" in question_joined
        or "anmälan" in question_joined
        or "dataläcka" in question_joined
        or "dataläckor" in question_joined
    ):
        if "gdpr_personal_data_breach" in filename_text:
            score += 140
        if "imy_gdpr_supervision" in filename_text:
            score += 25
        if "nis2_incident_reporting" in filename_text:
            score -= 40

        if "data breach assessment checklist" in section_text:
            score += 80
        if "swedish summary" in section_text:
            score += 60
        if "reporting to imy" in section_text:
            score += 45
        if "affected individuals" in section_text:
            score += 30
        if "main authority" in section_text:
            score += 20
        if "cybersecurity connection" in section_text:
            score += 15
        if "official source" in section_text or "useful questions" in section_text:
            score -= 30

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