# CyberLex Sweden Source Update History

## Purpose

This document tracks updates to the CyberLex Sweden knowledge base.

The goal is to make source changes more transparent and easier to review.

Each entry should describe:

- date of update
- source file changed
- topic
- reason for the update
- official sources used
- version notes

---

## Update Log

| Date | Source file | Topic | Change | Version notes |
|---|---|---|---|---|
| 2026-05-30 | `gdpr_personal_data_breach.md` | GDPR personal data breach reporting | Added educational summary, IMY authority information, reporting information, official source links, source date, and disclaimer | Initial educational summary added |
| 2026-05-30 | `nis2_cybersecurity_law.md` | NIS2 and Swedish Cybersecurity Act | Added educational summary, MSB authority information, cybersecurity responsibilities, incident reporting overview, official source links, source date, and disclaimer | Initial educational summary added |
| 2026-05-30 | `cybercrime_dataintrang.md` | Swedish cybercrime law and dataintrång | Added educational summary, legal reference, practical explanation, penetration testing connection, official source links, source date, and disclaimer | Initial educational summary added |
| 2026-05-30 | `gdpr_core_principles.md` | GDPR core principles | Added GDPR principles source for questions about data protection principles | Initial educational summary added |
| 2026-05-30 | `eu_attacks_against_information_systems.md` | EU attacks against information systems | Added EU cybercrime source connected to illegal access, system interference, and data interference | Initial educational summary added |
| 2026-05-30 | `eu_cyber_resilience_act.md` | EU Cyber Resilience Act | Added EU product cybersecurity source for products with digital elements | Initial educational summary added |
| 2026-05-31 | `imy_gdpr_supervision.md` | IMY and GDPR supervision in Sweden | Added separate IMY source for Swedish GDPR supervision and personal data protection authority questions | Initial educational summary added |
| 2026-05-31 | `nis2_incident_reporting.md` | NIS2 incident reporting in Sweden | Added dedicated source for cybersecurity incident reporting under the Swedish Cybersecurity Act and overlap with GDPR | Initial educational summary added |
| 2026-05-31 | `eu_dora_digital_operational_resilience.md` | EU DORA and digital operational resilience | Added DORA source for financial-sector cybersecurity, ICT risk management, incident reporting, and third-party ICT risk | Initial educational summary added |

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
## 2026-06-01 - Official source link formatting update

Updated CyberLex Sweden knowledge base source sections to use labeled Markdown links instead of raw URLs.

Changed format from:

```text
Source name
https://source-url