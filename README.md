# CyberLex Sweden

CyberLex Sweden is a final school project and educational legal-tech prototype focused on Swedish and EU cybersecurity law.

The project works as a local AI-style assistant that helps users search selected cybersecurity-law topics through a trusted local Markdown knowledge base. It uses source-based search, source routing, structured answers, citation details, official source links, source metadata, source freshness labels, topic labels, practical explanations, assessment checklists, and an experimental retrieval panel.

CyberLex Sweden does **not** provide legal advice. It is built for learning, demonstration, and portfolio use.

---

## Project Purpose

Cybersecurity law can be difficult to understand because relevant information is spread across many different sources, including:

- Swedish law
- EU regulations and directives
- Swedish government agencies
- cybersecurity authorities
- data protection authorities
- financial-sector cybersecurity rules
- product cybersecurity rules

CyberLex Sweden explores how a focused, source-grounded assistant can help users find relevant cybersecurity-law information in a safer and more transparent way.

The main design goal is simple:

```text
Better sources first. Better AI second.
```

The prototype should show where an answer comes from, what source section was matched, and what limitations apply.

---

## Current Prototype Status

CyberLex Sweden currently runs as a local Streamlit application.

The current version is a source-grounded, rule-based prototype. It does not yet use a full language model, live web browsing, or production vector search.

Completed major improvements include:

- Local Markdown knowledge base
- Source-based search and chunk ranking
- Source routing for supported legal topics
- English and Swedish interface support
- Swedish retrieval improvements
- Structured answer cards
- Citation details
- Official source links
- Source metadata display
- Source quality labels
- Source freshness labels
- Source match confidence labels
- Detected topic labels
- Practical explanation cards
- Topic-based assessment checklists
- Relevant source context cards
- Other matching source section cards
- Example question panel
- Experimental AI search sidebar
- Local source audit script
- Weekly GitHub Actions source audit workflow
- Manual test documentation
- Product roadmap
- Technical design documentation
- Source update history

Vector search was investigated and documented, but the implementation is paused for now because the local Python/package setup needs a stable Python version for AI dependencies.

---

## Supported Topics

CyberLex Sweden currently focuses on selected Swedish and EU cybersecurity-law topics.

Supported areas include:

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

## Knowledge Base Sources

The local knowledge base is stored in the `data/` folder.

Current source files:

```text
data/cybercrime_dataintrang.md
data/eu_attacks_against_information_systems.md
data/eu_cyber_resilience_act.md
data/eu_dora_digital_operational_resilience.md
data/gdpr_core_principles.md
data/gdpr_personal_data_breach.md
data/imy_gdpr_supervision.md
data/nis2_cybersecurity_law.md
data/nis2_incident_reporting.md
```

Each knowledge file is designed to include:

- topic
- main authority or legal source
- key idea
- important points
- practical explanation or checklist where useful
- cybersecurity connection
- useful questions
- official source links
- source metadata
- disclaimer

The application does not browse the web live when answering. It answers only from the local trusted source files.

---

## Current Features

The current prototype can:

- load local Markdown knowledge base files
- split source documents into searchable chunks
- match user questions to relevant source sections
- route specific questions to the most relevant source file
- generate simple source-based answers
- display structured citation details
- display the matched source file and section
- display official source links connected to the matched file
- display source metadata, including source date and version notes
- display source quality labels
- display source freshness labels
- display source match confidence
- display detected topic labels
- show matched source excerpts and supporting source context
- show practical explanations
- show topic-based assessment checklists
- show other matching source sections
- support English and Swedish interface labels
- provide example questions
- refuse out-of-scope questions
- display legal disclaimers
- run a local source audit
- run a weekly GitHub Actions source audit workflow

---

## Experimental AI Search

CyberLex Sweden includes an experimental AI search panel in the sidebar.

This panel uses:

```text
app/vector_search.py
```

Despite the file name, the current experimental search is still rule-based. It does not yet use embeddings, ChromaDB, FAISS, or a full language model.

The experimental search is used to test retrieval ranking before future vector search or RAG integration.

It currently uses:

- Markdown chunking
- keyword matching
- useful-section boosts
- weak-section penalties
- topic-specific routing rules
- source-specific score boosts and penalties

Example Swedish retrieval tests now supported:

| Question | Expected source |
|---|---|
| `Vad är NIS2?` | `nis2_cybersecurity_law.md` |
| `Vad ska ett företag göra efter en ransomwareattack?` | `nis2_incident_reporting.md` |
| `Vad är IMY?` | `imy_gdpr_supervision.md` |
| `Vad är DORA?` | `eu_dora_digital_operational_resilience.md` |
| `Vad betyder cybersäkerhetskrav för digitala produkter?` | `eu_cyber_resilience_act.md` |
| `Vad säger EU om attacker mot informationssystem?` | `eu_attacks_against_information_systems.md` |
| `Vad är olaglig åtkomst enligt EU-regler?` | `eu_attacks_against_information_systems.md` |

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

The expected result is:

```text
Files marked OK: 9
Files needing review: 0
```

The audit does **not** browse the web and does **not** confirm whether the law is currently up to date. It only checks the local project files.

A weekly GitHub Actions workflow also exists for source auditing:

```text
.github/workflows/source-audit.yml
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
│   ├── ai_rag_plan.md
│   ├── legal_disclaimer.md
│   ├── privacy_policy.md
│   ├── product_roadmap.md
│   ├── project_overview.md
│   ├── project_plan.md
│   ├── source_audit_report.md
│   ├── source_list.md
│   ├── source_policy.md
│   ├── source_update_history.md
│   ├── technical_design.md
│   ├── terms_of_use.md
│   ├── test_cases.md
│   └── vector_search_plan.md
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

### 5. Start the app

```powershell
python -m streamlit run app/main.py
```

This starts CyberLex Sweden locally in the browser.

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

Check Python syntax for the experimental retrieval module:

```powershell
python -m py_compile app/vector_search.py
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
- `docs/source_update_history.md` - source update history and knowledge base change log
- `docs/source_audit_report.md` - generated local source audit report
- `docs/test_cases.md` - manual and experimental retrieval test cases
- `docs/technical_design.md` - application architecture and technical design
- `docs/product_roadmap.md` - product roadmap and future development plan
- `docs/vector_search_plan.md` - vector search plan
- `docs/ai_rag_plan.md` - future RAG plan
- `docs/terms_of_use.md` - draft terms of use
- `docs/privacy_policy.md` - draft privacy policy
- `docs/legal_disclaimer.md` - legal disclaimer for educational use

---

## Important Limitations

CyberLex Sweden is an educational prototype.

Current limitations:

- It does not provide legal advice.
- It does not replace official authority guidance.
- It does not replace a qualified lawyer or professional compliance review.
- It does not browse the web live.
- It only answers from local Markdown source files.
- It covers selected cybersecurity-law topics only.
- The current answers are rule-based.
- The experimental AI search is not real vector search yet.
- Source freshness labels describe stored local review dates only.
- The source audit checks file structure, not live legal currency.

For serious legal, regulatory, or compliance decisions, official sources and qualified legal advice should be checked.

---

## Future Improvements

Planned or possible improvements include:

- Revisit vector search using Python 3.12 or another stable AI-compatible environment
- Add embeddings with `sentence-transformers`
- Add ChromaDB or FAISS
- Compare keyword search with vector search
- Add RAG-style answer generation
- Keep answers grounded only in trusted local source material
- Add more Swedish and EU cybersecurity-law sources
- Improve source update workflows
- Improve visual design
- Prepare public deployment documentation
- Strengthen Terms of Use, Privacy Policy, and Legal Disclaimer
- Continue bilingual Swedish and English source expansion
- Consider trademark and brand protection if the project develops further

---

## Disclaimer

CyberLex Sweden is a school project and educational prototype.

It provides simplified information from selected local source summaries and official source links. It is not legal advice, does not guarantee legal accuracy or currentness, and should not be used as the sole basis for legal, compliance, or security decisions.
