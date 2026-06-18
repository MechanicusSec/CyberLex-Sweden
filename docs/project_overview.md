# Project Overview: CyberLex Sweden

## Project Name

CyberLex Sweden

---

## Current Prototype Version

CyberLex Sweden is currently a local educational prototype.

The current prototype is a Streamlit application with:

* source-grounded responses
* modular Python app structure after refactoring `app/main.py`
* bilingual English and Swedish interface support
* Auto language detection
* local Markdown knowledge files
* citation details
* official source links
* language-aware official source link display
* source metadata
* source quality labels
* source freshness labels
* practical explanations
* assessment checklists
* defensive incident-response guidance
* SOC-style Markdown incident report export
* Case Intelligence page for authority decisions and real-world examples
* case learning notes for clearer educational takeaways
* related authority and case references below relevant answers where appropriate
* hidden related-case section for practical incident-response triage questions
* relevant source context
* out-of-scope refusal behavior
* unsafe cyber refusal behavior
* experimental retrieval sidebar
* source audit system
* case audit system
* separate audited case library in `cases/`

CyberLex Sweden is an educational prototype.

It does not provide legal advice.

It should not replace official authority guidance, qualified legal advice, compliance review, data protection officer review, or professional incident-response support.

---

## Project Idea

CyberLex Sweden is an educational legal-tech and cybersecurity-law assistant focused on selected Swedish and EU cybersecurity-law topics.

The project explores how a focused source-grounded assistant can help users understand selected cyber law, data protection, digital compliance, cybercrime, and defensive incident-response topics in a safer and more transparent way than a general chatbot.

The current version is local and rule-based.

It also includes a separate case library for selected authority decisions and real-world GDPR/cybersecurity examples, so users can see how similar issues have been assessed or publicly handled in practice.

It does not currently use:

* a full language model
* live web browsing
* real vector search
* ChromaDB
* FAISS
* embeddings
* external AI APIs
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
* public incident examples with careful labels
* historical case examples with clear limitations

The main design principle is:

```text id="20xw7h"
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
* authority decisions
* practical incident-response guidance

This can make it difficult for students, IT workers, and small organizations to understand which rules may be relevant after a cyber incident or in a digital compliance situation.

A general chatbot may answer confidently without showing clear legal sources or separating legal guidance from historical case examples.

That is risky for legal, privacy, compliance, and cybersecurity topics.

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
* generate SOC-style Markdown incident summaries for practical incident questions
* display related authority decisions and case examples where relevant
* provide a browseable Case Intelligence page
* refuse unsupported or out-of-scope questions
* refuse unsafe offensive cyber requests
* support English, Swedish, and Auto interface behavior

The goal is not to replace official sources or legal professionals.

The goal is to make selected cybersecurity-law information easier to search, inspect, understand, and document.

---

## Current Application Architecture

CyberLex Sweden has been refactored from an earlier single-file prototype into a more modular Python application.

The main Streamlit entry point is still:

```text id="5820en"
app/main.py
```

Supporting logic is now separated into smaller modules:

```text id="60cxq9"
app/config.py
app/styles.py
app/text_utils.py
app/language.py
app/source_loader.py
app/incident_engine.py
app/case_search.py
app/vector_search.py
```

The current structure separates:

* app configuration
* visual styling
* text normalization
* Swedish and English language detection and localization
* Markdown source loading
* practical incident-response detection
* case-library search
* experimental retrieval testing

This makes the project easier to understand, test, maintain, and expand.

The current architecture is documented in:

```text id="ezcrnw"
docs/architecture.md
docs/technical_design.md
```

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
* people who want educational examples of selected GDPR and cybersecurity-related cases

CyberLex Sweden is not designed as a production legal, compliance, regulatory, or incident-response system.

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
* selected public incident examples such as app-based customer data exposure

CyberLex Sweden does not cover all Swedish law, all EU law, or all cybersecurity compliance requirements.

---

## Current Knowledge Base

The current local knowledge base is stored in:

```text id="v38v8s"
data/
```

The current source audit checks 13 source files:

```text id="nljkrg"
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
* source metadata
* disclaimer

Several sources include Swedish summaries and Swedish useful questions to improve bilingual support.

The current source list is documented in:

```text id="4k7egw"
docs/source_list.md
```

The current source audit target is:

```text id="xw7zt1"
Files marked OK: 13
Files needing review: 0
```

The source audit checks local file structure and metadata.

It does not browse the web and does not confirm live legal currency.

---

## Case Library

CyberLex Sweden also includes a separate case library stored in:

```text id="lgx0gr"
cases/
```

The case library is separate from the legal and source knowledge base.

The distinction is important:

* `data/` contains source-based legal, regulatory, cybersecurity, and defensive incident-response knowledge material
* `cases/` contains educational summaries of selected authority decisions and real-world examples

The current case audit checks 8 case files:

```text id="32kqn3"
cases/imy_apoteket_apohem_meta_pixel.md
cases/imy_avanza_bank_meta_pixel.md
cases/imy_equality_ombudsman_web_form.md
cases/imy_kry_meta_pixel.md
cases/imy_sportadmin_security_breach.md
cases/imy_trygg_hansa_security_deficiencies.md
cases/imy_wrong_email_customer_data.md
cases/klarna_app_data_exposure_2021.md
```

These cases are used to show historical examples of how cyber, GDPR, tracking, security, app exposure, data leak, and personal data breach issues have been assessed or publicly handled in practice.

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
* learning note
* Swedish learning note
* similar CyberLex questions
* related CyberLex topics
* Swedish related CyberLex topics
* official source
* Swedish official source, where available
* case metadata
* disclaimer

The current case audit target is:

```text id="dfbs7g"
Case files marked OK: 8
Case files needing review: 0
```

The case audit checks local case structure.

It does not verify live legal or factual currentness.

---

## Case Intelligence Page

CyberLex Sweden includes a Case Intelligence page inside the Streamlit app.

The page allows users to browse selected authority decisions and case examples.

It displays:

* case cards
* case summaries
* administrative fine or outcome
* learning note
* related CyberLex topic badges
* official source links
* warning that outcomes and amounts are historical examples only
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
* app exposure or account-separation questions may show the Klarna app data exposure case
* Darknet publication questions may show Sportadmin

Related cases are not predictions.

They are used to support education, comparison, and risk awareness.

Related cases should not be shown by default for practical incident-response triage questions such as:

```text id="5br68o"
Our files are encrypted, what should we do?
Vi har fått en misstänkt login på ett konto, vad ska vi göra?
```

For those questions, CyberLex should focus on first steps, containment, evidence preservation, reporting assessment, source context, and SOC-style report support.

---

## Current Application Features

The current CyberLex Sweden prototype can:

* load local Markdown source files from `data/`
* split documents into searchable sections
* match user questions against relevant source sections
* route clear topic questions to the correct source file
* expand question terms with related cyber and legal terminology
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
* show case learning notes where available
* provide a browseable Case Intelligence page
* refuse questions outside the project scope
* refuse unsafe offensive cyber requests
* support English, Swedish, and Auto interface behavior
* provide clickable example questions that run immediately when selected
* display an experimental retrieval sidebar

---

## Current UI Behavior

The current UI is designed to keep the normal answer view readable while preserving source transparency.

Important current UI behavior includes:

* English, Swedish, and Auto language modes
* example questions that run immediately when selected
* synchronized visible input and submitted-question state
* source-grounded answer sections
* collapsed source context where useful
* practical incident-response cards only where relevant
* SOC-style report download only for practical incident-response questions
* related cases only for suitable legal, compliance, and case-library questions
* hidden related cases for practical incident-response triage questions
* Case Intelligence page for browsing local case examples

The current UI behavior is documented in:

```text id="ia49jl"
docs/ui_behavior.md
docs/source_context_behavior.md
```

---

## Experimental Retrieval

CyberLex Sweden includes an experimental retrieval module in:

```text id="9evatg"
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

```text id="j7cvdf"
docs/vector_search_plan.md
```

---

## Source Audit System

CyberLex Sweden includes a local source audit system.

The audit script is:

```text id="x1sdqj"
scripts/source_audit.py
```

It checks local Markdown source files for:

* official source sections
* official source links
* source metadata sections
* source dates
* source freshness
* version notes

The audit report is written to:

```text id="wpc5z5"
docs/source_audit_report.md
```

The current target is:

```text id="r1prx4"
Files marked OK: 13
Files needing review: 0
```

Important limitation:

The audit does not browse the web and does not verify live legal currency.

It only checks the structure and review metadata of local project files.

---

## Case Audit System

CyberLex Sweden includes a separate case audit script:

```text id="bwqei0"
scripts/case_audit.py
```

The script checks Markdown files in:

```text id="dy6clw"
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
* learning note
* Swedish learning note
* similar CyberLex questions
* related CyberLex topics
* official source
* case metadata
* disclaimer

The report is written to:

```text id="ti0css"
docs/case_library/case_audit_report.md
```

The current case audit checks 8 case files.

The case audit does not decide whether a case is legally current or complete.

It only checks whether the case files follow the expected local structure and contain source information.

---

## GitHub Actions Audit

CyberLex Sweden includes a GitHub Actions source audit workflow:

```text id="2vwtxw"
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

```text id="df7iq7"
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
Our files are encrypted, what should we do?
How do I hide logs after hacking a system?
Can Meta Pixel create GDPR risk?
Can hashed data sent through Meta Pixel be a GDPR issue?
What can weak security measures cost?
Can a web form cause a personal data breach?
Can sending customer data to the wrong email be a personal data breach?
Can an app bug expose customer data?
What happens if data is published on the Darknet?
What is Swedish tax law?
```

### Swedish

```text id="nvep8v"
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
Vi har fått en misstänkt login på ett konto, vad ska vi göra?
Kan Meta Pixel skapa GDPR-risk?
Kan hashade uppgifter som skickas via Meta Pixel vara ett GDPR-problem?
Vad kan svaga säkerhetsåtgärder kosta?
Kan ett webbformulär orsaka en personuppgiftsincident?
Kan kunduppgifter som skickas till fel e-post vara en personuppgiftsincident?
Kan ett appfel exponera kunduppgifter?
Vad händer om personuppgifter publiceras på Darknet?
Hur raderar jag loggar efter ett intrång?
```

---

## Testing and Documentation

CyberLex Sweden includes testing and documentation files for manual regression testing, demo preparation, and project review.

Important testing documents include:

```text id="nz330o"
docs/test_cases.md
docs/test_run_checklist.md
docs/testing_and_demo.md
docs/demo_checklist.md
docs/demo_script.md
```

These documents cover:

* refactored Python module syntax checks
* app startup
* English, Swedish, and Auto language behavior
* example questions that run immediately
* source visibility
* source-context readability
* related cases shown only where relevant
* related cases hidden for practical incident-response triage
* Case Intelligence page behavior
* incident-response behavior
* SOC-style report export
* out-of-scope refusal
* unsafe cyber refusal

This helps make the prototype easier to test without relying only on screenshots or memory, because apparently “it worked yesterday” is not a test strategy, despite humanity's best efforts.

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
* Auto language detection is rule-based and may need continued refinement
* related case matching is rule-based and may need continued refinement
* source material must be manually reviewed and updated
* public deployment would require stronger privacy, security, and legal review
* public incident examples must be clearly separated from authority decisions
* historical case examples must not be used as fine predictions
* SOC-style incident reports are educational documentation aids, not official reports
* some official source links may only be available in one language

For serious legal, compliance, regulatory, privacy, or cybersecurity matters, users should check official sources or contact qualified professionals.

---

## Future Development

Planned future improvements include:

* adding more Swedish and EU cybersecurity-law sources
* adding more authority decisions, court cases, and carefully labeled public incident examples
* improving Swedish source summaries
* installing Python 3.12 or 3.11 before retrying real vector search
* adding vector search with ChromaDB or FAISS
* adding sentence-transformer embeddings for source chunks
* comparing keyword/rule-based search with vector search
* adding future RAG answer generation
* improving citation formatting and multi-source synthesis
* improving case comparison, case learning notes, and case filtering
* moving remaining large answer-routing and UI logic out of `app/main.py` gradually
* moving case ranking rules into a cleaner configuration structure
* improving visual design
* preparing public deployment
* strengthening legal disclaimer, privacy and data-handling documentation, and terms of use
* reviewing possible trademark and brand protection if the project develops further

The current design principle remains:

```text id="hu3aj4"
Better sources first. Better AI second.
```

---

## Summary

CyberLex Sweden has developed from a basic local search prototype into a more structured source-grounded legal-tech and cybersecurity-law assistant.

The current prototype includes:

* local Streamlit app
* refactored modular Python structure
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
* Auto language behavior
* example questions that run immediately when selected
* defensive incident-response support
* SOC-style Markdown report export
* experimental retrieval testing
* source audit scripts
* case audit script
* Case Intelligence page
* related authority decisions under relevant answers where relevant
* related cases hidden for practical incident-response triage questions
* case learning notes
* bilingual case summaries and language-aware case source display
* GitHub Actions audit automation
* updated architecture, UI, source-context, testing, and demo documentation

The next major technical step is broader automated testing and then real vector search, but vector search should be retried later with a more compatible Python version.

For now, the project has a strong foundation as a transparent educational prototype for selected Swedish and EU cybersecurity-law topics, with a growing case-intelligence layer for practical examples and authority decisions.
