# CyberLex Sweden Source History

## Purpose

This document tracks important updates to the CyberLex Sweden knowledge base, source structure, source audit workflow, case-library support, retrieval behavior, source-related documentation, and final project hardening work.

The goal is to make source changes transparent and easier to review.

CyberLex Sweden is an educational prototype. This source history does not prove that the law is currently up to date. It records changes made to the local project files.

---

## What This File Tracks

This file tracks major changes to:

* local knowledge base files in `data/`
* local case-library files in `cases/`
* source metadata and official source links
* source audit tooling
* case audit tooling
* source-related documentation
* retrieval and source-routing behavior
* incident-response source support
* final source and documentation cleanup

This file does not replace:

| Document                                 | Purpose                                                                            |
| ---------------------------------------- | ---------------------------------------------------------------------------------- |
| `docs/source_list.md`                    | Lists current source files and trusted source areas.                               |
| `docs/source_policy.md`                  | Defines source rules, audit limits, refusal behavior, and source-grounding policy. |
| `docs/source_audit_report.md`            | Shows the generated result from the latest local source audit.                     |
| `docs/source_context_behavior.md`        | Explains how source context should appear in the app.                              |
| `docs/test_cases.md`                     | Defines manual regression tests.                                                   |
| `docs/case_library/case_audit_report.md` | Shows the generated result from the latest local case audit.                       |

---

## Current Source Status

The current source audit checks 13 local source files.

Expected audit target:

```text
Files marked OK: 13
Files needing review: 0
```

The real current audit result should always be confirmed by running:

```powershell
python scripts/source_audit.py
```

Important limitation:

The source audit checks local Markdown structure and metadata. It does not browse the web and does not prove that legal sources, authority guidance, or regulatory material are currently up to date.

If a source file is marked as needing review, it should be fixed before final hand-in or clearly marked as incomplete.

---

## Current Knowledge Base Files

The current local knowledge base files are:

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

---

## Current Case Library Files

CyberLex Sweden also includes a separate local case library in:

```text
cases/
```

Current case files:

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

The case library is different from the main source knowledge base.

`data/` contains the main legal, regulatory, cybersecurity, and incident-response source material.

`cases/` contains educational examples, authority decisions, public incident examples, outcomes, fines, learning notes, and related case context.

Case examples are not fine predictions and should not replace the main source-grounded answer.

---

## Current Source Maintenance Files

Current source maintenance and documentation files include:

```text
docs/source_list.md
docs/source_policy.md
docs/source_history.md
docs/source_audit_report.md
docs/source_context_behavior.md
docs/test_cases.md
docs/technical_design.md
docs/vector_search_plan.md
docs/case_library/case_audit_report.md
scripts/source_audit.py
scripts/case_audit.py
scripts/add_missing_metadata.py
.github/workflows/source-audit.yml
```

---

## Current App and Retrieval Files

The app has been partly refactored from one large file into smaller modules.

Current expected app files:

```text
app/main.py
app/config.py
app/styles.py
app/text_utils.py
app/language.py
app/source_loader.py
app/incident_engine.py
app/case_search.py
app/vector_search.py
```

Responsibilities:

| File                     | Main responsibility                                                                                                                                                   |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `app/main.py`            | Streamlit app flow, UI rendering, answer display, routing glue, and remaining main logic.                                                                             |
| `app/config.py`          | App settings, paths, page title, icon, and layout config.                                                                                                             |
| `app/styles.py`          | CSS and visual styling.                                                                                                                                               |
| `app/text_utils.py`      | Shared helpers for text normalization, keyword handling, and phrase matching.                                                                                         |
| `app/language.py`        | English, Swedish, and Auto language behavior, localized labels, localized section names, case-title localization, and source-label localization.                      |
| `app/source_loader.py`   | Markdown source loading, official source extraction, metadata extraction, section extraction, document loading, and chunk splitting.                                  |
| `app/incident_engine.py` | Detection of practical incident-response questions, including phishing, suspicious login, compromised account, data leak, ransomware, malware, and suspected hacking. |
| `app/case_search.py`     | Related case search and case-library matching.                                                                                                                        |
| `app/vector_search.py`   | Experimental retrieval sidebar and rule-based retrieval testing.                                                                                                      |

Important note:

Despite the name, `app/vector_search.py` does not currently use real embeddings or a vector database. It is still rule-based and experimental.

---

## Update Log

| Date       | File or area                                     | Topic                         | Change                                                                                                                                           | Result                                                                           |
| ---------- | ------------------------------------------------ | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- |
| 2026-05-30 | `data/gdpr_personal_data_breach.md`              | GDPR breach                   | Added educational source summary, IMY reporting context, official links, source date, and disclaimer.                                            | Initial GDPR breach support added.                                               |
| 2026-05-30 | `data/nis2_cybersecurity_law.md`                 | NIS2                          | Added educational source summary, MSB authority context, cybersecurity responsibilities, official links, source date, and disclaimer.            | Initial NIS2 support added.                                                      |
| 2026-05-30 | `data/cybercrime_dataintrang.md`                 | Dataintrång                   | Added Swedish cybercrime and unauthorized access source summary.                                                                                 | Initial cybercrime support added.                                                |
| 2026-05-30 | `data/gdpr_core_principles.md`                   | GDPR principles               | Added source file for GDPR principles.                                                                                                           | GDPR principle questions supported.                                              |
| 2026-05-30 | `data/eu_attacks_against_information_systems.md` | EU cybercrime                 | Added source for Directive 2013/40/EU and attacks against information systems.                                                                   | EU cybercrime support added.                                                     |
| 2026-05-30 | `data/eu_cyber_resilience_act.md`                | CRA                           | Added source for product cybersecurity and the Cyber Resilience Act.                                                                             | CRA support added.                                                               |
| 2026-05-31 | `data/imy_gdpr_supervision.md`                   | IMY                           | Added separate source for Swedish GDPR supervision and IMY authority questions.                                                                  | IMY questions route more clearly.                                                |
| 2026-05-31 | `data/nis2_incident_reporting.md`                | Incident reporting            | Added dedicated source for NIS2 incident reporting and overlap with GDPR.                                                                        | Incident-reporting questions improved.                                           |
| 2026-05-31 | `data/eu_dora_digital_operational_resilience.md` | DORA                          | Added source for DORA, ICT risk, incident reporting, and third-party ICT risk.                                                                   | DORA support added.                                                              |
| 2026-06-01 | All files in `data/`                             | Official links                | Converted raw official URLs to readable Markdown links.                                                                                          | Official source display improved.                                                |
| 2026-06-01 | `docs/source_list.md`                            | Source documentation          | Updated source list with current knowledge base files and link formatting notes.                                                                 | Source documentation improved.                                                   |
| 2026-06-01 | `docs/source_policy.md`                          | Source rules                  | Updated rules for trusted source handling, official links, metadata, and limitations.                                                            | Source governance improved.                                                      |
| 2026-06-01 | `docs/test_cases.md`                             | Testing                       | Updated tests for source matching, official links, metadata, source confidence, and out-of-scope refusal.                                        | Source-related test coverage improved.                                           |
| 2026-06-01 | `docs/technical_design.md`                       | Technical documentation       | Updated design notes for source routing, chunk search, citation display, metadata, and answer structure.                                         | Technical documentation aligned with app behavior.                               |
| 2026-06-03 | `scripts/source_audit.py`                        | Source audit                  | Added script to check source files for official source sections, official links, metadata, source date, and version notes.                       | Repeatable source audit added.                                                   |
| 2026-06-03 | `docs/source_audit_report.md`                    | Source audit report           | Added generated source audit report.                                                                                                             | Local source status became visible.                                              |
| 2026-06-03 | `scripts/add_missing_metadata.py`                | Metadata helper               | Added helper script for adding missing source metadata.                                                                                          | Metadata maintenance improved.                                                   |
| 2026-06-03 | All files in `data/`                             | Source metadata               | Added or standardized `## Source metadata` sections.                                                                                             | Source audit structure improved.                                                 |
| 2026-06-03 | `data/gdpr_personal_data_breach.md`              | GDPR cleanup                  | Removed duplicate source sections and standardized links and metadata.                                                                           | GDPR breach source passed audit.                                                 |
| 2026-06-03 | `data/imy_gdpr_supervision.md`                   | IMY cleanup                   | Removed duplicate source sections and standardized links and metadata.                                                                           | IMY supervision source passed audit.                                             |
| 2026-06-03 | `.github/workflows/source-audit.yml`             | GitHub Actions                | Added weekly source audit workflow.                                                                                                              | Automated source-structure audit added.                                          |
| 2026-06-03 | `docs/vector_search_plan.md`                     | Future retrieval              | Added future vector search planning document.                                                                                                    | Future semantic retrieval path documented.                                       |
| 2026-06-03 | `app/vector_search.py`                           | Experimental retrieval        | Added experimental retrieval module separate from the main answer system.                                                                        | Retrieval testing became safer.                                                  |
| 2026-06-03 | `app/main.py`                                    | Experimental sidebar          | Added sidebar for experimental retrieval testing.                                                                                                | Source retrieval could be tested in the UI.                                      |
| 2026-06-03 | `app/vector_search.py`                           | Ranking logic                 | Improved ranking by boosting useful sections and penalizing weak support sections.                                                               | Better section-level retrieval.                                                  |
| 2026-06-03 | `app/vector_search.py`                           | DORA retrieval                | Improved DORA ranking for `What is DORA?`.                                                                                                       | DORA source appears more reliably.                                               |
| 2026-06-03 | `app/vector_search.py`                           | Unauthorized access retrieval | Improved English unauthorized access routing to Swedish dataintrång material.                                                                    | Cybercrime retrieval improved.                                                   |
| 2026-06-03 | `data/nis2_incident_reporting.md`                | Incident checklist            | Added incident assessment checklist.                                                                                                             | Ransomware and incident questions improved.                                      |
| 2026-06-03 | `app/vector_search.py`                           | Ransomware retrieval          | Improved ransomware ranking toward NIS2 incident reporting and incident checklist.                                                               | Ransomware retrieval improved.                                                   |
| 2026-06-03 | `data/nis2_incident_reporting.md`                | Swedish incident support      | Added Swedish summary for ransomware, malware, cyber incidents, NIS2, GDPR overlap, and documentation.                                           | Swedish incident support improved.                                               |
| 2026-06-03 | `data/gdpr_personal_data_breach.md`              | Swedish GDPR breach           | Added Swedish summary and data breach assessment checklist.                                                                                      | Swedish breach questions improved.                                               |
| 2026-06-03 | `app/vector_search.py`                           | Swedish GDPR retrieval        | Improved routing for Swedish personuppgiftsincident questions.                                                                                   | Swedish GDPR breach retrieval improved.                                          |
| 2026-06-03 | `app/vector_search.py`                           | Code fix                      | Fixed indentation and function structure after scoring updates.                                                                                  | Experimental search compiled successfully.                                       |
| 2026-06-03 | `docs/technical_design.md`                       | Technical docs                | Documented experimental search, source audit, metadata helper, GitHub audit, source labels, and incident checklist.                              | Technical design updated.                                                        |
| 2026-06-03 | `docs/test_cases.md`                             | Tests                         | Added tests for experimental search, audit, GitHub Actions, ransomware, cyber incidents, and Swedish GDPR retrieval.                             | Test coverage improved.                                                          |
| 2026-06-03 | `data/nis2_cybersecurity_law.md`                 | Swedish NIS2                  | Expanded Swedish support for NIS2, cybersäkerhetslagen, risk management, covered organizations, and management responsibility.                   | Broad Swedish NIS2 questions improved.                                           |
| 2026-06-03 | `app/vector_search.py`                           | Swedish NIS2 retrieval        | Improved routing for Swedish NIS2 and Swedish Cybersecurity Act questions.                                                                       | NIS2 law and incident reporting became easier to separate.                       |
| 2026-06-03 | `data/eu_dora_digital_operational_resilience.md` | Swedish DORA                  | Expanded DORA source with Swedish summaries, ICT risk, third-party risk, testing, and relationship notes.                                        | Swedish DORA questions improved.                                                 |
| 2026-06-03 | `data/eu_cyber_resilience_act.md`                | Swedish CRA                   | Expanded CRA source with Swedish summaries, product cybersecurity, vulnerability handling, and security updates.                                 | Swedish CRA questions improved.                                                  |
| 2026-06-03 | `app/vector_search.py`                           | CRA retrieval                 | Improved routing for Swedish digital-product cybersecurity and CRA questions.                                                                    | CRA retrieval became more accurate.                                              |
| 2026-06-03 | `data/eu_attacks_against_information_systems.md` | EU attacks                    | Expanded EU attacks source with Swedish summary, DDoS, botnets, illegal access, interference, and misuse of tools.                               | EU cybercrime support improved.                                                  |
| 2026-06-03 | `app/vector_search.py`                           | EU attacks retrieval          | Improved routing for Swedish EU cybercrime questions.                                                                                            | EU attacks source became easier to retrieve.                                     |
| 2026-06-08 | `data/imy_gdpr_security_measures.md`             | GDPR security                 | Added IMY-focused GDPR security-measure source.                                                                                                  | MFA, encryption, and technical/organizational measure questions improved.        |
| 2026-06-08 | `data/nis2_sector_scope_guidance.md`             | NIS2 scope                    | Added NIS2 sector-scope guidance for applicability, sectors, Annex 1 and Annex 2, entity types, registration, jurisdiction, and size assessment. | NIS2 applicability questions improved.                                           |
| 2026-06-08 | `docs/source_audit_report.md`                    | Audit status                  | Generated source audit report for 13 files.                                                                                                      | Audit status became visible in documentation.                                    |
| 2026-06-10 | `app/main.py`                                    | Final hardening               | Improved self-description routing, NIS2 annex/entity handling, Swedish section localization, source context display, and incident routing.       | Demo readiness improved.                                                         |
| 2026-06-10 | `app/main.py`                                    | SOC report export             | Added SOC-style Markdown incident report export.                                                                                                 | Incident documentation support improved.                                         |
| 2026-06-10 | `docs/test_cases.md`                             | Regression testing            | Updated tests for self-description, NIS2 scope, NIS2 annexes, GDPR/IMY security, incident response, SOC export, and refusal behavior.            | Final regression test coverage improved.                                         |
| 2026-06-10 | `README.md`                                      | Project documentation         | Updated README with current status, suggested test questions, known limitations, and future improvements.                                        | README aligned with current app.                                                 |
| 2026-06-10 | `docs/demo_script.md`                            | Demo documentation            | Added or improved demo script for presentation flow, SOC export, safety boundaries, limitations, and future improvements.                        | Presentation support improved.                                                   |
| 2026-06-10 | `docs/source_context_behavior.md`                | Source context                | Updated expected behavior for source context, incident filtering, Swedish labels, and fallback avoidance.                                        | Source-context behavior documented.                                              |
| 2026-06-10 | `docs/source_list.md`                            | Source documentation          | Updated source list to reflect 13 checked files and source audit behavior.                                                                       | Source list aligned with current knowledge base.                                 |
| 2026-06-10 | `docs/source_policy.md`                          | Source policy                 | Updated source policy to reflect 13 checked files, source audit behavior, source history filename, and defensive cyber guidance rules.           | Source policy aligned with current state.                                        |
| 2026-06-14 | `cases/`                                         | Case library                  | Added and expanded real-world GDPR and cybersecurity-related case examples.                                                                      | Case examples became available for educational comparison.                       |
| 2026-06-14 | `app/case_search.py`                             | Case matching                 | Added related case search and keyword matching for case-library questions.                                                                       | Relevant cases could be shown for supported compliance questions.                |
| 2026-06-14 | `scripts/case_audit.py`                          | Case audit                    | Added case audit support for local case files.                                                                                                   | Case-library structure became easier to verify.                                  |
| 2026-06-14 | `docs/case_library/case_audit_report.md`         | Case audit report             | Added generated case audit report.                                                                                                               | Case-library status became visible.                                              |
| 2026-06-15 | `app/main.py` and app modules                    | Case Intelligence             | Added or improved Case Intelligence page and related case display behavior.                                                                      | Users could browse case cards separately from normal answers.                    |
| 2026-06-15 | `app/language.py`                                | Auto language                 | Improved English, Swedish, and Auto language behavior, including Swedish questions containing English legal or technical terms.                  | Mixed-language cyber/legal questions were handled more predictably.              |
| 2026-06-15 | `app/incident_engine.py`                         | Incident triage filtering     | Improved detection of practical incident-response questions.                                                                                     | Related cases could be hidden for urgent triage questions.                       |
| 2026-06-16 | `docs/ui_behavior.md`                            | UI documentation              | Updated UI behavior documentation for current app behavior, Auto mode, instant examples, related cases, and Case Intelligence.                   | UI documentation aligned with current app.                                       |
| 2026-06-16 | `docs/testing_and_demo.md`                       | Testing and demo              | Updated testing and demo documentation for current regression behavior and final demo flow.                                                      | Testing and demo docs aligned with current app.                                  |
| 2026-06-16 | `docs/project_overview.md`                       | Project overview              | Updated project overview with current architecture, UI behavior, case library, incident support, and limitations.                                | Project overview aligned with current prototype.                                 |
| 2026-06-16 | `docs/product_roadmap.md`                        | Roadmap                       | Updated roadmap with completed case-library milestone, modular app status, and future maintainability/RAG plans.                                 | Roadmap aligned with current direction.                                          |
| 2026-06-16 | `docs/project_plan.md`                           | Project plan                  | Updated project plan with Case Library phase, Git push policy, current source list, and current success criteria.                                | Project plan aligned with current work.                                          |
| 2026-06-18 | `docs/source_list.md`                            | Source documentation cleanup  | Updated source list to avoid stale audit-result claims and align with 13-file audit target.                                                      | Source list now points to audit confirmation instead of hardcoding stale status. |
| 2026-06-18 | `docs/source_policy.md`                          | Source policy cleanup         | Updated source policy with case-library policy, source/case audit distinction, Auto language policy, and batch-based Git workflow.               | Source policy now matches the current CyberLex behavior.                         |
| 2026-06-18 | `docs/source_history.md`                         | Source history cleanup        | Updated source history with current app modules, case library, audit targets, and recent documentation cleanup.                                  | Source history now reflects the current prototype state.                         |

---

## Detailed Notes

## 2026-05-30 - Initial Source Base

Initial educational source summaries were added for the first CyberLex Sweden knowledge base files.

Initial topics included:

* GDPR personal data breach reporting
* NIS2 and Swedish cybersecurity law
* Swedish cybercrime law and dataintrång
* GDPR core principles
* EU attacks against information systems
* EU Cyber Resilience Act

Purpose:

* build the first local source base
* give the app trusted source material to search
* support citation details and official source links
* keep answers limited to cybersecurity law, cybercrime, GDPR, NIS2, and related EU cybersecurity topics

Result:

CyberLex Sweden could answer basic questions using local Markdown files instead of unsupported generated claims.

---

## 2026-05-31 - Additional Authority and Incident Sources

Additional source files were added to improve coverage.

Added files:

* `data/imy_gdpr_supervision.md`
* `data/nis2_incident_reporting.md`
* `data/eu_dora_digital_operational_resilience.md`

Purpose:

* separate IMY supervision questions from GDPR breach reporting questions
* add a dedicated source for NIS2 incident reporting
* add DORA coverage for financial-sector ICT risk and digital operational resilience
* improve source routing between different legal frameworks

Result:

CyberLex Sweden became better at routing questions to the correct source file.

---

## 2026-06-01 - Official Source Link Formatting

Official source sections were updated to use labeled Markdown links instead of raw URLs.

Old format:

```text
Source name
https://source-url
```

New format:

```markdown
[Source name](https://source-url)
```

Purpose:

* improve readability
* improve Streamlit display
* make source citations easier to understand
* prepare source files for future AI/RAG use

Result:

Official source links display as readable clickable labels.

---

## 2026-06-03 - Source Audit System

A local source audit script was added:

```text
scripts/source_audit.py
```

The script checks Markdown files in:

```text
data/
```

It checks for:

* official source section
* official source links
* source metadata section
* source date
* source freshness
* version notes

It generates:

```text
docs/source_audit_report.md
```

Important limitation:

The audit does not browse the web and does not confirm whether the law is currently up to date.

It only checks the local project files.

Result:

CyberLex Sweden gained a repeatable local source audit process.

---

## 2026-06-03 - Metadata Helper Script

A metadata helper script was added:

```text
scripts/add_missing_metadata.py
```

Purpose:

* add missing `## Source metadata` sections to local Markdown source files
* standardize source date and version notes format
* help older source files follow the same structure as newer files

Standard metadata format:

```markdown
## Source metadata

Source date: Last checked: YYYY-MM-DD

Version notes: Source reviewed for CyberLex Sweden educational prototype.
```

Result:

The knowledge base source files became easier to audit and maintain.

---

## 2026-06-03 - Experimental Retrieval Module

An experimental retrieval module was added:

```text
app/vector_search.py
```

Purpose:

* test improved retrieval separately from the main app
* build a safe foundation for future vector search
* avoid breaking the main CyberLex answer system while testing ranking changes
* compare experimental retrieval behavior with the existing main source search

Current behavior:

* loads Markdown files from `data/`
* splits them into chunks
* cleans text
* scores chunks
* boosts useful sections
* penalizes weak sections
* applies topic-specific ranking rules
* returns ranked source matches

Important limitation:

Despite the file name, the current module does not use true vector embeddings or a vector database.

Result:

CyberLex Sweden gained a separate experimental retrieval system.

---

## 2026-06-03 - Retrieval Improvements

The experimental retrieval logic was improved.

Improved areas included:

* DORA retrieval
* unauthorized access retrieval
* ransomware retrieval
* Swedish GDPR personal data breach retrieval
* Swedish IMY retrieval
* Swedish NIS2 retrieval
* Swedish CRA retrieval
* Swedish EU attacks retrieval

Purpose:

* make experimental search prefer real explanatory sections
* avoid ranking metadata or official-source sections too high
* distinguish similar frameworks such as NIS2, GDPR, DORA, CRA, and cybercrime
* improve Swedish retrieval support

Result:

The experimental search became more useful and predictable.

---

## 2026-06-08 - Additional Source Expansion

Two important source files were added or improved:

```text
data/imy_gdpr_security_measures.md
data/nis2_sector_scope_guidance.md
```

Purpose:

* improve GDPR/IMY questions about security measures, MFA, encryption, access control, and risk-based controls
* improve NIS2 questions about applicability, sectors, Annex 1 and Annex 2, registration, jurisdiction, and entity classification

Result:

CyberLex Sweden gained stronger support for common final-demo questions:

```text
Vad säger IMY om säkerhetsåtgärder?
Does GDPR require MFA?
Gäller NIS2 för oss?
Vad är bilaga 1 och bilaga 2 i NIS2?
```

---

## 2026-06-10 - Final Demo Hardening

CyberLex Sweden was updated and reviewed for final project readiness.

Affected areas included:

* `app/main.py`
* `README.md`
* `docs/test_cases.md`
* `docs/source_context_behavior.md`
* `docs/demo_script.md`
* source documentation

Main improvements:

* improved direct CyberLex self-description routing
* improved NIS2 sector-scope, annex, and entity-type handling
* improved Swedish source-section localization
* improved source-context readability
* improved incident-response routing
* added SOC-style Markdown incident report export
* improved unsafe cyber misuse refusal behavior
* updated test cases and demo documentation

Purpose:

* make the project easier to test before final presentation
* reduce demo risk
* document current app behavior clearly
* avoid major architecture refactoring before the final project demonstration

Result:

CyberLex Sweden reached a stable demo-ready state as a local educational prototype.

---

## 2026-06-14 - Case Library Expansion

The local case library was expanded in:

```text
cases/
```

Current case examples include GDPR, Meta Pixel, data exposure, security-measure, and breach-related examples.

Purpose:

* provide real-world educational examples
* help users understand practical consequences
* show how authority decisions and public incidents relate to CyberLex topics
* support case-library questions without turning the app into a fine calculator

Result:

CyberLex Sweden gained a stronger case-based learning layer.

---

## 2026-06-15 - Case Intelligence and Related Case Behavior

The app was improved with Case Intelligence support and better related-case behavior.

Main behavior:

* related cases appear for suitable compliance and case-library questions
* related cases are hidden for urgent practical incident-response triage questions
* Case Intelligence page allows browsing case cards
* case links follow language behavior where possible

Purpose:

* keep historical examples useful without distracting from urgent incident triage
* separate legal/compliance learning from practical containment advice
* make the case library visible and easier to test

Result:

CyberLex Sweden became stronger as both a learning project and a practical cybersecurity-law prototype.

---

## 2026-06-16 - Documentation Batch Cleanup

A 10-file documentation cleanup batch was completed.

Updated files:

```text
docs/ui_behavior.md
docs/source_context_behavior.md
docs/test_cases.md
docs/test_run_checklist.md
docs/testing_and_demo.md
docs/demo_checklist.md
docs/demo_script.md
docs/project_overview.md
docs/product_roadmap.md
docs/project_plan.md
```

The batch updated documentation to reflect:

* refactored Python module structure
* Auto language behavior
* example questions running immediately
* related cases shown only where relevant
* related cases hidden for practical incident-response triage
* Case Intelligence page
* source audit
* case audit
* test and demo flow
* current limitations
* future roadmap
* batch-based Git push workflow

Purpose:

* make final documentation match the current app
* reduce stale project notes
* prepare for stable checkpoint commits
* avoid risky code changes before final verification

Result:

Core project documentation became aligned with the current prototype.

---

## 2026-06-18 - Source Documentation Cleanup

The source documentation cleanup continued with:

```text
docs/source_list.md
docs/source_policy.md
docs/source_history.md
```

Main improvements:

* removed stale hardcoded audit-result claims
* aligned documentation with the 13-file source audit target
* clarified that audits check local structure, not live legal currentness
* added stronger distinction between `data/` source files and `cases/` case examples
* documented Case Intelligence and case-audit behavior
* documented current modular app structure
* documented batch-based Git workflow

Purpose:

* keep source governance documentation consistent
* avoid contradictions between source list, source policy, source history, and audit report
* make the project easier to evaluate and maintain

Result:

Source documentation now better reflects the current CyberLex Sweden prototype.

---

## Source Review Rules

When a knowledge base source is added or updated, check:

1. The source file has a clear topic.
2. The source file uses trusted legal, authority, or defensive cybersecurity sources.
3. The source file includes official source links.
4. The source file includes a source date.
5. The source file includes version notes.
6. The source file includes a disclaimer.
7. The source file is added to `docs/source_list.md`.
8. The source file is covered by at least one test case in `docs/test_cases.md`.
9. The source file passes `scripts/source_audit.py`.
10. Significant source changes are mentioned in this source history.
11. New Swedish source sections are tested with Swedish questions.
12. Retrieval changes are checked with `python -m py_compile` before commit.

---

## Case Review Rules

When a case-library file is added or updated, check:

1. The case has a clear title and topic.
2. The case identifies authority, jurisdiction, year, and case type where possible.
3. The case explains what happened in plain language.
4. The case explains why it matters for CyberLex Sweden.
5. The case includes outcome, fine, or cost information where known.
6. The case avoids treating fines as automatic predictions.
7. The case includes official or reliable source links.
8. The case includes useful CyberLex questions or related topics.
9. The case passes `scripts/case_audit.py`.
10. Significant case-library changes are mentioned in this source history or relevant case documentation.

---

## Current Source Audit Goal

The current source audit goal is:

```text
Files marked OK: 13
Files needing review: 0
```

The current actual audit result should be checked locally with:

```powershell
python scripts/source_audit.py
```

If the audit reports issues, fix the affected source file or clearly mark it as incomplete before final hand-in.

---

## Future Source Update Priorities

Future source work should focus on:

* fixing or removing source files marked as needing review
* improving Swedish source summaries
* adding more Swedish legal sources
* adding more EU cybersecurity law sources
* strengthening GDPR, NIS2, DORA, CRA, and incident-response coverage
* adding more source-specific test cases
* improving source review routines
* adding automated link checks
* adding source retirement rules
* preparing source-to-chunk metadata for future vector search and RAG

---

## Git Workflow Note

The preferred workflow is:

```text
Work locally.
Commit stable checkpoints.
Push after 10 to 15 meaningful changes or a clear milestone.
```

Current documentation cleanup should be batched before commit where practical.

Generated audit reports may change when audit scripts run. If they changed because of a real documentation or source update, they should be reviewed and committed together with the related source documentation.

---

## Final Note

CyberLex Sweden is source-grounded by design.

The source history shows how the local knowledge base, case library, source policy, source audit workflow, and retrieval behavior changed over time, but it does not prove that the legal content is currently up to date.

The source audit checks local structure and metadata.

The case audit checks local case-file structure.

For real legal, compliance, regulatory, or incident-response decisions, official sources and qualified professionals should still be consulted.

Because reality insists on being difficult, this distinction matters.
