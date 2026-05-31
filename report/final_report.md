# CyberLex Sweden Final Report

## Project Title

CyberLex Sweden: An AI Assistant Prototype for Swedish Cybersecurity Law and Digital Compliance

## Student

Robert Banderby

---

## Project Summary

CyberLex Sweden is a final school project focused on building a prototype AI-style assistant for Swedish cybersecurity law and digital compliance.

The goal of the project is to make selected legal and cybersecurity information easier to search and understand by using a structured local knowledge base, source-based search, simple answer generation, official source links, source metadata, and citation details.

The current prototype focuses on Swedish and EU cybersecurity-related legal topics, including GDPR, IMY, NIS2, Swedish cybercrime law, EU cybersecurity law, the Cyber Resilience Act, and DORA.

CyberLex Sweden is an educational prototype. It does not provide official legal advice.

---

## Source Quality Policy

CyberLex Sweden also includes a source update history documented in:

```text
docs/source_update_history.md
```

The purpose of the source quality policy is to make sure that the project uses trusted and traceable legal or authority-based sources.

The project prioritizes:

- official government sources
- official authority sources
- official EU legal sources
- clear source references
- source dates
- version notes
- educational summaries that can be reviewed

This is important because legal and cybersecurity topics can be risky if an application gives unsupported or unclear answers.

---

## 1. Background

Cybersecurity law can be difficult to understand because relevant information is spread across many different sources.

These sources can include:

- Swedish laws
- EU regulations
- EU directives
- Swedish government agencies
- cybersecurity authorities
- data protection authorities
- official legal databases

For students, IT workers, and smaller organizations, it can be difficult to quickly understand which rules may apply in a cyber incident or digital compliance situation.

A normal chatbot may give confident but unsupported answers. This is especially risky in legal topics.

CyberLex Sweden was created as a prototype to explore how an AI-style assistant could help users find and understand selected cybersecurity law information in a safer and more transparent way.

---

## 2. Problem Description

The main problem is that cybersecurity-related legal information is often:

- spread across several authorities and legal sources
- written in complex legal or administrative language
- difficult to search without knowing the exact legal terms
- risky to summarize incorrectly
- unsuitable for unsupported AI guessing

CyberLex Sweden tries to reduce that risk by using a local trusted knowledge base and showing which source file and source section were used for each answer.

The prototype does not try to replace a lawyer, court, authority, or official legal source.

---

## 3. Project Goal

The goal of the project was to build a working prototype that can:

- load trusted local knowledge base files
- search legal and cybersecurity information by topic
- split Markdown source files into searchable chunks
- match user questions to relevant source sections
- route specific questions to the correct knowledge file
- generate simple source-based answers
- show the source file and source section used
- display structured citation details
- display official source links
- display source metadata
- show the matched source excerpt
- refuse unsupported out-of-scope questions

---

## 4. Scope

The current prototype covers a limited set of Swedish and EU cybersecurity law topics.

The current scope includes:

- GDPR and personal data breach notification in Sweden
- IMY and Swedish GDPR supervision
- GDPR core principles
- NIS2 and the Swedish Cybersecurity Act
- NIS2 incident reporting
- Swedish cybercrime law and dataintrång
- EU attacks against information systems
- EU Cyber Resilience Act
- EU DORA, the Digital Operational Resilience Act
- Digital compliance and cybersecurity-related legal topics

The prototype does not cover all Swedish law.

For example, a question about Swedish tax law should be refused because it is outside the CyberLex Sweden project scope.

---

## 5. Tools and Technologies

### Visual Studio Code

Visual Studio Code was used as the main code editor.

It was used to write:

- Python code
- Markdown documentation
- source files
- test cases
- the final report

### Python

Python was used as the main programming language for the application.

Python was chosen because it is widely used for web prototypes, automation, data processing, and AI-related projects.

### Streamlit

Streamlit was used to create the local web application.

Streamlit makes it possible to turn a Python script into a browser-based interface with input fields, sidebars, formatted text, warnings, and result sections.

### Markdown

Markdown was used for documentation and knowledge base files.

Markdown is simple to read and works well for GitHub documentation, structured notes, and source-based text files.

### Git

Git was used for version control.

Git tracks changes in the project and creates a development history through commits.

### GitHub

GitHub was used to store the project online.

GitHub makes it possible to show the code, documentation, project history, and commits.

---

## 6. Project Structure

The project is organized into several folders:

```text
CyberLex-Sweden
├── app
│   └── main.py
├── data
│   ├── cybercrime_dataintrang.md
│   ├── eu_attacks_against_information_systems.md
│   ├── eu_cyber_resilience_act.md
│   ├── eu_dora_digital_operational_resilience.md
│   ├── gdpr_core_principles.md
│   ├── gdpr_personal_data_breach.md
│   ├── imy_gdpr_supervision.md
│   ├── nis2_cybersecurity_law.md
│   └── nis2_incident_reporting.md
├── docs
│   ├── project_overview.md
│   ├── project_plan.md
│   ├── source_list.md
│   ├── source_policy.md
│   ├── technical_design.md
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
```

---

## 7. Knowledge Base

CyberLex Sweden uses local Markdown files as its trusted knowledge base.

Each file in the `data` folder represents one legal or regulatory topic.

The current knowledge base includes:

| File | Topic |
|---|---|
| `gdpr_personal_data_breach.md` | GDPR personal data breaches and IMY breach notification |
| `imy_gdpr_supervision.md` | IMY and Swedish GDPR supervision |
| `gdpr_core_principles.md` | GDPR core principles |
| `nis2_cybersecurity_law.md` | NIS2 and the Swedish Cybersecurity Act |
| `nis2_incident_reporting.md` | NIS2 incident reporting in Sweden |
| `cybercrime_dataintrang.md` | Swedish cybercrime law and dataintrång |
| `eu_attacks_against_information_systems.md` | EU rules on attacks against information systems |
| `eu_cyber_resilience_act.md` | EU Cyber Resilience Act |
| `eu_dora_digital_operational_resilience.md` | EU DORA and financial-sector digital operational resilience |

Each knowledge file is structured with headings such as:

- Topic
- Main authority or legal source
- Key idea
- Important points
- Cybersecurity connection
- Useful questions
- Official source
- Source date
- Version notes
- Disclaimer

This structure makes it easier for the app to search and display relevant source sections.

---

## 8. Application Functionality

The current application can:

1. Load Markdown files from the `data` folder
2. Extract official source links from the knowledge base files
3. Extract source date and version notes from knowledge base files
4. Split documents into smaller chunks based on Markdown headings
5. Check whether a question belongs to the CyberLex Sweden project scope
6. Search chunks using keyword matching, question intent, and source routing
7. Select the best matching source chunk
8. Generate simple source-based answers
9. Display structured citation details
10. Display official source links
11. Display source metadata
12. Display the matched source excerpt
13. Refuse questions outside the project scope

---

## 9. How the Application Works

The application follows this basic flow:

```text
User question
↓
Scope check
↓
Source routing
↓
Chunk search
↓
Best source match
↓
Simple answer generation
↓
Citation details and source excerpt display
```

First, the user enters a question in the Streamlit interface.

The application checks whether the question is inside the project scope.

If the question is outside the scope, the application refuses to answer.

If the question is inside the scope, the application searches the local Markdown knowledge base.

The search system uses:

- question keywords
- source section titles
- source text
- useful section bonuses
- weak section penalties
- source routing for specific legal topics

The best matching source section is then used to generate a simple answer.

The app also displays the source file, source section, relevance score, official source links, source metadata, and matched source excerpt.

This makes the answer more transparent and reviewable.

---

## 10. Source Routing

Source routing was added to improve accuracy.

Some legal topics share similar words, especially GDPR, NIS2, cybersecurity incidents, and data protection. Without routing, the app may choose the wrong source file.

Source routing helps direct specific questions to the correct knowledge file.

Examples:

| Question type | Target source |
|---|---|
| What is IMY? | `imy_gdpr_supervision.md` |
| What are the GDPR principles? | `gdpr_core_principles.md` |
| What is NIS2 incident reporting? | `nis2_incident_reporting.md` |
| What is dataintrång? | `cybercrime_dataintrang.md` |
| What is the Cyber Resilience Act? | `eu_cyber_resilience_act.md` |
| What is DORA? | `eu_dora_digital_operational_resilience.md` |

This makes the prototype more reliable than simple keyword matching alone.

---

## 11. Citation Details and Source Metadata

CyberLex Sweden displays citation details for each supported answer.

The citation details include:

- matched knowledge file
- matched section
- relevance score
- official source links
- source date
- version notes

The source metadata helps show when a source summary was last checked and what version of the educational summary is being used.

Example metadata:

```text
Source date: Last checked: 2026-05-31
Version notes: Initial educational summary added for CyberLex Sweden.
```

This improves transparency and makes the project easier to review.

---

## 12. Testing

Manual testing was documented in:

```text
docs/test_cases.md
```

The tests checked that CyberLex Sweden can:

- load trusted knowledge files
- match questions to relevant source sections
- generate simple source-based answers
- display citation details
- display official source links
- display source metadata
- refuse unsupported questions

Tested questions included:

- What authority handles GDPR in Sweden?
- When must a personal data breach be reported?
- What is NIS2?
- What is dataintrång?
- What are the GDPR principles?
- What is the Cyber Resilience Act?
- What is DORA?
- What is third-party ICT risk under DORA?
- What is Swedish tax law?

The out-of-scope test for Swedish tax law was successfully refused.

---

## 13. Results

The project successfully produced a working local prototype.

The prototype can answer supported cybersecurity-law questions using local trusted source files.

It can show:

- a short source-based answer
- the matched source file
- the matched source section
- a relevance score
- official source links
- source metadata
- the matched source excerpt
- an important legal limitation

The project also successfully refuses out-of-scope questions when no trusted source exists.

This shows that CyberLex Sweden can provide a more controlled and transparent approach than a general chatbot for selected cybersecurity-law topics.

---

## 14. Limitations

The current prototype has several limitations:

- It only covers selected Swedish and EU cybersecurity law topics
- It uses simplified educational summaries
- It does not yet use vector search
- It does not yet use a full language model
- It does not provide legal advice
- It depends on the quality and completeness of the local knowledge base
- It may still need more detailed source routing as the knowledge base grows
- It is currently a local prototype and is not publicly deployed

These limitations are acceptable for the current prototype stage.

The purpose is to demonstrate the concept, not to replace legal professionals or official authorities.

---

## 15. Future Improvements

Future improvements include:

- adding more Swedish and EU legal sources
- adding vector search with ChromaDB or FAISS
- connecting a language model for better natural language answers
- improving citation formatting
- adding source update history
- improving the visual design
- deploying the app publicly
- adding Terms of Use and Privacy Policy
- considering trademark protection if the project develops further

---

## 16. Ethical and Legal Considerations

Because CyberLex Sweden deals with legal and cybersecurity-related topics, it is important that the project does not pretend to provide official legal advice.

The application includes a disclaimer explaining that the answers are simplified and educational.

CyberLex Sweden should not provide instructions for committing cybercrime.

The project should focus on lawful cybersecurity, education, legal awareness, compliance, and source-based explanations.

When the project grows, Terms of Use and a Privacy Policy should be added before public deployment.

The project also includes draft user-facing policy documents:

- `docs/terms_of_use.md`
- `docs/privacy_policy.md`
- `docs/legal_disclaimer.md`

These documents explain that CyberLex Sweden is an educational prototype, does not provide legal advice, should not be used for unlawful cybersecurity activity, and must be reviewed before any future public deployment.

---

## 17. Conclusion

CyberLex Sweden demonstrates how a focused AI-style assistant can help users search and understand selected Swedish and EU cybersecurity law topics.

The project uses a local trusted knowledge base, chunk-based search, source routing, simple answer generation, citation details, official source links, source metadata, and out-of-scope refusal.

The result is a working educational prototype that is transparent, reviewable, and safer than a general unsupported chatbot for this type of topic.

CyberLex Sweden is not a finished legal product, but it provides a strong foundation for future development.