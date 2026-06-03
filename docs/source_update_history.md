# CyberLex Sweden Source Update History

## Purpose

This document tracks updates to the CyberLex Sweden knowledge base, source structure, source maintenance tools, source retrieval logic, and source-related documentation.

The goal is to make source changes transparent and easier to review.

Each entry should describe:

- date of update
- source file or project file changed
- topic
- reason for the update
- official sources used when relevant
- version notes

This document is part of the CyberLex Sweden source governance process. It helps explain how the local knowledge base developed over time and why specific changes were made.

CyberLex Sweden is an educational prototype. This update history does not prove that the law is currently up to date. It records changes made to the local project files.

---

## Update Log

| Date | Source file or project file | Topic | Change | Version notes |
|---|---|---|---|---|
| 2026-05-30 | `data/gdpr_personal_data_breach.md` | GDPR personal data breach reporting | Added educational summary, IMY authority information, reporting information, official source links, source date, and disclaimer | Initial educational summary added |
| 2026-05-30 | `data/nis2_cybersecurity_law.md` | NIS2 and Swedish Cybersecurity Act | Added educational summary, MSB authority information, cybersecurity responsibilities, incident reporting overview, official source links, source date, and disclaimer | Initial educational summary added |
| 2026-05-30 | `data/cybercrime_dataintrang.md` | Swedish cybercrime law and dataintrång | Added educational summary, legal reference, practical explanation, penetration testing connection, official source links, source date, and disclaimer | Initial educational summary added |
| 2026-05-30 | `data/gdpr_core_principles.md` | GDPR core principles | Added GDPR principles source for questions about data protection principles | Initial educational summary added |
| 2026-05-30 | `data/eu_attacks_against_information_systems.md` | EU attacks against information systems | Added EU cybercrime source connected to illegal access, system interference, and data interference | Initial educational summary added |
| 2026-05-30 | `data/eu_cyber_resilience_act.md` | EU Cyber Resilience Act | Added EU product cybersecurity source for products with digital elements | Initial educational summary added |
| 2026-05-31 | `data/imy_gdpr_supervision.md` | IMY and GDPR supervision in Sweden | Added separate IMY source for Swedish GDPR supervision and personal data protection authority questions | Initial educational summary added |
| 2026-05-31 | `data/nis2_incident_reporting.md` | NIS2 incident reporting in Sweden | Added dedicated source for cybersecurity incident reporting under the Swedish Cybersecurity Act and overlap with GDPR | Initial educational summary added |
| 2026-05-31 | `data/eu_dora_digital_operational_resilience.md` | EU DORA and digital operational resilience | Added DORA source for financial-sector cybersecurity, ICT risk management, incident reporting, and third-party ICT risk | Initial educational summary added |
| 2026-06-01 | All files in `data/` | Official source link formatting | Converted official source links from raw URL format to labeled Markdown link format | Official source link display improved |
| 2026-06-01 | `docs/source_list.md` | Source documentation | Updated the source list to include current knowledge base files and source link formatting notes | Source documentation updated |
| 2026-06-01 | `docs/source_policy.md` | Source rules | Added or updated rules for trusted source handling, official links, metadata, and limitations | Source governance improved |
| 2026-06-01 | `docs/test_cases.md` | Testing documentation | Updated test cases for source matching, official links, metadata display, source confidence, and out-of-scope refusal | Test coverage improved |
| 2026-06-01 | `docs/technical_design.md` | Technical documentation | Updated technical design to describe source routing, chunk search, citation display, metadata display, and answer structure | Technical documentation improved |
| 2026-06-03 | `scripts/source_audit.py` | Source audit script | Added a local source audit script that checks source files for official source sections, official links, source metadata, source date, and version notes | Source maintenance tooling added |
| 2026-06-03 | `docs/source_audit_report.md` | Source audit report | Added generated source audit report showing the status of all local source files | Source audit reporting added |
| 2026-06-03 | `scripts/add_missing_metadata.py` | Metadata helper script | Added helper script for adding missing source metadata sections to local Markdown source files | Metadata maintenance improved |
| 2026-06-03 | All files in `data/` | Source metadata | Added or standardized `## Source metadata` sections across knowledge base files | Metadata structure standardized |
| 2026-06-03 | `data/gdpr_personal_data_breach.md` | GDPR breach source cleanup | Removed duplicate source sections, standardized official links, and updated source metadata | Source reviewed and cleaned |
| 2026-06-03 | `data/imy_gdpr_supervision.md` | IMY supervision source cleanup | Removed duplicate source sections, standardized official links, and updated source metadata | Source reviewed and cleaned |
| 2026-06-03 | `.github/workflows/source-audit.yml` | Weekly source audit workflow | Added GitHub Actions workflow to run the source audit automatically and update the audit report | Weekly source audit automation added |
| 2026-06-03 | `docs/source_audit_report.md` | Source audit status | Confirmed that all 9 local source files are marked OK by the audit script | Source audit passed |
| 2026-06-03 | `docs/vector_search_plan.md` | Future vector search plan | Added planning document for future vector search, embeddings, and RAG development | Future AI retrieval planning added |
| 2026-06-03 | `app/vector_search.py` | Experimental AI search module | Added experimental search module for testing retrieval separately from the main answer system | Experimental retrieval module added |
| 2026-06-03 | `app/main.py` | Experimental AI search sidebar | Added sidebar panel for testing experimental source retrieval without replacing the main CyberLex answer system | Experimental search visible in app |
| 2026-06-03 | `app/vector_search.py` | Experimental ranking logic | Improved experimental ranking by boosting useful sections and penalizing weak support sections such as official source, metadata, disclaimer, and useful questions | Retrieval ranking improved |
| 2026-06-03 | `app/vector_search.py` | DORA retrieval | Improved DORA ranking so `What is DORA?` prefers `eu_dora_digital_operational_resilience.md` and the `Key idea` section | DORA retrieval improved |
| 2026-06-03 | `app/vector_search.py` | Unauthorized access retrieval | Improved unauthorized access ranking so English questions about illegal access prefer `cybercrime_dataintrang.md` | Cybercrime retrieval improved |
| 2026-06-03 | `data/nis2_incident_reporting.md` | Incident assessment checklist | Added a dedicated incident assessment checklist section for ransomware, malware, cyber incidents, and suspected reportable incidents | Practical incident source improved |
| 2026-06-03 | `app/vector_search.py` | Ransomware retrieval | Improved ransomware ranking so `What should a company do after a ransomware attack?` prefers `nis2_incident_reporting.md` and `Incident assessment checklist` | Ransomware retrieval improved |
| 2026-06-03 | `data/nis2_incident_reporting.md` | Swedish NIS2 incident reporting support | Added Swedish summary for ransomware, malware, cyber incidents, NIS2, the Swedish Cybersecurity Act, MSB, GDPR overlap, and incident documentation | Swedish NIS2 incident support added |
| 2026-06-03 | `data/gdpr_personal_data_breach.md` | Swedish GDPR breach support | Added Swedish summary and data breach assessment checklist for personuppgiftsincidenter, IMY, GDPR, 72-timmarsregeln, affected individuals, and breach documentation | Swedish GDPR breach support added |
| 2026-06-03 | `app/vector_search.py` | Swedish GDPR breach retrieval | Added Swedish GDPR breach terms, boosted GDPR breach source sections, and reduced incorrect NIS2 ranking for Swedish personuppgiftsincident questions | Swedish GDPR retrieval improved |
| 2026-06-03 | `app/vector_search.py` | Experimental search code fix | Fixed indentation and function structure in the experimental search module after retrieval logic updates | Experimental search syntax fixed |
| 2026-06-03 | `docs/technical_design.md` | Technical documentation | Updated technical design to document experimental AI search, source audit system, metadata helper script, weekly GitHub Actions audit, source quality labels, source freshness labels, and incident assessment checklist | Technical design updated |
| 2026-06-03 | `docs/test_cases.md` | Test documentation | Updated test cases to include experimental AI search tests, source audit tests, GitHub Actions audit test, and updated expected sections for ransomware/cyber incident questions | Test cases updated |

---

## Detailed Update Notes

## 2026-05-30 - Initial source base

Initial educational source summaries were added for the first CyberLex Sweden knowledge base files.

The goal was to create a trusted local Markdown knowledge base that could support simple source-grounded answers about selected Swedish and EU cybersecurity law topics.

Initial topics included:

- GDPR personal data breach reporting
- NIS2 and Swedish cybersecurity law
- Swedish cybercrime law and dataintrång
- GDPR core principles
- EU attacks against information systems
- EU Cyber Resilience Act

Affected files:

- `data/gdpr_personal_data_breach.md`
- `data/nis2_cybersecurity_law.md`
- `data/cybercrime_dataintrang.md`
- `data/gdpr_core_principles.md`
- `data/eu_attacks_against_information_systems.md`
- `data/eu_cyber_resilience_act.md`

Purpose:

- Build the first local source base.
- Give the app trusted source material to search.
- Support citation details and official source links.
- Keep answers limited to cybersecurity law, cybercrime, GDPR, NIS2, and related EU cybersecurity topics.

Result:

CyberLex Sweden could answer basic questions using local Markdown files instead of unsupported generated claims.

---

## 2026-05-31 - Additional authority and incident reporting sources

Additional source files were added to improve coverage for Swedish GDPR supervision, NIS2 incident reporting, and DORA.

Added files:

- `data/imy_gdpr_supervision.md`
- `data/nis2_incident_reporting.md`
- `data/eu_dora_digital_operational_resilience.md`

Purpose:

- Separate IMY supervision questions from GDPR breach reporting questions.
- Add a dedicated source for NIS2 incident reporting and Swedish cybersecurity incident reporting.
- Add DORA coverage for financial-sector ICT risk and digital operational resilience.
- Improve source routing for different legal frameworks.

Result:

CyberLex Sweden became better at routing questions to the correct source file instead of relying only on general keyword overlap.

---

## 2026-06-01 - Official source link formatting update

The official source sections in the knowledge base were updated to use labeled Markdown links instead of raw URLs.

Changed format from:

```text
Source name
https://source-url
```

to:

```markdown
[Source name](https://source-url)
```

Purpose:

- Improve readability of official source links in the CyberLex interface.
- Preserve all existing useful sources.
- Make source citations easier to understand for users.
- Prepare the project for future AI/RAG-based answer generation.
- Make source display more consistent in Streamlit.

Affected source files included:

- `data/gdpr_core_principles.md`
- `data/imy_gdpr_supervision.md`
- `data/gdpr_personal_data_breach.md`
- `data/nis2_cybersecurity_law.md`
- `data/nis2_incident_reporting.md`
- `data/cybercrime_dataintrang.md`
- `data/eu_attacks_against_information_systems.md`
- `data/eu_cyber_resilience_act.md`
- `data/eu_dora_digital_operational_resilience.md`

Result:

Official source links display as readable clickable labels inside the Streamlit app.

---

## 2026-06-03 - Source audit system added

A local source audit script was added:

```text
scripts/source_audit.py
```

The script checks all Markdown files in:

```text
data/
```

The script checks for:

- official source section
- official source links
- source metadata section
- source date
- source freshness
- version notes

The script generates:

```text
docs/source_audit_report.md
```

Purpose:

- Make source maintenance more visible.
- Check whether local source files follow the expected structure.
- Detect missing official links or metadata.
- Create a repeatable source review process.
- Provide evidence that the knowledge base is maintained.

Important limitation:

The audit does not browse the web and does not confirm whether the law is currently up to date.

It only checks the local project files.

Result:

CyberLex Sweden gained a repeatable local source audit process.

---

| 2026-06-03 | `data/imy_gdpr_supervision.md` | Swedish IMY supervision support | Added Swedish summary for IMY, GDPR supervision, dataskydd, personuppgiftsskydd, tillsyn, klagomål, and cybersecurity incidents involving personal data | Swedish IMY support added |
| 2026-06-03 | `app/vector_search.py` | Swedish IMY retrieval | Improved retrieval so Swedish questions such as `Vad är IMY?` prefer `imy_gdpr_supervision.md` instead of GDPR breach material | Swedish IMY retrieval improved |

## 2026-06-03 - Metadata helper script added

A metadata helper script was added:

```text
scripts/add_missing_metadata.py
```

Purpose:

- Add missing `## Source metadata` sections to local Markdown source files.
- Standardize source date and version notes format.
- Help bring older source files into the same structure as newer files.

Standard metadata format:

```markdown
## Source metadata

Source date: Last checked: 2026-06-03

Version notes: Source reviewed for CyberLex Sweden educational prototype.
```

Result:

The knowledge base source files became easier to audit and maintain.

---

## 2026-06-03 - Source metadata standardized

The source files in `data/` were updated to include or standardize source metadata.

Affected files included all current source files:

- `data/cybercrime_dataintrang.md`
- `data/eu_attacks_against_information_systems.md`
- `data/eu_cyber_resilience_act.md`
- `data/eu_dora_digital_operational_resilience.md`
- `data/gdpr_core_principles.md`
- `data/gdpr_personal_data_breach.md`
- `data/imy_gdpr_supervision.md`
- `data/nis2_cybersecurity_law.md`
- `data/nis2_incident_reporting.md`

Purpose:

- Support source freshness labels in the app.
- Support source audit reporting.
- Make every local source file show a stored review date.
- Make every local source file include version notes.

Result:

The audit report was able to mark all 9 local source files as OK after missing metadata and duplicate source issues were corrected.

---

## 2026-06-03 - GDPR and IMY source cleanup

Two source files had duplicate source sections and inconsistent source structure:

- `data/gdpr_personal_data_breach.md`
- `data/imy_gdpr_supervision.md`

They were cleaned and standardized.

Changes included:

- removing duplicate official source sections
- keeping useful official source links
- standardizing source metadata
- updating version notes
- keeping disclaimers
- making the files pass the source audit

Purpose:

- Remove duplicated source structure.
- Improve source audit results.
- Make citation display more reliable.
- Prevent official links from being missed by the audit script.

Result:

Both source files passed the source audit.

---

## 2026-06-03 - Weekly GitHub Actions source audit added

A GitHub Actions workflow was added:

```text
.github/workflows/source-audit.yml
```

The workflow can run manually from the GitHub Actions tab and is scheduled to run weekly.

The workflow:

1. checks out the repository
2. sets up Python
3. runs `python scripts/source_audit.py`
4. updates `docs/source_audit_report.md`
5. commits the updated report if changes are found

Purpose:

- Automate the local source audit.
- Keep the audit report updated.
- Show that the project has a maintenance process.
- Make source review easier over time.

Important limitation:

The workflow does not verify live legal updates online.

It only checks the local source file structure.

Result:

The GitHub Actions workflow successfully ran and produced a successful workflow result.

---

## 2026-06-03 - Source audit report passed

The generated audit report showed:

```text
Files marked OK: 9
Files needing review: 0
```

The report file is:

```text
docs/source_audit_report.md
```

Purpose:

- Confirm that all local knowledge base files had the required source structure.
- Confirm that all source files had official links and metadata.
- Provide a reviewable maintenance report.

Result:

All 9 knowledge base files were marked OK.

---

## 2026-06-03 - Vector search plan added

A planning document was added:

```text
docs/vector_search_plan.md
```

Purpose:

- Describe the planned future vector search upgrade.
- Explain why vector search is useful.
- Explain the difference between keyword search and meaning-based search.
- Prepare the project for embeddings and RAG later.

The plan explains that future versions may use:

- sentence-transformers
- embeddings
- ChromaDB
- FAISS
- RAG-based answer generation

Result:

CyberLex Sweden now has a documented path toward future AI-assisted retrieval.

---

## 2026-06-03 - Experimental AI search module added

An experimental search module was added:

```text
app/vector_search.py
```

Purpose:

- Test improved retrieval separately from the main app.
- Build a safe foundation for future vector search.
- Avoid breaking the main CyberLex answer system while testing ranking changes.
- Compare experimental retrieval behavior with the existing main source search.

Current behavior:

- loads Markdown files from `data/`
- splits them into chunks
- cleans text
- scores chunks
- boosts useful sections
- penalizes weak sections
- applies topic-specific ranking rules
- returns ranked source matches

Important limitation:

Despite the file name, the current module does not yet use true vector embeddings or a vector database.

It is an experimental retrieval module that prepares the project for future vector search.

Result:

CyberLex Sweden gained a separate experimental retrieval system.

---

## 2026-06-03 - Experimental AI search sidebar added

The main Streamlit app was updated to show an experimental AI search panel in the sidebar.

Affected file:

```text
app/main.py
```

Purpose:

- Let the user test experimental retrieval directly in the app.
- Show source file, source section, and score for experimental matches.
- Compare retrieval quality before changing the main answer system.
- Keep the main CyberLex answer system stable while testing improvements.

Result:

The sidebar can now test questions such as:

```text
What is DORA?
```

```text
Is unauthorized access illegal in Sweden?
```

```text
What should a company do after a ransomware attack?
```

---

## 2026-06-03 - Experimental ranking improved

The ranking logic in `app/vector_search.py` was improved.

Changes included:

- boosting useful content sections
- penalizing weak support sections
- adding topic-specific boosts
- reducing false matches to weak sections
- improving DORA retrieval
- improving unauthorized access retrieval
- improving ransomware retrieval

Useful sections boosted include:

- incident assessment checklist
- data breach assessment checklist
- Swedish summary
- key idea
- important points
- main authority
- reporting to IMY
- affected individuals
- incident reporting
- cybersecurity connection
- practical explanation
- relationship with GDPR breach reporting
- third-party ICT risk
- legal reference

Weak sections penalized include:

- useful questions
- official source
- source metadata
- source date
- version notes
- disclaimer
- topic
- introduction

Purpose:

- Make experimental search prefer real explanatory sections.
- Stop example-question sections or source-link sections from ranking too high.
- Improve section-level retrieval quality.

Result:

The experimental search became more useful and more predictable.

---

## 2026-06-03 - DORA retrieval improved

Experimental search for:

```text
What is DORA?
```

was improved.

Expected top result:

```text
eu_dora_digital_operational_resilience.md
Section: Key idea
```

Purpose:

- Make DORA questions match the DORA source file.
- Prefer explanatory DORA sections over weak support sections such as official source or useful questions.

Result:

DORA questions now correctly return the DORA source and the `Key idea` section near the top.

---

## 2026-06-03 - Unauthorized access retrieval improved

Experimental search for:

```text
Is unauthorized access illegal in Sweden?
```

was improved.

Expected top result:

```text
cybercrime_dataintrang.md
Section: Key idea
```

Purpose:

- Make English unauthorized access questions match Swedish cybercrime material.
- Connect the English phrase “unauthorized access” with the Swedish concept `dataintrång`.

Result:

Unauthorized access questions now correctly retrieve the cybercrime dataintrång source.

---

## 2026-06-03 - NIS2 incident assessment checklist added

The source file:

```text
data/nis2_incident_reporting.md
```

was updated with a new section:

```text
Incident assessment checklist
```

Purpose:

- Improve answers for practical incident-response questions.
- Give CyberLex a stronger source chunk for ransomware, malware, cyber incident, and suspected reporting questions.
- Help the app answer what an organization should check after an incident.

The checklist covers:

- when the incident was discovered
- which systems, services, accounts, or networks were affected
- whether essential or important services were disrupted
- whether personal data may have been affected
- whether NIS2 or Swedish Cybersecurity Act reporting may be relevant
- whether GDPR personal data breach notification to IMY may also be relevant
- what containment and recovery actions were taken
- what logs, evidence, decisions, and timelines were preserved
- whether internal incident response procedures were followed

Result:

The source file became more useful for practical ransomware and cyber incident questions.

---

## 2026-06-03 - Swedish NIS2 incident reporting summary added

The source file:

```text
data/nis2_incident_reporting.md
```

was updated with a Swedish summary section.

Purpose:

- Improve support for Swedish questions about ransomware, malware, cyber incidents, NIS2, the Swedish Cybersecurity Act, MSB, GDPR overlap, and incident reporting.
- Help Swedish search terms match the correct local source file.
- Support bilingual CyberLex Sweden testing.
- Make the source more useful for Swedish users.

The Swedish summary covers:

- ransomwareattacker
- skadlig kod
- cybersäkerhetsincidenter
- incidentrapportering
- NIS2
- cybersäkerhetslagen
- GDPR-overlap
- personuppgiftsincidenter
- IMY
- MSB
- loggar, bevis, beslut och tidslinjer

Result:

Swedish ransomware and cyber incident questions now match the NIS2 incident reporting source more reliably.

---

## 2026-06-03 - Ransomware retrieval improved

Experimental search for:

```text
What should a company do after a ransomware attack?
```

was improved.

Expected top result:

```text
nis2_incident_reporting.md
Section: Incident assessment checklist
```

Purpose:

- Stop general ransomware questions from incorrectly ranking DORA first.
- Route ransomware questions toward NIS2 incident reporting and the new checklist section.
- Keep GDPR breach material relevant as supporting context when personal data may be affected.

Result:

The experimental search now correctly ranks the NIS2 incident assessment checklist as the top result for ransomware questions.

---

## 2026-06-03 - Swedish GDPR personal data breach summary added

The source file:

```text
data/gdpr_personal_data_breach.md
```

was updated with a Swedish summary and a data breach assessment checklist.

Purpose:

- Improve support for Swedish questions about personuppgiftsincidenter, IMY, GDPR, 72-timmarsregeln, dataläckor, affected individuals, and data breach assessment.
- Help Swedish questions match the GDPR personal data breach source instead of the broader NIS2 incident source.
- Support bilingual CyberLex Sweden testing.
- Give CyberLex stronger source chunks for practical GDPR breach questions.

The Swedish summary covers:

- what a personuppgiftsincident is
- when IMY may need to be notified
- the 72-hour rule
- risk to individuals' rights and freedoms
- affected individuals
- documentation of decisions, logs, evidence, and timeline
- the difference between all incidents and reportable incidents

Result:

Swedish personal data breach questions now have better source support inside the GDPR breach file.

---

## 2026-06-03 - Swedish GDPR breach retrieval improved

The experimental search module was updated:

```text
app/vector_search.py
```

Changes included:

- added Swedish GDPR breach terms to experimental retrieval
- boosted `gdpr_personal_data_breach.md` for Swedish personuppgiftsincident questions
- boosted `Data breach assessment checklist`
- boosted `Swedish summary`
- boosted `Reporting to IMY`
- reduced incorrect NIS2 ranking for Swedish GDPR breach questions
- fixed indentation and function structure in the experimental search code

Purpose:

- Make Swedish questions such as `Vad ska ett företag göra efter en personuppgiftsincident?` match the GDPR breach source.
- Prevent broad incident wording from incorrectly ranking NIS2 above GDPR breach material.
- Improve bilingual retrieval quality.

Expected top results now include:

```text
gdpr_personal_data_breach.md
Section: Swedish summary
```

or:

```text
gdpr_personal_data_breach.md
Section: Data breach assessment checklist
```

Result:

The experimental search now correctly retrieves the GDPR personal data breach source for Swedish personuppgiftsincident questions.

---

## 2026-06-03 - Experimental search code structure fixed

The experimental search module was corrected after adding the Swedish GDPR retrieval logic.

Affected file:

```text
app/vector_search.py
```

Issue:

The GDPR scoring block and `return score` line had indentation problems after editing.

Purpose:

- Restore valid Python syntax.
- Keep all scoring logic inside the `score_chunk()` function.
- Make the experimental search module compile correctly.
- Preserve the improved Swedish GDPR retrieval logic.

Verification command:

```powershell
python -m py_compile app/vector_search.py
```

Result:

The experimental search module compiled successfully after the structure was corrected.

---

## 2026-06-03 - Technical documentation updated

The technical design document was updated:

```text
docs/technical_design.md
```

The update documented:

- experimental AI search module
- experimental AI search sidebar
- experimental ranking logic
- incident assessment checklist source design
- source audit system
- metadata helper script
- weekly GitHub Actions audit
- source quality labels
- source freshness labels
- current technical status

Purpose:

- Keep technical documentation aligned with the actual project.
- Explain current system design clearly.
- Separate current rule-based prototype features from planned future vector search and RAG.

Result:

The technical design now reflects the current CyberLex Sweden prototype.

---

## 2026-06-03 - Test cases updated

The test cases document was updated:

```text
docs/test_cases.md
```

The update added or improved test coverage for:

- experimental AI search sidebar
- DORA experimental retrieval
- unauthorized access experimental retrieval
- ransomware experimental retrieval
- cyber incident experimental retrieval
- data breach experimental retrieval
- local source audit script
- source audit report
- metadata helper script
- GitHub Actions weekly source audit
- source audit limitation wording
- updated ransomware expected section
- updated cyber incident expected section
- Swedish GDPR breach retrieval behavior

Purpose:

- Keep tests aligned with the current prototype.
- Document the expected behavior of the experimental retrieval system.
- Show that source audit and GitHub Actions workflow are part of the tested project.

Result:

The test cases now cover the current source-grounded app, experimental AI search, source maintenance workflow, and improved Swedish retrieval behavior.

---

## Source Review Rules

When a knowledge base source is added or updated, the following should be checked:

1. The source file has a clear topic.
2. The source file uses trusted legal or authority-based sources.
3. The source file includes official source links.
4. The source file includes a source date.
5. The source file includes version notes.
6. The source file includes a disclaimer.
7. The source file is added to `docs/source_list.md`.
8. The source file is covered by at least one test case in `docs/test_cases.md`.
9. The source file passes `scripts/source_audit.py`.
10. The source file is mentioned in this source update history when the change is significant.
11. New Swedish source sections should be tested with Swedish questions in the experimental AI search sidebar.
12. Retrieval changes should be tested with `python -m py_compile` before commit.

---

## Current Knowledge Base Files

The current trusted knowledge base files are:

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

---

## Current Source Maintenance Files

The current source maintenance and documentation files include:

```text
docs/source_list.md
docs/source_policy.md
docs/source_update_history.md
docs/source_audit_report.md
docs/test_cases.md
docs/technical_design.md
docs/vector_search_plan.md
scripts/source_audit.py
scripts/add_missing_metadata.py
.github/workflows/source-audit.yml
```

---

## Current Retrieval Files

The current retrieval-related project files include:

```text
app/main.py
app/vector_search.py
```

`app/main.py` contains the main Streamlit application and the experimental search sidebar.

`app/vector_search.py` contains the experimental retrieval module used for testing source ranking before real vector search is added.

---

## Current Source Status

The current source audit goal is:

```text
Files marked OK: 9
Files needing review: 0
```

This means every local source file should have:

- official source links
- source metadata
- source date
- version notes
- consistent source structure

This does not mean that the legal content has been verified online during the audit.

It only means that the local source files pass the structural source audit.

---

## Current Retrieval Status

The current experimental retrieval goals include:

```text
What is DORA?
```

Expected top source:

```text
eu_dora_digital_operational_resilience.md
Section: Key idea
```

```text
What should a company do after a ransomware attack?
```

Expected top source:

```text
nis2_incident_reporting.md
Section: Incident assessment checklist
```

```text
Vad ska ett företag göra efter en ransomwareattack?
```

Expected top source:

```text
nis2_incident_reporting.md
Section: Incident assessment checklist
```

```text
Vad ska ett företag göra efter en personuppgiftsincident?
```

Expected top source:

```text
gdpr_personal_data_breach.md
Section: Swedish summary
```

or:

```text
gdpr_personal_data_breach.md
Section: Data breach assessment checklist
```

These retrieval results are part of the experimental AI search sidebar and do not yet replace the main CyberLex answer system.

---

## Future Source Update Priorities

Future source work should focus on:

- improving Swedish source summaries
- adding more Swedish legal sources
- adding more EU cybersecurity law sources
- strengthening GDPR, NIS2, DORA, CRA, and cybercrime coverage
- improving bilingual Swedish and English source coverage
- reviewing source dates regularly
- expanding test cases when new sources are added
- improving source update notes when legal summaries change
- eventually adding a workflow for checking whether official source pages have changed

---

## Important Limitation

This update history tracks local project changes.

It does not confirm that any law, regulation, authority page, or official guidance is currently up to date.

For real legal or compliance decisions, the official source should always be checked directly.