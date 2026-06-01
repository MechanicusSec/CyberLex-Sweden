# CyberLex Sweden AI and RAG Plan

## Purpose

CyberLex Sweden is currently a source-based educational prototype that searches local Markdown knowledge files and generates rule-based answers.

A future version could use AI to produce more natural, complete, and flexible answers. However, because the project deals with cybersecurity law, GDPR, NIS2, incident reporting, DORA, cybercrime, and digital compliance, the AI must remain source-grounded.

CyberLex Sweden should not provide legal advice and should not answer legal or compliance questions without trusted source material.

---

## Current system

The current CyberLex Sweden prototype uses:

- Local Markdown files in `data/`
- Keyword-based search
- Source routing
- Chunk ranking
- Rule-based answer generation
- Official source links
- Source date and version notes
- Matched source excerpts
- Out-of-scope refusal

This makes the current system simple, transparent, and suitable for an educational prototype.

---

## Future AI goal

The future goal is to make CyberLex Sweden answer more naturally while still using trusted sources.

A future AI version should be able to:

- Read the user question
- Search the CyberLex knowledge base
- Retrieve relevant source sections
- Summarize legal and compliance information in plain language
- Combine information from multiple trusted source sections
- Include source references
- Show official source links
- Show source date and version notes
- Refuse to answer if no trusted source is found
- Clearly state that the answer is not legal advice

---

## Recommended architecture: RAG

The recommended future architecture is Retrieval-Augmented Generation, also called RAG.

RAG means that the system retrieves relevant trusted source material before generating an answer.

The flow should be:

1. The user asks a question.
2. CyberLex checks whether the question is within scope.
3. CyberLex searches trusted source documents.
4. CyberLex retrieves the most relevant source sections.
5. An AI model receives the user question and the retrieved source text.
6. The AI writes an answer based only on those sources.
7. CyberLex displays the answer, citations, official links, source metadata, and disclaimer.

The AI should not answer from general memory alone.

---

## Future answer flow

```text
User question
↓
Scope check
↓
Source retrieval
↓
Best matching chunks selected
↓
AI receives question + trusted source excerpts
↓
AI generates source-grounded answer
↓
CyberLex displays answer, citations, official links, source metadata, and disclaimer