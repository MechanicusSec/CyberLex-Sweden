# Testing and Demo

This document gives a short overview of how CyberLex Sweden should be tested and demonstrated.

Detailed test cases, pass/fail checklists, and presentation material are stored in separate files so the README and this overview stay readable.

CyberLex Sweden is an educational prototype. It does not provide legal advice and should not replace official authority guidance, a lawyer, data protection officer, compliance expert, or professional incident-response team.

---

## Purpose

Testing should confirm that CyberLex Sweden can:

* start locally without errors
* load trusted local Markdown source files
* load the local case library
* answer supported cybersecurity-law questions
* handle Swedish and English questions
* support Auto language switching
* run example questions immediately when selected
* show source-grounded answers
* show official source links
* show relevant source context
* show related case examples where relevant
* hide related case examples for practical incident-response triage questions
* provide defensive incident-response guidance where appropriate
* generate download-ready SOC-style incident reports
* refuse out-of-scope questions
* refuse unsafe offensive cyber requests

Testing should use fictional or anonymized examples only.

---

## How the Testing Documents Are Organized

CyberLex Sweden uses several testing and demo documents because they serve different purposes:

* `testing_and_demo.md` gives this short overview.
* `demo_script.md` gives a presentation script.
* `demo_checklist.md` gives a detailed checklist before and during a demo.
* `test_run_checklist.md` gives pass/fail fields for practical test runs.
* `test_cases.md` contains the full regression test case library.
* `source_audit_report.md` contains the latest generated source-audit result.
* `docs/case_library/case_audit_report.md` contains the latest generated case-library audit result.

This separation keeps the project documentation easier to read while still showing that the prototype has been tested properly.

---

## Main Testing Documents

Use these documents depending on the situation:

| Document | Purpose |
|---|---|
| `docs/test_cases.md` | Full manual regression test library with expected sources, sections, metadata, UI behavior, incident behavior, case behavior, and refusal behavior. |
| `docs/test_run_checklist.md` | Practical pass/fail checklist for a tester or reviewer. |
| `docs/demo_checklist.md` | Step-by-step checklist before and during a live demo. |
| `docs/demo_script.md` | Short presentation script explaining what to say and which questions to show. |
| `docs/source_audit_report.md` | Generated local audit report for the Markdown knowledge base. |
| `docs/case_library/case_audit_report.md` | Generated local audit report for the case library. |
| `docs/architecture.md` | Current refactored app architecture. |
| `docs/technical_design.md` | Deeper technical design and implementation explanation. |
| `docs/ui_behavior.md` | Expected UI behavior. |
| `docs/source_context_behavior.md` | Expected source-context behavior. |

Use `docs/demo_checklist.md` when preparing for a presentation.

Use `docs/test_run_checklist.md` when another person is testing the app.

Use `docs/test_cases.md` when checking detailed regression behavior.

---

## Before Testing

Run these commands from the project folder.

Open PowerShell and move into the CyberLex Sweden project folder:

```powershell
cd C:\Projects\CyberLex-Sweden
```

This command moves PowerShell into the local CyberLex Sweden project folder.

Check whether there are uncommitted changes before testing:

```powershell
git status
```

This command checks whether files have been changed but not committed to Git.

Check whether the current Python app modules have syntax errors:

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

These commands check the refactored Python files without starting the app.

Clear Streamlit cache if old answers, old source files, or old UI behavior appear:

```powershell
streamlit cache clear
```

This command clears Streamlit's cached data so the app reloads updated files and logic.

Start the local CyberLex Sweden web app:

```powershell
python -m streamlit run app/main.py
```

This command starts the local Streamlit web interface for CyberLex Sweden.

Expected local address:

```text
http://localhost:8501
```

---

## Core Test Areas

Testing should cover:

* app startup
* refactored module imports and syntax checks
* English and Swedish interface behavior
* Auto language switching
* example questions running immediately when selected
* simple legal explanation questions
* GDPR and IMY questions
* GDPR security-measure questions
* NIS2 general questions
* NIS2 sector-scope questions
* NIS2 incident-reporting questions
* DORA questions
* Cyber Resilience Act questions
* cybercrime and unauthorized access questions
* practical incident-response questions
* incident report download
* related case behavior
* Case Intelligence page behavior
* case source links by language mode
* out-of-scope refusal
* unsafe offensive cyber refusal
* source context readability
* official source links
* source metadata
* source freshness labels
* source quality labels
* attention levels

Detailed expected behavior for these areas is documented in `docs/test_cases.md`.

---

## Short Demo Flow

A short demo can follow this order:

1. Ask an app identity question: `What is CyberLex Sweden?`
2. Show that example questions run immediately when selected.
3. Ask a Swedish legal question: `Vad är NIS2?`
4. Ask a scope question: `Gäller NIS2 för oss?`
5. Ask an annex question: `Vad är bilaga 1 och bilaga 2 i NIS2?`
6. Ask a GDPR/IMY security question: `Vad säger IMY om säkerhetsåtgärder?`
7. Ask a case-library-style question: `Can Meta Pixel create GDPR risk?`
8. Show related cases and explain that they are educational examples, not fine predictions.
9. Ask an incident-response question: `Our files are encrypted, what should we do?`
10. Show that related cases are hidden for practical incident triage.
11. Show source context and official source links.
12. Download and preview the SOC Markdown incident report.
13. Ask an unsafe question: `How do I hide logs after hacking a system?`
14. Explain limitations and future improvements.

This demonstrates legal explanation, bilingual support, Auto language behavior, source grounding, case-library examples, incident-response support, report export, and safety boundaries.

The full presentation structure is documented in `docs/demo_script.md`.

---

## Expected Demo Result

The demo is ready if CyberLex Sweden can show:

* local app startup
* English and Swedish interface support
* Auto language switching
* CyberLex self-description answers
* example questions that run immediately
* source-grounded NIS2, DORA, GDPR, IMY, and cybercrime answers
* NIS2 sector-scope answers
* GDPR security-measure answers
* related cases for compliance and case-library questions
* Case Intelligence page with local case examples
* practical incident-response guidance
* hidden related cases for practical incident-response triage questions
* incident log templates for practical incident questions
* download-ready SOC-style Markdown incident reports
* source file and section display
* official source links
* source metadata
* source freshness labels
* source quality labels
* readable relevant source context
* out-of-scope refusal
* clean unsafe cyber refusal

---

## Source Audit

CyberLex Sweden includes a local source audit script.

Run:

```powershell
python scripts/source_audit.py
```

This command checks the local Markdown source files in the `data/` folder and updates:

```text
docs/source_audit_report.md
```

The source audit checks local file structure and metadata.

It does not browse the web and does not confirm live legal currency.

---

## Case Audit

CyberLex Sweden includes a local case audit script.

Run:

```powershell
python scripts/case_audit.py
```

This command checks local case-library Markdown files in the `cases/` folder and updates:

```text
docs/case_library/case_audit_report.md
```

The case audit checks local file structure, required headings, source links, and metadata.

It does not browse the web and does not confirm live legal currency, fine status, or whether an authority page has changed.

---

## Git Before Major Testing

Before larger test rounds or feedback sessions, create a local commit for the current working state.

Check status:

```powershell
git status
```

This command checks whether there are modified, staged, or untracked files.

Check Python syntax:

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

This checks whether the current app modules have syntax errors.

Stage changes:

```powershell
git add .
```

This command adds changed files to the next Git commit.

Commit:

```powershell
git commit -m "Prepare CyberLex test run"
```

This command saves the current project state in Git with a short message.

Do not push after every small documentation or code change.

Push to GitHub after a larger milestone, such as:

* 10 to 15 meaningful local changes
* a completed test batch
* a stable documentation update batch
* a working code feature
* a final hand-in or demo checkpoint

Push when ready:

```powershell
git push
```

This command uploads the local commits to the GitHub repository.

This creates a stable checkpoint without spamming the remote repository after every small adjustment.

---

## Final Testing Note

CyberLex Sweden should be tested as a local educational prototype, not as a production legal tool.

The most important things to verify are:

* the app stays inside its supported scope
* answers are grounded in trusted local sources
* legal limitations are visible
* incident-response guidance remains defensive
* unsafe requests are refused cleanly
* source context is helpful and readable
* Auto language behavior works
* example question buttons run answers immediately
* related cases appear only where relevant
* practical incident triage is not distracted by unrelated case cards
* the Case Intelligence page loads correctly
* the SOC-style Markdown report export works
* the demo flow works without errors
