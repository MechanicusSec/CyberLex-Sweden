from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="CyberLex Sweden",
    page_icon="💻",
    layout="wide"
)

DATA_DIR = Path("data")


def clean_words(text):
    """
    Converts text into simple searchable words.
    This makes matching easier by removing punctuation and using lowercase text.
    """
    punctuation = ",.?!:;()[]{}\"'`"
    text = text.lower()

    for mark in punctuation:
        text = text.replace(mark, " ")

    return text.split()


def extract_official_sources(content):
    """
    Extracts URLs from the official source section of a Markdown document.
    These URLs are shown in the app so users can trace answers back to trusted sources.
    """
    lines = content.splitlines()
    sources = []
    in_official_source_section = False

    for line in lines:
        stripped_line = line.strip()

        if stripped_line.lower() == "## official source":
            in_official_source_section = True
            continue

        if in_official_source_section and stripped_line.startswith("## "):
            break

        if in_official_source_section and stripped_line.startswith("http"):
            sources.append(stripped_line)

    return sources

def extract_section_text(content, heading):
    """
    Extracts text from a specific Markdown heading section.

    Example:
    If heading is '## Source date', this function returns the text under that heading
    until the next Markdown heading starts.
    """
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
    """
    Extracts source date and version notes from a Markdown knowledge file.
    """
    source_date = extract_section_text(content, "## Source date")
    version_notes = extract_section_text(content, "## Version notes")

    if not source_date:
        source_date = "No source date stored for this document yet."

    if not version_notes:
        version_notes = "No version notes stored for this document yet."

    return {
        "source_date": source_date,
        "version_notes": version_notes
    }


def load_documents():
    """
    Loads all Markdown files from the data folder.
    Also extracts official source links, source dates, and version notes.
    """
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
    """
    Splits a Markdown document into smaller chunks based on headings.
    Each chunk keeps track of the source filename, section title, and official source links.

    Very small chunks are ignored because they usually only contain a heading
    and do not give useful legal information.
    """
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
    """
    Loads all documents and splits them into searchable chunks.
    """
    documents = load_documents()
    all_chunks = []

    for document in documents:
        chunks = split_into_chunks(document)
        all_chunks.extend(chunks)

    return documents, all_chunks

def get_target_source_file(question):
    """
    Detects when a question clearly belongs to a specific knowledge file.
    This prevents CyberLex from selecting the wrong source file when multiple files contain similar words.
    """
    question_lower = question.lower().strip()

    if (
        "gdpr principles" in question_lower
        or "gdpr principle" in question_lower
        or "what are the gdpr principles" in question_lower
    ):
        return "gdpr_core_principles.md"

    if question_lower == "gdpr" or "what is gdpr" in question_lower:
        return "gdpr_core_principles.md"

    if (
        "cyber resilience act" in question_lower
        or "products with digital elements" in question_lower
        or "product security" in question_lower
    ):
        return "eu_cyber_resilience_act.md"

    if (
        "attacks against information systems" in question_lower
        or "eu law about attacks" in question_lower
        or "eu cybercrime" in question_lower
    ):
        return "eu_attacks_against_information_systems.md"

    return None
def search_chunks(question, chunks):
    """
    Searches document chunks using keyword matching, question intent, and source routing.

    This version improves ranking by:
    - ignoring weak common words
    - lowering broad sections like Topic
    - boosting sections that match the user's question type
    - forcing the correct source file when the question clearly belongs to one file
    """
    stopwords = {
        "what", "when", "where", "which", "who", "why", "how",
        "is", "are", "was", "were", "be", "been", "being",
        "a", "an", "the", "to", "in", "on", "of", "for", "and",
        "or", "with", "from", "this", "that", "it", "does", "do",
        "must", "should", "can"
    }

    useful_sections = {
        "key idea",
        "reporting to imy",
        "main authority",
        "important points",
        "incident reporting",
        "legal reference",
        "practical explanation",
        "cybersecurity connection",
        "swedish connection"
    }

    weak_sections = {
        "useful questions",
        "source",
        "official source",
        "source date",
        "version notes",
        "disclaimer",
        "introduction",
        "topic"
    }

    question_lower = question.lower()
    target_source_file = get_target_source_file(question)

    question_words = [
        word for word in clean_words(question)
        if len(word) > 2 and word not in stopwords
    ]

    results = []

    for chunk in chunks:
        filename = chunk["filename"]
        filename_lower = filename.lower()
        chunk_words = clean_words(chunk["content"])
        chunk_text = chunk["content"].lower()
        section_text = chunk["section"].lower()

        score = 0

        # If the question clearly belongs to a specific file,
        # strongly punish all other files.
        if target_source_file:
            if filename_lower == target_source_file.lower():
                score += 100
            else:
                score -= 100

        # Basic keyword score
        for word in question_words:
            if word in chunk_words:
                score += 4

            if word in section_text:
                score += 3

            if word in chunk_text:
                score += 1

        # General useful section bonus
        for useful_section in useful_sections:
            if useful_section in section_text:
                score += 5

        # Weak section penalty
        for weak_section in weak_sections:
            if weak_section in section_text:
                score -= 10

        # Question-intent bonuses
        if "authority" in question_lower or "handles" in question_lower or "supervises" in question_lower:
            if "main authority" in section_text:
                score += 25
            if "imy" in chunk_text or "integritetsskyddsmyndigheten" in chunk_text:
                score += 8

        if "reported" in question_lower or "report" in question_lower or "72" in question_lower:
            if "reporting to imy" in section_text:
                score += 25
            if "72 hours" in chunk_text:
                score += 10

        if "nis2" in question_lower or "cybersecurity act" in question_lower:
            if "nis2_cybersecurity_law" in filename_lower:
                score += 50
            if "key idea" in section_text:
                score += 15
            if "important points" in section_text:
                score += 15
            if "incident reporting" in section_text:
                score += 10

        if "dataintrång" in question_lower or "data intrusion" in question_lower or "unauthorized access" in question_lower:
            if "cybercrime_dataintrang" in filename_lower:
                score += 50
            if "key idea" in section_text:
                score += 15
            if "legal reference" in section_text:
                score += 15
            if "practical explanation" in section_text:
                score += 15

        if "gdpr principles" in question_lower or "gdpr principle" in question_lower or "principles" in question_lower:
            if "important points" in section_text:
                score += 25
            if "key idea" in section_text:
                score += 15
            if "gdpr" in chunk_text:
                score += 10

        if "what is gdpr" in question_lower:
            if "key idea" in section_text:
                score += 20
            if "main authority" in section_text:
                score += 10
            if "gdpr" in chunk_text:
                score += 10

        if "attacks against information systems" in question_lower or "information systems" in question_lower or "eu cybercrime" in question_lower:
            if "key idea" in section_text:
                score += 20
            if "important points" in section_text:
                score += 15
            if "swedish connection" in section_text:
                score += 10

        if "cyber resilience act" in question_lower or "products with digital elements" in question_lower or "product security" in question_lower:
            if "key idea" in section_text:
                score += 20
            if "important points" in section_text:
                score += 15
            if "cybersecurity connection" in section_text:
                score += 10

        if score > 0:
            results.append(
    {
        "filename": chunk["filename"],
        "section": chunk["section"],
        "content": chunk["content"],
        "score": score,
        "official_sources": chunk["official_sources"],
        "source_date": chunk["source_date"],
        "version_notes": chunk["version_notes"]
    }
)

    results.sort(key=lambda item: item["score"], reverse=True)
    return results

def generate_simple_answer(question, best_match):
    """
    Generates a simple source-based answer from the best matching chunk.
    This is not full AI. It uses the matched source section and basic rules
    to create a clearer answer for the user.
    """
    question_lower = question.lower()
    section_lower = best_match["section"].lower()

    if "personal data breach" in question_lower or "breach" in question_lower:
        if "reporting to imy" in section_lower:
            answer = (
                "A personal data breach may need to be reported to IMY, "
                "the Swedish Authority for Privacy Protection. If notification is required, "
                "the breach should normally be reported within 72 hours after the organization becomes aware of it."
            )
        elif "main authority" in section_lower:
            answer = (
                "The Swedish authority connected to GDPR and personal data protection is IMY, "
                "Integritetsskyddsmyndigheten."
            )
        else:
            answer = (
                "This question is related to personal data breaches under GDPR. "
                "The matched source section should be reviewed for the exact project information."
            )

    elif "gdpr principles" in question_lower or "gdpr principle" in question_lower or "principles" in question_lower:
        answer = (
            "GDPR includes core principles such as lawfulness, fairness and transparency, "
            "purpose limitation, data minimisation, accuracy, storage limitation, integrity and confidentiality, "
            "and accountability. These principles guide how organizations should process and protect personal data."
        )

    elif "what is gdpr" in question_lower or question_lower.strip() == "gdpr":
        answer = (
            "GDPR is the General Data Protection Regulation. It is an EU regulation that controls how personal data "
            "may be processed and protected. In Sweden, IMY supervises GDPR and personal data protection."
        )

    elif "gdpr" in question_lower or "authority" in question_lower:
        answer = (
            "In Sweden, GDPR and personal data protection are handled by IMY, "
            "Integritetsskyddsmyndigheten, the Swedish Authority for Privacy Protection."
        )

    elif "nis2" in question_lower or "cybersecurity act" in question_lower:
        answer = (
            "NIS2 is an EU cybersecurity directive. In Sweden, it is connected to the Swedish Cybersecurity Act. "
            "The rules focus on cybersecurity risk management, security measures, and incident reporting for covered organizations."
        )

    elif "dataintrång" in question_lower or "data intrusion" in question_lower or "unauthorized access" in question_lower:
        answer = (
            "Dataintrång means data intrusion under Swedish criminal law. "
            "It is connected to unauthorized access to, or interference with, data or information systems."
        )

    elif "attacks against information systems" in question_lower or "information systems" in question_lower or "eu cybercrime" in question_lower:
        answer = (
            "The EU rules on attacks against information systems are connected to cybercrime. "
            "They cover areas such as illegal access, system interference, data interference, and cooperation between authorities. "
            "This helps explain how cyber attacks against systems are treated as criminal conduct in Europe."
        )

    elif "cyber resilience act" in question_lower or "products with digital elements" in question_lower or "product security" in question_lower:
        answer = (
            "The Cyber Resilience Act is an EU regulation about cybersecurity requirements for products with digital elements. "
            "It focuses on secure product design, vulnerability handling, and cybersecurity responsibilities for actors involved with digital products."
        )

    else:
        answer = (
            "CyberLex Sweden found a relevant trusted source section, but this prototype cannot yet generate a detailed legal explanation for this question."
        )

    source_lines = "\n".join(
        [f"- {source}" for source in best_match.get("official_sources", [])]
    )

    if not source_lines:
        source_lines = "- No official source URL stored for this document yet."

    return f"""
## Short answer

{answer}

## Source used

- File: `{best_match["filename"]}`
- Section: `{best_match["section"]}`
- Relevance score: `{best_match["score"]}`

## Official source links

{source_lines}

## Source metadata

- Source date: {best_match["source_date"]}
- Version notes: {best_match["version_notes"]}

## Important limitation

This answer is generated from a simplified local knowledge base. CyberLex Sweden is an educational project and does not provide legal advice.
"""


def is_cyberlaw_question(question):
    """
    Checks whether the user question belongs to the CyberLex Sweden project scope.

    The project scope is Swedish cybersecurity law, cybercrime law,
    GDPR, NIS2, incident reporting, data protection, and digital compliance.
    """
    allowed_keywords = {
        "cyber",
        "cybersecurity",
        "security",
        "gdpr",
        "personal",
        "data",
        "breach",
        "incident",
        "nis2",
        "cybersecurity act",
        "cybersäkerhetslagen",
        "dataintrång",
        "intrusion",
        "unauthorized",
        "access",
        "hacking",
        "malware",
        "privacy",
        "imy",
        "integritetsskyddsmyndigheten",
        "msb",
        "information system",
        "information systems",
        "digital",
        "compliance",
        "cyber resilience",
        "cyber resilience act",
        "products with digital elements",
        "product security",
        "eu cybercrime",
        "legal basis",
        "controller",
        "processor",
        "accountability",
        "principles"
    }

    question_lower = question.lower()

    for keyword in allowed_keywords:
        if keyword in question_lower:
            return True

    return False


st.title("CyberLex Sweden")
st.subheader("AI Assistant for Swedish Cybersecurity Law and Digital Compliance")

st.markdown("""
CyberLex Sweden is a final school project focused on creating an AI assistant that helps users understand Swedish cybersecurity law.

The system is designed to work with trusted sources about:

- Swedish cybercrime law
- GDPR and personal data breaches
- NIS2 and cybersecurity responsibilities
- EU cybersecurity law
- Cyber Resilience Act
- Incident reporting
- Digital compliance for organizations
""")

st.warning(
    "Important: CyberLex Sweden is an educational project. "
    "It does not provide official legal advice and should not replace a qualified lawyer or official authority guidance."
)

st.divider()

documents, chunks = load_chunks()

st.sidebar.header("Knowledge Base")
st.sidebar.write(f"Loaded documents: {len(documents)}")
st.sidebar.write(f"Searchable chunks: {len(chunks)}")

st.sidebar.subheader("Documents")
for doc in documents:
    st.sidebar.write(f"- {doc['filename']}")

st.header("Ask a question")

question = st.text_input(
    "Write a question about Swedish cybersecurity law:"
)

if question:
    if not is_cyberlaw_question(question):
        st.error(
            "No trusted source was found for this question. "
            "CyberLex Sweden only covers Swedish cybersecurity law, cybercrime, GDPR, NIS2, "
            "incident reporting, data protection, EU cybersecurity law, and related digital compliance topics."
        )

    else:
        search_results = search_chunks(question, chunks)

        if search_results:
            best_match = search_results[0]
            minimum_score = 12

            if best_match["score"] < minimum_score:
                st.error(
                    "No strong trusted source match was found for this question. "
                    "CyberLex Sweden cannot answer confidently yet."
                )
            else:
                st.subheader("CyberLex Answer")
                st.markdown(generate_simple_answer(question, best_match))

                st.subheader("Matched Source Excerpt")
                st.text_area(
                    "Relevant source section",
                    best_match["content"],
                    height=250
                )

                st.subheader("All Matching Source Sections")

                for result in search_results[:5]:
                    st.write(
                        f"**{result['filename']}** | "
                        f"Section: **{result['section']}** | "
                        f"Relevance score: {result['score']}"
                    )

                st.info(
                    "Next development step: connect this chunk-based search to AI-generated explanations."
                )

        else:
            st.error(
                "No trusted source was found for this question. "
                "CyberLex Sweden cannot answer confidently yet."
            )
else:
    st.write("Enter a question above to search the CyberLex Sweden knowledge base.")