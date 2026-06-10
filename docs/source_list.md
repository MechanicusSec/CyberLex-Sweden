# CyberLex Sweden Source List

## Purpose

This document lists the trusted source areas and local knowledge files used by CyberLex Sweden.

CyberLex Sweden should only answer legal, compliance, cybersecurity-law, and defensive incident-response questions from selected trusted source material.

The system should avoid guessing, unsupported legal claims, and answers outside the project scope.

This source list supports:

* source transparency
* source review
* knowledge base maintenance
* source audit checks
* testing and demo preparation
* future vector search or RAG development
* project documentation and final reporting

CyberLex Sweden is an educational prototype. It does not provide legal advice.

---

## Source Categories

CyberLex Sweden uses source material from these categories:

* Swedish law
* EU law and regulations
* Swedish government agencies
* cybersecurity authorities
* data protection authorities
* police and cybercrime information
* financial-sector digital resilience sources
* product cybersecurity regulation sources
* defensive incident-response guidance

Trusted sources should normally come from official legal databases, official authority websites, recognized EU institutions, or well-known cybersecurity authorities.

---

## Current Local Knowledge Base Files

CyberLex Sweden currently uses Markdown knowledge files in:

```text
data/
```

The current local source audit checks 13 files:

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

The current audit result is:

```text
Files marked OK: 12
Files needing review: 1
```

The file currently needing review is:

```text
data/gdpr_imy_edpb_security_guidance.md
```

Reason:

```text
Missing official source section, official source links, source metadata, source date, and version notes.
```

This file should either be fixed or removed before final hand-in, depending on whether it is actually used by the app.

---

## Required Source File Structure

Each source file should include, where relevant:

* `## Topic`
* `## Main authority`
* `## Main legal source`
* `## Key idea`
* `## Important points`
* cybersecurity or practical connection
* useful questions
* `## Official source`
* `## Source metadata`
* disclaimer

The exact headings may vary slightly depending on the source type, but each file should clearly show:

* what the source topic is
* which authority or legal source it is based on
* what the key idea is
* which questions it supports
* which official links support the content
* when the file was last checked
* what changed in the file
* that the material is educational and not legal advice

---

## Source File Overview

| Local file                                       | Main topic                                     | Main source type                                              | Status       |
| ------------------------------------------------ | ---------------------------------------------- | ------------------------------------------------------------- | ------------ |
| `data/cyber_incident_response_playbook.md`       | Defensive cyber incident response              | Defensive incident-response guidance and authority references | Reviewed     |
| `data/cybercrime_dataintrang.md`                 | Swedish cybercrime and dataintrång             | Swedish legal source                                          | Reviewed     |
| `data/eu_attacks_against_information_systems.md` | EU attacks against information systems         | EU directive                                                  | Reviewed     |
| `data/eu_cyber_resilience_act.md`                | Cyber Resilience Act                           | EU regulation                                                 | Reviewed     |
| `data/eu_dora_digital_operational_resilience.md` | DORA and digital operational resilience        | EU regulation                                                 | Reviewed     |
| `data/gdpr_core_principles.md`                   | GDPR core principles                           | EU regulation                                                 | Reviewed     |
| `data/gdpr_imy_edpb_security_guidance.md`        | GDPR, IMY, and EDPB security guidance          | Data protection guidance                                      | Needs review |
| `data/gdpr_personal_data_breach.md`              | GDPR personal data breach notification         | EU regulation and IMY guidance                                | Reviewed     |
| `data/imy_gdpr_security_measures.md`             | IMY GDPR security measures                     | Swedish authority guidance                                    | Reviewed     |
| `data/imy_gdpr_supervision.md`                   | IMY and Swedish GDPR supervision               | Swedish authority source                                      | Reviewed     |
| `data/nis2_cybersecurity_law.md`                 | NIS2 and Swedish cybersecurity law             | EU directive and Swedish authority guidance                   | Reviewed     |
| `data/nis2_incident_reporting.md`                | NIS2 incident reporting                        | EU directive and Swedish authority guidance                   | Reviewed     |
| `data/nis2_sector_scope_guidance.md`             | NIS2 scope, sectors, and entity classification | Swedish/EU cybersecurity-law guidance                         | Reviewed     |

---

## 1. Defensive Incident-Response Guidance

### Cyber Incident Response Playbook

**Local file:** `data/cyber_incident_response_playbook.md`

**Topic:** Defensive first steps for common cybersecurity incidents.

Used for questions about:

* suspected hacking
* unauthorized access
* suspicious login activity
* suspicious MFA activity
* suspicious email or phishing
* clicked links
* opened attachments
* entered credentials
* compromised accounts
* ransomware
* malware
* encrypted files
* data leaks
* evidence preservation
* incident documentation
* escalation and reporting assessment

Main source type:

* defensive cybersecurity guidance
* authority-based incident-response references
* educational CyberLex incident handling summary

Source metadata status:

```text
Source date: Last checked: 2026-06-04
Status: Reviewed
```

---

## 2. Swedish Legal Sources

### Sveriges Riksdag

Website:

```text
https://www.riksdagen.se
```

Purpose:

Sveriges Riksdag provides official Swedish laws and legal documents.

Relevant areas:

* Brottsbalken
* Swedish criminal law
* dataintrång
* unauthorized access
* cybercrime-related offences
* laws related to electronic communication
* laws related to national security and preparedness

Why this source is trusted:

The Riksdag website is an official source for Swedish legislation.

Used in CyberLex Sweden for:

```text
data/cybercrime_dataintrang.md
```

---

## 3. Swedish Data Protection Authority

### IMY - Integritetsskyddsmyndigheten

Website:

```text
https://www.imy.se
```

Purpose:

IMY is the Swedish Authority for Privacy Protection.

Relevant areas:

* GDPR
* personal data breaches
* personal data breach notification
* data protection responsibilities
* security measures
* technical and organizational measures
* incident notification
* data controller and processor responsibilities
* Swedish GDPR supervision

Why this source is trusted:

IMY is the official Swedish authority responsible for supervising data protection and GDPR compliance in Sweden.

Used in CyberLex Sweden for:

```text
data/imy_gdpr_supervision.md
data/imy_gdpr_security_measures.md
data/gdpr_personal_data_breach.md
```

The file `data/gdpr_imy_edpb_security_guidance.md` may also use IMY-related material, but it currently needs review before it should be treated as a clean source file.

---

## 4. Swedish Cybersecurity and Civil Preparedness

### MSB - Myndigheten för samhällsskydd och beredskap

Website:

```text
https://www.msb.se
```

Purpose:

MSB provides guidance on cybersecurity, information security, incident reporting, NIS, and NIS2-related cybersecurity requirements.

Relevant areas:

* cybersecurity requirements
* NIS and NIS2
* Swedish Cybersecurity Act topics
* incident reporting
* information security
* societal resilience and preparedness

Why this source is trusted:

MSB is a Swedish government authority responsible for civil protection, preparedness, and parts of national cybersecurity coordination.

Used in CyberLex Sweden for:

```text
data/nis2_cybersecurity_law.md
data/nis2_incident_reporting.md
data/cyber_incident_response_playbook.md
```

---

## 5. Swedish Cybersecurity Coordination

### MCF - Myndigheten för cybersäkerhet och civilt försvar

Purpose:

MCF-related guidance may be used for Swedish cybersecurity law, NIS2 scope, sector coverage, registration, and entity classification material where relevant to the current Swedish cybersecurity framework.

Relevant areas:

* Swedish Cybersecurity Act scope
* NIS2 sector coverage
* essential and important entities
* registration
* size assessment
* jurisdiction
* public administration questions

Used in CyberLex Sweden for:

```text
data/nis2_sector_scope_guidance.md
```

Important note:

This source area should be reviewed carefully when Swedish implementation guidance changes.

---

## 6. EU Legal Sources

### EUR-Lex

Website:

```text
https://eur-lex.europa.eu
```

Purpose:

EUR-Lex provides official access to European Union law.

Relevant areas:

* GDPR
* NIS2 Directive
* Cyber Resilience Act
* DORA
* Directive 2013/40/EU on attacks against information systems
* EU cybersecurity and data protection rules

Why this source is trusted:

EUR-Lex is the official EU legal database.

Used in CyberLex Sweden for:

```text
data/gdpr_core_principles.md
data/gdpr_personal_data_breach.md
data/nis2_cybersecurity_law.md
data/nis2_incident_reporting.md
data/nis2_sector_scope_guidance.md
data/eu_attacks_against_information_systems.md
data/eu_cyber_resilience_act.md
data/eu_dora_digital_operational_resilience.md
```

---

## 7. European Data Protection Sources

### European Data Protection Board

Website:

```text
https://www.edpb.europa.eu
```

Purpose:

The European Data Protection Board provides guidance and interpretation related to GDPR.

Relevant areas:

* GDPR guidance
* data protection principles
* security measures
* personal data breach guidance
* cross-border data protection issues
* controller and processor responsibilities

Why this source is trusted:

The EDPB provides official European-level guidance on data protection law.

Current use:

EDPB material may be used for GDPR security guidance and future expansion.

The file below currently needs review before it should be treated as fully source-complete:

```text
data/gdpr_imy_edpb_security_guidance.md
```

---

## 8. CERT-SE and Cybersecurity Incident Support

### CERT-SE

Purpose:

CERT-SE provides cybersecurity incident support and guidance in Sweden.

Relevant areas:

* cyber incident reporting
* incident handling
* vulnerability warnings
* defensive cybersecurity guidance
* escalation support for serious incidents

Used in CyberLex Sweden for:

```text
data/cyber_incident_response_playbook.md
```

Important note:

CERT-SE guidance supports defensive incident-response handling. It should not be used to provide offensive cyber instructions.

---

## 9. EU DORA: Digital Operational Resilience Act

**Local file:** `data/eu_dora_digital_operational_resilience.md`

**Topic:** Digital operational resilience and cybersecurity requirements for the EU financial sector.

**Main legal source:** Regulation (EU) 2022/2554, Digital Operational Resilience Act.

Used for questions about:

* DORA
* Digital Operational Resilience Act
* digital operational resilience
* financial-sector cybersecurity
* ICT risk management
* ICT-related incident reporting
* ICT third-party risk
* resilience testing
* relationship between DORA, NIS2, and GDPR

Official source examples:

* EUR-Lex Regulation (EU) 2022/2554
* European Commission DORA information
* European Banking Authority DORA information
* EIOPA DORA information
* ESMA DORA information

Source metadata status:

```text
Source date: Last checked: 2026-06-03
Status: Reviewed
```

---

## 10. EU Cyber Resilience Act

**Local file:** `data/eu_cyber_resilience_act.md`

**Topic:** Cybersecurity requirements for products with digital elements.

**Main legal source:** Regulation (EU) 2024/2847, Cyber Resilience Act.

Used for questions about:

* Cyber Resilience Act
* CRA
* products with digital elements
* product cybersecurity
* cybersecurity by design
* vulnerability handling
* security updates
* manufacturers, importers, and distributors
* relationship between CRA, NIS2, GDPR, and DORA

Official source examples:

* EUR-Lex Regulation (EU) 2024/2847
* European Commission Cyber Resilience Act information
* European Commission CRA implementation information

Source metadata status:

```text
Source date: Last checked: 2026-06-03
Status: Reviewed
```

---

## 11. EU Attacks Against Information Systems

**Local file:** `data/eu_attacks_against_information_systems.md`

**Topic:** EU cybercrime rules on attacks against information systems.

**Main legal source:** Directive 2013/40/EU on attacks against information systems.

Used for questions about:

* attacks against information systems
* illegal access under EU cybercrime rules
* illegal system interference
* illegal data interference
* illegal interception
* misuse of tools
* botnets
* DDoS attacks
* relationship with Swedish dataintrång

Official source examples:

* EUR-Lex Directive 2013/40/EU
* EUR-Lex summary on attacks against information systems

Source metadata status:

```text
Source date: Last checked: 2026-06-03
Status: Reviewed
```

---

## 12. GDPR and Personal Data Protection

### GDPR Core Principles

**Local file:** `data/gdpr_core_principles.md`

**Topic:** Core GDPR principles.

Used for questions about:

* GDPR principles
* lawfulness, fairness, and transparency
* purpose limitation
* data minimisation
* accuracy
* storage limitation
* integrity and confidentiality
* accountability

Main legal source:

* Regulation (EU) 2016/679, General Data Protection Regulation

Source metadata status:

```text
Source date: Last checked: 2026-06-03
Status: Reviewed
```

### GDPR Personal Data Breach Notification

**Local file:** `data/gdpr_personal_data_breach.md`

**Topic:** Personal data breach notification and IMY reporting.

Used for questions about:

* personal data breaches
* personuppgiftsincident
* 72-hour reporting assessment
* breach notification to IMY
* affected individuals
* GDPR and cyber incidents

Main source types:

* GDPR
* IMY guidance

Source metadata status:

```text
Source date: Last checked: 2026-06-03
Status: Reviewed
```

### IMY GDPR Supervision

**Local file:** `data/imy_gdpr_supervision.md`

**Topic:** IMY and Swedish GDPR supervision.

Used for questions about:

* IMY
* Swedish GDPR authority
* data protection supervision
* privacy protection authority
* complaints and supervision

Main source type:

* Swedish authority source

Source metadata status:

```text
Source date: Last checked: 2026-06-03
Status: Reviewed
```

### IMY GDPR Security Measures

**Local file:** `data/imy_gdpr_security_measures.md`

**Topic:** GDPR security measures and technical or organizational security controls.

Used for questions about:

* IMY security guidance
* GDPR security measures
* MFA
* encryption
* access control
* logging
* backups
* risk-based technical and organizational measures

Main source type:

* Swedish authority guidance

Source metadata status:

```text
Source date: Last checked: 2026-06-08
Status: Reviewed
```

### GDPR, IMY, and EDPB Security Guidance

**Local file:** `data/gdpr_imy_edpb_security_guidance.md`

**Topic:** GDPR, IMY, and EDPB security guidance.

Current status:

```text
Needs review
```

Current audit issues:

* missing `## Official source` section
* no official source links found
* missing `## Source metadata` section
* missing source date
* missing version notes
* no review date stored

Recommended action:

This file should be fixed or removed before final hand-in.

If it duplicates `data/imy_gdpr_security_measures.md`, consider deleting it after checking whether the app still references it.

---

## 13. NIS2 and Swedish Cybersecurity Law

### NIS2 Cybersecurity Law

**Local file:** `data/nis2_cybersecurity_law.md`

**Topic:** NIS2 and the Swedish Cybersecurity Act.

Used for questions about:

* NIS2
* cybersäkerhetslagen
* cybersecurity risk management
* security measures
* covered organizations
* management responsibility
* supply chain security
* relationship with GDPR and DORA

Main source types:

* NIS2 Directive
* MSB guidance
* Swedish cybersecurity law material

Source metadata status:

```text
Source date: Last checked: 2026-06-03
Status: Reviewed
```

### NIS2 Incident Reporting

**Local file:** `data/nis2_incident_reporting.md`

**Topic:** Incident reporting under NIS2 and Swedish cybersecurity rules.

Used for questions about:

* NIS2 incident reporting
* cybersecurity incident reporting
* ransomware attacks
* malware incidents
* incident assessment
* evidence preservation
* logs and timelines
* overlap with GDPR personal data breach reporting

Main source types:

* NIS2 Directive
* MSB guidance
* Swedish cybersecurity law material

Source metadata status:

```text
Source date: Last checked: 2026-06-03
Status: Reviewed
```

### NIS2 Sector Scope Guidance

**Local file:** `data/nis2_sector_scope_guidance.md`

**Topic:** NIS2 scope, covered sectors, registration, size assessment, and entity classification.

Used for questions about:

* whether NIS2 applies
* sectors covered by the Swedish Cybersecurity Act
* essential and important entities
* Annex 1 and Annex 2
* municipalities
* public administration
* size assessment
* jurisdiction
* registration

Main source types:

* NIS2 Directive
* Swedish cybersecurity implementation guidance
* MCF guidance where relevant

Source metadata status:

```text
Source date: Last checked: 2026-06-08
Status: Reviewed
```

---

## 14. Swedish Cybercrime and Dataintrång

**Local file:** `data/cybercrime_dataintrang.md`

**Topic:** Swedish cybercrime law and dataintrång.

Used for questions about:

* dataintrång
* unauthorized access
* obehörig åtkomst
* illegal access in Sweden
* account compromise
* permission and scope in security testing
* Swedish criminal-law context for cybercrime

Main source type:

* Swedish legal source

Source metadata status:

```text
Source date: Last checked: 2026-06-03
Status: Reviewed
```

---

## Source Audit

CyberLex Sweden includes a local source audit script:

```text
scripts/source_audit.py
```

The script checks source files in:

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

The script generates:

```text
docs/source_audit_report.md
```

Current audit result:

```text
Files marked OK: 12
Files needing review: 1
```

Important limitation:

The source audit does not browse the web and does not verify whether the law is currently up to date.

It only checks that the local project files contain the required source structure.

---

## Weekly Source Audit Workflow

CyberLex Sweden includes a GitHub Actions workflow:

```text
.github/workflows/source-audit.yml
```

The workflow can be run manually and is scheduled to run weekly.

It runs:

```powershell
python scripts/source_audit.py
```

Then updates:

```text
docs/source_audit_report.md
```

if needed.

This workflow is a source-structure audit, not a live legal-currentness audit.

---

## Source Review Requirements

Before a source file is used for CyberLex Sweden answers, it should have:

* a clear topic
* a main authority or legal source
* a key idea
* important points
* cybersecurity or practical connection
* useful questions
* official source links
* source metadata
* source date
* version notes
* disclaimer

If any of these are missing, the source should be marked for review.

---

## Future Source Handling

Future versions of CyberLex Sweden may improve source handling by adding:

* source categories
* source owners or reviewers
* stronger source status values
* source update reminders
* automated link checks
* source retirement rules
* separate review dates for each official source link
* live legal update review workflow
* source-to-chunk metadata for future vector search or RAG

---

## Current Limitation

This source list describes the local source structure and trusted source categories for the CyberLex Sweden educational prototype.

It does not prove that every legal source is currently up to date.

For important legal, compliance, regulatory, or incident-response decisions, users should check official sources and qualified professional advice.

CyberLex Sweden remains an educational project, not a legal authority.
