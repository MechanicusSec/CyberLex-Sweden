# Project Overview: CyberLex Sweden

## Project Name

CyberLex Sweden

---

## Current Prototype Version

CyberLex Sweden is currently a local educational prototype.

The current prototype is a Streamlit application with:

* source-grounded responses
* bilingual English and Swedish interface support
* local Markdown knowledge files
* citation details
* official source links
* language-aware official source link display
* source metadata
* source quality labels
* source freshness labels
* practical explanations
* assessment checklists
* incident-response guidance
* SOC-style Markdown incident report export
* Case Intelligence page for authority decisions and real-world examples
* related authority/case references below relevant answers
* relevant source context
* out-of-scope refusal behavior
* unsafe cyber refusal behavior
* an experimental retrieval sidebar
* a separate audited case library in `cases/`

CyberLex Sweden is an educational prototype.

It does not provide legal advice.

---

## Project Idea

CyberLex Sweden is an educational legal-tech and cybersecurity-law assistant focused on selected Swedish and EU cybersecurity-law topics.

The project explores how a focused AI-style assistant can help users understand selected cyber law, data protection, digital compliance, cybercrime, and incident-response topics in a safer and more transparent way than a general chatbot.

The current version is local and rule-based. It also includes a separate case library for selected authority decisions and real-world GDPR/cybersecurity examples, so users can see how similar issues have been assessed in practice.

It does not currently use:

* a full language model
* live web browsing
* real vector search
* ChromaDB
* FAISS
* RAG answer generation

Instead, it uses:

* selected Markdown source files
* source routing
* keyword scoring
* topic expansion
* rule-based answer generation
* source metadata
* official source links
* transparent source display
* selected authority-decision summaries
* historical case examples with clear limitations

The main design principle is:

```text
Better sources first. Better AI second.
```

---

## Problem

Cybersecurity law is difficult to understand because relevant information is spread across many different places, including:

* Swedish laws
* EU regulations and directives
* Swedish government agencies
* EU institutions
* cybersecurity authorities
* data protection authorities
* sector-specific compliance guidance
* official legal databases

This can make it difficult for students, IT workers, and small organizations to understand which rules may be relevant after a cyber incident or in a digital compliance situation.

A general chatbot may answer confidently without showing clear legal sources or separating legal guidance from historical case examples.

That is risky for legal and cybersecurity topics.

CyberLex Sweden was created to test a more transparent approach: answers should be based on selected local source material, and users should be able to see which source file and source section supported the answer.

---

## Solution

CyberLex Sweden uses a trusted local Markdown knowledge base together with source-based search and rule-based answer generation.

The system is designed to:

* answer only from selected CyberLex source files
* show citation details for the matched source
* show official source links
* show language-aware official source links where possible
* show source metadata and review dates
* show source quality and source freshness labels
* display practical explanations and assessment checklists
* provide defensive incident-response support where relevant
* generate SOC-style Markdown incident summaries
* display related authority decisions and case examples where relevant
* provide a browseable Case Intelligence page
* refuse unsupported or out-of-scope questions
* refuse unsafe offensive cyber requests
* support both English and Swedish interface text

The goal is not to replace official sources or legal professionals.

The goal is to make selected cybersecurity-law information easier to search, inspect, understand, and document.

---

## Target Users

CyberLex Sweden is designed for:

* IT students
* cybersecurity students
* IT support staff
* small organizations
* people learning about Swedish cybersecurity law
* people learning about GDPR, NIS2, DORA, CRA, cybercrime, and incident reporting
* people who want a clearer overview of selected Swedish and EU digital compliance topics

---

## Supported Topic Areas

The current prototype supports source-based educational answers about selected material related to:

* GDPR
* GDPR core principles
* GDPR security measures
* personal data breaches
* IMY and Swedish GDPR supervision
* NIS2
* the Swedish Cybersecurity Act
* NIS2 sector scope and applicability
* NIS2 incident reporting
* Swedish cybercrime law and dataintrång
* EU attacks against information systems
* Cyber Resilience Act
* DORA, the Digital Operational Resilience Act
* ransomware and cyber incident assessment
* suspicious emails and phishing
* suspicious logins
* compromised accounts
* customer data leaks
* defensive cyber incident response
* overlap between GDPR, NIS2, DORA, CRA, and cybercrime topics
* selected IMY authority decisions about Meta Pixel, weak security, web forms, wrong email disclosures, Darknet publication, and administrative fines

CyberLex Sweden does not cover all Swedish law, all EU law, or all cybersecurity compliance requirements.

---

## Current Knowledge Base

The current local knowledge base is stored in:

```text
data/
```

The current source audit checks 13 source files:

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

Each source file should include structured sections such as:

* topic
* main authority or legal source
* key idea
* important points
* practical or cybersecurity connection
* useful questions
* official source links
* language-aware official source link display
* source metadata
* disclaimer

Several sources include Swedish summaries and Swedish useful questions to improve bilingual support.

The current source list is documented in:

```text
docs/source_list.md
```

---

## Case Library

CyberLex Sweden also includes a separate case library stored in:

```text
cases/
```

The case library is separate from the legal/source knowledge base.

The distinction is important:

* `data/` contains source-based legal and cybersecurity knowledge material
* `cases/` contains educational summaries of selected authority decisions and real-world examples

The current case library includes selected IMY-related cases such as:

```text
cases/imy_apoteket_apohem_meta_pixel.md
cases/imy_avanza_bank_meta_pixel.md
cases/imy_equality_ombudsman_web_form.md
cases/imy_kry_meta_pixel.md
cases/imy_sportadmin_security_breach.md
cases/imy_trygg_hansa_security_deficiencies.md
cases/imy_wrong_email_customer_data.md
```

These cases are used to show historical examples of how cyber, GDPR, tracking, security, data leak, and personal data breach issues have been assessed in practice.

CyberLex Sweden should not treat historical fine amounts as predictions.

Case examples are educational references only.

The case files include structured sections such as:

* case type
* jurisdiction
* year
* authority or court
* topic
* short summary
* Swedish short summary
* what happened
* legal issue
* decision or outcome
* fine or cost
* Swedish fine or cost
* why it matters for CyberLex
* similar CyberLex questions
* related CyberLex topics
* Swedish related CyberLex topics
* official source
* Swedish official source, where available
* case metadata
* disclaimer

---

## Case Intelligence Page

CyberLex Sweden includes a Case Intelligence page inside the Streamlit app.

The page allows users to browse selected authority decisions and case examples.

It displays:

* case cards
* case summaries
* administrative fine or outcome
* related CyberLex topic badges
* official source links
* a warning that outcomes and amounts are historical examples only
* filtering/search across case titles, summaries, outcomes, topics, and source links

The Case Intelligence page supports Swedish and English display logic.

When the interface is set to Swedish, the app prefers Swedish case sections and Swedish source labels where available.

When the interface is set to English, the app prefers English case sections and English source labels where available.

When the interface is set to Auto, the app can show broader available source information.

If a matching source language is missing, the app should still show an available official source rather than hiding sources completely.

---

## Related Cases in Answers

CyberLex Sweden can show related case references below normal answers.

This helps connect a general legal or cybersecurity question to historical examples.

Examples:

* Meta Pixel questions may show Apoteket/Apohem, Avanza, or Kry examples
* weak security questions may show Trygg-Hansa or Sportadmin examples
* web form questions may show the Equality Ombudsman case
* wrong email questions may show the wrong email customer data case
* Darknet publication questions may show Sportadmin

Related cases are not predictions.

They are used to support education, comparison, and risk awareness.


---

## Current Application Features

The current CyberLex Sweden prototype can:

* load local Markdown source files from `data/`
* split documents into searchable sections
* match user questions against relevant source sections
* route clear topic questions to the correct source file
* expand question terms with related cyber/legal terminology
* generate simple source-based answers
* show detected topic labels
* show citation details
* show source quality labels
* show source freshness labels
* show source match confidence
* show official source links
* show language-aware official source links where possible
* show source metadata
* show important legal limitations
* generate practical explanations
* generate topic-based assessment checklists
* show relevant source context
* show other matching source sections
* handle practical incident-response questions
* generate SOC-style Markdown incident summaries
* show related authority decisions and case examples
* provide a browseable Case Intelligence page
* refuse questions outside the project scope
* refuse unsafe offensive cyber requests
* support English and Swedish interface modes
* provide clickable example questions
* display an experimental retrieval sidebar

---

## Experimental Retrieval

CyberLex Sweden includes an experimental retrieval module in:

```text
app/vector_search.py
```

Despite the name, this module does not currently use true vector embeddings.

It is still rule-based.

It currently uses:

* Markdown source loading
* heading-based chunking
* keyword matching
* useful-section boosts
* weak-section penalties
* topic-specific routing rules
* source-specific boosts and penalties

The experimental retrieval sidebar helps test source ranking before any future vector search or RAG system is connected to the main answer flow.

A real vector search attempt was paused because the local Python environment used Python 3.14, which caused compatibility problems with AI package dependencies.

The vector search plan remains documented for future work in:

```text
docs/vector_search_plan.md
```

---

## Source Audit System

CyberLex Sweden includes a local source audit system.

The audit script is:

```text
scripts/source_audit.py
```

It checks local Markdown source files for:

* official source sections
* official source links
* language-aware official source link display
* source metadata sections
* source dates
* source freshness
* version notes

The audit report is written to:

```text
docs/source_audit_report.md
```

The current target is:

```text
Files marked OK: 13
Files needing review: 0
```

Important limitation:

The audit does not browse the web and does not verify live legal currency.

It only checks the structure and review metadata of local project files.

---

## Case Audit System

CyberLex Sweden includes a separate case audit script:

```text
scripts/case_audit.py
```

The script checks Markdown files in:

```text
cases/
```

It ignores template and index files and checks actual case files for required structure.

The case audit checks whether each case file has required sections such as:

* case type
* jurisdiction
* year
* authority or court
* topic
* short summary
* what happened
* legal issue
* decision or outcome
* fine or cost
* why it matters for CyberLex
* similar CyberLex questions
* related CyberLex topics
* official source
* case metadata
* disclaimer

The report is written to:

```text
docs/case_library/case_audit_report.md
```

The current case audit checks 7 case files.

The case audit does not decide whether a case is legally current or complete.

It only checks whether the case files follow the expected local structure and contain source information.

---

## GitHub Actions Audit

CyberLex Sweden includes a GitHub Actions source audit workflow:

```text
.github/workflows/source-audit.yml
```

The workflow can run automatically on a schedule or manually from GitHub Actions.

It:

1. checks out the repository
2. sets up Python
3. runs `python scripts/source_audit.py`
4. updates `docs/source_audit_report.md`
5. commits the updated report if changes are found

This helps keep the source audit report current.

It does not replace real legal review.

---

## Example Questions

Example questions CyberLex Sweden should be able to handle include:

### English

```text
What is CyberLex Sweden?
What is IMY?
What is NIS2?
Does NIS2 apply to us?
What are Annex 1 and Annex 2 in NIS2?
What is DORA?
What is the Cyber Resilience Act?
What are the GDPR principles?
Does GDPR require MFA?
When must a personal data breach be reported?
Is unauthorized access illegal in Sweden?
What should we do if we receive a suspicious email?
What should we do if an account is compromised?
Customer data may have leaked
Our files are encrypted
How do I hide logs after hacking a system?
Can Meta Pixel create GDPR risk?
Can hashed data sent through Meta Pixel be a GDPR issue?
What can weak security measures cost?
Can a web form cause a personal data breach?
Can sending customer data to the wrong email be a personal data breach?
What happens if data is published on the Darknet?
What is Swedish tax law?
```

### Swedish

```text
Vad är CyberLex Sweden?
Vad är IMY?
Vad är NIS2?
Gäller NIS2 för oss?
Vad är bilaga 1 och bilaga 2 i NIS2?
Vad är DORA?
Vad är Cyber Resilience Act?
Vad är dataintrång?
Vilka är GDPR-principerna?
Vad säger IMY om säkerhetsåtgärder?
När måste en personuppgiftsincident rapporteras?
Vad gör vi om vi ser misstänkt inloggning?
Kunddata kan ha läckt
Våra filer har krypterats
Kan Meta Pixel skapa GDPR-risk?
Kan hashade uppgifter som skickas via Meta Pixel vara ett GDPR-problem?
Vad kan svaga säkerhetsåtgärder kosta?
Kan ett webbformulär orsaka en personuppgiftsincident?
Kan kunduppgifter som skickas till fel e-post vara en personuppgiftsincident?
Vad händer om personuppgifter publiceras på Darknet?
Hur raderar jag loggar efter ett intrång?
```

---

## Out-of-Scope and Unsafe Questions

CyberLex Sweden should refuse questions that are not related to selected Swedish or EU cybersecurity law, data protection, cybercrime, incident reporting, or digital compliance.

Examples of out-of-scope topics:

* Swedish tax law
* family law
* medical advice
* investment advice
* unrelated political topics
* general trivia
* recipes

CyberLex Sweden should also refuse unsafe cyber requests, such as:

* hiding logs
* deleting traces
* stealing credentials
* bypassing detection
* exploiting systems without authorization
* maintaining unauthorized access
* malware deployment

The refusal should explain that the request is outside the CyberLex Sweden project scope or unsafe.

---

## Limitations

CyberLex Sweden is an educational prototype.

Current limitations include:

* it does not provide legal advice
* it only covers selected topics
* it uses simplified educational source summaries
* it does not browse the web live
* it does not verify current legal updates online
* it does not yet use real vector search
* it does not yet use a full language model
* it does not yet use RAG answer generation
* the experimental retrieval sidebar is still rule-based
* source material must be manually reviewed and updated
* public deployment would require stronger privacy, security, and legal review
* historical case examples must not be used as fine predictions
* some official source links may only be available in one language

For serious legal, compliance, regulatory, or cybersecurity matters, users should check official sources or contact qualified professionals.

---

## Future Development

Planned future improvements include:

* adding more Swedish and EU cybersecurity-law sources
* adding more authority decisions and court cases
* improving Swedish source summaries
* installing Python 3.12 or 3.11 before retrying real vector search
* adding vector search with ChromaDB or FAISS
* adding sentence-transformer embeddings for source chunks
* comparing keyword/rule-based search with vector search
* adding future RAG answer generation
* improving citation formatting and multi-source synthesis
* improving case comparison and case filtering
* moving case ranking rules into a cleaner configuration structure
* improving visual design
* preparing public deployment
* strengthening legal disclaimer, privacy policy, and terms of use
* reviewing possible trademark and brand protection if the project develops further

The current design principle remains:

```text
Better sources first. Better AI second.
```

---

## Summary

CyberLex Sweden has developed from a basic local search prototype into a more structured source-grounded legal-tech and cybersecurity-law assistant.

The current prototype includes:

* local Streamlit app
* Markdown knowledge base
* citation details
* official source links
* language-aware official source link display
* source metadata
* source quality labels
* source freshness labels
* practical explanations
* assessment checklists
* bilingual interface support
* defensive incident-response support
* SOC-style Markdown report export
* experimental retrieval testing
* source audit scripts
* case audit script
* Case Intelligence page
* related authority decisions under relevant answers
* bilingual case summaries and language-aware case source display
* GitHub Actions audit automation
* updated project documentation

The next major technical step is real vector search, but that should be retried later with a more compatible Python version.

For now, the project has a strong foundation as a transparent educational prototype for selected Swedish and EU cybersecurity-law topics, with a growing case-intelligence layer for practical examples and authority decisions.
