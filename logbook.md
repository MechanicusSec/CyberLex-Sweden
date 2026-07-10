# CyberLex Sweden Logbook

## Project

CyberLex Sweden

## Purpose

This logbook summarizes the main work completed during the CyberLex Sweden komvuxarbete project.

The project is a local educational Streamlit prototype for selected Swedish and EU cybersecurity-law, digital compliance, GDPR, NIS2, DORA, Cyber Resilience Act, cybercrime, case examples, and defensive incident-response learning.

---

## 2026-06 — Project setup and early prototype

### Work completed

* Created the CyberLex Sweden project as a local Python and Streamlit application.
* Set up the main project structure with folders for app code, data sources, documentation, scripts, tests, and reports.
* Created the first version of the local Markdown knowledge base.
* Added early source-grounded answer behavior.
* Added support for official source links and source metadata.
* Added the first Streamlit user interface.
* Added Git version control and GitHub repository support.

### Result

The project started as a working local prototype that could answer selected cybersecurity-law questions from local Markdown source files.

---

## 2026-06 — Knowledge base and source structure

### Work completed

* Built the local `data/` knowledge base.
* Added source files for GDPR, IMY, NIS2, Swedish cybercrime law, EU attacks against information systems, Cyber Resilience Act, DORA, and defensive incident response.
* Added structured source sections such as topic, key idea, important points, official source links, source metadata, and disclaimers.
* Added Swedish summaries and Swedish useful questions where needed.
* Added documentation for source policy, source list, and source history.

### Result

CyberLex Sweden became more transparent because answers could be connected to local source files and official source links.

---

## 2026-06 — Application refactoring

### Work completed

* Refactored the application from a larger single-file prototype into a more modular Python structure.
* Created or improved supporting modules such as:
  * `app/routing.py`
  * `app/incident_engine.py`
  * `app/incident_reports.py`
  * `app/source_loader.py`
  * `app/source_context.py`
  * `app/language.py`
  * `app/case_search.py`
  * `app/vector_search.py`
* Improved question routing so that common legal and cybersecurity questions are sent to better matching source files.
* Improved source-context display and source-confidence explanations.

### Result

The code became easier to test, maintain, and explain in the final report.

---

## 2026-06 — Incident-response support

### Work completed

* Added detection for practical incident-response questions.
* Added support for topics such as:
  * suspicious email
  * phishing
  * suspicious links
  * suspicious login activity
  * compromised accounts
  * customer data leaks
  * suspected hacking
  * unauthorized access
  * ransomware
  * malware
  * encrypted files
* Added practical first-step guidance.
* Added assessment checklists.
* Added SOC-style Markdown incident report generation.
* Added safe refusal behavior for harmful cyber misuse requests.

### Result

CyberLex Sweden could support defensive incident-response learning while refusing unsafe requests such as hiding logs, stealing credentials, bypassing detection, or committing unauthorized access.

---

## 2026-06 — Bilingual support

### Work completed

* Added English, Swedish, and Auto language behavior.
* Added Swedish labels, Swedish examples, Swedish limitation text, and Swedish answer-support behavior.
* Improved Swedish keyword matching for cybersecurity and legal topics.
* Added Swedish case sections where available.
* Improved language-aware official source display.

### Result

The app became usable for both English and Swedish project review and demonstrations.

---

## 2026-06 — Case Intelligence

### Work completed

* Created the `cases/` case-library structure.
* Added selected GDPR, cybersecurity, public incident, and authority-decision examples.
* Added case parsing and case search support.
* Added related-case display under suitable answers.
* Added a separate Case Intelligence page.
* Added case learning notes and related topic badges.
* Added warnings that case examples are educational and not fine predictions.

### Result

CyberLex Sweden gained a practical case-learning layer that connects legal and cybersecurity concepts to real-world examples.

---

## 2026-06 to 2026-07 — Case library expansion

### Work completed

Added and improved case files including:

* Apoteket/Apohem Meta Pixel
* Avanza Meta Pixel
* Kry Meta Pixel
* Equality Ombudsman web form
* Trygg-Hansa security deficiencies
* Sportadmin security breach
* Indecap wrong-email customer data
* Klarna app data exposure
* Spotify access request
* Region Skåne USB security case
* Statens servicecenter breach notification
* SL/WÅAB alcohol testing
* Miljödata data leak
* Bonnier News profiling sanction

### Result

The case library became broader and now includes tracking, profiling, security deficiencies, breach notification, web forms, wrong-recipient disclosure, app exposure, workplace testing, public-sector incidents, access rights, and large data leak examples.

---

## 2026-07 — Case Intelligence filters and comparison view

### Work completed

* Improved the Case Intelligence page.
* Added filters for case topics and categories.
* Added a comparison view for filtered cases.
* Updated case-search helper logic to support case filtering and comparison rows.
* Kept the app focused without adding unnecessary extra download features.

### Result

The Case Intelligence page became easier to use and more useful for review, comparison, and learning.

---

## 2026-07 — Testing and audits

### Work completed

* Added and improved automated tests using `pytest`.
* Added source audit script:
  * `scripts/source_audit.py`
* Added case audit script:
  * `scripts/case_audit.py`
* Added source watch script:
  * `scripts/source_watch.py`
* Added GitHub Actions workflows for:
  * tests
  * source audit
  * source watch
* Repeatedly ran tests and audits during development.

### Current expected test result

```text
50 passed
```

### Result

The project became easier to verify and maintain.

---

## 2026-07 — Documentation cleanup

### Work completed

* Shortened and cleaned up `README.md`.
* Shortened and cleaned up `docs/project_overview.md`.
* Updated the final report in `report/final_report.md`.
* Connected the final report more clearly to network technician and IT support skills.
* Documented project limitations, safety boundaries, privacy considerations, and future improvements.

### Result

The project documentation became clearer and more suitable for komvuxarbete submission.

---

## 2026-07 — Bonnier profiling case

### Work completed

* Added `cases/imy_bonnier_profiling_sanction_2023.md`.
* Added a new GDPR case category covering profiling, marketing, cookies, consent, legitimate interest, customer data, and targeted advertising.
* Updated the final report to include the expanded case library.

### Result

The case library became more balanced because it no longer focused only on breaches, tracking, and security incidents.

---

## 2026-07 — Source watch link fix

### Work completed

* Ran the source watch script.
* Found one failed official source URL in `data/cyber_incident_response_playbook.md`.
* The old MSB voluntary IT incident reporting link redirected to a 404 page.
* Updated the source link to the current NCSC/CERT-SE voluntary IT incident reporting URL.
* Updated the source date and version notes in the incident response playbook.
* Reran source watch, source audit, case audit, and tests.

### Result

The broken official source link was fixed and the source-watch result was improved.

---

## 2026-07 — Finalization for komvuxarbete

### Work completed

* Stopped adding new app features to keep the prototype stable.
* Prepared the project as a finished komvuxarbete package.
* Confirmed that screenshots are not necessary for the final submission.
* Focused final evidence on:
  * final report
  * README
  * project overview
  * source audit report
  * source watch report
  * case audit report
  * tests
  * GitHub commit history
  * working local app
  * source and case structure
* Created this logbook as a summary of the project work.

### Result

CyberLex Sweden is ready to be presented as a completed educational prototype for a komvuxarbete with IT, network technician, cybersecurity, documentation, testing, and digital compliance relevance.

---

## Final project status

CyberLex Sweden currently includes:

* local Streamlit application
* modular Python app structure
* local Markdown knowledge base
* official source links and source metadata
* source quality and freshness labels
* Swedish, English, and Auto language behavior
* defensive incident-response support
* SOC-style Markdown report export
* unsafe cyber refusal behavior
* out-of-scope refusal behavior
* Case Intelligence page
* case filters and comparison view
* expanded case library
* source audit script
* source watch script
* case audit script
* automated tests
* GitHub Actions workflows
* final report and supporting documentation

CyberLex Sweden remains an educational prototype and does not provide legal advice.
