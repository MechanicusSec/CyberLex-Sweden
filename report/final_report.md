# CyberLex Sweden Final Report

## Project Title

CyberLex Sweden: An AI Assistant Prototype for Swedish Cybersecurity Law and Digital Compliance

## Student

Robert Banderby

## Project Summary

CyberLex Sweden is a final school project focused on building a prototype AI-style assistant for Swedish cybersecurity law and digital compliance.
## Source Quality Policy

CyberLex Sweden includes a source quality policy documented in:

```text
docs/source_policy.md

The goal of the project is to make legal and cybersecurity information easier to search and understand by using a structured knowledge base, source-based search, and simple answer generation.

The current prototype focuses on:

- GDPR and personal data breaches
- NIS2 and Swedish cybersecurity responsibilities
- Swedish cybercrime law and dataintrång
- Incident reporting
- Out-of-scope question refusal

CyberLex Sweden is an educational project and does not provide official legal advice.

---

## 1. Background

Cybersecurity law can be difficult to understand because relevant information is spread across different sources, including Swedish law, EU regulations, government agencies, cybersecurity authorities, and data protection guidance.

For students, IT workers, and smaller organizations, it can be hard to quickly understand which rules may apply in a cyber incident or digital compliance situation.

CyberLex Sweden was created as a prototype to explore how an AI-style assistant could help users find and understand Swedish cybersecurity law information in a safer and more structured way.

---

## 2. Problem Description

The main problem is that cybersecurity-related legal information is often:

- spread across several authorities and legal sources
- written in complex legal or administrative language
- difficult to search for without knowing the exact legal terms
- risky to explain incorrectly if an AI system guesses without sources

A normal chatbot may give confident but unsupported answers. This is especially risky in legal topics.

CyberLex Sweden tries to reduce that risk by using a local trusted knowledge base and showing which source section was used.

---

## 3. Project Goal

The goal of the project was to build a working prototype that can:

- load trusted local knowledge base files
- search legal and cybersecurity information by topic
- match user questions to relevant source sections
- generate simple source-based answers
- show source file and source section
- refuse unsupported out-of-scope questions

---

## 4. Scope

The current prototype covers a limited set of Swedish cybersecurity law topics:

- GDPR and personal data breach reporting
- IMY and data protection responsibility
- NIS2 and the Swedish Cybersecurity Act
- cybersecurity incident reporting
- dataintrång under Swedish criminal law

The prototype does not cover all Swedish law. It also does not provide legal advice.

---

## 5. Tools and Technologies

### Visual Studio Code

Visual Studio Code was used as the main code editor.

It was used to write:

- Python code
- Markdown documentation
- project notes
- test cases
- the final report

### Python

Python was used as the main programming language for the application.

Python was chosen because it is widely used for AI, data processing, web prototypes, and automation.

### Streamlit

Streamlit was used to create the local web application.

Streamlit makes it possible to turn a Python script into a browser-based interface with input fields, text output, sidebars, and warning messages.

### Markdown

Markdown was used for documentation and knowledge base files.

Markdown is simple to read and works well for project documentation, GitHub, and structured text files.

### Git

Git was used for version control.

Git tracks changes in the project, makes it possible to create commits, and helps document the development process.

### GitHub

GitHub was used to store the project online.

GitHub makes it possible to show the project code, documentation, commits, and development history.

---

## 6. Project Structure

The project is organized into several folders:

```text
CyberLex-Sweden
├── app
├── data
├── docs
├── report
├── screenshots
├── sources
├── .gitignore
├── COPYRIGHT.md
├── README.md
└── requirements.txt