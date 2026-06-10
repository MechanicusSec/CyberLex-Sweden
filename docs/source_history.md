# CyberLex Sweden Source History

## Purpose

This document tracks important updates to the CyberLex Sweden knowledge base, source structure, source audit workflow, retrieval behavior, source-related documentation, and final project hardening work.

The goal is to make source changes transparent and easier to review.

CyberLex Sweden is an educational prototype. This source history does not prove that the law is currently up to date. It records changes made to the local project files.

---

## What This File Tracks

This file tracks major changes to:

* local knowledge base files in `data/`
* source metadata and official source links
* source audit tooling
* source-related documentation
* retrieval and source-routing behavior
* incident-response source support
* final source and documentation cleanup

This file does not replace:

| Document                          | Purpose                                                                            |
| --------------------------------- | ---------------------------------------------------------------------------------- |
| `docs/source_list.md`             | Lists current source files and trusted source areas.                               |
| `docs/source_policy.md`           | Defines source rules, audit limits, refusal behavior, and source-grounding policy. |
| `docs/source_audit_report.md`     | Shows the generated result from the latest local source audit.                     |
| `docs/source_context_behavior.md` | Explains how source context should appear in the app.                              |
| `docs/test_cases.md`              | Defines manual regression tests.                                                   |

---

## Current Source Status

The current source audit checks 13 local source files.

Current audit result:

```text id="x6xh91"
Files marked OK: 12
Files needing review: 1
```

The file currently needing review is:

```text id="9976pl"
data/gdpr_imy_edpb_security_guidance.md
```

Reason:

```text id="t14joj"
Missing official source section, official source links, source metadata section, source date, and version notes.
```

This file should be fixed or removed before final hand-in if it is not used.

---

## Current Knowledge Base Files

The current local knowledge base files are:

```text id="27t4o4"
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

## Current Source Maintenance Files

Current source maintenance and documentation files include:

```text id="o355wz"
docs/source_list.md
docs/source_policy.md
docs/source_history.md
docs/source_audit_report.md
docs/source_context_behavior.md
docs/test_cases.md
docs/technical_design.md
docs/vector_search_plan.md
scripts/source_audit.py
scripts/add_missing_metadata.py
.github/workflows/source-audit.yml
```

---

## Current Retrieval Files

Current retrieval-related project files include:

```text id="fffohi"
app/main.py
app/vector_search.py
```

`app/main.py` contains the main Streamlit application and the experimental retrieval sidebar.

`app/vector_search.py` contains the experimental rule-based retrieval module used for testing source ranking before real vector search is added.

Despite the name, `app/vector_search.py` does not currently use real embeddings or a vector database.

---

## Update Log

| Date       | File or area                                     | Topic                         | Change                                                                                                                                           | Result                                                                    |
| ---------- | ------------------------------------------------ | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------- |
| 2026-05-30 | `data/gdpr_personal_data_breach.md`              | GDPR breach                   | Added educational source summary, IMY reporting context, official links, source date, and disclaimer.                                            | Initial GDPR breach support added.                                        |
| 2026-05-30 | `data/nis2_cybersecurity_law.md`                 | NIS2                          | Added educational source summary, MSB authority context, cybersecurity responsibilities, official links, source date, and disclaimer.            | Initial NIS2 support added.                                               |
| 2026-05-30 | `data/cybercrime_dataintrang.md`                 | Dataintrång                   | Added Swedish cybercrime and unauthorized access source summary.                                                                                 | Initial cybercrime support added.                                         |
| 2026-05-30 | `data/gdpr_core_principles.md`                   | GDPR principles               | Added source file for GDPR principles.                                                                                                           | GDPR principle questions supported.                                       |
| 2026-05-30 | `data/eu_attacks_against_information_systems.md` | EU cybercrime                 | Added source for Directive 2013/40/EU and attacks against information systems.                                                                   | EU cybercrime support added.                                              |
| 2026-05-30 | `data/eu_cyber_resilience_act.md`                | CRA                           | Added source for product cybersecurity and the Cyber Resilience Act.                                                                             | CRA support added.                                                        |
| 2026-05-31 | `data/imy_gdpr_supervision.md`                   | IMY                           | Added separate source for Swedish GDPR supervision and IMY authority questions.                                                                  | IMY questions route more clearly.                                         |
| 2026-05-31 | `data/nis2_incident_reporting.md`                | Incident reporting            | Added dedicated source for NIS2 incident reporting and overlap with GDPR.                                                                        | Incident-reporting questions improved.                                    |
| 2026-05-31 | `data/eu_dora_digital_operational_resilience.md` | DORA                          | Added source for DORA, ICT risk, incident reporting, and third-party ICT risk.                                                                   | DORA support added.                                                       |
| 2026-06-01 | All files in `data/`                             | Official links                | Converted raw official URLs to readable Markdown links.                                                                                          | Official source display improved.                                         |
| 2026-06-01 | `docs/source_list.md`                            | Source documentation          | Updated source list with current knowledge base files and link formatting notes.                                                                 | Source documentation improved.                                            |
| 2026-06-01 | `docs/source_policy.md`                          | Source rules                  | Updated rules for trusted source handling, official links, metadata, and limitations.                                                            | Source governance improved.                                               |
| 2026-06-01 | `docs/test_cases.md`                             | Testing                       | Updated tests for source matching, official links, metadata, source confidence, and out-of-scope refusal.                                        | Source-related test coverage improved.                                    |
| 2026-06-01 | `docs/technical_design.md`                       | Technical documentation       | Updated design notes for source routing, chunk search, citation display, metadata, and answer structure.                                         | Technical documentation aligned with app behavior.                        |
| 2026-06-03 | `scripts/source_audit.py`                        | Source audit                  | Added script to check source files for official source sections, official links, metadata, source date, and version notes.                       | Repeatable source audit added.                                            |
| 2026-06-03 | `docs/source_audit_report.md`                    | Source audit report           | Added generated source audit report.                                                                                                             | Local source status became visible.                                       |
| 2026-06-03 | `scripts/add_missing_metadata.py`                | Metadata helper               | Added helper script for adding missing source metadata.                                                                                          | Metadata maintenance improved.                                            |
| 2026-06-03 | All files in `data/`                             | Source metadata               | Added or standardized `## Source metadata` sections.                                                                                             | Source audit structure improved.                                          |
| 2026-06-03 | `data/gdpr_personal_data_breach.md`              | GDPR cleanup                  | Removed duplicate source sections and standardized links and metadata.                                                                           | GDPR breach source passed audit.                                          |
| 2026-06-03 | `data/imy_gdpr_supervision.md`                   | IMY cleanup                   | Removed duplicate source sections and standardized links and metadata.                                                                           | IMY supervision source passed audit.                                      |
| 2026-06-03 | `.github/workflows/source-audit.yml`             | GitHub Actions                | Added weekly source audit workflow.                                                                                                              | Automated source-structure audit added.                                   |
| 2026-06-03 | `docs/vector_search_plan.md`                     | Future retrieval              | Added future vector search planning document.                                                                                                    | Future semantic retrieval path documented.                                |
| 2026-06-03 | `app/vector_search.py`                           | Experimental retrieval        | Added experimental retrieval module separate from the main answer system.                                                                        | Retrieval testing became safer.                                           |
| 2026-06-03 | `app/main.py`                                    | Experimental sidebar          | Added sidebar for experimental retrieval testing.                                                                                                | Source retrieval could be tested in the UI.                               |
| 2026-06-03 | `app/vector_search.py`                           | Ranking logic                 | Improved ranking by boosting useful sections and penalizing weak support sections.                                                               | Better section-level retrieval.                                           |
| 2026-06-03 | `app/vector_search.py`                           | DORA retrieval                | Improved DORA ranking for `What is DORA?`.                                                                                                       | DORA source appears more reliably.                                        |
| 2026-06-03 | `app/vector_search.py`                           | Unauthorized access retrieval | Improved English unauthorized access routing to Swedish dataintrång material.                                                                    | Cybercrime retrieval improved.                                            |
| 2026-06-03 | `data/nis2_incident_reporting.md`                | Incident checklist            | Added incident assessment checklist.                                                                                                             | Ransomware and incident questions improved.                               |
| 2026-06-03 | `app/vector_search.py`                           | Ransomware retrieval          | Improved ransomware ranking toward NIS2 incident reporting and incident checklist.                                                               | Ransomware retrieval improved.                                            |
| 2026-06-03 | `data/nis2_incident_reporting.md`                | Swedish incident support      | Added Swedish summary for ransomware, malware, cyber incidents, NIS2, GDPR overlap, and documentation.                                           | Swedish incident support improved.                                        |
| 2026-06-03 | `data/gdpr_personal_data_breach.md`              | Swedish GDPR breach           | Added Swedish summary and data breach assessment checklist.                                                                                      | Swedish breach questions improved.                                        |
| 2026-06-03 | `app/vector_search.py`                           | Swedish GDPR retrieval        | Improved routing for Swedish personuppgiftsincident questions.                                                                                   | Swedish GDPR breach retrieval improved.                                   |
| 2026-06-03 | `app/vector_search.py`                           | Code fix                      | Fixed indentation and function structure after scoring updates.                                                                                  | Experimental search compiled successfully.                                |
| 2026-06-03 | `docs/technical_design.md`                       | Technical docs                | Documented experimental search, source audit, metadata helper, GitHub audit, source labels, and incident checklist.                              | Technical design updated.                                                 |
| 2026-06-03 | `docs/test_cases.md`                             | Tests                         | Added tests for experimental search, audit, GitHub Actions, ransomware, cyber incidents, and Swedish GDPR retrieval.                             | Test coverage improved.                                                   |
| 2026-06-03 | `data/nis2_cybersecurity_law.md`                 | Swedish NIS2                  | Expanded Swedish support for NIS2, cybersäkerhetslagen, risk management, covered organizations, and management responsibility.                   | Broad Swedish NIS2 questions improved.                                    |
| 2026-06-03 | `app/vector_search.py`                           | Swedish NIS2 retrieval        | Improved routing for Swedish NIS2 and Swedish Cybersecurity Act questions.                                                                       | NIS2 law and incident reporting became easier to separate.                |
| 2026-06-03 | `data/eu_dora_digital_operational_resilience.md` | Swedish DORA                  | Expanded DORA source with Swedish summaries, ICT risk, third-party risk, testing, and relationship notes.                                        | Swedish DORA questions improved.                                          |
| 2026-06-03 | `data/eu_cyber_resilience_act.md`                | Swedish CRA                   | Expanded CRA source with Swedish summaries, product cybersecurity, vulnerability handling, and security updates.                                 | Swedish CRA questions improved.                                           |
| 2026-06-03 | `app/vector_search.py`                           | CRA retrieval                 | Improved routing for Swedish digital-product cybersecurity and CRA questions.                                                                    | CRA retrieval became more accurate.                                       |
| 2026-06-03 | `data/eu_attacks_against_information_systems.md` | EU attacks                    | Expanded EU attacks source with Swedish summary, DDoS, botnets, illegal access, interference, and misuse of tools.                               | EU cybercrime support improved.                                           |
| 2026-06-03 | `app/vector_search.py`                           | EU attacks retrieval          | Improved routing for Swedish EU cybercrime questions.                                                                                            | EU attacks source became easier to retrieve.                              |
| 2026-06-08 | `data/imy_gdpr_security_measures.md`             | GDPR security                 | Added IMY-focused GDPR security-measure source.                                                                                                  | MFA, encryption, and technical/organizational measure questions improved. |
| 2026-06-08 | `data/nis2_sector_scope_guidance.md`             | NIS2 scope                    | Added NIS2 sector-scope guidance for applicability, sectors, Annex 1 and Annex 2, entity types, registration, jurisdiction, and size assessment. | NIS2 applicability questions improved.                                    |
| 2026-06-08 | `docs/source_audit_report.md`                    | Audit status                  | Generated source audit report for 13 files.                                                                                                      | Audit showed 12 OK and 1 needing review.                                  |
| 2026-06-10 | `app/main.py`                                    | Final hardening               | Improved self-description routing, NIS2 annex/entity handling, Swedish section localization, source context display, and incident routing.       | Demo readiness improved.                                                  |
| 2026-06-10 | `app/main.py`                                    | SOC report export             | Added SOC-style Markdown incident report export.                                                                                                 | Incident documentation support improved.                                  |
| 2026-06-10 | `docs/test_cases.md`                             | Regression testing            | Updated tests for self-description, NIS2 scope, NIS2 annexes, GDPR/IMY security, incident response, SOC export, and refusal behavior.            | Final regression test coverage improved.                                  |
| 2026-06-10 | `README.md`                                      | Project documentation         | Updated README with current status, suggested test questions, known limitations, and future improvements.                                        | README aligned with current app.                                          |
| 2026-06-10 | `docs/demo_script.md`                            | Demo documentation            | Added or improved demo script for presentation flow, SOC export, safety boundaries, limitations, and future improvements.                        | Presentation support improved.                                            |
| 2026-06-10 | `docs/source_context_behavior.md`                | Source context                | Updated expected behavior for source context, incident filtering, Swedish labels, and fallback avoidance.                                        | Source-context behavior documented.                                       |
| 2026-06-10 | `docs/source_list.md`                            | Source documentation          | Updated source list to reflect 13 checked files, 12 OK, and 1 needing review.                                                                    | Source list aligned with audit.                                           |
| 2026-06-10 | `docs/source_policy.md`                          | Source policy                 | Updated source policy to reflect 13 checked files, current audit status, source history filename, and defensive cyber guidance rules.            | Source policy aligned with current state.                                 |

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

```text id="m5aa61"
Source name
https://source-url
```

New format:

```markdown id="orivw9"
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

```text id="1rrbvv"
scripts/source_audit.py
```

The script checks Markdown files in:

```text id="nzzwzk"
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

```text id="l3mkt5"
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

```text id="ti5j79"
scripts/add_missing_metadata.py
```

Purpose:

* add missing `## Source metadata` sections to local Markdown source files
* standardize source date and version notes format
* help older source files follow the same structure as newer files

Standard metadata format:

```markdown id="k3t4yy"
## Source metadata

Source date: Last checked: YYYY-MM-DD

Version notes: Source reviewed for CyberLex Sweden educational prototype.
```

Result:

The knowledge base source files became easier to audit and maintain.

---

## 2026-06-03 - Experimental Retrieval Module

An experimental retrieval module was added:

```text id="gndqxk"
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

```text id="8ngzr8"
data/imy_gdpr_security_measures.md
data/nis2_sector_scope_guidance.md
```

Purpose:

* improve GDPR/IMY questions about security measures, MFA, encryption, access control, and risk-based controls
* improve NIS2 questions about applicability, sectors, Annex 1 and Annex 2, registration, jurisdiction, and entity classification

Result:

CyberLex Sweden gained stronger support for common final-demo questions:

```text id="a2cobb"
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

## Current Source Audit Goal

The current source audit goal is:

```text id="wlwbw9"
Files marked OK: 13
Files needing review: 0
```

The current actual audit result is:

```text id="94jcna"
Files marked OK: 12
Files needing review: 1
```

The next source-maintenance task is to fix or remove:

```text id="cg9l4z"
data/gdpr_imy_edpb_security_guidance.md
```

---

## Future Source Update Priorities

Future source work should focus on:

* fixing or removing source files marked `Needs review`
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

## Final Note

CyberLex Sweden is source-grounded by design.

The source history shows how the local knowledge base and retrieval behavior changed over time, but it does not prove that the legal content is currently up to date.

The source audit checks local structure and metadata.

For real legal, compliance, regulatory, or incident-response decisions, official sources and qualified professionals should still be consulted.

Because reality insists on being difficult, this distinction matters.
