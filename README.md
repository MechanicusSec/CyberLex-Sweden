# CyberLex Sweden

CyberLex Sweden is a final school project and educational legal-tech prototype focused on Swedish and EU cybersecurity law, cyber incident response, GDPR, NIS2, DORA, the Cyber Resilience Act, cybercrime, data protection, and digital compliance.

CyberLex Sweden runs as a local Streamlit application. It searches a trusted local Markdown knowledge base and gives source-grounded, rule-based answers with official source links, source metadata, practical guidance where useful, and clear limitations.

CyberLex Sweden does **not** provide legal advice. It is built for learning, demonstration, and portfolio use.

---

## Project Purpose

Cybersecurity law and incident response can be difficult to understand because relevant information is spread across Swedish law, EU regulations, public authorities, data protection guidance, cybersecurity guidance, and practical incident-response material.

CyberLex Sweden explores how a focused assistant can help users find relevant cybersecurity-law and incident-response information in a safer and more transparent way.

The main design goal is:

```text
Better sources first. Better AI second.
```

The prototype should show where an answer comes from, what source section was matched, what practical steps may be relevant, and what limitations apply.

---

## Intended Audience

CyberLex Sweden is intended for:

- students and teachers reviewing cybersecurity-law topics
- junior IT and cybersecurity learners
- project reviewers and demo testers
- users who want a simplified overview of selected Swedish and EU cybersecurity-law topics
- users who want defensive incident-response learning support

It is not intended to replace official authority guidance, qualified legal advice, compliance review, or professional incident response.

---

## Current Prototype Status

CyberLex Sweden is currently a **source-grounded, rule-based prototype**.

It does not yet use:

- a full language model for answer generation
- live web browsing
- production vector search
- embeddings, ChromaDB, or FAISS

Vector search and RAG-style development have been investigated and documented, but implementation is paused until the local Python/package setup is stable.

---

## What CyberLex Does

CyberLex Sweden currently supports:

### Source-grounded answers

- loads local Markdown knowledge base files
- splits source documents into searchable chunks
- matches user questions to relevant source sections
- routes supported questions to stronger source files
- generates structured CyberLex summary answers
- shows official source links and source metadata

### Legal and compliance guidance

- explains selected GDPR, IMY, NIS2, DORA, Cyber Resilience Act, cybercrime, and digital compliance topics
- shows source freshness labels based on local review dates
- displays detected topic labels and CyberLex attention levels
- supports Swedish and English interface handling

### Defensive incident-response support

- gives defensive first-step guidance for selected practical incident questions
- supports suspicious login, phishing, compromised account, data leak, ransomware, malware, and suspected intrusion scenarios
- shows incident log templates where useful
- creates download-ready incident summaries for documentation support

### Safety boundaries

- refuses out-of-scope questions
- refuses or redirects unsafe offensive cyber requests
- keeps legal and incident-response disclaimers visible

Detailed behavior is documented in:

```text
docs/ui_behavior.md
docs/source_context_behavior.md
docs/testing_and_demo.md
docs/privacy_and_data_handling.md
```

---

## Supported Topics

CyberLex Sweden currently focuses on selected Swedish and EU cybersecurity-law topics and defensive incident-response topics.

### Legal and compliance topics

- GDPR and personal data breach notification in Sweden
- IMY and Swedish GDPR supervision
- GDPR core principles
- GDPR security measures
- NIS2 and the Swedish Cybersecurity Act
- NIS2 sector scope and applicability
- NIS2 incident reporting
- Swedish cybercrime law and unauthorized access offences, `dataintrång`
- EU attacks against information systems
- EU Cyber Resilience Act
- EU DORA, the Digital Operational Resilience Act
- digital compliance and cybersecurity-related legal topics

### Practical incident-response topics

- suspected hacking or intrusion
- suspicious login activity
- suspicious email and phishing
- compromised accounts
- data leaks
- personal data breach response
- ransomware and malware
- encrypted files
- evidence preservation
- incident documentation
- reporting assessment
- recovery planning

Out-of-scope questions, such as Swedish tax law, should be refused by the application.

Unsafe cyber requests, such as hacking, stealing credentials, hiding logs, deleting traces, or bypassing detection, should also be refused or redirected toward defensive guidance.

---

## Knowledge Base Sources

The local knowledge base is stored in the `data/` folder.

Current source files include:

```text
data/cybercrime_dataintrang.md
data/cyber_incident_response_playbook.md
data/eu_attacks_against_information_systems.md
data/eu_cyber_resilience_act.md
data/eu_dora_digital_operational_resilience.md
data/gdpr_core_principles.md
data/gdpr_personal_data_breach.md
data/gdpr_imy_edpb_security_guidance.md
data/imy_gdpr_security_measures.md
data/imy_gdpr_supervision.md
data/nis2_cybersecurity_law.md
data/nis2_incident_reporting.md
data/nis2_sector_scope_guidance.md
```

Each knowledge file is designed to include:

- topic
- main authority or legal source
- key idea
- important points
- practical explanation or checklist where useful
- useful questions
- official source links
- source metadata
- disclaimer or limitation notes where relevant

The application does not browse the web live when answering. It answers only from the local trusted source files.

---

## Safety Boundary

CyberLex Sweden is designed for defensive, educational, and compliance-oriented use.

CyberLex Sweden can help with:

- understanding selected cybersecurity-law topics
- understanding selected EU cybersecurity regulations and directives
- defensive incident-response steps
- evidence preservation
- documentation and timeline building
- GDPR/IMY reporting assessment
- NIS2 and Swedish Cybersecurity Act reporting assessment
- recovery planning
- source-grounded learning

CyberLex Sweden must not help with:

- hacking systems
- exploiting vulnerabilities
- stealing credentials
- hiding traces
- deleting logs
- bypassing detection
- evading investigation
- performing unauthorized access

This boundary is part of the project design.

---

## Privacy and Data Handling

CyberLex Sweden is currently a local educational prototype.

In the current local version:

- user questions are processed during the local Streamlit session
- no production database storage is implemented
- no intentional analytics or telemetry is implemented by the app
- generated incident summaries are created for the user to download
- users should avoid entering real sensitive incident data into the prototype

More detail is available in:

```text
docs/privacy_and_data_handling.md
```

---

## Tools and Technologies

| Tool | Purpose |
|---|---|
| Python | Main programming language used to build the app |
| Streamlit | Creates the local web interface |
| Markdown | Used for documentation and local knowledge base files |
| Git | Tracks project changes and commit history |
| GitHub | Stores the project online |
| GitHub Actions | Runs the weekly source audit workflow |
| VS Code | Code editor used during development |
| PowerShell | Used to run local commands on Windows |

---

## Project Structure

```text
CyberLex-Sweden
├── .github
│   └── workflows
│       └── source-audit.yml
├── app
│   ├── main.py
│   └── vector_search.py
├── data
│   └── local Markdown knowledge base files
├── docs
│   └── project documentation
├── report
│   └── final_report.md
├── screenshots
├── scripts
│   ├── add_missing_metadata.py
│   └── source_audit.py
├── sources
├── .gitignore
├── COPYRIGHT.md
├── README.md
└── requirements.txt
```

---

## How to Run Locally

### 1. Open the project folder

```powershell
cd C:\Projects\CyberLex-Sweden
```

This moves PowerShell into the CyberLex Sweden project folder.

### 2. Create a virtual environment if needed

```powershell
python -m venv .venv
```

This creates an isolated Python environment for the project.

### 3. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

This activates the local Python environment.

You should see:

```text
(.venv)
```

at the start of the terminal line.

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

This installs the Python packages listed in `requirements.txt`.

### 5. Check Python syntax

```powershell
python -m py_compile app/main.py
```

This checks whether the main app file has Python syntax errors.

If the command gives no output, the syntax check usually passed.

### 6. Start the app

```powershell
python -m streamlit run app/main.py
```

This starts CyberLex Sweden locally in the browser.

Expected local address:

```text
http://localhost:8501
```

---

## Useful Commands

Run the app:

```powershell
python -m streamlit run app/main.py
```

Run the source audit:

```powershell
python scripts/source_audit.py
```

Run the experimental retrieval module:

```powershell
python app/vector_search.py
```

Check Python syntax for the main app:

```powershell
python -m py_compile app/main.py
```

Check Python syntax for the experimental retrieval module:

```powershell
python -m py_compile app/vector_search.py
```

Clear Streamlit cache:

```powershell
streamlit cache clear
```

Check Git status:

```powershell
git status
```

---

## Documentation

Additional project documentation is available in the `docs/` folder.

Important documents include:

- `docs/project_overview.md` - project overview and background
- `docs/project_plan.md` - project plan and schedule
- `docs/source_list.md` - trusted source list
- `docs/source_policy.md` - source quality policy
- `docs/source_context_behavior.md` - source routing and source-context behavior
- `docs/source_update_history.md` - source update history and knowledge base change log
- `docs/source_audit_report.md` - generated local source audit report
- `docs/test_cases.md` - manual and experimental retrieval test cases
- `docs/testing_and_demo.md` - practical testing and demo guidance
- `docs/demo_checklist.md` - demo preparation and presentation checklist
- `docs/test_run_checklist.md` - practical checklist for running a first test pass
- `docs/ui_behavior.md` - user interface behavior
- `docs/technical_design.md` - application architecture and technical design
- `docs/product_roadmap.md` - product roadmap and future development plan
- `docs/vector_search_plan.md` - vector search plan
- `docs/ai_rag_plan.md` - future RAG plan
- `docs/privacy_and_data_handling.md` - privacy and local data-handling notes
- `docs/terms_of_use.md` - draft terms of use
- `docs/privacy_policy.md` - draft privacy policy
- `docs/legal_disclaimer.md` - legal disclaimer for educational use

---

## Testing and Demo

Manual test cases are documented in:

```text
docs/test_cases.md
```

Demo and test-run guidance is documented in:

```text
docs/testing_and_demo.md
docs/demo_checklist.md
docs/test_run_checklist.md
```

Testing should include:

- core legal questions
- Swedish and English language behavior
- source metadata and official source links
- GDPR/IMY questions
- NIS2 sector-scope questions
- NIS2 incident-reporting questions
- practical incident-response questions
- suspicious login, phishing, compromised account, data leak, ransomware, and malware scenarios
- downloaded incident summaries
- out-of-scope refusal behavior
- unsafe offensive cyber refusal behavior
- source-context readability checks
- source audit checks

---

## Source Audit System

CyberLex Sweden includes a local source audit script:

```text
scripts/source_audit.py
```

The script checks the Markdown files in `data/` for required source structure, including:

- official source section
- official source links
- source metadata section
- source date
- source freshness label
- version notes

It generates:

```text
docs/source_audit_report.md
```

The audit does **not** browse the web and does **not** confirm whether the law is currently up to date. It only checks the local project files.

A weekly GitHub Actions workflow also exists for source auditing:

```text
.github/workflows/source-audit.yml
```

---

## Important Limitations

CyberLex Sweden is an educational prototype.

Current limitations:

- it does not provide legal advice
- it does not replace official authority guidance
- it does not replace a qualified lawyer or professional compliance review
- it does not replace a professional incident-response team
- it does not browse the web live
- it only answers from local Markdown source files
- it covers selected cybersecurity-law and incident-response topics only
- the current answers are rule-based
- the experimental AI search is not real vector search yet
- source freshness labels describe stored local review dates only
- the source audit checks file structure, not live legal currency
- incident-response guidance is simplified for educational use
- downloaded incident summaries are documentation aids and do not replace internal incident-response records, legal review, or official reporting
- attention levels are educational signals and do not replace legal, regulatory, or incident-response risk assessment
- practical explanation cards and source-context filtering are rule-based and may need continued refinement
- continued bilingual source expansion is still needed

For serious legal, regulatory, compliance, or security decisions, official sources and qualified professionals should be checked.

---

## Future Improvements

Planned or possible improvements include:

- improve professional formatting of downloaded incident summaries
- add optional prepared-by, organization, date/time, and incident ID fields to downloaded summaries
- add fuller Swedish source sections to the Markdown knowledge base
- add copy/export features for broader non-incident answers, checklists, and sources
- continue refining source context selection
- continue refining incident-type source context filtering
- revisit vector search using Python 3.12 or another stable AI-compatible environment
- add embeddings with `sentence-transformers`
- add ChromaDB or FAISS
- compare keyword search with vector search
- add RAG-style answer generation
- keep answers grounded only in trusted local source material
- add more Swedish and EU cybersecurity-law sources
- improve source update workflows
- improve visual design
- prepare public deployment documentation
- strengthen Terms of Use, Privacy Policy, and Legal Disclaimer
- continue bilingual Swedish and English source expansion
- consider trademark and brand protection if the project develops further

---

## Disclaimer

CyberLex Sweden is a school project and educational prototype.

It provides simplified information from selected local source summaries and official source links. It is not legal advice, does not guarantee legal accuracy or currentness, and should not be used as the sole basis for legal, compliance, or security decisions.

For real incidents, legal questions, regulatory reporting, or compliance decisions, users should check official sources and contact qualified professionals.
