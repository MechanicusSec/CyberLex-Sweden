# Project Overview: CyberLex Sweden

## Project Name

CyberLex Sweden

## Current Prototype Version

CyberLex Sweden is currently at **prototype version 0.5**.

This version is a local Streamlit application with a styled answer layout, source-grounded responses, bilingual interface support, citation details, official source links, source metadata, source quality labels, source freshness labels, practical explanations, assessment checklists, source context cards, and an experimental AI search sidebar.

CyberLex Sweden is an educational prototype. It does **not** provide legal advice.

---

## Project Idea

CyberLex Sweden is an educational legal-tech and cybersecurity-law assistant focused on Swedish cybersecurity law, EU cybersecurity regulation, cybercrime, data protection, incident reporting, and digital compliance.

The project explores how a focused AI-style assistant can help users understand selected cyber law topics in a safer and more transparent way than a general chatbot.

The current version is still local and rule-based. It does not use a full language model, live web browsing, real vector search, ChromaDB, FAISS, or RAG yet.

Instead, it uses selected Markdown source files, source routing, keyword scoring, topic expansion, rule-based answer generation, and transparent source display.

---

## Problem

Cybersecurity law is difficult to understand because relevant information is spread across many different places, including:

- Swedish laws
- EU regulations and directives
- Swedish government agencies
- EU institutions
- cybersecurity authorities
- data protection authorities
- sector-specific compliance guidance
- official legal databases

This makes it difficult for students, IT workers, and small organizations to quickly understand which rules may apply after a cyber incident or in a digital compliance situation.

A general chatbot may answer confidently without showing clear legal sources. That is risky for legal and cybersecurity topics.

CyberLex Sweden was created to test a more transparent approach: answers should be based on selected local source material, and users should be able to see which source file and source section supported the answer.

---

## Solution

CyberLex Sweden uses a trusted local Markdown knowledge base together with source-based search and rule-based answer generation.

The system is designed to:

- answer only from selected CyberLex source files
- show citation details for the matched source
- show official source links
- show source metadata and review dates
- show source quality and source freshness labels
- display practical explanations and assessment checklists
- refuse unsupported or out-of-scope questions
- support both English and Swedish interface text

The goal is not to replace official sources or legal professionals. The goal is to make selected cybersecurity-law information easier to search, inspect, and understand.

---

## Target Users

CyberLex Sweden is designed for:

- IT students
- cybersecurity students
- IT support staff
- small organizations
- people learning about Swedish cybersecurity law
- people learning about GDPR, NIS2, DORA, CRA, cybercrime, and incident reporting
- people who want a clearer overview of selected Swedish and EU digital compliance topics

---

## Supported Topic Areas

The current prototype supports source-based educational answers about:

- GDPR
- GDPR core principles
- personal data breaches
- IMY and Swedish GDPR supervision
- NIS2
- the Swedish Cybersecurity Act
- NIS2 incident reporting
- Swedish cybercrime law and dataintrång
- EU attacks against information systems
- EU Cyber Resilience Act
- DORA, the Digital Operational Resilience Act
- ransomware and cyber incident assessment
- digital compliance responsibilities
- overlap between GDPR, NIS2, DORA, CRA, and cybercrime rules

---

## Current Knowledge Base

The current local knowledge base is stored in the `data/` folder.

Current source files:

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

Each source file should include structured sections such as:

- topic
- main authority or legal source
- key idea
- important points
- practical or cybersecurity connection
- useful questions
- official source links
- source metadata
- disclaimer

Most sources now also include Swedish summaries or Swedish useful questions to improve Swedish retrieval and bilingual support.

---

## Current Application Features

The current CyberLex Sweden prototype can:

- load local Markdown source files from `data/`
- split documents into searchable sections
- match user questions against relevant source sections
- route clear topic questions to the correct source file
- expand question terms with related cyber/legal terminology
- generate simple source-based answers
- show detected topic labels
- show citation details
- show source quality labels
- show source freshness labels
- show source match confidence
- show official source links
- show source metadata
- show important legal limitations
- generate practical explanations
- generate topic-based assessment checklists
- show relevant source context
- show other matching source sections
- refuse questions outside the project scope
- support English and Swedish interface modes
- provide clickable example questions
- display an experimental AI search sidebar

---

## Experimental AI Search

CyberLex Sweden includes an experimental retrieval module in:

```text
app/vector_search.py
```

Despite the name, this module does **not** currently use true vector embeddings. It is still rule-based.

It currently uses:

- Markdown source loading
- heading-based chunking
- keyword matching
- useful-section boosts
- weak-section penalties
- topic-specific routing rules
- source-specific boosts and penalties

The experimental search is shown in the Streamlit sidebar. It helps test retrieval ranking before any future vector search or RAG system is connected to the main answer flow.

A real vector search attempt was started, but paused because the local Python environment used Python 3.14, which caused compatibility problems with AI package dependencies. The vector search plan remains documented for future work.

---

## Completed Swedish Retrieval Improvements

The experimental retrieval logic has been improved so Swedish questions route to more accurate local source files.

Examples:

| Topic | Example question | Expected source |
|---|---|---|
| NIS2 law | `Vad är NIS2?` | `nis2_cybersecurity_law.md` |
| Swedish Cybersecurity Act | `Vad är cybersäkerhetslagen?` | `nis2_cybersecurity_law.md` |
| NIS2 risk management | `Vad betyder riskhantering enligt NIS2?` | `nis2_cybersecurity_law.md` |
| Ransomware | `Vad ska ett företag göra efter en ransomwareattack?` | `nis2_incident_reporting.md` |
| GDPR breach | `Vad ska ett företag göra efter en personuppgiftsincident?` | `gdpr_personal_data_breach.md` |
| IMY | `Vad är IMY?` | `imy_gdpr_supervision.md` |
| GDPR principles | `Vilka är GDPR-principerna?` | `gdpr_core_principles.md` |
| Dataintrång | `Vad är dataintrång?` | `cybercrime_dataintrang.md` |
| DORA | `Vad är DORA?` | `eu_dora_digital_operational_resilience.md` |
| Cyber Resilience Act | `Vad betyder cybersäkerhetskrav för digitala produkter?` | `eu_cyber_resilience_act.md` |
| EU attacks against information systems | `Vad säger EU om attacker mot informationssystem?` | `eu_attacks_against_information_systems.md` |
| EU illegal access | `Vad är olaglig åtkomst enligt EU-regler?` | `eu_attacks_against_information_systems.md` |
| EU DDoS rules | `Vad säger EU om DDoS-attacker?` | `eu_attacks_against_information_systems.md` |

These improvements help CyberLex Sweden separate similar but legally different topics.

For example:

- NIS2 questions should not steal CRA product-security questions.
- EU cybercrime questions should not be confused with direct Swedish dataintrång questions.
- DORA financial-sector resilience questions should not be treated as general NIS2 questions.
- GDPR breach questions should not be confused with general IMY authority questions.

---

## Source Audit System

CyberLex Sweden includes a local source audit system.

The audit script is:

```text
scripts/source_audit.py
```

It checks local Markdown source files for:

- official source sections
- official source links
- source metadata sections
- source dates
- source freshness
- version notes

The audit report is written to:

```text
docs/source_audit_report.md
```

The current goal is:

```text
Files marked OK: 9
Files needing review: 0
```

Important limitation: the audit does not browse the web and does not verify live legal currency. It only checks the structure and review metadata of local project files.

---

## GitHub Actions Audit

CyberLex Sweden includes a weekly GitHub Actions source audit workflow:

```text
.github/workflows/source-audit.yml
```

The workflow can run automatically each week or manually from GitHub Actions.

It:

1. checks out the repository
2. sets up Python
3. runs `python scripts/source_audit.py`
4. updates `docs/source_audit_report.md`
5. commits the updated report if changes are found

This helps keep the source audit report current, but it does not replace real legal review.

---

## Example Questions

Example questions CyberLex Sweden should be able to handle include:

### English

```text
What is IMY?
What is NIS2?
What is DORA?
What is the Cyber Resilience Act?
What are the GDPR principles?
When must a personal data breach be reported?
Is unauthorized access illegal in Sweden?
What should a company do after a ransomware attack?
Can an incident need to be reported under both NIS2 and GDPR?
What does EU law say about attacks against information systems?
```

### Swedish

```text
Vad är IMY?
Vad är NIS2?
Vad är DORA?
Vad är Cyber Resilience Act?
Vad är dataintrång?
Vilka är GDPR-principerna?
När måste en personuppgiftsincident rapporteras?
Vad ska ett företag göra efter en ransomwareattack?
Vad betyder cybersäkerhetskrav för digitala produkter?
Vad säger EU om attacker mot informationssystem?
```

---

## Out-of-Scope Questions

CyberLex Sweden should refuse questions that are not related to Swedish or EU cybersecurity law, data protection, cybercrime, incident reporting, or digital compliance.

Examples of out-of-scope topics:

- Swedish tax law
- family law
- general criminal law outside cybercrime
- medical advice
- investment advice
- unrelated political topics
- general trivia

The refusal should explain that the question is outside the CyberLex Sweden project scope.

---

## Limitations

CyberLex Sweden is an educational prototype.

Current limitations include:

- it does not provide legal advice
- it only covers selected topics
- it uses simplified educational source summaries
- it does not browse the web live
- it does not verify current legal updates online
- it does not yet use real vector search
- it does not yet use a full language model
- it does not yet use RAG answer generation
- the experimental AI search is still rule-based
- source material must be manually reviewed and updated
- public deployment would require stronger privacy, security, and legal review

For serious legal or compliance matters, users should check official sources or contact a qualified legal professional.

---

## Future Development

Planned future improvements include:

- adding more Swedish and EU cybersecurity-law sources
- improving Swedish source summaries
- installing Python 3.12 or 3.11 before retrying real vector search
- adding vector search with ChromaDB or FAISS
- adding sentence-transformer embeddings for source chunks
- comparing keyword/rule-based search with vector search
- adding future RAG answer generation
- improving citation formatting and multi-source synthesis
- improving visual design
- preparing public deployment
- strengthening legal disclaimer, privacy policy, and terms of use
- reviewing possible trademark and brand protection if the project develops further

The current design principle remains:

```text
Better sources first. Better AI second.
```

---

## Summary

CyberLex Sweden has developed from a basic local search prototype into a more structured source-grounded legal-tech and cybersecurity-law assistant.

The current prototype includes a local Streamlit app, Markdown knowledge base, citation details, official source links, source metadata, source quality labels, source freshness labels, practical explanations, assessment checklists, bilingual interface support, experimental retrieval testing, source audit scripts, GitHub Actions audit automation, and updated project documentation.

The next major technical step is real vector search, but that should be retried later with a more compatible Python version.

For now, the project has a strong foundation as a transparent educational prototype for selected Swedish and EU cybersecurity-law topics.
