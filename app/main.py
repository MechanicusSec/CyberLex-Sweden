import streamlit as st

st.set_page_config(
    page_title="CyberLex Sweden",
    page_icon="⚖️",
    layout="wide"
)

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

st.header("Ask a question")

question = st.text_input(
    "Write a question about Swedish cybersecurity law:"
)

if question:
    st.subheader("Answer")
    st.write(
        "This is the first prototype. Later, this answer will be generated using trusted Swedish and EU legal sources."
    )

    st.subheader("Your question")
    st.write(question)

    st.info(
        "Next development step: connect the app to a source-based document search system."
    )
else:
    st.write("Enter a question above to test the interface.")