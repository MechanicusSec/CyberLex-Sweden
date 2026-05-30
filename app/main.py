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


def load_documents():
    """
    Loads all Markdown files from the data folder.
    """
    documents = []

    for file_path in DATA_DIR.glob("*.md"):
        content = file_path.read_text(encoding="utf-8")
        documents.append(
            {
                "filename": file_path.name,
                "content": content
            }
        )

    return documents


def split_into_chunks(document):
    """
    Splits a Markdown document into smaller chunks based on headings.
    Each chunk keeps track of the source filename and section title.

    Very small chunks are ignored because they usually only contain a heading
    and do not give useful legal information.
    """
    filename = document["filename"]
    content = document["content"]

    chunks = []
    current_title = "Introduction"
    current_lines = []

    def save_chunk(title, lines):
        chunk_content = "\n".join(lines).strip()

        # Remove empty chunks and heading-only chunks
        plain_words = clean_words(chunk_content)

        if len(plain_words) < 8:
            return

        chunks.append(
            {
                "filename": filename,
                "section": title,
                "content": chunk_content
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


def search_chunks(question, chunks):
    """
    Searches document chunks using keyword matching and question intent.

    This version improves ranking by:
    - ignoring weak common words
    - lowering broad sections like Topic
    - boosting sections that match the user's question type
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
        "practical explanation"
    }

    weak_sections = {
        "useful questions",
        "source",
        "disclaimer",
        "introduction",
        "topic"
    }

    question_lower = question.lower()

    question_words = [
        word for word in clean_words(question)
        if len(word) > 2 and word not in stopwords
    ]

    results = []

    for chunk in chunks:
        chunk_words = clean_words(chunk["content"])
        chunk_text = chunk["content"].lower()
        section_text = chunk["section"].lower()

        score = 0

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
            if "key idea" in section_text:
                score += 15
            if "important points" in section_text:
                score += 15
            if "incident reporting" in section_text:
                score += 10

        if "dataintrång" in question_lower or "data intrusion" in question_lower or "unauthorized access" in question_lower:
            if "key idea" in section_text:
                score += 15
            if "legal reference" in section_text:
                score += 15
            if "practical explanation" in section_text:
                score += 15

        if score > 0:
            results.append(
                {
                    "filename": chunk["filename"],
                    "section": chunk["section"],
                    "content": chunk["content"],
                    "score": score
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
    content = best_match["content"]

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

    else:
        answer = (
            "CyberLex Sweden found a relevant trusted source section, but this prototype cannot yet generate a detailed legal explanation for this question."
        )

    return f"""
## Short answer

{answer}

## Source used

- File: `{best_match["filename"]}`
- Section: `{best_match["section"]}`
- Relevance score: `{best_match["score"]}`

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
        "digital",
        "compliance"
    }

    question_lower = question.lower()

    for keyword in allowed_keywords:
        if keyword in question_lower:
            return True

    return False


st.divider()

documents, chunks = load_chunks()

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
            "incident reporting, data protection, and related digital compliance topics."
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