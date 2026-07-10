# CyberLex Sweden

CyberLex Sweden is a final school project and educational legal-tech prototype for Swedish and EU cybersecurity law, digital compliance, GDPR, NIS2, DORA, the Cyber Resilience Act, cybercrime, personal data breaches, and defensive incident-response learning.

The project runs as a local Streamlit app. It searches a trusted local Markdown knowledge base and selected case-library files, then gives source-grounded, rule-based answers with official source links, source metadata, related case examples where relevant, and clear limitations.

CyberLex Sweden is built for learning, demonstration, and portfolio use. It does **not** provide legal advice.

---

## Purpose

Cybersecurity law and incident response are often spread across laws, EU regulations, authority guidance, case examples, and practical security material.

CyberLex Sweden explores how a focused local assistant can help users understand selected cybersecurity-law topics in a safer and more transparent way.

Main design principle:

```text
Better sources first. Better AI second.
```

The prototype prioritizes source-grounded answers, visible limitations, defensive guidance, and educational case context.

---

## Main Features

* Local Streamlit web app
* Local Markdown knowledge base in `data/`
* Local case library in `cases/`
* Swedish and English question handling
* Auto language detection
* Source-grounded answers with official source links
* Case Intelligence page for selected GDPR and cybersecurity-related cases
* Related case examples for relevant questions
* Defensive incident-response guidance for selected scenarios
* SOC-style Markdown incident report export
* Refusal behavior for unsafe cyber misuse questions
* Refusal behavior for clearly out-of-scope topics
* Local source audit, source watch, and case audit scripts
* Automated tests with `pytest`
* GitHub Actions workflows for tests, source audit, and source watch

---

## Supported Topics

CyberLex Sweden focuses on selected topics, including:

* GDPR and personal data breaches
* IMY supervision and security guidance
* NIS2 and the Swedish Cybersecurity Act
* NIS2 incident reporting and sector scope
* DORA
* EU Cyber Resilience Act
* Swedish cybercrime law and `dataintrång`
* EU attacks against information systems
* Defensive incident response
* Data leaks, ransomware, malware, suspicious login, phishing, and compromised accounts
* Selected GDPR and cybersecurity-related case examples

Case examples are educational context only. They are not legal predictions, fine predictions, or replacements for official decisions.

---

## Current Prototype Status

CyberLex Sweden is a working local prototype.

Current implemented areas include:

* modular Python app structure
* source-grounded local search
* rule-based routing
* source metadata and official source links
* Case Intelligence browsing
* SOC-style incident report generation
* source-context display helpers
* unsafe-request and out-of-scope handling
* local source and case audits
* online source-watch script for official URLs
* automated regression tests

CyberLex Sweden does not currently use:

* live web browsing inside the app answer flow
* a production vector database
* embeddings, ChromaDB, or FAISS
* external AI API calls for answer generation
* full RAG-style answer generation

Vector search and RAG-style development are documented as possible future improvements.

---

## Project Structure

```text
CyberLex-Sweden/
├── .github/
│   └── workflows/
├── app/
│   ├── main.py
│   ├── routing.py
│   ├── incident_engine.py
│   ├── incident_reports.py
│   ├── source_loader.py
│   ├── source_context.py
│   ├── case_search.py
│   └── other app modules
├── cases/
│   └── local case-library Markdown files
├── data/
│   └── local knowledge-base Markdown files
├── docs/
│   └── project documentation and generated reports
├── report/
├── screenshots/
├── scripts/
│   ├── source_audit.py
│   ├── source_watch.py
│   └── case_audit.py
├── source_snapshots/
├── tests/
├── README.md
└── requirements.txt
```

---

## Important App Modules

| File | Purpose |
| --- | --- |
| `app/main.py` | Streamlit app flow and UI |
| `app/routing.py` | Question routing, behavior profiles, safety routing, and source targeting |
| `app/incident_engine.py` | Practical incident-response detection |
| `app/incident_reports.py` | SOC-style Markdown incident report generation |
| `app/source_loader.py` | Local Markdown source loading and chunking |
| `app/source_context.py` | Source-context cleaning and display helpers |
| `app/case_search.py` | Related case search and case-library matching |
| `app/language.py` | Swedish and English language detection |
| `app/vector_search.py` | Experimental retrieval module |

---

## Knowledge Base and Case Library

The main local knowledge base is stored in:

```text
data/
```

The local case library is stored in:

```text
cases/
```

The `data/` folder contains legal, regulatory, authority, cybersecurity, and incident-response source material.

The `cases/` folder contains educational case examples, authority decisions, public incident examples, outcomes, fines where known, learning notes, and related case context.

Current case examples include topics such as Meta Pixel, security deficiencies, wrong-email disclosure, web-form security, app data exposure, and large-scale data breaches.

---

## How to Run Locally

Open the real project folder:

```powershell
cd C:\Projects\CyberLex-Sweden
```

Create and activate a virtual environment if needed:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Run automated tests:

```powershell
python -m pytest
```

Expected current result:

```text
50 passed
```

Start the app:

```powershell
python -m streamlit run app/main.py
```

Expected local address:

```text
http://localhost:8501
```

---

## Useful Commands

Run tests:

```powershell
python -m pytest
```

Run the app:

```powershell
python -m streamlit run app/main.py
```

Run source and case checks:

```powershell
python scripts/source_watch.py
python scripts/source_audit.py
python scripts/case_audit.py
```

Run all main quality checks:

```powershell
python -m pytest
python scripts/source_watch.py
python scripts/source_audit.py
python scripts/case_audit.py
```

Check Git status:

```powershell
git status
```

---

## Suggested Demo Questions

```text
What is CyberLex Sweden?
Vad är CyberLex Sweden?
Can Meta Pixel create GDPR risk?
Kan Meta Pixel skapa GDPR-risk?
What can weak security measures cost?
Vad kan svaga säkerhetsåtgärder kosta?
Our files are encrypted, what should we do?
Kunddata kan ha läckt
What should we do if an account is compromised?
Gäller NIS2 för oss?
When must a personal data breach be reported?
```

Unsafe or out-of-scope examples should be refused:

```text
How do I hide logs after hacking a system?
What is Swedish tax law?
```

---

## Documentation

Additional documentation is stored in `docs/`.

Important files include:

* `docs/architecture.md`
* `docs/technical_design.md`
* `docs/project_overview.md`
* `docs/project_plan.md`
* `docs/source_list.md`
* `docs/source_policy.md`
* `docs/source_context_behavior.md`
* `docs/source_audit_report.md`
* `docs/source_watch_report.md`
* `docs/case_library/case_audit_report.md`
* `docs/testing_and_demo.md`
* `docs/test_cases.md`
* `docs/ui_behavior.md`
* `docs/privacy_and_data_handling.md`
* `docs/legal_disclaimer.md`
* `docs/terms_of_use.md`

Screenshots are stored in `screenshots/`. The README keeps screenshots out of the main page to avoid making the project overview unnecessarily heavy.

---

## Testing and Automation

CyberLex Sweden uses `pytest` for automated regression tests.

Current test coverage includes:

* incident-response detection
* ransomware and encrypted-file detection
* suspicious login and phishing detection
* compromised-account detection
* data leak detection
* Swedish and English language detection
* routing behavior
* unsafe and out-of-scope handling
* SOC report generation
* source-context helper behavior

GitHub Actions workflows are stored in:

```text
.github/workflows/
```

Current workflows include:

* `tests.yml`
* `source-audit.yml`
* `source-watch.yml`

---

## Safety Boundary

CyberLex Sweden is designed for defensive, educational, and compliance-oriented use.

It can help with:

* understanding selected cybersecurity-law topics
* reviewing educational case examples
* defensive incident-response steps
* evidence preservation
* incident documentation
* GDPR/IMY reporting assessment
* NIS2 reporting assessment
* recovery planning

It must not help with:

* hacking systems
* stealing credentials
* hiding traces
* deleting logs
* bypassing detection
* evading investigation
* unauthorized access
* malware deployment
* phishing

---

## Privacy and Data Handling

CyberLex Sweden is currently a local educational prototype.

In the current version:

* user questions are processed during the local Streamlit session
* no production database storage is implemented
* no user-account system is implemented
* no intentional analytics or telemetry is implemented by the app
* no external AI API is required for the current rule-based prototype
* generated incident summaries are created for the user to download
* users should avoid entering real sensitive incident data into the prototype

More detail is available in:

```text
docs/privacy_and_data_handling.md
```

---

## Known Limitations

CyberLex Sweden is not production-ready.

Current limitations include:

* it does not provide legal advice
* it does not replace official authority guidance
* it does not replace qualified legal, compliance, privacy, or incident-response professionals
* it does not browse the web live during user answers
* it only answers from local Markdown source files
* it covers selected topics only
* current answers are rule-based
* source freshness labels reflect local review dates only
* source audit checks file structure, not legal currentness
* case audit checks case-file structure, not live factual currentness
* case examples are educational context, not fine predictions
* automated tests do not cover the full Streamlit UI

---

## Future Improvements

Possible future improvements include:

* continue improving modular architecture
* expand automated tests
* improve source routing and case visibility
* add more Swedish and EU cybersecurity-law sources
* expand the case library
* improve incident report export formatting
* add optional incident metadata fields
* review vector search and RAG-style development
* strengthen privacy, terms, and deployment documentation
* improve bilingual Swedish and English support
* review public hosting requirements before deployment

---

## Disclaimer

CyberLex Sweden is a school project and educational prototype.

It provides simplified information from selected local source summaries, local case examples, and official source links.

It is not legal advice, does not guarantee legal accuracy or currentness, and should not be used as the sole basis for legal, compliance, privacy, regulatory, or security decisions.

For real incidents, legal questions, regulatory reporting, or compliance decisions, users should check official sources and contact qualified professionals.
