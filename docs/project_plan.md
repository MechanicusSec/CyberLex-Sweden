# CyberLex Sweden Project Plan

## Purpose

This document describes the project plan for CyberLex Sweden and summarizes how the project developed from an early idea into a working educational legal-tech prototype.

CyberLex Sweden is a local source-grounded prototype focused on selected Swedish and EU cybersecurity-law topics, data protection, digital compliance, cybercrime, and defensive incident-response support.

CyberLex Sweden does not provide legal advice.

---

## Project Summary

CyberLex Sweden was planned as a final school project with an estimated duration of 4 to 6 weeks.

The project has now moved beyond the original basic prototype plan. The main prototype, local source system, testing, documentation, and demo preparation are largely completed.

The current phase is focused on:

* final documentation cleanup
* final testing
* final demo preparation
* final GitHub cleanup
* optional low-risk polish before hand-in

Larger technical upgrades, such as real vector search, RAG, public deployment, and further code modularization, should be treated as future work.

---

## Main Goal

The main goal was to build a source-grounded assistant that helps users understand selected Swedish and EU cybersecurity-law topics using trusted local source material.

The project goals were to:

* create a working local Streamlit prototype
* use a trusted local Markdown knowledge base
* answer only from supported source topics
* display source context and official source links
* show source metadata and limitations
* refuse unsupported or out-of-scope questions
* refuse unsafe offensive cyber requests
* support both English and Swedish use
* document the project clearly for review and future development

---

## Current Project Status

CyberLex Sweden is currently a working local prototype.

Completed major features include:

* Streamlit web interface
* modular Python app structure after refactoring `app/main.py`
* local Markdown knowledge base
* source-based search
* rule-based routing
* source-grounded answers
* bilingual interface support
* Auto language detection
* official source links
* source metadata
* source quality labels
* source freshness labels
* source confidence explanations
* detected topic labels
* styled answer cards
* practical explanation cards
* assessment checklist cards
* relevant source context display
* expandable source excerpts
* other matching source sections
* example question buttons that run immediately when selected
* experimental retrieval sidebar
* defensive incident-response guidance
* hidden related-case section for practical incident-response triage questions
* SOC-style Markdown incident report export
* out-of-scope refusal behavior
* unsafe cyber refusal behavior
* source audit script
* source audit report
* GitHub Actions source audit workflow
* testing and demo documentation
* technical design documentation
* architecture documentation
* UI behavior documentation
* source-context behavior documentation
* source policy documentation
* final project documentation

The current version is stable enough for final testing and demonstration.

---

## Current Knowledge Base

The current local knowledge base is stored in:

```text
data/
```

Current local source files include:

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

The exact source list should be checked against:

```text
docs/source_list.md
```

The source list is the main reference for current source files.

---

## Phase 1: Planning and Scope

### Goal

Define the project idea, scope, source approach, and initial documentation.

### Completed Work

* Created the project identity: CyberLex Sweden
* Defined the project as a Swedish/EU cybersecurity-law assistant
* Limited the project scope to selected cyber, data protection, and digital compliance topics
* Chose a source-grounded design
* Created the basic project folder structure
* Created initial documentation
* Identified trusted source categories
* Wrote initial project overview and source policy material

### Result

CyberLex Sweden had a clear concept before the main prototype work began.

The most important early design decision was:

```text
Better sources first. Better AI second.
```

This means the project focuses first on trusted source material and source transparency before adding more advanced AI features.

---

## Phase 2: Source Collection and Knowledge Base

### Goal

Create a local knowledge base using selected trusted Swedish and EU cybersecurity-law sources.

### Completed Work

* Created Markdown knowledge files in the `data/` folder
* Added official source links
* Added source metadata
* Added source dates and version notes
* Added source quality information
* Added Swedish summaries where useful
* Added useful questions to support testing and retrieval
* Expanded the knowledge base with NIS2, GDPR, IMY, DORA, CRA, cybercrime, and incident-response material

### Result

CyberLex Sweden now has a reviewed local knowledge base that supports the current prototype scope.

The source audit and source list help keep this knowledge base easier to review.

---

## Phase 3: Basic Prototype

### Goal

Build a working local app that can answer selected questions from the local knowledge base.

### Completed Work

* Created the main app entry point:

```text
app/main.py
```

* Added a Streamlit interface
* Added local question input
* Added answer display
* Added source file loading
* Added source matching
* Added basic refusal behavior
* Added example questions

### Result

CyberLex Sweden became a working local web app.

The app could load local Markdown files and answer selected questions from supported source material.

---

## Phase 4: Source-Grounded Answer System

### Goal

Improve how CyberLex Sweden finds sources, shows evidence, and avoids unsupported answers.

### Completed Work

* Added Markdown chunking by section headings
* Added keyword-based source search
* Added rule-based source routing
* Added topic-specific boosts and penalties
* Added official source links
* Added source metadata display
* Added source quality labels
* Added source freshness labels
* Added source confidence explanations
* Added relevant source context
* Added other matching source sections
* Added source-grounded short answers
* Added refusal behavior for unsupported topics

### Result

CyberLex Sweden now gives answers with visible source support instead of unsupported free-form responses.

The app shows users where the answer came from and what limitations apply.

---

## Phase 5: Interface and Answer Layout

### Goal

Make the prototype easier to understand, test, and demonstrate.

### Completed Work

* Styled answer cards
* Styled citation details
* Styled official source links
* Styled source metadata
* Styled important limitation notices
* Styled CyberLex attention levels
* Practical explanation cards
* Assessment checklist expanders
* Relevant source context expanders
* Other matching source sections
* Example question buttons
* Example questions that run immediately when selected
* Improved layout spacing
* Cleaner footer and disclaimer placement
* More compact source context by default

### Result

CyberLex Sweden became easier to present and review.

The interface now separates answer, source, limitation, practical guidance, and supporting context more clearly.

---

## Phase 6: English and Swedish Support

### Goal

Support both English and Swedish as main project languages.

### Completed Work

* English interface mode
* Swedish interface mode
* Auto language detection
* English and Swedish example questions
* Swedish labels for major answer sections
* Swedish routing improvements
* Swedish source summaries where useful
* Swedish incident-response behavior
* Swedish unsafe-request refusal behavior
* Swedish source-section localization for selected labels
* mixed Swedish/English cybersecurity-law question handling

### Current Supported Examples

CyberLex Sweden can handle questions such as:

```text
What is NIS2?
Vad är NIS2?
Gäller NIS2 för oss?
Vad är bilaga 1 och bilaga 2 i NIS2?
Vad säger IMY om säkerhetsåtgärder?
Does GDPR require MFA?
Customer data may have leaked
Kunddata kan ha läckt
Our files are encrypted
Våra filer har krypterats
How do I hide logs after hacking a system?
Hur raderar jag loggar efter ett intrång?
```

### Result

The project has stronger bilingual support than the original prototype plan.

More bilingual source summaries and answer wording can still be improved later.

---

## Phase 7: Incident-Response Support

### Goal

Add practical defensive support for common cybersecurity incident scenarios.

### Completed Work

CyberLex Sweden can now detect and respond to practical incident questions about:

* suspicious emails
* suspicious links
* SMS phishing
* suspicious logins
* compromised accounts
* possible data leaks
* personal data breaches
* ransomware or encrypted files
* suspected hacking or intrusion

Incident answers focus on:

* containment
* evidence preservation
* logging and documentation
* escalation
* recovery planning
* GDPR/NIS2 reporting assessment where relevant

For practical incident-response triage questions, related historical case examples should stay hidden by default so the answer stays focused on immediate defensive handling.

### SOC Markdown Report Export

CyberLex Sweden can generate a SOC-style Markdown incident report for practical incident-response questions.

The report includes:

* report metadata
* purpose
* question or reported event
* handling note
* SOC triage
* recommended first steps
* SOC action support
* SOC control checklist
* incident log template
* source note
* disclaimer

### Result

The project now demonstrates both legal-tech explanation and practical defensive incident-response support.

---

## Phase 8: Safety and Refusal Behavior

### Goal

Keep CyberLex Sweden within its intended educational and defensive scope.

### Completed Work

CyberLex Sweden refuses:

* unsupported out-of-scope questions
* unrelated legal topics
* general non-cyber questions
* unsafe offensive cyber requests
* credential theft
* log hiding
* trace deletion
* detection bypassing
* unauthorized access guidance

Unsafe cyber requests are redirected toward lawful defensive handling, evidence preservation, documentation, and proper reporting.

### Result

The project has clear safety boundaries.

This is important because CyberLex Sweden covers cybersecurity topics and should not become a guide for misuse.

---

## Phase 9: Case Library and Case Intelligence

### Goal

Add educational case examples so users can connect general legal and cybersecurity questions to real-world authority decisions, public incidents, and historical examples.

### Completed Work

* Added separate case library folder:

```text
cases/
```

* Added 8 checked case files
* Added case index and case template
* Added related case search
* Added Case Intelligence page
* Added expandable case cards
* Added case summaries
* Added Swedish case summaries where available
* Added learning notes
* Added Swedish learning notes where available
* Added administrative fine or outcome sections
* Added official source links
* Added language-aware case source display
* Added case audit script:

```text
scripts/case_audit.py
```

* Added case audit report:

```text
docs/case_library/case_audit_report.md
```

### Result

CyberLex Sweden can show related case examples for suitable compliance and case-library questions while keeping those examples separate from the main legal/source knowledge base.

Historical case examples are educational context and should not be presented as fine predictions or legal outcome predictions.

---

## Phase 10: Source Audit and Maintenance

### Goal

Make source quality easier to review and maintain.

### Completed Work

* Added source metadata blocks
* Added source dates
* Added version notes
* Added source quality labels
* Added source freshness labels
* Added:

```text
scripts/source_audit.py
```

* Added:

```text
docs/source_audit_report.md
```

* Added source history documentation:

```text
docs/source_history.md
```

* Added source policy documentation:

```text
docs/source_policy.md
```

* Added GitHub Actions source audit workflow

### Source Audit Command

```powershell
python scripts/source_audit.py
```

This command checks the local Markdown source files in the `data/` folder and updates the source audit report.

### Important Limitation

The source audit checks local file structure and metadata.

It does not browse the web and does not confirm whether legal information is currently up to date.

### Result

CyberLex Sweden now has a repeatable local source-audit process.

---

## Phase 11: Testing and Validation

### Goal

Document test behavior and verify that the prototype works before final hand-in.

### Completed Work

* Added full manual regression test cases:

```text
docs/test_cases.md
```

* Added practical tester checklist:

```text
docs/test_run_checklist.md
```

* Added demo checklist:

```text
docs/demo_checklist.md
```

* Added demo script:

```text
docs/demo_script.md
```

* Added testing overview:

```text
docs/testing_and_demo.md
```

### Tested Areas

CyberLex Sweden has been tested for:

* app startup
* Python syntax
* source loading
* source matching
* English answers
* Swedish answers
* Auto language switching
* example questions that run immediately
* official source links
* source metadata
* source context readability
* GDPR/IMY questions
* NIS2 questions
* DORA questions
* Cyber Resilience Act questions
* cybercrime questions
* incident-response questions
* related cases shown for case-library questions
* related cases hidden for practical incident triage
* Case Intelligence page
* SOC Markdown report download
* out-of-scope refusal
* unsafe cyber refusal

### Result

The project has a documented manual testing process and expected behavior for the main supported topics.

---

## Phase 12: Documentation and Final Preparation

### Goal

Prepare documentation for final school hand-in and future development.

### Current Documentation Areas

The project documentation includes:

* project overview
* project plan
* technical design
* architecture
* UI behavior
* source context behavior
* source list
* source policy
* source history
* source context behavior
* source audit report
* testing and demo material
* legal disclaimer
* privacy and data handling
* terms of use
* product roadmap
* AI/RAG plan
* vector search plan

### Result

CyberLex Sweden now has enough documentation to explain:

* what the project is
* what problem it solves
* how the app works
* what sources it uses
* how testing works
* what limitations apply
* what future improvements are planned

---

## Postponed Technical Work

Some technical improvements should be postponed until after final hand-in.

### Real Vector Search

Real vector search was planned but paused because the local environment used Python 3.14, which caused dependency compatibility issues with AI packages.

Future vector search should be revisited with Python 3.12 or Python 3.11.

The detailed plan is documented in:

```text
docs/vector_search_plan.md
```

### RAG and AI-Generated Answers

A future version may use Retrieval-Augmented Generation, also called RAG.

This should only be added after retrieval quality is reliable and source grounding is preserved.

The detailed plan is documented in:

```text
docs/ai_rag_plan.md
```

### Further Code Modularization

The earlier large `app/main.py` file has already been partly refactored into smaller modules:

```text
app/config.py
app/styles.py
app/text_utils.py
app/language.py
app/source_loader.py
app/incident_engine.py
app/case_search.py
app/vector_search.py
```

The app entry point is still:

```text
app/main.py
```

Further future refactor work could split remaining logic into modules such as:

```text
app/ui_components.py
app/answer_engine.py
app/search_engine.py
app/source_context.py
app/incident_reports.py
app/safety.py
```

Further refactoring should be gradual and tested carefully, not done immediately before final hand-in unless there is enough time and low risk.

---

## Near-Term Final Hand-In Checklist

Before final delivery, check:

* [ ] Python syntax checks pass for all current app modules
* [ ] `python scripts/source_audit.py` runs successfully
* [ ] `python scripts/case_audit.py` runs successfully
* [ ] `python -m streamlit run app/main.py` starts correctly
* [ ] main English questions work
* [ ] main Swedish questions work
* [ ] Auto language switching works
* [ ] example questions run immediately when selected
* [ ] related cases appear for suitable case-library questions
* [ ] related cases are hidden for practical incident triage questions
* [ ] Case Intelligence page loads correctly
* [ ] source context is readable
* [ ] official source links are visible
* [ ] SOC Markdown report download works
* [ ] out-of-scope refusal works
* [ ] unsafe cyber refusal works
* [ ] README is current
* [ ] docs are current
* [ ] final report or presentation material is current
* [ ] no unwanted generated files are committed
* [ ] `git status` shows a clean working tree

---

## Git and Push Policy

For the current cleanup phase, CyberLex Sweden should not be pushed to GitHub after every small edit.

Recommended workflow:

1. make local changes
2. test the changed behavior
3. commit stable local checkpoints
4. collect several meaningful changes
5. push after a stable batch or milestone

Good push moments include:

* 10 to 15 meaningful local changes
* a completed documentation batch
* a completed test batch
* a stable code feature
* a final hand-in or demo checkpoint

This keeps the repository cleaner while the project is still changing quickly.

---

## Useful Final Commands

Move into the project folder:

```powershell
cd C:\Projects\CyberLex-Sweden
```

This command moves PowerShell into the local CyberLex Sweden project folder.

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

These commands check whether the current Python app modules have syntax errors.

Run source audit:

```powershell
python scripts/source_audit.py
```

This command checks the local Markdown source files and updates the source audit report.

Run case audit:

```powershell
python scripts/case_audit.py
```

This command checks the local case-library files and updates the case audit report.

Start the app:

```powershell
python -m streamlit run app/main.py
```

This command starts the local Streamlit web app.

Check Git status:

```powershell
git status
```

This command checks whether there are uncommitted file changes.

Stage changes:

```powershell
git add .
```

This command stages modified, new, and deleted files for the next commit.

Commit changes:

```powershell
git commit -m "Update CyberLex project planning documentation"
```

This command saves the staged changes in Git with a clear message.

Push changes only after a stable batch or milestone:

```powershell
git push
```

This command uploads local commits to GitHub.

Do not push after every small documentation or code edit. A better workflow is to push after 10 to 15 meaningful changes, a completed documentation batch, a completed test batch, or a final demo/hand-in checkpoint.

---

## Success Criteria

The current project phase is successful when CyberLex Sweden can:

* run locally with Streamlit
* load trusted local source files
* answer supported questions from local source material
* display source details and official links
* show source metadata and limitations
* support English and Swedish questions
* support Auto language behavior
* run example questions immediately when selected
* show related cases where relevant
* hide related cases during practical incident triage
* provide defensive incident-response guidance where useful
* generate a SOC-style Markdown incident report
* refuse out-of-scope questions
* refuse unsafe cyber requests
* pass the main manual test cases
* load the Case Intelligence page correctly
* maintain clear documentation
* remain honest about limitations

---

## Summary

The original 4 to 6 week project plan has been largely completed for the current prototype phase.

CyberLex Sweden now has:

* a working local Streamlit app
* a partly refactored modular Python app structure
* a trusted local Markdown knowledge base
* source-grounded answers
* official source links
* source metadata
* bilingual interface support
* Auto language behavior
* example questions that run immediately
* related case examples where relevant
* Case Intelligence page
* practical incident-response support
* SOC-style Markdown report export
* safety refusal behavior
* source audit support
* case audit support
* manual test cases
* demo documentation
* roadmap documentation
* future AI and vector search plans

The next major technical upgrade is broader automated testing and then real vector search, but vector search should be done later with a stable Python version and a low-risk implementation plan.

For the final hand-in, the focus should remain on polish, testing, documentation consistency, and presentation readiness.
