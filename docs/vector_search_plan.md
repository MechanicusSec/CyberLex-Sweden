# CyberLex Sweden Vector Search Plan

## Purpose

This document explains the planned vector search upgrade for CyberLex Sweden.

The current CyberLex Sweden prototype uses local Markdown files, source routing, keyword scoring, topic expansion, rule-based answers, and transparent source display.

The next AI improvement is to add vector search so the app can match questions by meaning, not only by exact keywords.

---

## Current search method

CyberLex Sweden currently uses rule-based local search.

The current search system:

- loads Markdown files from the `data/` folder
- splits the files into source chunks
- cleans the user question into searchable words
- expands important terms with related cybersecurity and legal words
- scores source chunks based on word overlap and section relevance
- routes clear questions to the most relevant source file
- returns the best source match and supporting source context

This works well for clear questions, but it still depends heavily on keywords.

---

## Why vector search is useful

Vector search helps CyberLex Sweden understand meaning.

For example, these questions may mean similar things:

```text
What should a company do after a ransomware attack?
```