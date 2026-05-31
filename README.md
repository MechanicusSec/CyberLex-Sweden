# CyberLex Sweden

CyberLex Sweden is a final school project focused on building an AI-style assistant for Swedish cybersecurity law and digital compliance.

The goal is to help users search and understand selected Swedish and EU cyber law topics by using a trusted local knowledge base, source-based search, simple answer generation, citation details, source metadata, and official source links.

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
- Route specific questions to the most relevant source file
- Generate simple source-based answers
- Display structured citation details
- Display the source file and source section used
- Display official source links connected to the answer
- Display source metadata, including source date and version notes
- Show the matched source excerpt
- Refuse out-of-scope questions
- Display legal disclaimers

---

## Current Scope

CyberLex Sweden currently focuses on:

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

Out-of-scope questions, such as Swedish tax law, should be refused by the application.

---

## Source Coverage

CyberLex Sweden currently includes source material about:

- GDPR and personal data breach notification in Sweden
- IMY and Swedish GDPR supervision
- GDPR core principles
- NIS2 and the Swedish Cybersecurity Act
- NIS2 incident reporting
- Swedish cybercrime law and dataintrång
- EU attacks against information systems
- EU Cyber Resilience Act
- EU DORA, the Digital Operational Resilience Act, for financial-sector cybersecurity and ICT resilience

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

## Documentation

Additional project documentation is available in the `docs/` folder:

- `docs/project_overview.md` - project overview and background
- `docs/project_plan.md` - project plan and schedule
- `docs/source_list.md` - trusted source list
- `docs/source_policy.md` - source quality policy
- `docs/test_cases.md` - manual test cases
- `docs/technical_design.md` - application architecture and technical design

---

## Project Structure

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

## How to Run the Project Locally

Create and activate the Python virtual environment, then start the Streamlit app.

```powershell
.\venv\Scripts\Activate.ps1
```

This activates the local Python environment used by the project.

```powershell
streamlit run app/main.py
```

This starts the CyberLex Sweden web application locally in the browser.

---

## Important Limitation

CyberLex Sweden is an educational prototype.

The application gives simplified source-based explanations from a local knowledge base. It does not provide legal advice and should not replace official authority guidance, qualified legal advice, or current legal sources.

---

## Future Improvements

Planned improvements include:

- Adding more Swedish and EU cybersecurity law sources
- Adding vector search with ChromaDB or FAISS
- Connecting a language model for better natural language answers
- Improving citation formatting
- Adding source update history
- Improving the visual design
- Deploying the app publicly
- Adding Terms of Use and Privacy Policy
- Considering trademark protection if the project develops further