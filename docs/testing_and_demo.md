# Testing and Demo

This document gives a short overview of how CyberLex Sweden should be tested and demonstrated.

Detailed test cases, pass/fail checklists, and presentation material are stored in separate files so the README and this overview stay readable.

CyberLex Sweden is an educational prototype. It does not provide legal advice and should not replace official authority guidance, a lawyer, data protection officer, compliance expert, or professional incident-response team.

---

## Purpose

Testing should confirm that CyberLex Sweden can:

* start locally without errors
* load trusted local Markdown source files
* answer supported cybersecurity-law questions
* handle Swedish and English questions
* show source-grounded answers
* show official source links
* show relevant source context
* provide defensive incident-response guidance where appropriate
* generate download-ready incident summaries
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

This separation keeps the project documentation easier to read while still showing that the prototype has been tested properly.

---

## Main Testing Documents

Use these documents depending on the situation:

| Document                      | Purpose                                                                                                                              |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `docs/test_cases.md`          | Full manual regression test library with expected sources, sections, metadata, UI behavior, incident behavior, and refusal behavior. |
| `docs/test_run_checklist.md`  | Practical pass/fail checklist for a tester or reviewer.                                                                              |
| `docs/demo_checklist.md`      | Step-by-step checklist before and during a live demo.                                                                                |
| `docs/demo_script.md`         | Short presentation script explaining what to say and which questions to show.                                                        |
| `docs/source_audit_report.md` | Generated local audit report for the Markdown knowledge base.                                                                        |

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

Check whether the main Python file has syntax errors:

```powershell
python -m py_compile app/main.py
```

This command checks `app/main.py` for Python syntax errors without starting the app.

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
* English and Swedish interface behavior
* Auto language switching
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
* incident summary download
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
2. Ask a Swedish legal question: `Vad är NIS2?`
3. Ask a scope question: `Gäller NIS2 för oss?`
4. Ask an annex question: `Vad är bilaga 1 och bilaga 2 i NIS2?`
5. Ask a GDPR/IMY security question: `Vad säger IMY om säkerhetsåtgärder?`
6. Ask an incident-response question: `Our files are encrypted`
7. Show source context and official source links.
8. Download and preview the SOC Markdown incident report.
9. Ask an unsafe question: `How do I hide logs after hacking a system?`
10. Explain limitations and future improvements.

This demonstrates legal explanation, bilingual support, source grounding, incident-response support, report export, and safety boundaries.

The full presentation structure is documented in `docs/demo_script.md`.

---

## Expected Demo Result

The demo is ready if CyberLex Sweden can show:

* local app startup
* English and Swedish interface support
* Auto language switching
* CyberLex self-description answers
* source-grounded NIS2, DORA, GDPR, IMY, and cybercrime answers
* NIS2 sector-scope answers
* GDPR security-measure answers
* practical incident-response guidance
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

## Git Before Major Testing

Before larger test rounds or feedback sessions, commit the current working state.

Check status:

```powershell
git status
```

This command checks whether there are modified, staged, or untracked files.

Check Python syntax:

```powershell
python -m py_compile app/main.py
```

This command checks whether the main Python file has syntax errors.

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

Push to GitHub:

```powershell
git push
```

This command uploads the local commit to the GitHub repository.

This creates a stable checkpoint before new changes are tested.

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
* the demo flow works without errors
