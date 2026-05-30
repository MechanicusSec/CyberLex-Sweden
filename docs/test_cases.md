# CyberLex Sweden Test Cases

## Purpose

This document contains manual test cases for the CyberLex Sweden prototype.

The goal is to verify that the application can:

- Load trusted knowledge base files
- Search source material by chunks
- Match user questions to relevant source sections
- Generate simple source-based answers
- Show the source file and source section used
- Avoid unsupported answers when no trusted source exists

---

## Test Environment

The tests were performed locally using:

- Windows 11
- Visual Studio Code
- Python virtual environment
- Streamlit
- Local Markdown knowledge base files in the `data/` folder

Application command:

```powershell
streamlit run app/main.py