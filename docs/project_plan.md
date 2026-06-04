# CyberLex Sweden Project Plan

## Purpose

This document describes the planned work for CyberLex Sweden and tracks how the project developed from an early prototype into the current source-grounded educational application.

CyberLex Sweden is an educational legal-tech and cybersecurity-law prototype. It focuses on selected Swedish and EU cybersecurity law, cybercrime, data protection, incident reporting, and digital compliance topics.

The project does not provide legal advice.

---

## Project Duration

Estimated duration: 4 to 6 weeks.

The project has now moved beyond the original basic prototype plan. The main prototype, source expansion, testing, and documentation phases are largely completed.

Further work is now focused on polish, final testing, optional UI improvements, and later technical upgrades such as real vector search and RAG.

---

## Main Goal

Build a source-grounded assistant that helps users understand selected Swedish and EU cybersecurity-law topics using trusted local source material.

The main goals are:

- create a working local Streamlit prototype
- use a trusted local Markdown knowledge base
- answer only from supported source topics
- display citation details and official source links
- show source metadata and limitations
- refuse unsupported or out-of-scope questions
- support both English and Swedish interface use
- document the project clearly for review and future development

---

## Current Status

CyberLex Sweden is currently a working local prototype.

Completed major features include:

- Streamlit web interface
- local Markdown knowledge base
- rule-based source search
- source routing
- source-grounded answers
- bilingual interface support
- official source links
- source metadata
- source quality labels
- source freshness labels
- source confidence explanations
- detected topic labels
- styled answer cards
- practical explanation cards
- assessment checklist cards
- relevant source context display
- other matching source sections
- example question buttons
- experimental AI search sidebar
- source audit script
- weekly GitHub Actions source audit workflow
- expanded source documentation
- test cases
- technical design documentation
- product roadmap
- final report
- README update

The first attempt at real vector search was paused because the local system only had Python 3.14 available, which caused package compatibility issues with AI libraries. Vector search remains planned for later, preferably using Python 3.12 or 3.11.

---

## Phase 1: Planning and Research

### Original goal

- Define project scope
- Create project folders
- Create documentation files
- Identify trusted legal and cybersecurity sources
- Write project overview
- Write source list

### Status

Completed.

### Completed work

- Created project identity as CyberLex Sweden
- Defined scope around Swedish and EU cybersecurity law
- Created project folder structure
- Created initial documentation files
- Identified trusted source categories
- Added project overview
- Added source list
- Added source policy
- Added legal disclaimer, Terms of Use, and Privacy Policy drafts

### Result

CyberLex Sweden had a clear concept, project scope, source policy, and documentation structure before the main prototype work continued.

---

## Phase 2: Source Collection and Knowledge Base

### Original goal

- Collect official Swedish and EU sources
- Save links and documents
- Organize material by topic
- Prepare text files for the AI system

### Status

Completed for the current prototype scope.

### Completed source files

The current local knowledge base includes:

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

### Supported topics

The current source files support selected questions about:

- Swedish cybercrime and dataintrång
- EU attacks against information systems
- Cyber Resilience Act
- DORA
- GDPR core principles
- GDPR personal data breach notification
- IMY and Swedish GDPR supervision
- NIS2 and Swedish cybersecurity law
- NIS2 incident reporting
- ransomware and cyber incident assessment
- overlap between GDPR, NIS2, DORA, CRA, and cybercrime topics

### Result

The project now has 9 reviewed local knowledge files with official source links and source metadata.

The local source audit target is:

```text
Files marked OK: 9
Files needing review: 0
```

---

## Phase 3: Basic Prototype

### Original goal

- Install Python tools
- Create a simple Streamlit app
- Build a basic chatbot interface
- Test simple questions and answers

### Status

Completed.

### Completed work

- Created `app/main.py`
- Added Streamlit interface
- Added local question input
- Added answer display
- Added source-based search
- Added basic source matching
- Added out-of-scope refusal behavior
- Added example questions

### Result

CyberLex Sweden became a working local web app that could answer selected questions from local Markdown files.

---

## Phase 4: Source-Based Answer System

### Original goal

- Add document search
- Add vector database
- Make the AI answer from trusted sources
- Add citations or source references

### Status

Partly completed and partly postponed.

### Completed work

- Added document loading from `data/`
- Added Markdown chunking by headings
- Added source search
- Added source routing
- Added keyword expansion
- Added citation details
- Added official source links
- Added source metadata
- Added source quality labels
- Added source freshness labels
- Added source confidence explanations
- Added relevant source context
- Added other matching source sections
- Added rule-based source-grounded short answers

### Postponed work

Real vector search was planned and partially prepared, but implementation was paused.

Reason:

- The local environment used Python 3.14.
- Some AI packages required for `sentence-transformers` were not fully compatible with that setup.
- The package `tokenizers` attempted to build from source and required compiler tools.
- The safer plan is to return to vector search later with Python 3.12 or Python 3.11.

### Result

The current version does not use real vector search or RAG yet.

However, it does have a stable source-grounded rule-based search system and an experimental retrieval module.

---

## Phase 5: User Interface and Answer Layout Improvements

### Goal

Improve readability, transparency, and usability.

### Status

Completed for prototype version 0.5.

### Completed work

- Styled citation details card
- Styled official source links card
- Styled source metadata card
- Important limitation card
- CyberLex attention level card
- Practical explanation card
- Assessment checklist expander
- Relevant source context cards
- Other matching source section cards
- Detected topic labels
- Source quality labels
- Source freshness labels
- Source match confidence explanations
- Clickable example questions
- Sidebar version label
- Sidebar future AI mode note

### Result

CyberLex Sweden now presents answers in a clearer and more reviewable way.

The app shows the user not only an answer, but also why that answer was selected and which local source material supports it.

---

## Phase 6: Swedish and English Support

### Goal

Support both English and Swedish as main languages.

### Status

Partly completed and still improving.

### Completed work

- English interface mode
- Swedish interface mode
- English and Swedish example questions
- Swedish labels for major answer sections
- Swedish source summaries in major source files
- Swedish retrieval tests
- Swedish routing improvements for key topics

### Current supported Swedish retrieval examples

| Swedish question | Expected source |
|---|---|
| `Vad är NIS2?` | `nis2_cybersecurity_law.md` |
| `Vad är cybersäkerhetslagen?` | `nis2_cybersecurity_law.md` |
| `Vad ska ett företag göra efter en ransomwareattack?` | `nis2_incident_reporting.md` |
| `Vad ska ett företag göra efter en personuppgiftsincident?` | `gdpr_personal_data_breach.md` |
| `Vad är IMY?` | `imy_gdpr_supervision.md` |
| `Vilka är GDPR-principerna?` | `gdpr_core_principles.md` |
| `Vad är dataintrång?` | `cybercrime_dataintrang.md` |
| `Vad är DORA?` | `eu_dora_digital_operational_resilience.md` |
| `Vad betyder cybersäkerhetskrav för digitala produkter?` | `eu_cyber_resilience_act.md` |
| `Vad säger EU om attacker mot informationssystem?` | `eu_attacks_against_information_systems.md` |

### Result

The project now has much stronger Swedish support than the original prototype plan.

More Swedish answer wording and source summaries can still be improved later.

---

## Phase 7: Source Audit and Maintenance

### Goal

Make the local source system easier to review and maintain.

### Status

Completed for the current prototype.

### Completed work

- Added `scripts/source_audit.py`
- Added `scripts/add_missing_metadata.py`
- Added `docs/source_audit_report.md`
- Added source metadata blocks
- Added source update history
- Added weekly GitHub Actions source audit workflow
- Updated source list
- Updated source policy

### Source audit command

```powershell
python scripts/source_audit.py
```

### Expected audit result

```text
Files marked OK: 9
Files needing review: 0
```

### Important limitation

The source audit does not browse the web and does not verify whether the law is currently up to date.

It only checks the structure and metadata of the local project files.

### Result

CyberLex Sweden now has a repeatable source structure check and a weekly automated GitHub workflow.

---

## Phase 8: Testing and Validation

### Original goal

- Test legal questions
- Test cybersecurity questions
- Improve answer quality
- Add safety rules
- Add screenshots

### Status

Mostly completed.

### Completed work

- Added `docs/test_cases.md`
- Added core knowledge base tests
- Added UI card tests
- Added ransomware tests
- Added GDPR breach tests
- Added DORA tests
- Added CRA tests
- Added EU attacks tests
- Added Swedish retrieval tests
- Added source audit tests
- Added GitHub Actions source audit tests
- Tested out-of-scope refusal

### Tested behavior

CyberLex Sweden has been tested for:

- source loading
- source matching
- official source links
- source metadata
- source quality labels
- source freshness labels
- practical explanations
- checklists
- Swedish and English interface behavior
- experimental AI search routing
- refusal of unsupported topics

### Result

The project has a documented manual testing process and expected results for the main supported topics.

---

## Phase 9: Documentation and Final Report

### Original goal

- Write final report
- Prepare screenshots
- Prepare demo
- Prepare presentation
- Final project cleanup

### Status

Mostly completed.

### Completed documentation

- `README.md`
- `docs/project_overview.md`
- `docs/project_plan.md`
- `docs/source_list.md`
- `docs/source_policy.md`
- `docs/test_cases.md`
- `docs/technical_design.md`
- `docs/product_roadmap.md`
- `docs/vector_search_plan.md`
- `docs/source_update_history.md`
- `docs/legal_disclaimer.md`
- `docs/privacy_policy.md`
- `docs/terms_of_use.md`
- `report/final_report.md`

### Remaining work

- final screenshot review
- final demo rehearsal
- optional UI polish
- final GitHub cleanup
- final check that all documents agree with the current prototype state

### Result

The project now has strong documentation for review, maintenance, and future development.

---

## Phase 10: Future Vector Search and RAG

### Goal

Add real semantic retrieval and later AI-generated source-grounded answers.

### Status

Planned for later.

### Current decision

The first vector-search attempt was paused.

The planned future approach is:

1. Install Python 3.12 or 3.11.
2. Recreate the virtual environment using the stable Python version.
3. Add `sentence-transformers`.
4. Build a local embedding index.
5. Compare vector search results against the current rule-based retrieval.
6. Keep source metadata attached to every chunk.
7. Add vector search as a separate test mode first.
8. Only later connect vector search to the main app.
9. Add RAG-style answer generation only after retrieval is reliable.

### Important design rule

Future AI or RAG answers must remain source-grounded.

The model should not answer legal or compliance questions freely from general memory.

If no trusted source supports the answer, CyberLex Sweden should refuse.

---

## Near-Term Next Steps

The next practical improvements are:

1. Final UI polish
2. Final screenshot preparation
3. Final demo testing
4. Final README and documentation review
5. Check all links and source metadata
6. Run source audit one final time
7. Run main manual test cases again
8. Make sure GitHub repository is clean
9. Prepare final presentation or walkthrough
10. Return to vector search later with Python 3.12 or 3.11

---

## Success Criteria

The current project phase is successful when CyberLex Sweden can:

- run locally with Streamlit
- load all 9 local source files
- answer supported questions from trusted source material
- display citation details
- display official source links
- display source metadata
- show source quality and freshness labels
- show practical explanations and checklists
- support both English and Swedish interface use
- route Swedish questions to correct source files
- refuse unsupported out-of-scope questions
- pass manual test cases
- generate a clean source audit report
- maintain clear documentation
- remain honest about limitations

---

## Final Project Cleanup Checklist

Before final delivery, check:

- [ ] `python scripts/source_audit.py` runs successfully
- [ ] audit report shows `Files marked OK: 9`
- [ ] audit report shows `Files needing review: 0`
- [ ] `python -m streamlit run app/main.py` starts correctly
- [ ] main supported English questions work
- [ ] main supported Swedish questions work
- [ ] out-of-scope refusal works
- [ ] README is current
- [ ] final report is current
- [ ] test cases are current
- [ ] source list is current
- [ ] source policy is current
- [ ] technical design is current
- [ ] product roadmap is current
- [ ] project overview is current
- [ ] no unwanted generated files are committed
- [ ] `git status` shows a clean working tree

---

## Summary

The original 4 to 6 week plan has been largely completed for the current prototype phase.

CyberLex Sweden now has:

- a working Streamlit app
- a reviewed local Markdown knowledge base
- source-grounded answers
- transparent citation details
- official source links
- source metadata
- styled answer cards
- bilingual interface support
- improved Swedish retrieval
- source audit automation
- manual test cases
- project documentation
- final report material
- a realistic future plan for vector search and RAG

The next major technical upgrade is real vector search, but that should be done later with a stable Python version.

For now, the project should focus on final polishing, testing, screenshots, and presentation readiness.
