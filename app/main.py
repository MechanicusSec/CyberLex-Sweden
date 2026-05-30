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
    """
    filename = document["filename"]
    content = document["content"]

    chunks = []
    current_title = "Introduction"
    current_lines = []

    for line in content.splitlines():
        if line.startswith("#"):
            if current_lines:
                chunks.append(
                    {
                        "filename": filename,
                        "section": current_title,
                        "content": "\n".join(current_lines).strip()
                    }
                )

            current_title = line.replace("#", "").strip()
            current_lines = [line]
        else:
            current_lines.append(line)

    if current_lines:
        chunks.append(
            {
                "filename": filename,
                "section": current_title,
                "content": "\n".join(current_lines).strip()
            }
        )

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
    Searches document chunks using keyword matching.
    This version ignores weak common words and gives better scores to useful legal content sections.
    """
    stopwords = {
        "what", "when", "where", "which", "who", "why", "how",
        "is", "are", "was", "were", "be", "been", "being",
        "a", "an", "the", "to", "in", "on", "of", "for", "and",
        "or", "with", "from", "this", "that", "it", "does", "do"
    }

    useful_sections = {
        "key idea",
        "reporting to imy",
        "main authority",
        "important points",
        "incident reporting",
        "legal reference",
        "practical explanation",
        "topic"
    }

    weak_sections = {
        "useful questions",
        "source",
        "disclaimer"
    }

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

        for word in question_words:
            if word in chunk_words:
                score += 4

            if word in section_text:
                score += 3

            if word in chunk_text:
                score += 1

        for useful_section in useful_sections:
            if useful_section in section_text:
                score += 5

        for weak_section in weak_sections:
            if weak_section in section_text:
                score -= 8

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


def create_basic_answer(question, best_match):
    """
    Creates a simple structured answer using the best matching source chunk.
    This is still not full AI, but it gives a clearer source-grounded result.
    """
    return f"""
## Short answer

CyberLex Sweden found information related to your question in the trusted knowledge base.

**Your question:** {question}

The most relevant source section is:

**{best_match["section"]}**

from:

**{best_match["filename"]}**

This means the question appears to be connected to this specific source section. The source excerpt below should be used to understand the answer.

## Source used

- File: `{best_match["filename"]}`
- Section: `{best_match["section"]}`
- Relevance score: `{best_match["score"]}`

## Important limitation

This answer is based on source matching and a simplified local knowledge base. CyberLex Sweden does not provide legal advice.
"""


st.title("CyberLex Sweden")
st.subheader("AI Assistant for Swedish Cybersecurity Law and Digital Compliance")

st.markdown("""
CyberLex Sweden is a final school project focused on creating an AI assistant that helps users understand Swedish cybersecurity law.

The system is designed to work with trusted sources about:

- Swedish cybercrime law
- GDPR and personal data breaches
- NIS2 and cybersecurity responsibilities
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
    search_results = search_chunks(question, chunks)

    if search_results:
        best_match = search_results[0]

        st.subheader("CyberLex Answer")
        st.markdown(create_basic_answer(question, best_match))

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