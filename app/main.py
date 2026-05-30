from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="CyberLex Sweden",
    page_icon="⚖️",
    layout="wide"
)

DATA_DIR = Path("data")


def load_documents():
    """
    Loads all Markdown files from the data folder.
    Each file becomes one searchable document.
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


def search_documents(question, documents):
    """
    Searches the documents using simple keyword matching.
    This is a basic first version before adding real AI/vector search.
    """
    question_words = question.lower().split()
    results = []

    for doc in documents:
        content_lower = doc["content"].lower()
        score = 0

        for word in question_words:
            if word in content_lower:
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


def create_basic_answer(question, best_match):
    """
    Creates a simple answer using the best matching document.
    Later this will be replaced with an AI-generated answer.
    """
    return f"""
CyberLex Sweden found a relevant source for your question:

**Question:** {question}

Based on the current knowledge base, this topic is covered in:

**Source file:** `{best_match["filename"]}`

The system is currently using simple document search. In the next version, this will be upgraded to AI-generated answers with stronger source references.
"""


st.title("CyberLex Sweden")
st.subheader("AI Assistant for Swedish Cybersecurity Law and Digital Compliance")

st.markdown("""
CyberLex Sweden is a final school project focused on creating an AI assistant that helps users understand Swedish cybersecurity law.

The system is planned to cover topics such as:

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

        st.subheader("Answer")
        st.markdown(create_basic_answer(question, best_match))

        st.subheader("Matched source content")
        st.text_area(
            "Source excerpt",
            best_match["content"],
            height=350
        )

        st.info(
            "This answer is based on a local source file. "
            "The next development step is to add AI-generated explanations and better citations."
        )

    else:
        st.error(
            "No trusted source was found for this question. "
            "CyberLex Sweden cannot answer confidently yet."
        )
else:
    st.write("Enter a question above to search the CyberLex Sweden knowledge base.")