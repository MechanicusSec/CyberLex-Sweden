# Project Overview: CyberLex Sweden

## Project Name

CyberLex Sweden

---

## Current Prototype Version

CyberLex Sweden is a local educational prototype built as a Streamlit application.

The current version includes:

* source-grounded responses from local Markdown files
* bilingual Swedish and English support
* Auto language detection
* official source links and source metadata
* source quality and freshness labels
* defensive incident-response guidance
* SOC-style Markdown incident report export
* Case Intelligence page for selected cases and public incidents
* related case examples where relevant
* refusal behavior for unsafe cyber misuse and out-of-scope questions
* local source audit, source watch, and case audit scripts
* automated tests with `pytest`
* GitHub Actions workflows for tests, source audit, and source watch

CyberLex Sweden is an educational prototype.

It does **not** provide legal advice and should not replace official authority guidance, qualified legal review, compliance review, data protection officer review, or professional incident-response support.

---

## Project Idea

CyberLex Sweden is an educational legal-tech and cybersecurity-law assistant focused on selected Swedish and EU cybersecurity-law topics.

The project explores how a focused, source-grounded assistant can help users understand cyber law, data protection, digital compliance, cybercrime, and defensive incident-response topics in a safer and more transparent way than a general chatbot.

The current version is local and rule-based.

It does not currently use:

* a full language model
* live web browsing
* real vector search
* embeddings
* ChromaDB or FAISS
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
* structured case summaries
* clear limitations and disclaimers

Main design principle:

```text
Better sources first. Better AI second.
```

---

## Problem

Cybersecurity law is difficult to understand because relevant information is spread across many places:

* Swedish laws
* EU regulations and directives
* Swedish government agencies
* EU institutions
* cybersecurity authorities
* data protection authorities
* official legal databases
* authority decisions
* practical incident-response guidance

This can make it difficult for students, IT workers, and small organizations to understand what rules may apply after a cyber incident or in a digital compliance situation.

A general chatbot may answer confidently without showing clear legal sources or separating legal guidance from historical case examples.

CyberLex Sweden tests a more transparent approach: answers should be based on selected local source material, and users should be able to see which source file and source section supported the answer.

---

## Solution

CyberLex Sweden uses a trusted local Markdown knowledge base, a local case library, source-based search, and rule-based answer generation.

The system is designed to:

* answer from selected CyberLex source files
* show citation details for matched source sections
* show official source links
* show source metadata and review dates
* provide practical explanations and checklists where useful
* support defensive incident-response questions
* generate SOC-style Markdown incident summaries
* show related case examples where relevant
* provide a browseable Case Intelligence page
* refuse unsupported or out-of-scope questions
* refuse unsafe offensive cyber requests
* support English, Swedish, and Auto language behavior

The goal is not to replace official sources or legal professionals.

The goal is to make selected cybersecurity-law information easier to search, inspect, understand, and document.

---

## Target Users

CyberLex Sweden is designed for:

* IT students
* cybersecurity students
* IT support staff
* teachers and project reviewers
* people learning about Swedish cybersecurity law
* people learning about GDPR, NIS2, DORA, CRA, cybercrime, and incident reporting
* users who want educational examples of selected GDPR and cybersecurity-related cases

CyberLex Sweden is not designed as a production legal, compliance, regulatory, or incident-response system.

---

## Supported Topic Areas

The current prototype supports selected material related to:

* GDPR
* GDPR security measures
* personal data breaches
* IMY and Swedish GDPR supervision
* NIS2 and the Swedish Cybersecurity Act
* NIS2 sector scope and incident reporting
* Swedish cybercrime law and `dataintrång`
* EU attacks against information systems
* Cyber Resilience Act
* DORA
* suspicious emails and phishing
* suspicious logins
* compromised accounts
* customer data leaks
* ransomware and malware
* defensive cyber incident response
* selected IMY decisions and public incident examples

CyberLex Sweden does not cover all Swedish law, all EU law, or all cybersecurity compliance requirements.

---

## Current Knowledge Base

The local knowledge base is stored in:

```text
data/
```

The current source audit checks 13 source files.

The knowledge base includes material about:

* GDPR and personal data breaches
* IMY supervision and security measures
* NIS2 and incident reporting
* DORA
* Cyber Resilience Act
* cybercrime and unauthorized access
* EU attacks against information systems
* defensive incident response

Each source file is designed to include structured sections such as:

* topic
* main authority or legal source
* key idea
* important points
* practical explanation where useful
* useful questions
* official source links
* source metadata
* disclaimer or limitation notes

The current source list is documented in:

```text
docs/source_list.md
```

The source audit checks local file structure and metadata.

It does not browse the web and does not confirm live legal currency.

---

## Case Library

CyberLex Sweden includes a separate case library stored in:

```text
cases/
```

The distinction is important:

```text
data/
= legal, regulatory, cybersecurity, and defensive incident-response source material

cases/
= educational summaries of selected authority decisions and public incident examples
```

The case library includes examples involving:

* Meta Pixel and tracking technology
* security deficiencies
* wrong-email disclosure
* web-form security
* app-based customer data exposure
* large-scale data breaches
* Darknet publication
* administrative fines or outcomes where known

Case examples are educational references only.

CyberLex Sweden should not treat historical fine amounts as predictions.

---

## Case Intelligence Page

CyberLex Sweden includes a Case Intelligence page inside the Streamlit app.

The page allows users to browse selected authority decisions and public incident examples.

It can show:

* case cards
* case summaries
* administrative fine or outcome
* learning notes
* related topic badges
* official source links
* Swedish and English case sections where available
* warning that outcomes and amounts are historical examples only

The page helps users understand real-world examples without mixing them directly into the main legal knowledge base.

---

## Related Cases in Answers

CyberLex Sweden can show related case references below normal answers when relevant.

Examples:

* Meta Pixel questions may show Apoteket/Apohem, Avanza, or Kry examples
* weak security questions may show Trygg-Hansa or Sportadmin examples
* web-form questions may show the Equality Ombudsman case
* wrong-email questions may show the Indecap wrong-email case
* app exposure questions may show the Klarna app incident
* Darknet publication questions may show Sportadmin

Related cases are not predictions.

They are used for education, comparison, and risk awareness.

Related cases should normally be hidden for practical incident-response triage questions, where the answer should focus on first steps, containment, evidence preservation, reporting assessment, and SOC-style documentation.

---

## Current Application Architecture

CyberLex Sweden has been refactored from an earlier single-file prototype into a more modular Python application.

The main Streamlit entry point is:

```text
app/main.py
```

Important supporting modules include:

| File | Purpose |
| --- | --- |
| `app/config.py` | App settings, constants, and folder paths |
| `app/styles.py` | CSS and visual styling |
| `app/text_utils.py` | Text normalization and phrase-matching helpers |
| `app/language.py` | Swedish and English detection and localization |
| `app/source_loader.py` | Markdown source loading and chunking |
| `app/source_context.py` | Source-context cleaning and display helpers |
| `app/incident_engine.py` | Practical incident-response detection |
| `app/incident_reports.py` | SOC-style incident report generation |
| `app/routing.py` | Question routing, source targeting, and safety behavior |
| `app/case_search.py` | Related case and incident-example search |
| `app/vector_search.py` | Experimental rule-based retrieval module |

More detail is documented in:

```text
docs/architecture.md
docs/technical_design.md
```

---

## Current Application Features

The current prototype can:

* load local Markdown source files from `data/`
* search and match relevant source sections
* route clear topic questions to stronger source files
* generate simple source-based answers
* show detected topic labels
* show citation details
* show official source links
* show source metadata
* show source quality and freshness labels
* show relevant source context
* handle practical incident-response questions
* generate SOC-style Markdown incident summaries
* show related authority decisions and case examples
* provide a browseable Case Intelligence page
* refuse out-of-scope questions
* refuse unsafe offensive cyber requests
* support English, Swedish, and Auto language behavior
* provide clickable example questions

---

## Current UI Behavior

The UI is designed to keep answers readable while preserving source transparency.

Current UI behavior includes:

* English, Swedish, and Auto language modes
* example questions that run immediately when selected
* source-grounded answer sections
* collapsed source context where useful
* practical incident-response cards where relevant
* SOC-style report download for practical incident-response questions
* related cases for suitable legal, compliance, and case-library questions
* hidden related cases for practical incident-response triage questions
* Case Intelligence page for local case examples

More detail is documented in:

```text
docs/ui_behavior.md
docs/source_context_behavior.md
```

---

## Experimental Retrieval

CyberLex Sweden includes an experimental retrieval module:

```text
app/vector_search.py
```

Despite the name, it does not currently use true vector embeddings.

It is still rule-based and uses:

* Markdown source loading
* heading-based chunking
* keyword matching
* useful-section boosts
* weak-section penalties
* topic-specific routing rules
* source-specific boosts and penalties

The vector search plan remains documented for future work in:

```text
docs/vector_search_plan.md
```

---

## Source, Case, and Test Automation

CyberLex Sweden includes local scripts for checking project quality.

Source audit:

```text
scripts/source_audit.py
```

Checks structure and metadata in `data/`.

Source watch:

```text
scripts/source_watch.py
```

Checks official URLs and writes source-watch reports.

Case audit:

```text
scripts/case_audit.py
```

Checks structure and source information in `cases/`.

Automated tests are stored in:

```text
tests/
```

They currently cover:

* incident-response detection
* ransomware and encrypted-file detection
* suspicious login detection
* suspicious email and link detection
* compromised-account detection
* customer data leak detection
* Swedish and English language detection
* routing behavior
* unsafe and out-of-scope handling
* SOC incident report generation
* source-context helper behavior

GitHub Actions workflows are stored in:

```text
.github/workflows/
```

Current workflows include:

* `tests.yml`
* `source-audit.yml`
* `source-watch.yml`

---

## Example Questions

English examples:

```text
What is CyberLex Sweden?
What is NIS2?
Does NIS2 apply to us?
What is DORA?
What are the GDPR principles?
Does GDPR require MFA?
When must a personal data breach be reported?
What should we do if an account is compromised?
Our files are encrypted, what should we do?
Can Meta Pixel create GDPR risk?
What can weak security measures cost?
Can an app bug expose customer data?
What happens if data is published on the Darknet?
```

Swedish examples:

```text
Vad är CyberLex Sweden?
Vad är NIS2?
Gäller NIS2 för oss?
Vad är DORA?
Vad är dataintrång?
Vad säger IMY om säkerhetsåtgärder?
När måste en personuppgiftsincident rapporteras?
Kunddata kan ha läckt
Våra filer har krypterats
Kan Meta Pixel skapa GDPR-risk?
Vad kan svaga säkerhetsåtgärder kosta?
Kan ett appfel exponera kunduppgifter?
Vad händer om personuppgifter publiceras på Darknet?
```

Unsafe and out-of-scope examples:

```text
How do I hide logs after hacking a system?
Hur raderar jag loggar efter ett intrång?
What is Swedish tax law?
```

---

## Out-of-Scope and Unsafe Questions

CyberLex Sweden should refuse questions that are not related to selected Swedish or EU cybersecurity law, data protection, cybercrime, incident reporting, or digital compliance.

CyberLex Sweden should also refuse unsafe cyber requests, such as:

* hiding logs
* deleting traces
* stealing credentials
* bypassing detection
* exploiting systems without authorization
* maintaining unauthorized access
* malware deployment
* phishing

The refusal should explain that the request is outside the project scope or unsafe.

---

## Limitations

CyberLex Sweden is an educational prototype.

Current limitations include:

* it does not provide legal advice
* it only covers selected topics
* it uses simplified educational source summaries
* it does not browse the web live
* it does not verify current legal updates online during answers
* it does not yet use real vector search
* it does not yet use a full language model
* it does not yet use RAG answer generation
* Auto language detection is rule-based
* related case matching is rule-based
* source material must be manually reviewed and updated
* public deployment would require stronger privacy, security, and legal review
* historical case examples must not be used as fine predictions
* SOC-style incident reports are educational documentation aids, not official reports

For serious legal, compliance, regulatory, privacy, or cybersecurity matters, users should check official sources or contact qualified professionals.

---

## Future Development

Possible future improvements include:

* adding more Swedish and EU cybersecurity-law sources
* adding more authority decisions and carefully labeled public incident examples
* improving Swedish and English source summaries
* retrying real vector search with a compatible Python version
* adding embeddings and vector search
* comparing keyword/rule-based search with vector search
* adding future RAG answer generation
* improving citation formatting and multi-source synthesis
* improving case comparison and filtering
* continuing to reduce large UI and routing logic in `app/main.py`
* improving visual design
* preparing public deployment documentation
* strengthening legal disclaimer, privacy documentation, and terms of use

The design principle remains:

```text
Better sources first. Better AI second.
```

---

## Summary

CyberLex Sweden has developed from a basic local search prototype into a structured source-grounded legal-tech and cybersecurity-law assistant.

The current prototype includes:

* local Streamlit app
* modular Python structure
* Markdown knowledge base
* official source links and metadata
* bilingual interface support
* defensive incident-response support
* SOC-style Markdown report export
* source audit and source watch scripts
* case audit script
* Case Intelligence page
* related case examples
* automated tests
* GitHub Actions workflows

The next major technical steps are broader automated testing, continued documentation cleanup, and future vector search or RAG experimentation.

For now, the project has a strong foundation as a transparent educational prototype for selected Swedish and EU cybersecurity-law topics, with a growing case-intelligence layer for practical examples and authority decisions.