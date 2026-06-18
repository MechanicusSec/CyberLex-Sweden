# CyberLex Sweden Technical Design

## Purpose

This document explains the technical design of the CyberLex Sweden prototype.

CyberLex Sweden is a local Streamlit application that answers questions about selected Swedish and EU cybersecurity-law topics using a trusted local Markdown knowledge base.

The prototype does not use a full language model yet.

Instead, it uses:

* source-based search
* question intent matching
* rule-based answer generation
* practical explanations
* assessment checklists
* detected topic labels
* source quality labels
* source freshness labels
* confidence explanations
* transparent source display
* defensive incident-response logic
* SOC-style Markdown report export
* case-library support for real authority decisions, public incident examples, and historical examples
* case learning notes for clear educational takeaways
* a Case Intelligence page for browsing GDPR and cybersecurity-related cases
* bilingual case display for Swedish and English summaries, outcomes, topics, and source links
* English, Swedish, and Auto language modes
* an experimental retrieval panel

CyberLex Sweden is designed as an educational legal-tech and cybersecurity-law prototype.

It does not provide legal advice and should not replace a qualified lawyer, official authority guidance, compliance review, data protection officer, or professional incident-response support.

---

## Application Architecture

CyberLex Sweden is built as a modular Python and Streamlit application.

The Streamlit entry point is:

```text
app/main.py
```

Earlier prototype versions placed most application logic directly inside `app/main.py`.

The current version has been partly refactored into smaller modules so the application is easier to understand, test, maintain, and extend.

Current app module structure:

```text
app/
├── main.py              # Streamlit app flow, UI rendering, answer display, and remaining routing glue
├── config.py            # App settings, page configuration, and folder paths
├── styles.py            # CSS and visual styling
├── text_utils.py        # Text normalization and matching helpers
├── language.py          # Swedish/English detection and localization
├── source_loader.py     # Markdown source loading, metadata extraction, and chunking
├── incident_engine.py   # Practical incident-response question detection
├── case_search.py       # Related case and incident-example search
└── vector_search.py     # Experimental rule-based retrieval functionality
```

The local knowledge base is stored in:

```text
data/
```

The educational case library is stored in:

```text
cases/
```

The project documentation is stored in:

```text
docs/
```

Maintenance scripts are stored in:

```text
scripts/
```

Case-library documentation and audit output are stored in:

```text
docs/case_library/
```

The GitHub Actions source-audit workflow is stored in:

```text
.github/workflows/source-audit.yml
```

The current architecture separates:

* Streamlit page flow
* configuration
* styling
* text normalization
* language detection and localization
* Markdown source loading
* incident-response detection
* case-library search
* experimental retrieval

This makes the project easier to understand, test, maintain, and expand.

---

## Main Components

## Current Python Modules

The current app code is split across several Python modules.

### `app/main.py`

`main.py` is the Streamlit entry point.

It controls:

* page layout
* sidebar navigation
* question input
* example question behavior
* answer display flow
* source result display
* practical explanation sections
* incident report download display
* Case Intelligence page rendering
* related case display rules
* remaining answer-routing glue

The file still contains a large amount of answer-routing and display logic, but it no longer contains every helper function from the earliest prototype.

Future refactoring may split more of this logic into separate modules, but the current structure is stable enough for the present prototype stage.

### `app/config.py`

`config.py` stores shared app constants and folder paths.

It includes:

* app title
* app icon
* Streamlit layout mode
* data folder path
* case folder path

### `app/styles.py`

`styles.py` contains CSS and visual styling.

It controls styling for:

* cards
* warnings
* source context panels
* topic badges
* case sections
* incident-response panels
* general layout behavior

### `app/text_utils.py`

`text_utils.py` contains shared text helper functions.

It supports:

* normalizing user questions
* cleaning searchable words
* checking whether text contains key terms or phrases
* shared keyword and phrase matching

These helpers are reused by routing, search, language detection, and incident detection.

### `app/language.py`

`language.py` handles language detection and localization.

It supports:

* English detection
* Swedish detection
* Auto language mode
* mixed Swedish/English cyber questions
* localized labels
* localized section names
* localized source labels
* localized related case titles
* example-question cleanup by language

This module is important because CyberLex Sweden is intended to support both Swedish and English users.

### `app/source_loader.py`

`source_loader.py` handles the trusted Markdown knowledge base.

It supports:

* loading Markdown files from `data/`
* extracting official source links
* extracting source metadata
* extracting source dates
* extracting version notes
* extracting sections
* splitting Markdown files into searchable chunks

This separates source loading from the Streamlit UI.

### `app/incident_engine.py`

`incident_engine.py` contains practical incident-response detection logic.

It detects questions about:

* suspected hacking
* unauthorized access
* suspicious login activity
* suspicious MFA activity
* suspicious links
* suspicious emails
* phishing
* compromised accounts
* ransomware
* malware
* encrypted files
* data leaks
* practical incident-response situations

This module helps the app decide when to show defensive first-step guidance and incident-response support.

### `app/case_search.py`

`case_search.py` handles case-library search.

It loads case files from `cases/`, extracts structured case sections, expands keywords, scores case relevance, and returns related case examples.

It supports related cases for suitable compliance and case-library questions.

It should not turn historical cases into fine predictions.

### `app/vector_search.py`

`vector_search.py` is an experimental retrieval module.

Despite the name, it currently remains rule-based and does not yet use true embeddings, FAISS, ChromaDB, or a full RAG pipeline.

The name is a little too ambitious, because apparently even filenames can have delusions of grandeur.

---

## Python

Python is the programming language used to build the application logic.

It handles:

* reading Markdown files through `source_loader.py`
* splitting documents into searchable chunks
* scoring search results
* routing questions to source files
* expanding question terms
* detecting question topics
* detecting practical incident-response questions through `incident_engine.py`
* detecting source quality labels
* detecting source freshness labels
* generating answers
* generating practical explanations
* generating assessment checklists
* generating incident-response report text
* generating source audit reports
* displaying results through Streamlit
* running experimental retrieval tests
* loading educational case files through `case_search.py`
* scoring related cases
* rendering bilingual case-library content
* filtering official case source links by selected language

Python is also used for the maintenance scripts in the `scripts/` folder.

---

## Streamlit

Streamlit is the Python framework used to create the CyberLex Sweden web interface.

It displays:

* the main page
* the sidebar
* the question input field
* answers
* detected topic cards
* citations
* official source links
* source quality labels
* source freshness labels
* source metadata
* confidence explanations
* warnings and disclaimers
* practical explanations
* assessment checklists
* incident log templates
* SOC Markdown report download button
* relevant source context
* other matching source sections
* experimental retrieval results
* Case Intelligence page
* searchable case cards
* related authority decisions below answers
* bilingual case summaries, outcomes, learning notes, topics, and source links

Streamlit is also used for interactive features such as:

* buttons
* expandable sections
* example question selection
* sidebar controls
* session state

Streamlit session state is used to manage:

* selected example questions
* submitted questions
* the visible question input
* whether the example question panel should be open or hidden
* sidebar and navigation state

When the user clicks an example question, the app now submits that example immediately instead of only filling the input field.

---

## Markdown Knowledge Base

CyberLex Sweden uses Markdown files in the `data/` folder as its trusted local knowledge base.

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

Each source file contains structured sections such as:

* topic
* key idea
* main authority
* main legal source
* important points
* practical explanation
* cybersecurity connection
* incident assessment checklist
* useful questions
* official source
* source metadata
* disclaimer

The knowledge base is intentionally local.

CyberLex Sweden does not browse the web live when answering questions.

This makes the prototype easier to control and explain, but it also means the source material must be reviewed and updated manually.

---

## Case Library

CyberLex Sweden includes a separate educational case library stored in:

```text
cases/
```

The case library is separate from the trusted legal and cybersecurity knowledge base in `data/`.

The separation is intentional:

```text
data/
= legal, regulatory, authority, and cybersecurity source knowledge

cases/
= historical authority decisions, real-world examples, outcomes, fines, and references
```

CyberLex Sweden should not treat historical cases as fine predictions or legal outcome predictions.

Case files are used as educational examples to show how similar GDPR, cybersecurity, tracking-technology, app-exposure, personal-data-breach, and security-measure issues have been assessed or publicly handled in practice.

The current case library contains 8 checked case files:

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

The case template is:

```text
cases/CASE_TEMPLATE.md
```

The case index is:

```text
cases/CASE_INDEX.md
```

Each case file should contain structured sections such as:

* case type
* jurisdiction
* year
* authority or court
* topic
* short summary
* Swedish short summary
* what happened
* Swedish what happened
* legal issue
* Swedish legal issue
* decision or outcome
* Swedish decision or outcome
* fine or cost
* Swedish fine or cost
* why it matters for CyberLex
* Swedish why it matters for CyberLex
* learning note
* Swedish learning note
* similar CyberLex questions
* related CyberLex topics
* Swedish related CyberLex topics
* official source
* Swedish official source, where available or needed
* case metadata
* disclaimer

The bilingual case sections allow the Case Intelligence page to display Swedish case content when the user selects Swedish, English content when the user selects English, and broader source visibility when the user uses automatic language mode.

Learning-note sections are displayed only when real content exists, so the UI avoids empty placeholder sections.

---

## Case Search and Related Cases

The case search module is:

```text
app/case_search.py
```

This module loads Markdown files from the `cases/` folder and scores how relevant each case is to the user question.

It supports:

* case file loading
* section extraction
* keyword expansion
* case-profile matching
* phrase-based scoring
* deterministic priority rules
* top-case ranking

The deterministic priority layer helps obvious questions return the most relevant case first.

Examples:

```text
Can hashed data sent through Meta Pixel be a GDPR issue?
→ IMY Kry Meta Pixel should rank first
```

```text
Can sending customer data to the wrong email be a personal data breach?
→ Wrong Email Customer Data Case should rank first
```

```text
Can an app bug expose customer data?
→ Klarna App Data Exposure 2021 should rank highly
```

```text
What happens if data is published on the Darknet?
→ Sportadmin Security Breach should rank first
```

```text
What can weak security measures cost?
→ Trygg-Hansa Security Deficiencies and Sportadmin should rank highly
```

Related cases can appear below normal CyberLex answers in a section such as:

```text
Related cases and authority decisions
```

This section is intended to support the answer with real historical examples.

It is not a prediction engine.

---

## Case Intelligence Page

CyberLex Sweden includes a Case Intelligence page inside the Streamlit application.

The current implementation is in:

```text
app/main.py
```

The sidebar navigation includes:

```text
Ask CyberLex
Case Intelligence
```

The Case Intelligence page lets the user browse the case library without asking a normal question.

It displays:

* a case-library introduction
* case search/filter input
* total case count
* shown case count
* limitation warning about historical outcomes
* foldable case cards
* summaries
* learning notes
* administrative fines or outcomes
* related topic badges
* official source links

The Case Intelligence page uses bilingual display logic.

When the selected language is English, it prefers English case sections.

When the selected language is Swedish, it prefers Swedish case sections.

When source-language mode is automatic, official source links can show both Swedish and English sources.

If a selected language has no matching source link, CyberLex falls back to available official sources so that users do not lose source transparency.

---

## Case Audit System

CyberLex Sweden includes a case audit script:

```text
scripts/case_audit.py
```

The script checks Markdown files in:

```text
cases/
```

It ignores:

```text
cases/CASE_TEMPLATE.md
cases/CASE_INDEX.md
```

The case audit checks whether each case file includes required sections, official source links, case source dates, and version notes.

The generated report is stored in:

```text
docs/case_library/case_audit_report.md
```

The expected current audit scope is:

```text
Case files checked: 8
```

The case audit does not verify live legal accuracy online.

It also does not decide whether a public incident example is equivalent to an authority decision, so case type labels must stay accurate in the Markdown files.

It checks whether the local case-library files follow the required CyberLex case structure.

---

## Question and Answer Flow

The normal question flow is:

1. The user enters a question or selects an example question.
2. Streamlit session state stores the active question.
3. Auto language mode determines whether the active question should use Swedish or English.
4. The app checks whether the question is about CyberLex Sweden itself.
5. The app checks whether the question is in scope.
6. The app checks whether the question is unsafe and should be refused.
7. The app routes supported questions toward a relevant source file where possible.
8. The app searches local Markdown chunks.
9. The best source match is used to build the main CyberLex answer.
10. The app displays supporting source links, source metadata, limitations, practical sections, and source context where relevant.
11. Related cases are shown only when the question is suitable for case-library examples.
12. SOC-style report download is shown only for practical incident-response questions.

The app does not browse the web live during this process.

---

## Auto Language Flow

CyberLex Sweden supports English, Swedish, and Auto language mode.

In Auto mode:

1. The app looks at the active question text.
2. `language.py` detects whether the question should be handled as English or Swedish.
3. The interface labels, answer headings, source labels, and case titles follow the detected language.
4. Mixed Swedish/English cybersecurity questions are handled with special rules.

Examples:

```text
Can Meta Pixel create GDPR risk?
→ English
```

```text
Kan Meta Pixel skapa GDPR-risk?
→ Svenska
```

```text
What is NIS2?
→ English
```

```text
Vad är NIS2?
→ Svenska
```

The language system is rule-based and may still need continued refinement as new question patterns appear.

---

## Example Question Flow

The example question panel is designed for testing and demonstration.

When a user clicks an example question:

1. the example is stored as the selected question
2. the same question is stored as the submitted question
3. the input field is filled
4. the example panel is hidden
5. the app reruns and displays the answer directly

This means the user should not need to click the normal search button after selecting an example question.

In Swedish mode, the app displays Swedish example questions and Swedish button labels.

---

## Related Case Display Rules

CyberLex Sweden can show related cases and incident examples below normal answers.

However, related cases are not shown for practical incident-response triage questions such as:

```text
Our files are encrypted, what should we do?
```

```text
Vi har fått en misstänkt login på ett konto, vad ska vi göra?
```

For those questions, the app should focus on defensive first steps, containment, evidence preservation, source context, and incident report support.

Related cases are mainly shown for legal, compliance, and case-library-style questions such as:

```text
Can Meta Pixel create GDPR risk?
```

```text
Kan ett appfel exponera kunduppgifter?
```

```text
What can weak security measures cost?
```

This keeps the answer focused on what the user is actually asking.

---

## Search and Retrieval Design

CyberLex searches the local knowledge base by:

1. Loading Markdown files from `data/`.
2. Splitting each file into smaller chunks based on headings.
3. Cleaning the user question into searchable words.
4. Expanding important question terms with related legal and cybersecurity terms.
5. Matching question words against chunk text and section titles.
6. Applying score boosts for useful sections.
7. Applying score penalties for weak sections.
8. Routing clear questions to the most relevant source file.
9. Ranking results by relevance score.

The best match is used for the main answer.

Additional matching sections may be shown for transparency.

This is rule-based retrieval.

It does not use semantic embeddings or a vector database yet.

The current design is deliberately transparent. The user can see:

* matched knowledge file
* matched section
* source quality label
* source freshness label
* confidence explanation
* official source links
* source metadata
* supporting source context

This makes the prototype easier to trust, inspect, and explain.

---

## Topic Keyword Expansion

CyberLex Sweden uses topic keyword expansion to improve local search matching.

The function:

```text
expand_question_terms(question)
```

adds related cybersecurity and legal terms when the user question contains important trigger words.

Examples:

* `ransomware` can expand into terms such as cyber incident, incident reporting, personal data breach, GDPR, NIS2, security measures, malware, logs, evidence, and unauthorized access.
* `malware` can expand into terms such as ransomware, cyber incident, security incident, incident response, containment, recovery, logs, and reporting.
* `unauthorized access` can expand into terms such as dataintrång, cybercrime, illegal access, information system, data intrusion, and unauthorized use.
* `DORA` can expand into terms such as digital operational resilience, financial sector, ICT risk, ICT incident, third-party ICT, resilience testing, and operational disruption.
* `NIS2` can expand into terms such as cybersecurity, incident reporting, essential entities, important entities, risk management, security measures, and MSB.
* `personal data breach` can expand into terms such as GDPR, IMY, 72 hours, notification, risk to rights and freedoms, affected individuals, and controller.

This helps the prototype find relevant source sections even when the user does not use the exact same words as the Markdown files.

This is still rule-based search.

It does not use a language model or vector database yet.

---

## Source Routing

The function:

```text
get_target_source_file(question)
```

routes clear questions to a specific knowledge file.

Examples:

* GDPR breach questions route to `gdpr_personal_data_breach.md`
* GDPR security-measure questions route to `imy_gdpr_security_measures.md`
* IMY authority questions route to `imy_gdpr_supervision.md`
* NIS2 sector-scope questions route to `nis2_sector_scope_guidance.md`
* NIS2 incident reporting questions route to `nis2_incident_reporting.md`
* NIS2 cybersecurity law questions route to `nis2_cybersecurity_law.md`
* DORA questions route to `eu_dora_digital_operational_resilience.md`
* Cyber Resilience Act questions route to `eu_cyber_resilience_act.md`
* Dataintrång or Swedish unauthorized access questions route to `cybercrime_dataintrang.md`
* EU attacks against information systems questions route to `eu_attacks_against_information_systems.md`
* practical incident-response questions route to `cyber_incident_response_playbook.md` where relevant
* case-library-style questions about Meta Pixel, weak security, wrong email disclosure, Darknet publication, web forms, and fines route toward better supporting source files

Source routing improves accuracy by preventing similar words from matching the wrong source file.

For example:

* a general ransomware question should not route to DORA unless the question specifically concerns financial-sector ICT resilience
* a CRA product-security question should not route to general NIS2 cybersecurity duties
* a personal data breach question should not be treated as a generic cyber incident only
* a Swedish dataintrång question should not be confused with broader EU cybercrime framework questions

Source routing is one of the main safeguards in the current prototype.

---

## Experimental Retrieval Module

CyberLex Sweden includes an experimental retrieval module:

```text
app/vector_search.py
```

This module is used to test improved retrieval separately from the main answer system.

Despite the name, the current experimental module does not use:

* true vector embeddings
* ChromaDB
* FAISS
* a full language model

It is an experimental rule-based retrieval engine that prepares the project for future vector search and RAG.

The module currently:

* loads Markdown source files from `data/`
* splits them into chunks based on Markdown headings
* cleans source text and user questions into searchable words
* scores chunks against the user question
* boosts useful content sections
* penalizes weak support sections
* applies topic-specific ranking rules
* returns ranked source matches

The module can be run directly from the terminal with:

```powershell
python app/vector_search.py
```

This allows retrieval testing without starting the full Streamlit app.

The experimental module is kept separate from `app/main.py` so it can be improved safely without breaking the main CyberLex answer system.

---

## Experimental Retrieval Sidebar

The Streamlit sidebar includes an experimental retrieval panel.

This panel allows the user to type a test question and see the top experimental source matches.

The panel displays:

* source file
* source section
* relevance score

The experimental retrieval panel does not replace the main CyberLex answer system.

It is used for testing retrieval quality before experimental logic is connected to the main answer flow.

Example test question:

```text
What is DORA?
```

Expected top match:

```text
eu_dora_digital_operational_resilience.md
Section: Key idea
```

Example test question:

```text
Is unauthorized access illegal in Sweden?
```

Expected top match:

```text
cybercrime_dataintrang.md
Section: Key idea
```

Example test question:

```text
What should a company do after a ransomware attack?
```

Expected top match may involve:

```text
cyber_incident_response_playbook.md
```

or:

```text
nis2_incident_reporting.md
Section: Incident assessment checklist
```

depending on the search mode and current routing.

---

## Ranking Logic

The experimental search module uses ranking logic to improve result order.

Useful content sections are boosted.

Examples of useful sections include:

* key idea
* important points
* main authority
* main legal source
* incident assessment checklist
* practical explanation
* Swedish summary
* reporting to IMY
* affected individuals
* incident reporting
* cybersecurity connection
* relationship with GDPR
* relationship with NIS2
* third-party ICT risk
* legal reference

Weak support sections are penalized.

Examples of weak sections include:

* useful questions
* official source
* source metadata
* source date
* version notes
* disclaimer
* topic
* introduction

This helps prevent support sections from ranking above actual explanatory sections.

---

## Detected Topic Labels

CyberLex Sweden displays a detected topic label above or near the answer.

The function:

```text
detect_question_topic(question, language)
```

identifies a simple topic category from the user question.

Examples of detected topic labels include:

* Ransomware or malware incident
* Suspicious email or phishing
* Suspicious login
* Compromised account
* Possible data leak
* GDPR data breach
* DORA and ICT risk
* NIS2 and cybersecurity duties
* NIS2 sector scope
* Unauthorized access / dataintrång
* Cyber Resilience Act and product security
* EU cybercrime and information systems
* General cybersecurity law question

In Swedish mode, the topic labels are displayed in Swedish where relevant.

The detected topic label does not replace source matching.

It is only a user-facing explanation of how CyberLex interpreted the question.

---

## Source Confidence Explanations

CyberLex Sweden converts the numeric relevance score from local search into a human-readable source confidence explanation.

The function:

```text
generate_source_confidence(score, language)
```

returns both:

* a confidence level
* a short explanation

The current English confidence levels are:

```text
Very strong
Strong
Moderate
Limited
```

In Swedish mode, these are displayed as:

```text
Mycket stark
Stark
Måttlig
Begränsad
```

The source confidence value does not represent legal certainty.

It only explains how strongly the user question matched the selected local source section.

---

## Source Quality Labels

CyberLex Sweden displays a source quality label inside the citation details card.

The function:

```text
detect_source_quality(filename, language)
```

checks the matched knowledge file name and returns a short user-facing description of what type of source the local file is based on.

Examples:

```text
cybercrime_dataintrang.md
→ Swedish legal source / criminal-law topic
```

```text
gdpr_personal_data_breach.md
→ IMY guidance and EU data protection source
```

```text
imy_gdpr_security_measures.md
→ Swedish authority guidance on GDPR security measures
```

```text
nis2_sector_scope_guidance.md
→ NIS2 sector-scope guidance
```

```text
cyber_incident_response_playbook.md
→ Defensive incident-response guidance
```

The source quality label does not prove legal authority by itself.

It explains what kind of source category the local Markdown file represents.

---

## Source Freshness Labels

CyberLex Sweden displays a source freshness label inside the source metadata card.

The function:

```text
detect_source_freshness(source_date, language)
```

checks the stored source date text from the matched Markdown knowledge file and returns a simple user-facing freshness label.

Examples:

```text
Last checked: 2026-06-08
→ Recently checked
```

```text
No source date
→ No review date stored
```

```text
Older stored date
→ Review recommended
```

In Swedish mode, the labels are displayed as:

```text
Nyligen kontrollerad
Inget granskningsdatum sparat
Granskning rekommenderas
```

The source freshness label does not check the internet and does not confirm that the law is currently up to date.

It only describes the stored review date in the local Markdown file.

---

## Source Audit System

CyberLex Sweden includes a local source audit system.

The source audit script is:

```text
scripts/source_audit.py
```

The script checks Markdown files in:

```text
data/
```

It checks whether each source file has:

* official source section
* official source links
* source metadata section
* source date
* source freshness information
* version notes

The script generates the audit report:

```text
docs/source_audit_report.md
```

The current target is:

```text
Files marked OK: 13
Files needing review: 0
```

The audit does not browse the web and does not verify whether the law has changed online.

It only checks whether the local project files contain the required source structure.

---

## Metadata Helper Script

CyberLex Sweden includes a helper script:

```text
scripts/add_missing_metadata.py
```

This script was used to add missing metadata blocks to Markdown files in the `data/` folder.

The metadata block follows this structure:

```markdown
## Source metadata

Source date: Last checked: YYYY-MM-DD

Version notes: Source reviewed for CyberLex Sweden educational prototype.
```

The helper script is not intended to replace proper source review.

It is mainly a maintenance tool used when files are missing required metadata.

The normal recurring check is handled by:

```text
scripts/source_audit.py
```

---

## GitHub Actions Audit

CyberLex Sweden includes a GitHub Actions workflow for source auditing.

The workflow file is:

```text
.github/workflows/source-audit.yml
```

The workflow can run manually from the GitHub Actions tab.

It may also be scheduled to run automatically.

The workflow performs these steps:

1. checks out the repository
2. sets up Python
3. runs the source audit script
4. updates `docs/source_audit_report.md`
5. commits the updated report if changes are found

The weekly audit does not check live legal changes online.

It only checks whether the local source files contain official links, source metadata, review dates, and version notes.

This means it is a source-structure audit, not a legal-currentness audit.

---

## CyberLex Answer Structure

CyberLex Sweden answers are designed to be source-grounded and transparent.

When a user asks an in-scope question, the app may display:

1. short answer
2. detected topic
3. citation details
4. official source links
5. source metadata
6. important limitation
7. attention level
8. practical explanation
9. assessment checklist
10. relevant source context
11. other matching source sections
12. related cases where relevant
13. incident log template where relevant
14. SOC Markdown report download where relevant

Not every section appears for every question.

Simple definition questions should not show unnecessary incident-response panels.

Practical incident-response questions may show more structured support.

Related cases should be hidden for urgent practical incident-response triage questions.

---

## Incident-Response Design

CyberLex Sweden can recognize selected practical incident-response questions.

Supported incident types include:

* suspicious email
* phishing
* clicked links
* opened attachments
* entered credentials
* suspicious login
* suspicious MFA activity
* compromised account
* suspected hacking
* malware
* ransomware
* encrypted files
* customer data leak
* possible personal data breach

For practical incident-response questions, CyberLex may show:

* recommended first steps
* incident assessment checklist
* incident log template
* SOC-style Markdown report download
* relevant source context

Incident-response guidance is defensive and educational.

It does not replace professional incident-response procedures.

---

## SOC Markdown Report Export

CyberLex Sweden can generate a SOC-style Markdown report for practical incident-response questions.

The report may include:

* report metadata
* purpose
* original question or reported event
* handling note
* SOC triage
* recommended first steps
* SOC action support
* SOC control checklist
* incident log template
* short source note
* disclaimer

The report is intended as a documentation aid for learning and testing.

It is not an official incident record, forensic report, legal assessment, regulatory notification, breach notification to IMY, or NIS2 incident report.

---

## Example Questions Panel

CyberLex Sweden includes an example questions panel below the main question input.

The purpose is to help users understand what kinds of questions the prototype can answer.

The panel can be shown or hidden with a Streamlit button.

Each example question is displayed with a button that lets the user fill the question input field automatically.

This is handled with Streamlit session state.

When the user clicks an example question, CyberLex:

1. stores the selected question in session state
2. stores the question as the submitted active question
3. fills the question input field with that question
4. hides the example questions panel
5. reruns the Streamlit app so the answer is generated immediately

In Swedish mode, the app displays Swedish example questions and Swedish button labels.

---

## Bilingual Interface Support

CyberLex Sweden supports both English and Swedish interface text.

The app can display:

* English labels
* Swedish labels
* English example questions
* Swedish example questions
* English limitation text
* Swedish limitation text
* English topic labels
* Swedish topic labels
* English source-confidence labels
* Swedish source-confidence labels
* English freshness labels
* Swedish freshness labels
* English case summaries
* Swedish case summaries
* English case outcomes
* Swedish case outcomes
* English case topic badges
* Swedish case topic badges
* language-aware official source links for cases
* case learning notes where available

The knowledge base includes Swedish summaries and Swedish useful-question sections across several supported source files.

The case library now also supports Swedish case sections.

The Case Intelligence page can display Swedish summaries, Swedish fine/outcome text, Swedish learning notes, Swedish topic badges, and language-aware official source links.

Swedish answer wording and source coverage can still be improved further, but the project has a stronger bilingual foundation than the earlier prototype.

---

## Limitations

CyberLex Sweden is an educational prototype.

Current technical limitations include:

* it does not use a full language model yet
* it does not use true vector embeddings yet
* the experimental retrieval module is still rule-based
* it does not browse the web live
* it only answers from local Markdown sources
* it only covers selected topics
* it uses rule-based answers and routing
* Auto language detection is rule-based and may need additional edge-case refinement
* it does not provide legal advice
* source material must be manually reviewed and updated
* the source audit checks local source structure, not live legal changes
* the case audit checks local case-file structure, not live legal or factual currentness
* confidence labels describe local source matching only, not legal certainty
* source freshness labels describe stored local review dates only, not live legal currency
* detected topic labels describe question interpretation only, not legal classification
* the experimental search panel is for testing and does not replace the main answer system yet
* case examples are historical and must not be presented as fine predictions
* public incident examples must be clearly separated from authority decisions
* some official case sources may exist only in English or only in Swedish
* case source-language filtering depends on available links and local case-file structure
* SOC reports are educational documentation aids, not official incident records

---

## Future Development

Future technical improvements may include:

* continued Swedish source refinement
* more Swedish and EU legal sources
* vector search with ChromaDB or FAISS
* local embeddings using sentence-transformers
* AI-generated answers using a RAG design
* stronger citation formatting
* more automated tests for the refactored modules
* possible future split of answer-generation, search-ranking, and UI rendering logic
* source update reminders
* live source review workflow
* more Swedish official case links where available
* more authority decisions, court decisions, and carefully labeled public incident examples for the case library
* stronger case metadata, learning notes, and filtering
* separate Streamlit page files for Case Intelligence when the app grows
* optional retrieval mode comparison
* public deployment
* improved visual design
* stronger legal disclaimer and Terms of Use
* privacy policy improvements
* bilingual Swedish and English source expansion
* trademark and brand protection review if the project develops further

---

## Future Refactor Ideas

Future refactoring could split more logic out of `app/main.py`.

Possible future modules:

```text
app/answer_engine.py
app/search_engine.py
app/source_context.py
app/incident_reports.py
app/ui_components.py
app/safety.py
app/semantic_search.py
```

These should not be rushed unless there is enough time to test properly.

The current priority should remain:

```text
Stable prototype first.
Broader automated tests second.
Real vector search later.
RAG only after reliable retrieval.
```

Because breaking a working project for “cleaner architecture” right before a deadline is the sort of ritual only humans and failing startups perform.

---

## Current Technical Status

CyberLex Sweden currently has:

* a working Streamlit interface
* a modular app structure after refactoring `app/main.py`
* a local Markdown knowledge base
* 13 source files checked by the source audit target
* rule-based source-grounded answers
* source routing
* keyword ranking
* topic keyword expansion
* detected topic labels
* source quality labels
* source freshness labels
* source confidence explanations
* official source link display
* source metadata display
* important limitation cards
* attention level cards
* practical explanation cards
* assessment checklist cards
* incident-response support
* SOC Markdown report export
* relevant source context display
* other matching source sections
* example question buttons that run immediately when selected
* bilingual interface support with Auto language detection
* experimental retrieval sidebar
* experimental retrieval module in `app/vector_search.py`
* case search module in `app/case_search.py`
* Case Intelligence page
* educational case library in `cases/`
* 8 checked case files
* bilingual case summaries, outcomes, learning notes, topics, and source links
* related cases and incident examples under relevant compliance/case-library answers
* hidden related-case section for practical incident-response triage questions
* source audit script in `scripts/source_audit.py`
* case audit script in `scripts/case_audit.py`
* metadata helper script in `scripts/add_missing_metadata.py`
* GitHub Actions source audit workflow
* improved Swedish routing for NIS2, GDPR, IMY, dataintrång, DORA, CRA, and EU attacks against information systems

The source-improvement and case-intelligence phase is largely complete for the current prototype scope, with 8 checked case files and learning-note support.

The next major technical step is broader test coverage for the refactored modules, case behavior, Auto language behavior, true vector search, and later a RAG-based answer mode that remains mandatory-source-grounded.

---

## Final Note

CyberLex Sweden is intentionally local-first, source-grounded, and cautious.

The current technical design favors transparency and control over flashy AI behavior.

That is not as glamorous as a machine claiming it understands the law, but it is far less likely to confidently invent nonsense while wearing a digital judge wig.
