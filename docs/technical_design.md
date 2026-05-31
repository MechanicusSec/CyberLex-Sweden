# CyberLex Sweden Technical Design

## Purpose

This document explains the technical design of the CyberLex Sweden prototype.

CyberLex Sweden is a local Streamlit application that answers questions about selected Swedish and EU cybersecurity law topics using a trusted local Markdown knowledge base.

The prototype does not use a full language model yet. Instead, it uses source-based search, question intent matching, and simple rule-based answer generation.

---

## Application Architecture

The application is built with:

- Python
- Streamlit
- Local Markdown files
- Rule-based source search
- Source metadata extraction
- Citation display

The main application file is:

```text
app/main.py