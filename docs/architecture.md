# CyberLex Sweden Architecture

This document explains the current technical structure of CyberLex Sweden after the application was refactored into smaller Python modules.

CyberLex Sweden is a local Streamlit prototype that searches a trusted Markdown knowledge base and provides source-grounded answers about Swedish and EU cybersecurity law, GDPR, NIS2, DORA, the Cyber Resilience Act, cybercrime, defensive incident response, and related legal-tech topics.

CyberLex Sweden also includes a separate educational case library for selected GDPR and cybersecurity-related case examples.

---

## Application Overview

CyberLex Sweden is built as a modular Python application.

The main app is started from:

```text
app/main.py
```

The supporting logic has been moved into separate files so the project is easier to understand, maintain, test, and extend.

The app currently supports:

* Swedish and English questions
* Auto language detection
* local Markdown source loading
* source-grounded answers
* official source links
* source metadata
* source quality labels
* source freshness labels
* matched source context
* practical incident-response guidance
* SOC-style Markdown report export
* related case and incident examples
* hidden related cases for practical incident-response triage
* Case Intelligence page
* source audit
* online source watch
* case audit
* automated regression tests with `pytest`
* GitHub Actions for source audit, source watch, and tests
* educational legal disclaimers
* unsafe cyber refusal
* out-of-scope refusal

CyberLex Sweden is local-first and source-grounded.

It does not browse the web live when answering questions.

It does not use a full language model, real vector search, embeddings, ChromaDB, FAISS, or RAG answer generation in the current prototype.

---

## Main Application File

### `app/main.py`

This is the main Streamlit application file.

It controls:

* page layout
* sidebar navigation
* user input
* example questions
* active submitted question state
* answer flow
* source search result display
* UI sections
* incident report display
* related case display
* Case Intelligence page rendering
* final rendered output

`main.py` remains the entry point of the application.

Earlier versions placed most logic inside this file. Larger support logic has now been moved into separate modules, especially routing logic, language handling, source loading, incident detection, and case search.

`main.py` should mainly handle Streamlit UI flow and rendering. Pure logic should gradually be moved into separate modules where it can be tested without launching Streamlit.

---

## Routing and Question Behavior

### `app/routing.py`

This file contains the main question-routing and behavior-profile logic.

It helps decide:

* whether a question is about CyberLex Sweden itself
* whether a question is inside CyberLex scope
* whether a question is unsafe and should be refused
* whether a question is a practical incident-response question
* whether related cases should be shown
* whether a SOC-style report should be shown
* whether a question should route to GDPR, NIS2, DORA, cybercrime, incident response, or another source topic
* which source file should be preferred for a question
* how many source-context cards should be shown
* whether NIS2 scope questions should use focused source context

Important routing examples:

```text
What is CyberLex Sweden?
→ self-description answer
```

```text
Can Meta Pixel create GDPR risk?
→ case-context answer with related cases
```

```text
Our files are encrypted, what should we do?
→ practical incident-response answer with SOC report support
```

```text
Vad är bilaga 1 och bilaga 2 i NIS2?
→ NIS2 sector-scope source routing
```

```text
How do I hide logs after hacking a system?
→ unsafe refusal
```

Moving this logic into `routing.py` makes it easier to test without importing the Streamlit app directly.

This is important because importing `app/main.py` also triggers Streamlit setup, which is not ideal for automated tests. Apparently even tests prefer not to wake the UI beast.

---

## Configuration

### `app/config.py`

This file stores shared application settings and paths.

It includes constants such as:

* app title
* app icon
* Streamlit layout mode
* data folder path
* case folder path

This keeps basic settings separate from the main app logic.

---

## Styling

### `app/styles.py`

This file contains the Streamlit CSS styling used by CyberLex Sweden.

It controls the visual design of:

* cards
* warning boxes
* topic badges
* source context boxes
* case sections
* incident-response sections
* general layout styling

Keeping styling in a separate file makes `main.py` easier to read, which is apparently something humans appreciate after creating a giant ritual scroll of UI code.

---

## Text Utilities

### `app/text_utils.py`

This file contains shared text helper functions.

It handles:

* normalizing question text
* cleaning words for search
* checking whether text contains important phrases
* reusable keyword and phrase matching

These helpers are used across the app for search, routing, language detection, case matching, and incident detection.

---

## Language Handling

### `app/language.py`

This file handles Swedish and English language behavior.

It includes logic for:

* detecting whether a question is Swedish or English
* supporting Auto language mode
* handling Swedish questions that include English technical terms
* localizing section names
* localizing source labels
* localizing related case titles
* keeping example questions aligned with the interface language
* supporting bilingual case display where available

The language system is important because CyberLex Sweden is intended to support both Swedish and English users.

Examples:

```text
Can Meta Pixel create GDPR risk?
→ English
```

```text
Kan Meta Pixel skapa GDPR-risk?
→ Swedish
```

```text
What is NIS2?
→ English
```

```text
Vad är NIS2?
→ Swedish
```

Auto language detection is rule-based and may still need refinement as new question patterns are added.

---

## Source Loading

### `app/source_loader.py`

This file handles the local trusted knowledge base in the `data/` folder.

It is responsible for:

* loading Markdown source files
* extracting official source links
* extracting source metadata
* reading source dates
* reading version notes
* extracting Markdown sections
* splitting Markdown files into searchable chunks

This module separates source loading from the Streamlit UI.

## Source Context Display

### `app/source_context.py`

This file builds and formats the relevant source-context cards shown below CyberLex answers.

It handles:

* cleaning source excerpts
* hiding low-value helper sections
* filtering checklist sections so they do not duplicate visible assessment checklists
* trimming long excerpts at readable sentence or paragraph boundaries
* keeping source excerpts aligned with the selected UI language
* creating short and expandable source-context previews
* converting internal source filenames into user-friendly source area names
* selecting useful source-context cards for the current question
* generating the HTML used for source-context cards

Moving this logic out of `app/main.py` keeps the Streamlit entry point smaller and makes source-context behavior easier to test without launching the full UI.

---

## Incident Detection

### `app/incident_engine.py`

This file contains incident-response detection logic.

It identifies whether a question is about:

* suspected hacking
* unauthorized access
* suspicious login activity
* suspicious MFA activity
* suspicious links
* suspicious emails
* phishing
* compromised accounts
* ransomware
* malware
* encrypted files
* data leaks
* practical incident-response situations

This allows CyberLex Sweden to give practical first-step guidance when a user describes a security incident.

It also helps decide when SOC-style report export should appear and when related case examples should be hidden.

---

## SOC Incident Reports

### `app/incident_reports.py`

This file contains SOC-oriented incident report generation logic.

It handles:

* incident log templates
* SOC triage blocks
* evidence and containment prompts
* SOC control checklists
* copy-ready Markdown incident reports
* plain-text cleanup for downloaded reports
* short source notes for incident summaries

This keeps incident report generation separate from the Streamlit UI in `app/main.py`.

The app calls this module when a practical incident-response question is detected. Non-incident questions do not generate SOC reports.

Moving this logic into `incident_reports.py` makes the SOC report feature easier to test without launching the full Streamlit interface.

---

## Case Library Search

### `app/case_search.py`

This file handles search logic for the local case library in the `cases/` folder.

It finds related cases and incident examples for questions involving:

* GDPR risks
* Meta Pixel
* app data exposure
* wrong-recipient disclosures
* security deficiencies
* data leaks
* fines and cost examples
* privacy and cybersecurity incidents
* public incident examples

The case library is used for educational examples.

It should not be presented as legal advice or as a prediction of fines or outcomes.

---

## Experimental Retrieval

### `app/vector_search.py`

This file contains experimental search functionality.

Despite the file name, it is currently **not real vector search**.

It does not currently use:

* embeddings
* ChromaDB
* FAISS
* semantic similarity
* a language model
* RAG

It is currently an experimental rule-based retrieval module.

It can be used to test source ranking separately from the main answer system.

Future versions of CyberLex Sweden may expand this into a stronger vector-search or RAG-based system using tools such as ChromaDB, FAISS, or another embedding-based search system.

For now, it should remain separate from the main answer system so the working prototype does not get sacrificed to the altar of “new feature optimism.”

---

## Data Folders

### `data/`

The `data/` folder contains trusted Markdown source files used by the main CyberLex knowledge base.

These files cover topics such as:

* GDPR
* IMY
* personal data breaches
* GDPR security measures
* NIS2
* the Swedish Cybersecurity Act
* NIS2 sector scope
* NIS2 incident reporting
* cybercrime and dataintrång
* EU attacks against information systems
* DORA
* the Cyber Resilience Act
* defensive incident-response guidance

The source files are educational summaries based on selected trusted legal, regulatory, authority, and cybersecurity sources.

They are not complete legal sources.

### `cases/`

The `cases/` folder contains real or educational case examples.

These files are used to show how similar GDPR, privacy, cybersecurity, data-exposure, tracking-technology, weak-security, or incident-related issues have appeared in practice.

The case examples are educational context and should not be treated as legal advice, fine predictions, or proof that another case would have the same outcome.

### `docs/`

The `docs/` folder contains project documentation, including:

* architecture documentation
* technical design
* source list
* source policy
* source history
* source audit report
* source watch report
* test cases
* demo guidance
* legal disclaimer
* privacy and data-handling notes
* terms of use
* vector search plan
* AI/RAG plan
* product roadmap

### `scripts/`

The `scripts/` folder contains maintenance scripts.

Current important scripts include:

```text
scripts/source_audit.py
scripts/source_watch.py
scripts/case_audit.py
scripts/add_missing_metadata.py
```

These scripts support project maintenance.

`source_audit.py` checks local source-file structure.

`source_watch.py` checks official source URLs online and detects possible changes or failed links.

`case_audit.py` checks local case-library structure.

`add_missing_metadata.py` supports source metadata maintenance.

The audit scripts do not prove legal currentness.

The source watcher detects possible changes in official online sources, but it does not automatically rewrite local legal summaries.

### `source_snapshots/`

The `source_snapshots/` folder stores source-watch state.

Current important file:

```text
source_snapshots/source_watch_state.json
```

This file stores URL fingerprints and metadata used by `scripts/source_watch.py`.

It does not store full webpage copies.

It helps CyberLex detect whether official source pages appear to have changed since the previous watch run.

### `tests/`

The `tests/` folder contains automated regression tests.

Current test files:

```text
tests/test_incident_engine.py
tests/test_incident_reports.py
tests/test_language_detection.py
tests/test_routing_logic.py
tests/test_source_context.py
```

The tests currently cover:

* incident-response detection
* ransomware and encrypted-file detection
* suspicious login detection
* suspicious link detection
* suspicious email detection
* compromised-account detection
* data leak detection
* Swedish and English language detection
* mixed Swedish/English cyber wording
* routing behavior for selected question types
* SOC incident report generation
* SOC triage report content
* incident log template generation
* source-context excerpt cleaning and display formatting
* unsafe refusal routing
* out-of-scope routing
* CyberLex self-description routing
* NIS2 sector-scope routing
* case-context routing

The test suite can be run with:

```powershell
python -m pytest
```

---

## Current Module Structure

```text
app/
├── main.py              # Streamlit app flow, UI rendering, answer display, and page behavior
├── routing.py           # Question routing, behavior profiles, source targeting, and safety/scope routing
├── config.py            # App settings and folder paths
├── styles.py            # CSS and visual styling
├── text_utils.py        # Text normalization and matching helpers
├── language.py          # Swedish/English detection and localization
├── source_loader.py     # Markdown source loading, metadata extraction, and chunking
├── source_context.py    # Source-context cleaning, filtering, friendly names, and card generation
├── incident_engine.py   # Incident-response question detection
├── incident_reports.py  # SOC report, triage, checklist, and incident-log generation
├── case_search.py       # Related case and incident-example search
└── vector_search.py     # Experimental rule-based retrieval functionality
```

---

## Source Knowledge Base

The current source audit target covers 13 local source files in `data/`:

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

Expected source audit target:

```text
Files marked OK: 13
Files needing review: 0
```

The actual result should always be confirmed by running:

```powershell
python scripts/source_audit.py
```

The audit checks local structure and metadata.

It does not check the internet and does not prove that laws or guidance are currently up to date.

---

## Online Source Watch

CyberLex Sweden includes an online source watch system.

The source watcher is run with:

```powershell
python scripts/source_watch.py
```

It reads official source URLs from the local Markdown files in `data/`.

It checks whether each official source URL can be reached and whether the fetched content appears to have changed since the previous run.

It generates:

```text
docs/source_watch_report.md
```

It stores source-watch state in:

```text
source_snapshots/source_watch_state.json
```

The source watch report may show:

* first snapshots
* unchanged sources
* changed sources
* failed checks
* redirects
* HTTP status codes
* content hashes
* recommended manual review actions

The source watcher does not automatically update local source summaries.

Changed or failed official sources should be reviewed manually before local Markdown files are updated.

---

## Case Library

The current case audit checks 8 local case files in `cases/`:

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

The case library supports:

* related case examples below suitable answers
* the Case Intelligence page
* bilingual case display where available
* official or reliable case source links
* educational learning notes
* case topic tags
* fine or outcome notes where known

Case examples should be separated from main legal source answers.

They are learning material, not legal predictions.

---

## Case Intelligence Page

CyberLex Sweden includes a Case Intelligence page in the Streamlit interface.

The sidebar navigation includes:

```text
Ask CyberLex
Case Intelligence
```

The Case Intelligence page allows users to browse the local case library without asking a normal question.

It displays:

* case-library introduction
* search or filter input
* total case count
* shown case count
* limitation warning
* foldable case cards
* summaries
* learning notes
* outcomes, fines, or costs where known
* related topic badges
* official source links

The page follows the selected language where possible.

In English mode, it prefers English case sections.

In Swedish mode, it prefers Swedish case sections.

In Auto mode, source links may show broader available language options.

---

## Question and Answer Flow

The normal question flow is:

1. The user enters a question or selects an example question.
2. Streamlit session state stores the active question.
3. Auto language mode determines whether the active question should use Swedish or English.
4. The app builds a question behavior profile using `app/routing.py`.
5. The app checks whether the question is about CyberLex Sweden itself.
6. The app checks whether the question is unsafe and should be refused.
7. The app checks whether the question is inside the supported CyberLex scope.
8. The app routes supported questions toward a relevant source file where possible.
9. The app searches local Markdown chunks from `data/`.
10. The best source match is used to build the main CyberLex answer.
11. The app displays supporting source links, source metadata, limitations, practical sections, and source context where relevant.
12. Related cases from `cases/` are shown only when the question is suitable for case-library examples.
13. SOC-style report download is shown only for practical incident-response questions.

The app does not browse the web live during this process.

---

## Example Question Flow

The example question panel is designed for testing and demonstration.

When a user clicks an example question:

1. the example is stored as the selected question
2. the same question is stored as the submitted question
3. the input field is filled
4. the example panel is hidden
5. the app reruns and displays the answer directly

This means the user should not need to click the normal search button after selecting an example question.

A tiny mercy in the otherwise vast desert of button-clicking.

---

## Related Case Display Rules

CyberLex Sweden can show related cases and incident examples below normal answers.

Related cases are mainly shown for legal, compliance, and case-library-style questions such as:

```text
Can Meta Pixel create GDPR risk?
```

```text
Kan ett appfel exponera kunduppgifter?
```

```text
What can weak security measures cost?
```

However, related cases are normally hidden for practical incident-response triage questions such as:

```text
Our files are encrypted, what should we do?
```

```text
Vi har fått en misstänkt login på ett konto, vad ska vi göra?
```

For those questions, the app should focus on:

* defensive first steps
* containment
* evidence preservation
* escalation
* source context
* incident report support

This keeps the answer focused on what the user is actually asking.

---

## SOC Report Export

CyberLex Sweden can generate SOC-style Markdown reports for practical incident-response questions.

This feature is generated by `app/incident_reports.py` and is covered by automated tests in `tests/test_incident_reports.py`.

These reports may include:

* report metadata
* purpose
* original question or reported event
* handling note
* SOC triage
* recommended first steps
* SOC action support
* SOC control checklist
* incident log template
* short source note
* disclaimer

SOC reports are educational documentation aids.

They are not official incident records, forensic reports, legal assessments, regulatory notifications, breach notifications to IMY, or NIS2 incident reports.

---

## Automated Tests

CyberLex Sweden includes automated tests using `pytest`.

Current test files:

```text
tests/test_incident_engine.py
tests/test_incident_reports.py
tests/test_language_detection.py
tests/test_routing_logic.py
tests/test_source_context.py
```

The tests currently verify selected core behavior:

* incident detection
* language detection
* routing behavior
* source target selection
* related-case visibility
* SOC report visibility
* SOC report Markdown generation
* incident log template generation
* source-context excerpt cleaning and display formatting
* unsafe request refusal
* out-of-scope refusal
* NIS2 scope behavior
* CyberLex self-description behavior

Run tests locally with:

```powershell
python -m pytest
```

Expected current result:

```text
50 passed
```

The GitHub Actions test workflow also runs these tests automatically.

Workflow file:

```text
.github/workflows/tests.yml
```

This workflow runs on:

* pushes to `main`
* pull requests to `main`
* manual workflow dispatch

The automated tests are not full UI tests yet.

They are a regression safety net for core logic. In less decorative terms: they stop future “small improvements” from silently punching holes in working behavior.

---

## GitHub Actions Workflows

CyberLex Sweden currently includes three GitHub Actions workflows:

```text
.github/workflows/source-audit.yml
.github/workflows/source-watch.yml
.github/workflows/tests.yml
```

### Weekly Source Audit

Runs:

```powershell
python scripts/source_audit.py
```

Purpose:

* checks local Markdown source structure
* updates `docs/source_audit_report.md`

This does not confirm live legal currentness.

### Weekly Source Watch

Runs:

```powershell
python scripts/source_watch.py
python scripts/source_audit.py
```

Purpose:

* checks official online source URLs
* detects possible source changes or failed links
* updates `docs/source_watch_report.md`
* updates `docs/source_audit_report.md`
* updates `source_snapshots/source_watch_state.json`

This does not update local legal summaries automatically.

### Tests

Runs:

```powershell
python -m pytest
```

Purpose:

* checks automated regression tests
* verifies selected incident, language, and routing behavior
* fails if core tested behavior breaks

---

## Why the App Was Refactored

Earlier versions of CyberLex Sweden had most of the logic inside `app/main.py`.

That worked for a prototype, but it made the file harder to read and maintain as the project grew.

The refactor improves the project by:

* making the code easier to understand
* separating UI from helper logic
* separating routing logic from Streamlit rendering
* separating SOC report generation from Streamlit rendering
* separating source-context display from Streamlit rendering
* making automated tests easier
* making future source-routing tests possible
* making the project look more professional
* making it easier to add new features later
* reducing the risk of breaking unrelated parts of the app

---

## Current Verification Commands

Run syntax checks:

```powershell
python -m py_compile app/main.py
python -m py_compile app/routing.py
python -m py_compile app/config.py
python -m py_compile app/styles.py
python -m py_compile app/text_utils.py
python -m py_compile app/language.py
python -m py_compile app/source_loader.py
python -m py_compile app/source_context.py
python -m py_compile app/incident_engine.py
python -m py_compile app/incident_reports.py
python -m py_compile app/case_search.py
python -m py_compile app/vector_search.py
python -m py_compile scripts/source_watch.py
```

These commands check whether the Python files can compile without syntax errors.

Run tests:

```powershell
python -m pytest
```

This runs automated regression tests.

Run audits and source watch:

```powershell
python scripts/source_watch.py
python scripts/source_audit.py
python scripts/case_audit.py
```

These commands run the online source watch, local source audit, and local case audit.

The audit commands check local file structure and metadata.

The source-watch command checks official URLs and possible source changes.

Run the app:

```powershell
python -m streamlit run app/main.py
```

This starts the local Streamlit application.

---

## Future Architecture Improvements

Possible future improvements include:

* moving answer-generation logic into `answer_engine.py`
* moving search-ranking logic into `search_engine.py`
* expanding tests for source-context edge cases and card selection behavior
* moving UI components into `ui_components.py`
* moving safety checks into a dedicated `safety.py` module if they grow beyond routing
* adding `semantic_search.py` for real vector search later
* adding automated tests for source ranking
* adding automated tests for case matching
* expanding automated tests for incident report generation and report edge cases
* adding automated tests for source watch behavior
* adding full Streamlit UI smoke tests later
* expanding vector search into a full RAG pipeline
* adding stronger citation handling
* improving deployment structure for Streamlit Cloud or another hosting platform

These improvements should be made gradually so the current working prototype remains stable.

The current technical priority should be:

```text
Stable prototype first.
Broader automated tests second.
Real vector search later.
RAG only after reliable retrieval.
```

---

## Important Limitation

CyberLex Sweden is an educational prototype.

It does not provide legal advice and should not replace:

* a qualified lawyer
* a data protection officer
* an official authority
* a compliance specialist
* a professional incident-response team
* internal organizational policies and procedures

The app should always make clear that its answers are educational and source-grounded, not official legal decisions.

The source audit and case audit are local structure checks only.

The source watcher can detect changed or failed official source URLs, but it does not understand legal meaning and does not update local legal summaries automatically.

They do not prove live legal accuracy or currentness.

---

## Final Note

CyberLex Sweden is built around a simple principle:

```text
Better sources first. Better AI second.
```

The current architecture supports that principle by keeping the system local, inspectable, source-grounded, cautious, and easier to test.

That may sound less exciting than a magical AI oracle. Which is good, since Oracles were mostly disaster machines with better branding.
