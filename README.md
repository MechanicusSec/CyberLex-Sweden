# CyberLex Sweden

CyberLex Sweden is a final school project focused on building an AI-style assistant for Swedish cybersecurity law and digital compliance.

The goal is to help users search and understand selected Swedish cyber law topics by using a trusted local knowledge base, source-based search, simple answer generation, and official source links.

CyberLex Sweden is an educational prototype. It does not provide official legal advice.

---

## Project Purpose

Cybersecurity law can be difficult to understand because relevant information is spread across different sources, such as:

- Swedish law
- EU regulations and directives
- Swedish government agencies
- cybersecurity authorities
- data protection authorities

CyberLex Sweden explores how a focused AI-style assistant can help users find relevant cybersecurity law information in a safer and more transparent way.

---

## Current Features

The current prototype can:

- Load local Markdown knowledge base files
- Split source documents into searchable chunks
- Match user questions to relevant source sections
- Generate simple source-based answers
- Display the source file and source section used
- Display official source links connected to the answer
- Show the matched source excerpt
- Refuse out-of-scope questions
- Display legal disclaimers

---

## Current Scope

CyberLex Sweden currently focuses on:

- GDPR and personal data breaches
- IMY and data protection responsibility
- NIS2 and Swedish cybersecurity responsibilities
- Cybersecurity incident reporting
- Swedish cybercrime law
- Dataintrång
- Unauthorized access and information system interference

Out-of-scope questions, such as Swedish tax law, should be refused by the application.

---

## Tools and Technologies

| Tool | Purpose |
|---|---|
| Python | Main programming language used to build the app |
| Streamlit | Creates the local web interface |
| Markdown | Used for documentation and knowledge base files |
| Git | Tracks project changes and commit history |
| GitHub | Stores the project online |
| VS Code | Code editor used during development |

---

## Project Structure

```text
CyberLex-Sweden
├── app
│   └── main.py
├── data
│   ├── cybercrime_dataintrang.md
│   ├── gdpr_personal_data_breach.md
│   └── nis2_cybersecurity_law.md
├── docs
│   ├── project_overview.md
│   ├── project_plan.md
│   ├── source_list.md
│   ├── source_policy.md
│   └── test_cases.md
├── report
│   └── final_report.md
├── screenshots
├── sources
│   └── notes
├── .gitignore
├── COPYRIGHT.md
├── README.md
└── requirements.txt