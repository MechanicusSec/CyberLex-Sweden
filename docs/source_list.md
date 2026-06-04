# CyberLex Sweden Source List

## Purpose

This document lists the trusted source areas and local knowledge files used by CyberLex Sweden.

CyberLex Sweden should only answer legal and cybersecurity questions from selected trusted source material. The system should avoid guessing, unsupported legal claims, and answers outside the project scope.

This source list supports:

- source transparency
- source review
- knowledge base maintenance
- source audit checks
- future vector search or RAG development
- project documentation and final reporting

CyberLex Sweden is an educational prototype. It does not provide legal advice.

---

## Source categories

CyberLex Sweden uses source material from these categories:

- Swedish law
- EU law and regulations
- Swedish government agencies
- cybersecurity authorities
- data protection authorities
- police and cybercrime information
- financial-sector digital resilience sources
- product cybersecurity regulation sources

Trusted sources should normally come from official legal databases, official authority websites, or recognized EU institutions.

---

## Local knowledge base files

CyberLex Sweden currently uses these Markdown knowledge files in the `data/` folder:

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

Each file should include:

- `## Topic`
- `## Main authority` or `## Main legal source`
- `## Key idea`
- `## Important points`
- cybersecurity or practical connection
- useful questions
- `## Official source`
- `## Source metadata`
- disclaimer

The current source audit target is:

```text
Files marked OK: 9
Files needing review: 0
```

---

## Source file overview

| Local file | Main topic | Main source type | Status |
|---|---|---|---|
| `data/cybercrime_dataintrang.md` | Swedish cybercrime and dataintrång | Swedish legal source | Reviewed |
| `data/eu_attacks_against_information_systems.md` | EU attacks against information systems | EU directive | Reviewed |
| `data/eu_cyber_resilience_act.md` | Cyber Resilience Act | EU regulation | Reviewed |
| `data/eu_dora_digital_operational_resilience.md` | DORA and digital operational resilience | EU regulation | Reviewed |
| `data/gdpr_core_principles.md` | GDPR core principles | EU regulation | Reviewed |
| `data/gdpr_personal_data_breach.md` | GDPR personal data breach notification | EU regulation and IMY guidance | Reviewed |
| `data/imy_gdpr_supervision.md` | IMY and Swedish GDPR supervision | Swedish authority source | Reviewed |
| `data/nis2_cybersecurity_law.md` | NIS2 and Swedish cybersecurity law | EU directive and Swedish authority guidance | Reviewed |
| `data/nis2_incident_reporting.md` | NIS2 incident reporting | EU directive and Swedish authority guidance | Reviewed |

---

## 1. Swedish legal sources

### Sveriges Riksdag

Website: https://www.riksdagen.se

Purpose:

Sveriges Riksdag provides official Swedish laws and legal documents.

Relevant areas:

- Brottsbalken
- Swedish criminal law
- dataintrång
- unauthorized access
- cybercrime-related offences
- laws related to electronic communication
- laws related to national security and preparedness

Why this source is trusted:

The Riksdag website is an official source for Swedish legislation.

Used in CyberLex Sweden for:

```text
data/cybercrime_dataintrang.md
```

---

## 2. Swedish data protection authority

### IMY - Integritetsskyddsmyndigheten

Website: https://www.imy.se

Purpose:

IMY is the Swedish Authority for Privacy Protection.

Relevant areas:

- GDPR
- personal data breaches
- personal data breach notification
- data protection responsibilities
- incident notification
- data controller and processor responsibilities
- Swedish GDPR supervision

Why this source is trusted:

IMY is the official Swedish authority responsible for supervising data protection and GDPR compliance in Sweden.

Used in CyberLex Sweden for:

```text
data/imy_gdpr_supervision.md
data/gdpr_personal_data_breach.md
```

---

## 3. Swedish cybersecurity and civil preparedness

### MSB - Myndigheten för samhällsskydd och beredskap

Website: https://www.msb.se

Purpose:

MSB provides guidance on cybersecurity, information security, incident reporting, NIS, and NIS2-related cybersecurity requirements.

Relevant areas:

- cybersecurity requirements
- NIS and NIS2
- Swedish Cybersecurity Act topics
- incident reporting
- information security
- societal resilience and preparedness

Why this source is trusted:

MSB is a Swedish government authority responsible for civil protection, preparedness, and parts of national cybersecurity coordination.

Used in CyberLex Sweden for:

```text
data/nis2_cybersecurity_law.md
data/nis2_incident_reporting.md
```

---

## 4. EU legal sources

### EUR-Lex

Website: https://eur-lex.europa.eu

Purpose:

EUR-Lex provides official access to European Union law.

Relevant areas:

- GDPR
- NIS2 Directive
- Cyber Resilience Act
- DORA
- Directive 2013/40/EU on attacks against information systems
- EU cybersecurity and data protection rules

Why this source is trusted:

EUR-Lex is the official EU legal database.

Used in CyberLex Sweden for:

```text
data/gdpr_core_principles.md
data/gdpr_personal_data_breach.md
data/nis2_cybersecurity_law.md
data/nis2_incident_reporting.md
data/eu_attacks_against_information_systems.md
data/eu_cyber_resilience_act.md
data/eu_dora_digital_operational_resilience.md
```

---

## 5. European data protection sources

### European Data Protection Board

Website: https://www.edpb.europa.eu

Purpose:

The European Data Protection Board provides guidance and interpretation related to GDPR.

Relevant areas:

- GDPR guidance
- data protection principles
- personal data breach guidance
- cross-border data protection issues
- controller and processor responsibilities

Why this source is trusted:

The EDPB provides official European-level guidance on data protection law.

Current use:

EDPB material may be used for future expansion. The current prototype mainly relies on EUR-Lex GDPR material and IMY guidance for the existing GDPR source files.

---

## 6. Swedish Police

### Polisen

Website: https://polisen.se

Purpose:

The Swedish Police provides information about cybercrime, reporting crime, fraud, and digital threats.

Relevant areas:

- reporting cybercrime
- fraud
- unauthorized access
- online threats
- digital criminal activity

Why this source is trusted:

Polisen is the official Swedish police authority.

Current use:

Polisen may be used for future expansion. The current Swedish cybercrime source mainly relies on Swedish legal material and educational explanation of dataintrång.

---

## 7. EU DORA: Digital Operational Resilience Act

**Local file:** `data/eu_dora_digital_operational_resilience.md`

**Topic:** Digital operational resilience and cybersecurity requirements for the EU financial sector.

**Main legal source:** Regulation (EU) 2022/2554, Digital Operational Resilience Act.

Used for questions about:

- DORA
- Digital Operational Resilience Act
- digital operational resilience
- financial-sector cybersecurity
- ICT risk management
- ICT-related incident reporting
- ICT third-party risk
- resilience testing
- relationship between DORA, NIS2, and GDPR

Official source examples:

- EUR-Lex Regulation (EU) 2022/2554
- European Commission DORA information
- European Banking Authority DORA information
- EIOPA DORA information
- ESMA DORA information

Source metadata status:

```text
Source date: Last checked: 2026-06-03
Status: Reviewed
```

---

## 8. EU Cyber Resilience Act

**Local file:** `data/eu_cyber_resilience_act.md`

**Topic:** Cybersecurity requirements for products with digital elements.

**Main legal source:** Regulation (EU) 2024/2847, Cyber Resilience Act.

Used for questions about:

- Cyber Resilience Act
- CRA
- products with digital elements
- product cybersecurity
- cybersecurity by design
- vulnerability handling
- security updates
- manufacturers, importers, and distributors
- relationship between CRA, NIS2, GDPR, and DORA

Official source examples:

- EUR-Lex Regulation (EU) 2024/2847
- European Commission Cyber Resilience Act information
- European Commission CRA implementation information

Source metadata status:

```text
Source date: Last checked: 2026-06-03
Status: Reviewed
```

---

## 9. EU attacks against information systems

**Local file:** `data/eu_attacks_against_information_systems.md`

**Topic:** EU cybercrime rules on attacks against information systems.

**Main legal source:** Directive 2013/40/EU on attacks against information systems.

Used for questions about:

- attacks against information systems
- illegal access under EU cybercrime rules
- illegal system interference
- illegal data interference
- illegal interception
- misuse of tools
- botnets
- DDoS attacks
- relationship with Swedish dataintrång

Official source examples:

- EUR-Lex Directive 2013/40/EU
- EUR-Lex summary on attacks against information systems

Source metadata status:

```text
Source date: Last checked: 2026-06-03
Status: Reviewed
```

---

## 10. GDPR and personal data protection

### GDPR core principles

**Local file:** `data/gdpr_core_principles.md`

**Topic:** Core GDPR principles.

Used for questions about:

- GDPR principles
- lawfulness, fairness, and transparency
- purpose limitation
- data minimisation
- accuracy
- storage limitation
- integrity and confidentiality
- accountability

Main legal source:

- Regulation (EU) 2016/679, General Data Protection Regulation

Source metadata status:

```text
Source date: Last checked: 2026-06-03
Status: Reviewed
```

### GDPR personal data breach notification

**Local file:** `data/gdpr_personal_data_breach.md`

**Topic:** Personal data breach notification and IMY reporting.

Used for questions about:

- personal data breaches
- personuppgiftsincident
- 72-hour reporting
- breach notification to IMY
- affected individuals
- GDPR and cyber incidents

Main source types:

- GDPR
- IMY guidance

Source metadata status:

```text
Source date: Last checked: 2026-06-03
Status: Reviewed
```

### IMY GDPR supervision

**Local file:** `data/imy_gdpr_supervision.md`

**Topic:** IMY and Swedish GDPR supervision.

Used for questions about:

- IMY
- Swedish GDPR authority
- data protection supervision
- privacy protection authority
- complaints and supervision

Main source type:

- Swedish authority source

Source metadata status:

```text
Source date: Last checked: 2026-06-03
Status: Reviewed
```

---

## 11. NIS2 and Swedish cybersecurity law

### NIS2 cybersecurity law

**Local file:** `data/nis2_cybersecurity_law.md`

**Topic:** NIS2 and the Swedish Cybersecurity Act.

Used for questions about:

- NIS2
- cybersäkerhetslagen
- cybersecurity risk management
- security measures
- covered organizations
- management responsibility
- supply chain security
- relationship with GDPR and DORA

Main source types:

- NIS2 Directive
- MSB guidance
- Swedish cybersecurity law material

Source metadata status:

```text
Source date: Last checked: 2026-06-03
Status: Reviewed
```

### NIS2 incident reporting

**Local file:** `data/nis2_incident_reporting.md`

**Topic:** Incident reporting under NIS2 and Swedish cybersecurity rules.

Used for questions about:

- NIS2 incident reporting
- cybersecurity incident reporting
- ransomware attacks
- malware incidents
- incident assessment
- evidence preservation
- logs and timelines
- overlap with GDPR personal data breach reporting

Main source types:

- NIS2 Directive
- MSB guidance
- Swedish cybersecurity law material

Source metadata status:

```text
Source date: Last checked: 2026-06-03
Status: Reviewed
```

---

## 12. Swedish cybercrime and dataintrång

**Local file:** `data/cybercrime_dataintrang.md`

**Topic:** Swedish cybercrime law and dataintrång.

Used for questions about:

- dataintrång
- unauthorized access
- obehörig åtkomst
- illegal access in Sweden
- account compromise
- permission and scope in security testing
- Swedish criminal-law context for cybercrime

Main source type:

- Swedish legal source

Source metadata status:

```text
Source date: Last checked: 2026-06-03
Status: Reviewed
```

---

## Source audit

CyberLex Sweden includes a local source audit script:

```text
scripts/source_audit.py
```

The script checks source files in:

```text
data/
```

It checks for:

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

Current expected audit result:

```text
Files marked OK: 9
Files needing review: 0
```

Important limitation:

The source audit does not browse the web and does not verify whether the law is currently up to date.

It only checks that the local project files contain the required source structure.

---

## Weekly source audit workflow

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

## Source review requirements

Before a source file is used for CyberLex Sweden answers, it should have:

- a clear topic
- a main authority or legal source
- a key idea
- important points
- cybersecurity or practical connection
- useful questions
- official source links
- source metadata
- source date
- version notes
- disclaimer

If any of these are missing, the source should be marked for review.

---

## Future source handling

Future versions of CyberLex Sweden may improve source handling by adding:

- source categories
- source owners or reviewers
- stronger source status values
- source update reminders
- automated link checks
- source retirement rules
- separate review dates for each official source link
- live legal update review workflow
- source-to-chunk metadata for future vector search or RAG

---

## Current limitation

This source list describes the local source structure and trusted source categories for the CyberLex Sweden educational prototype.

It does not prove that every legal source is currently up to date.

For important decisions, official sources and qualified legal advice should always be checked.
