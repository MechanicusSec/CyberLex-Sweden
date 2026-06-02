# Project Overview: CyberLex Sweden

## Project Name

CyberLex Sweden

## Current Prototype Version

CyberLex Sweden is currently at **prototype version 0.5**.

This version includes a local Streamlit application with a styled answer layout, source-grounded responses, bilingual interface support, citation details, official source links, source metadata, practical explanations, and assessment checklists.

## Project Idea

CyberLex Sweden is an educational legal-tech and cybersecurity assistant focused on Swedish cybersecurity law, EU cybersecurity regulation, and digital compliance.

The system is designed to answer questions about cybercrime, GDPR, NIS2, incident reporting, data protection, cybersecurity responsibilities, and related EU digital compliance rules that affect Sweden.

The long-term goal is to develop CyberLex Sweden into an AI-powered assistant. The current version is still a local, rule-based prototype that uses selected Markdown source files instead of a full language model.

## Problem

Cybersecurity law is difficult to understand because relevant information is spread across many different places, including:

- Swedish laws
- EU regulations and directives
- Government agencies
- Legal guidance documents
- Cybersecurity authorities
- Data protection authorities
- Sector-specific compliance rules

This makes it hard for students, IT workers, and small organizations to quickly understand which rules may apply in different situations.

## Solution

CyberLex Sweden uses a local knowledge base together with rule-based search and answer generation to provide clear educational answers in plain English or Swedish.

The system should not guess. It should answer based on selected documents, trusted source material, and official references.

The current prototype can:

- Load local Markdown source files from the `data/` folder
- Split documents into searchable sections
- Match user questions against relevant source sections
- Route clear topic questions to the correct source file
- Display citation details
- Display official source links
- Display source metadata
- Show important legal limitations
- Generate a short educational answer
- Generate a practical explanation
- Generate a topic-based assessment checklist
- Show relevant source context
- Show other matching source sections
- Refuse questions outside the project scope

## Target Users

CyberLex Sweden is designed for:

- IT students
- Cybersecurity students
- IT support staff
- Small organizations
- People learning about Swedish cybersecurity law
- People who want a clearer overview of GDPR, NIS2, cybercrime, and digital compliance topics

## Supported Topic Areas

The current prototype supports source-based educational answers about:

- GDPR
- Personal data breaches
- IMY and Swedish data protection supervision
- NIS2
- Swedish Cybersecurity Act topics
- Cybercrime and dataintrång
- EU Cyber Resilience Act
- DORA
- Incident reporting
- Digital compliance responsibilities

## Current Knowledge Base

The current local knowledge base includes Markdown files in the `data/` folder, including topics such as:

- Swedish cybercrime and dataintrång
- EU attacks against information systems
- EU Cyber Resilience Act
- DORA digital operational resilience
- GDPR core principles
- GDPR personal data breach reporting
- IMY GDPR supervision
- NIS2 cybersecurity law
- NIS2 incident reporting

## Example Questions

Example questions CyberLex Sweden should be able to handle include:

- Is unauthorized access illegal in Sweden?
- What should a company do after a ransomware attack?
- What is the difference between GDPR and NIS2?
- When must a personal data breach be reported?
- Can an incident need to be reported under both NIS2 and GDPR?
- Which Swedish authorities are involved in cybersecurity law?
- What legal responsibilities does an organization have after a cyber incident?
- What is DORA?
- What is the Cyber Resilience Act?
- What is dataintrång?

## Out-of-Scope Questions

CyberLex Sweden should refuse questions that are not related to Swedish or EU cybersecurity law, data protection, cybercrime, incident reporting, or digital compliance.

For example, the system should refuse questions about:

- Swedish tax law
- Family law
- General criminal law outside cybercrime
- Medical advice
- Investment advice
- Unrelated political topics
- General trivia

The refusal should explain that the question is outside the scope of CyberLex Sweden.

## Limitations

CyberLex Sweden is an educational prototype and does not provide official legal advice.

The system may help users understand legal and compliance concepts, but it cannot replace official sources, legal counsel, or professional compliance review.

For serious legal matters, users should always check official sources or contact a qualified legal professional.

## Future Development

Planned future improvements include:

- Adding more Swedish and EU legal sources
- Improving search ranking for complex questions
- Adding vector search with ChromaDB or FAISS
- Adding a future AI/RAG mode
- Improving citation formatting further
- Expanding Swedish and English support
- Improving the visual design
- Preparing public deployment
- Strengthening the legal disclaimer, privacy policy, and terms of use
- Reviewing possible trademark and brand protection if the project develops further