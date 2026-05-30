from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="CyberLex Sweden",
    page_icon="🔐",
    layout="wide"
)

DATA_DIR = Path("data")


def load_documents():
    """
    Loads all Markdown files from the data folder.
    Each Markdown file becomes one searchable document.
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


def clean_words(text):
    """
    Converts text into simple searchable words.
    This removes basic punctuation and makes everything lowercase.
    """
    punctuation = ",.?!:;()[]{}\"'`"
    text = text.lower()

    for mark in punctuation:
        text = text.replace(mark, " ")

    return text.split()


def search_documents(question, documents):
    """
    Searches the documents using keyword matching.
    Each document gets a score based on how many question words appear in it.
    """
    question_words = clean_words(question)
    results = []

    for doc in documents:
        content_words = clean_words(doc["content"])
        content_text = doc["content"].lower()

        score = 0

        for word in question_words:
            if len(word) > 2 and word in content_words:
                score += 2
            elif len(word) > 2 and word in content_text:
                score += 1

        if score > 0:
            results.append(
                {
                    "filename": doc["filename"],
                    "content": doc["content"],
                    "score": score
                }
            )

    results.sort(key=lambda item: item["score"], reverse=True)
    return results


def create_excerpt(content, question, excerpt_length=700):
    """
    Creates a shorter excerpt from the source document.
    It tries to find the first word from the question inside the source text.
    """
    content_lower = content.lower()
    question_words = clean_words(question)

    match_position = 0

    for word in question_words:
        if len(word) > 2:
            position = content_lower.find(word)
            if position != -1:
                match_position = position
                break

    start = max(match_position - 200, 0)
    end = min(start + excerpt_length, len(content))

    excerpt = content[start:end].strip()

    if start > 0:
        excerpt = "... " + excerpt

    if end < len(content):
        excerpt = excerpt + " ..."

    return excerpt


def create_basic_answer(question, best_match, excerpt):
    """
    Creates a simple structured answer using the best matching source.
    This is not full AI yet, but it formats the retrieved source into a clearer answer.
    """
    return f"""
## Short answer

CyberLex Sweden found information related to your question in the trusted knowledge base.

**Your question:** {question}

The most relevant source is:

**{best_match["filename"]}**

This means the question appears to be connected to the topic described in that source file. The source excerpt below should be used to understand the answer.

## Source used

- `{best_match["filename"]}`
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

documents = load_documents()

st.sidebar.header("Knowledge Base")
st.sidebar.write(f"Loaded documents: {len(documents)}")

for doc in documents:
    st.sidebar.write(f"- {doc['filename']}")

st.header("Ask a question")

question = st.text_input(
    "Write a question about Swedish cybersecurity law:"
)

if question:
    search_results = search_documents(question, documents)

    if search_results:
        best_match = search_results[0]
        excerpt = create_excerpt(best_match["content"], question)

        st.subheader("CyberLex Answer")
        st.markdown(create_basic_answer(question, best_match, excerpt))

        st.subheader("Matched Source Excerpt")
        st.text_area(
            "Relevant excerpt",
            excerpt,
            height=250
        )

        st.subheader("All Matching Sources")

        for result in search_results:
            st.write(
                f"**{result['filename']}** - relevance score: {result['score']}"
            )

        st.info(
            "Next development step: replace the basic keyword search with stronger AI-assisted answers and better citations."
        )

    else:
        st.error(
            "No trusted source was found for this question. "
            "CyberLex Sweden cannot answer confidently yet."
        )
else:
    st.write("Enter a question above to search the CyberLex Sweden knowledge base.")