# CyberLex Sweden Product Roadmap

## Purpose

This document describes the current prototype features, near-term improvements, future AI development path, and possible deployment improvements for CyberLex Sweden.

CyberLex Sweden is currently a local educational prototype. It uses trusted Markdown sources, rule-based search, and transparent answer structure instead of a full language model.

The roadmap helps separate what the prototype can do today from what could be added in future versions.

---

## Current prototype features

CyberLex Sweden currently includes the following prototype features:

- Local Markdown knowledge base in `data/`
- Source-based search and chunk ranking
- Source routing for clear topic questions
- Official source links with readable Markdown labels
- Source date and version notes
- Bilingual interface support for English and Swedish
- Auto language detection for user questions
- Rule-based short answers
- CyberLex attention level
- Practical explanation section
- Topic-based assessment checklist
- Collapsible source context
- Other matching source sections list
- Clickable example questions using Streamlit session state
- Sidebar prototype version label
- Sidebar future AI mode note
- Legal limitation notice

These features make the current version a transparent source-grounded educational prototype.

---

## Near-term improvements

Planned near-term improvements include:

- Add more Swedish and EU cybersecurity law sources
- Improve Swedish and English source summaries
- Add more test cases for each knowledge source
- Improve answer formatting and layout
- Add clearer visual styling for attention levels
- Improve source ranking for complex questions
- Add more documentation for source maintenance
- Review and strengthen disclaimers, Terms of Use, and Privacy Policy

---

## Future AI improvements

Future AI-related improvements may include:

- Vector search using ChromaDB or FAISS
- Retrieval-Augmented Generation, also called RAG
- AI-generated answers based only on trusted retrieved source sections
- Better multi-source answer synthesis
- Stronger citation handling
- Refusal when source material is insufficient
- Clear separation between legal information and practical guidance

The future AI version should remain source-grounded and should not answer legal or compliance questions from general model memory alone.

---

## Possible deployment improvements

Possible deployment improvements include:

- Public deployment through Streamlit Community Cloud, Render, Azure, or AWS
- Environment-based configuration
- Better project branding
- Improved UI layout for mobile screens
- Public-facing README updates
- Clear user-facing legal disclaimer

---

## Long-term vision

The long-term goal is to develop CyberLex Sweden into a source-grounded cyber/legal assistant for Swedish and EU cybersecurity law topics.

A future version should be able to:

- search by meaning instead of only keywords
- combine information from several trusted sources
- generate natural language answers from retrieved source sections
- show clear citations and source metadata
- refuse questions when trusted source material is missing
- support Swedish and English users
- remain educational and transparent

CyberLex Sweden should continue to prioritize source transparency, legal limitations, and cautious wording.