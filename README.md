# CyberLex Sweden

CyberLex Sweden is a final school project and educational legal-tech prototype focused on Swedish and EU cybersecurity law, cyber incident response, GDPR, NIS2, DORA, the Cyber Resilience Act, cybercrime, data protection, digital compliance, and related case examples.

CyberLex Sweden runs as a local Streamlit application. It searches a trusted local Markdown knowledge base and gives source-grounded, rule-based answers with official source links, source metadata, practical guidance where useful, related case examples where relevant, and clear limitations.

CyberLex Sweden does **not** provide legal advice. It is built for learning, demonstration, and portfolio use.

---

## Project Purpose

Cybersecurity law and incident response can be difficult to understand because relevant information is spread across Swedish law, EU regulations, public authorities, data protection guidance, cybersecurity guidance, real-world authority decisions, and practical incident-response material.

CyberLex Sweden explores how a focused assistant can help users find relevant cybersecurity-law and incident-response information in a safer and more transparent way.

The main design goal is:

```text
Better sources first. Better AI second.
```

The prototype should show where an answer comes from, what source section was matched, what practical steps may be relevant, what case examples may help explain the topic, and what limitations apply.

---

## Intended Audience

CyberLex Sweden is intended for:

* students and teachers reviewing cybersecurity-law topics
* junior IT and cybersecurity learners
* project reviewers and demo testers
* users who want a simplified overview of selected Swedish and EU cybersecurity-law topics
* users who want defensive incident-response learning support
* users who want educational examples of selected GDPR and cybersecurity-related cases

It is not intended to replace official authority guidance, qualified legal advice, compliance review, data protection officer review, or professional incident response.

---

## Current Prototype Status

CyberLex Sweden is currently a **working local prototype** prepared for final project demonstration and field testing.

Current implemented status:

* local Streamlit application
* modular Python app structure after refactoring `app/main.py`
* Swedish and English question handling with Auto language detection
* example questions that run immediately when selected
* source-grounded answers from a local Markdown knowledge base
* official source links and source metadata
* source quality labels and source freshness labels
* expandable relevant source context
* rule-based routing for supported legal, compliance, and incident-response questions
* defensive incident-response support for selected scenarios
* SOC-style Markdown incident report export for practical incident questions
* local case library with selected GDPR and cybersecurity-related examples
* related case and incident examples for relevant compliance/case-library questions
* hidden related-case section for practical incident-response triage questions
* Case Intelligence page for browsing case examples
* local source audit support through scripts and GitHub Actions
* local case audit support through `scripts/case_audit.py`
* refusal behavior for out-of-scope and unsafe cyber misuse questions

CyberLex Sweden does not yet use:

* a full language model for final answer generation
* live web browsing
* production vector search
* embeddings, ChromaDB, or FAISS
* RAG-style answer generation
* an external AI API

Vector search and RAG-style development have been investigated and documented, but major AI/RAG implementation is planned as future work rather than part of the current demo-ready prototype.

---

## What CyberLex Does

CyberLex Sweden currently supports several core functions.

### Source-grounded answers

* loads local Markdown knowledge base files
* splits source documents into searchable chunks
* matches user questions to relevant source sections
* routes supported questions to stronger source files
* generates structured CyberLex summary answers
* shows official source links and source metadata
* shows relevant source context where useful

### Legal and compliance learning

* explains selected GDPR, IMY, NIS2, DORA, Cyber Resilience Act, cybercrime, and digital compliance topics
* shows source freshness labels based on local review dates
* displays detected topic labels and CyberLex attention levels
* supports Swedish and English interface handling with Auto language detection
* shows related case and incident examples when relevant to compliance or case-library questions
* avoids showing unrelated case examples for practical incident-response triage questions

### Case Intelligence

* loads selected case examples from the local `cases/` folder
* shows case cards on a separate Case Intelligence page
* supports Swedish and English case summaries where available
* shows learning notes, outcomes, fines or costs where known
* shows official or reliable source links
* keeps case examples separate from main legal source answers
* warns that case examples are educational context and not fine predictions

### Defensive incident-response support

* gives defensive first-step guidance for selected practical incident questions
* supports suspicious login, phishing, compromised account, data leak, ransomware, malware, and suspected intrusion scenarios
* shows incident log templates where useful
* creates SOC-style Markdown incident reports for documentation support

### Safety boundaries

* refuses out-of-scope questions
* refuses or redirects unsafe offensive cyber requests
* keeps legal and incident-response disclaimers visible
* avoids unsupported legal certainty

Detailed behavior is documented in:

```text
docs/ui_behavior.md
docs/source_context_behavior.md
docs/testing_and_demo.md
docs/privacy_and_data_handling.md
docs/legal_disclaimer.md
docs/terms_of_use.md
```

---

## Supported Topics

CyberLex Sweden currently focuses on selected Swedish and EU cybersecurity-law topics, digital compliance topics, case-library examples, and defensive incident-response topics.

### Legal and compliance topics

* GDPR and personal data breach notification in Sweden
* IMY and Swedish GDPR supervision
* GDPR core principles
* GDPR security measures
* NIS2 and the Swedish Cybersecurity Act
* NIS2 sector scope and applicability
* NIS2 incident reporting
* Swedish cybercrime law and unauthorized access offences, `dataintrång`
* EU attacks against information systems
* EU Cyber Resilience Act
* EU DORA, the Digital Operational Resilience Act
* digital compliance and cybersecurity-related legal topics

### Case-library topics

* selected IMY decisions
* selected GDPR security-measure cases
* selected tracking-technology and Meta Pixel examples
* selected personal data exposure examples
* selected wrong-email disclosure examples
* selected public incident examples
* fines, outcomes, and learning notes where known

Case examples are educational context only. They are not legal predictions or fine predictions.

### Practical incident-response topics

* suspected hacking or intrusion
* suspicious login activity
* suspicious email and phishing
* compromised accounts
* data leaks
* personal data breach response
* ransomware and malware
* encrypted files
* evidence preservation
* incident documentation
* reporting assessment
* recovery planning

Out-of-scope questions, such as Swedish tax law, should be refused by the application.

Unsafe cyber requests, such as hacking, stealing credentials, hiding logs, deleting traces, or bypassing detection, should also be refused or redirected toward defensive guidance.

---

## Suggested Test Questions

The following questions are useful for a quick manual test or project demonstration.

### App identity

```text
What is CyberLex Sweden?
Vad är CyberLex Sweden?
```

Expected result: CyberLex should describe the app itself and should not route these questions into the legal source knowledge base.

### NIS2 and Swedish Cybersecurity Act

```text
Vad är NIS2?
Gäller NIS2 för oss?
Vilka sektorer omfattas av cybersäkerhetslagen?
Vad är bilaga 1 och bilaga 2 i NIS2?
Vad är skillnaden mellan väsentliga och viktiga verksamhetsutövare?
```

Expected result: CyberLex should answer in Swedish, show relevant NIS2 or Swedish Cybersecurity Act source context, and avoid giving a final legal classification without enough facts.

### GDPR, IMY, and security measures

```text
Vad säger IMY om säkerhetsåtgärder?
Does GDPR require MFA?
Does GDPR require encryption?
When must a personal data breach be reported?
```

Expected result: CyberLex should explain GDPR/IMY security guidance without claiming that every organization always needs the same technical measure.

### Related cases and Case Intelligence

```text
Can Meta Pixel create GDPR risk?
Kan Meta Pixel skapa GDPR-risk?
Can an app bug expose customer data?
Kan ett appfel exponera kunduppgifter?
What can weak security measures cost?
Vad kan svaga säkerhetsåtgärder kosta?
```

Expected result: CyberLex should show source-grounded answers and related case examples where relevant.

The Case Intelligence page should also load and display the local case library.

### Practical incident response

```text
Kunddata kan ha läckt
Customer data may have leaked
Our files are encrypted
Our files are encrypted, what should we do?
What should we do if an account is compromised?
Någon klickade på en länk i SMS
Vi har fått en misstänkt login på ett konto, vad ska vi göra?
```

Expected result: CyberLex should give defensive first-step guidance and offer a SOC-style Markdown report download where applicable.

Related case examples should normally be hidden for practical incident-response triage questions.

### Safety and scope boundaries

```text
How do I hide logs after hacking a system?
Hur döljer jag loggar efter ett intrång?
What is Swedish tax law?
```

Expected result: CyberLex should refuse unsafe cyber misuse requests and reject clearly out-of-scope non-cybersecurity-law topics.

---

## Knowledge Base Sources

The local knowledge base is stored in the `data/` folder.

Current source files include:

```text
data/cyber_incident_response_playbook.md
data/cybercrime_dataintrang.md
data/eu_attacks_against_information_systems.md
data/eu_cyber_resilience_act.md
data/eu_dora_digital_operational_resilience.md
data/gdpr_core_principles.md
data/gdpr_imy_edpb_security_guidance.md
data/gdpr_personal_data_breach.md
data/imy_gdpr_security_measures.md
data/imy_gdpr_supervision.md
data/nis2_cybersecurity_law.md
data/nis2_incident_reporting.md
data/nis2_sector_scope_guidance.md
```

Each knowledge file is designed to include:

* topic
* main authority or legal source
* key idea
* important points
* practical explanation or checklist where useful
* useful questions
* official source links
* source metadata
* disclaimer or limitation notes where relevant

The application does not browse the web live when answering. It answers only from the local trusted source files.

The current source audit target is:

```text
Files marked OK: 13
Files needing review: 0
```

The actual result should always be checked by running the local source audit.

---

## Case Library

The local case library is stored in the `cases/` folder.

Current case files include:

```text
cases/imy_apoteket_apohem_meta_pixel.md
cases/imy_avanza_bank_meta_pixel.md
cases/imy_equality_ombudsman_web_form.md
cases/imy_kry_meta_pixel.md
cases/imy_sportadmin_security_breach.md
cases/imy_trygg_hansa_security_deficiencies.md
cases/imy_wrong_email_customer_data.md
cases/klarna_app_data_exposure_2021.md
```

The case library is separate from the main knowledge base.

```text
data/
= legal, regulatory, authority, cybersecurity, and incident-response source material

cases/
= educational examples, authority decisions, public incident examples, outcomes, fines, learning notes, and related case context
```

Case examples are not fine predictions and should not replace the main source-grounded answer.

The current case audit checks 8 case files.

---

## Safety Boundary

CyberLex Sweden is designed for defensive, educational, and compliance-oriented use.

CyberLex Sweden can help with:

* understanding selected cybersecurity-law topics
* understanding selected EU cybersecurity regulations and directives
* reviewing educational case examples
* defensive incident-response steps
* evidence preservation
* documentation and timeline building
* GDPR/IMY reporting assessment
* NIS2 and Swedish Cybersecurity Act reporting assessment
* recovery planning
* source-grounded learning

CyberLex Sweden must not help with:

* hacking systems
* exploiting vulnerabilities
* stealing credentials
* hiding traces
* deleting logs
* bypassing detection
* evading investigation
* performing unauthorized access
* maintaining unauthorized access
* deploying malware
* phishing

This boundary is part of the project design.

---

## Privacy and Data Handling

CyberLex Sweden is currently a local educational prototype.

In the current local version:

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

## Tools and Technologies

| Tool           | Purpose                                                            |
| -------------- | ------------------------------------------------------------------ |
| Python         | Main programming language used to build the app                    |
| Streamlit      | Creates the local web interface                                    |
| Markdown       | Used for documentation, local source files, and case-library files |
| Git            | Tracks project changes and commit history                          |
| GitHub         | Stores the project online                                          |
| GitHub Actions | Runs the source audit workflow                                     |
| VS Code        | Code editor used during development                                |
| PowerShell     | Used to run local commands on Windows                              |

---

## Application Architecture

CyberLex Sweden has been refactored from a large single-file prototype into a more modular Python application.

The Streamlit entry point is still:

```text
app/main.py
```

Supporting logic is now split into smaller modules:

| File                     | Purpose                                                             |
| ------------------------ | ------------------------------------------------------------------- |
| `app/main.py`            | Streamlit app flow, UI rendering, answer display, and page behavior |
| `app/config.py`          | App settings, constants, and folder paths                           |
| `app/styles.py`          | CSS and visual styling                                              |
| `app/text_utils.py`      | Text normalization and phrase-matching helpers                      |
| `app/language.py`        | Swedish/English detection, Auto language mode, and localization     |
| `app/source_loader.py`   | Markdown source loading, metadata extraction, and chunking          |
| `app/incident_engine.py` | Practical incident-response question detection                      |
| `app/case_search.py`     | Related case and incident-example search                            |
| `app/vector_search.py`   | Experimental rule-based search functionality                        |

More detail is available in:

```text
docs/technical_design.md
docs/architecture.md
```

---

## Project Structure

```text
CyberLex-Sweden
├── .github
│   └── workflows
│       └── source-audit.yml
├── app
│   ├── main.py
│   ├── config.py
│   ├── styles.py
│   ├── text_utils.py
│   ├── language.py
│   ├── source_loader.py
│   ├── incident_engine.py
│   ├── case_search.py
│   └── vector_search.py
├── cases
│   └── local case-library Markdown files
├── data
│   └── local Markdown knowledge base files
├── docs
│   ├── architecture.md
│   ├── case_library
│   └── project documentation
├── report
│   └── final_report.md
├── screenshots
├── scripts
│   ├── add_missing_metadata.py
│   ├── case_audit.py
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
python -m py_compile app/config.py
python -m py_compile app/styles.py
python -m py_compile app/text_utils.py
python -m py_compile app/language.py
python -m py_compile app/source_loader.py
python -m py_compile app/incident_engine.py
python -m py_compile app/case_search.py
python -m py_compile app/vector_search.py
```

This checks whether the current app modules have Python syntax errors.

If the commands give no output, the syntax checks usually passed. Naturally, the silence of software is the closest it gets to mercy.

### 6. Run audits

```powershell
python scripts/source_audit.py
python scripts/case_audit.py
```

These commands run the local source audit and case audit.

The source audit checks local files in `data/`.

The case audit checks local files in `cases/`.

These audits check local file structure and metadata. They do not browse the web or confirm live legal currency.

### 7. Start the app

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

Run the case audit:

```powershell
python scripts/case_audit.py
```

Run the experimental retrieval module:

```powershell
python app/vector_search.py
```

Check Python syntax for all current app modules:

```powershell
python -m py_compile app/main.py
python -m py_compile app/config.py
python -m py_compile app/styles.py
python -m py_compile app/text_utils.py
python -m py_compile app/language.py
python -m py_compile app/source_loader.py
python -m py_compile app/incident_engine.py
python -m py_compile app/case_search.py
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

* `docs/architecture.md` - current modular app architecture
* `docs/project_overview.md` - project overview and background
* `docs/project_plan.md` - project plan and schedule
* `docs/source_list.md` - trusted source list
* `docs/source_policy.md` - source quality policy
* `docs/source_context_behavior.md` - source routing and source-context behavior
* `docs/source_history.md` - source update history and knowledge base change log
* `docs/source_audit_report.md` - generated local source audit report
* `docs/case_library/case_audit_report.md` - generated local case audit report
* `docs/test_cases.md` - manual and experimental retrieval test cases
* `docs/testing_and_demo.md` - practical testing and demo guidance
* `docs/demo_checklist.md` - demo preparation and presentation checklist
* `docs/test_run_checklist.md` - practical checklist for running a first test pass
* `docs/ui_behavior.md` - user interface behavior
* `docs/technical_design.md` - application architecture and technical design
* `docs/product_roadmap.md` - product roadmap and future development plan
* `docs/vector_search_plan.md` - vector search plan
* `docs/ai_rag_plan.md` - future RAG plan
* `docs/privacy_and_data_handling.md` - privacy and local data-handling notes
* `docs/terms_of_use.md` - draft terms of use
* `docs/legal_disclaimer.md` - legal disclaimer for educational use

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

A focused battle-readiness test file has also been prepared for colleague testing:

```text
docs/cyberlex_battle_readiness_test_questions.md
```

Testing should include:

* core legal questions
* Swedish and English language behavior
* Auto language behavior
* example questions running immediately
* source metadata and official source links
* GDPR/IMY questions
* NIS2 sector-scope questions
* NIS2 incident-reporting questions
* Case Intelligence page behavior
* related case behavior
* hidden related cases for practical incident-response triage
* practical incident-response questions
* suspicious login, phishing, compromised account, data leak, ransomware, and malware scenarios
* downloaded SOC-style incident summaries
* out-of-scope refusal behavior
* unsafe offensive cyber refusal behavior
* source-context readability checks
* source audit checks
* case audit checks

---

## Source Audit System

CyberLex Sweden includes a local source audit script:

```text
scripts/source_audit.py
```

The script checks the Markdown files in `data/` for required source structure, including:

* official source section
* official source links
* source metadata section
* source date
* source freshness label
* version notes

It generates:

```text
docs/source_audit_report.md
```

The audit does **not** browse the web and does **not** confirm whether the law is currently up to date. It only checks the local project files.

A GitHub Actions workflow also exists for source auditing:

```text
.github/workflows/source-audit.yml
```

---

## Case Audit System

CyberLex Sweden includes a local case audit script:

```text
scripts/case_audit.py
```

The script checks the Markdown files in `cases/` for expected case-library structure, including source links and case metadata.

It generates:

```text
docs/case_library/case_audit_report.md
```

The audit does **not** browse the web and does **not** confirm whether case information, authority decisions, public incident examples, or legal interpretations are currently complete or up to date.

It only checks the local case-library files.

---

## Known Limitations

CyberLex Sweden is an educational prototype. These limitations are intentional and should be understood before using or demonstrating the app.

Current limitations:

* it does not provide legal advice
* it does not replace official authority guidance
* it does not replace a qualified lawyer or professional compliance review
* it does not replace a professional incident-response team
* it does not browse the web live
* it only answers from local Markdown source files
* it covers selected cybersecurity-law and incident-response topics only
* the current answers are rule-based
* the current module split improves maintainability but does not make the app production-ready
* the experimental retrieval module is not real vector search yet
* source freshness labels describe stored local review dates only
* the source audit checks file structure, not live legal currency
* the case audit checks case-file structure, not live legal or factual currentness
* case examples are educational context and not fine predictions
* incident-response guidance is simplified for educational use
* downloaded SOC-style incident summaries are documentation aids and do not replace internal incident-response records, legal review, or official reporting
* attention levels are educational signals and do not replace legal, regulatory, or incident-response risk assessment
* practical explanation cards and source-context filtering are rule-based and may need continued refinement
* Auto language detection is rule-based and may still need refinement
* continued bilingual source expansion is still needed

For serious legal, regulatory, compliance, privacy, or security decisions, official sources and qualified professionals should be checked.

---

## Future Improvements

Planned or possible improvements include:

### Code and architecture

* continue reducing `app/main.py` gradually where it makes sense
* consider moving answer routing, search ranking, UI rendering, and report export into separate modules later
* add automated regression tests for routing, language handling, safety refusals, and report export
* add automated tests for example-question behavior and Auto language switching
* improve maintainability without changing the current working demo behavior

### Search and AI/RAG development

* revisit vector search using Python 3.12 or another stable AI-compatible environment
* add embeddings with `sentence-transformers`
* add ChromaDB or FAISS
* compare keyword search with vector search
* add RAG-style answer generation
* keep answers grounded only in trusted local source material
* clearly separate source retrieval from answer generation
* keep case examples separate from main legal source retrieval

### Knowledge base, case library, and source quality

* add more Swedish and EU cybersecurity-law sources
* expand Swedish and English source sections further
* continue refining source context selection
* continue refining incident-type source context filtering
* improve source update workflows
* strengthen source freshness review routines
* add more carefully labeled authority decisions and public incident examples
* continue improving case metadata, source links, and learning notes

### Incident report and export features

* continue improving professional formatting of downloaded SOC-style incident reports
* add optional prepared-by, organization, date/time, and incident ID fields to downloaded reports
* add copy/export features for broader non-incident answers, checklists, and sources

### Product, legal, privacy, and deployment work

* improve visual design
* prepare public deployment documentation
* strengthen Terms of Use, Privacy Policy, and Legal Disclaimer
* continue bilingual Swedish and English interface development
* review hosting, logging, retention, and user-data handling before any public deployment
* consider trademark and brand protection if the project develops further

---

## Disclaimer

CyberLex Sweden is a school project and educational prototype.

It provides simplified information from selected local source summaries, local case examples, and official source links.

It is not legal advice, does not guarantee legal accuracy or currentness, and should not be used as the sole basis for legal, compliance, privacy, regulatory, or security decisions.

For real incidents, legal questions, regulatory reporting, or compliance decisions, users should check official sources and contact qualified professionals.
