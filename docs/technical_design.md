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
* an experimental retrieval panel

CyberLex Sweden is designed as an educational legal-tech and cybersecurity-law prototype.

It does not provide legal advice and should not replace a qualified lawyer, official authority guidance, compliance review, data protection officer, or professional incident-response support.

---

## Application Architecture

The application is built with:

* Python
* Streamlit
* local Markdown files
* rule-based source search
* source routing
* topic keyword expansion
* source confidence explanations
* source quality labels
* source freshness labels
* detected topic labels
* source metadata extraction
* citation display
* bilingual interface support
* practical explanation generation
* topic-based assessment checklists
* SOC-style Markdown report generation
* experimental retrieval search
* source audit scripts
* GitHub Actions source audit automation

The main application file is:

```text
app/main.py
```

The experimental retrieval module is:

```text
app/vector_search.py
```

The local knowledge base is stored in:

```text
data/
```

The project documentation is stored in:

```text
docs/
```

Maintenance scripts are stored in:

```text
scripts/
```

The GitHub Actions workflow is stored in:

```text
.github/workflows/source-audit.yml
```

This structure separates the main app, trusted source files, documentation, maintenance scripts, and automation workflows.

This makes the project easier to understand, test, maintain, and expand.

---

## Main Components

## Python

Python is the programming language used to build the application logic.

It handles:

* reading Markdown files
* splitting documents into searchable chunks
* scoring search results
* routing questions to source files
* expanding question terms
* detecting question topics
* detecting source quality labels
* detecting source freshness labels
* generating answers
* generating practical explanations
* generating assessment checklists
* generating incident-response report text
* generating source audit reports
* displaying results through Streamlit
* running experimental retrieval tests

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

Streamlit is also used for interactive features such as:

* buttons
* expandable sections
* example question selection
* sidebar controls
* session state

Streamlit session state is used to remember selected example questions and whether the example question panel should be open or hidden.

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
12. incident log template, where relevant
13. SOC Markdown report download, where relevant

Not every section appears for every question.

Simple definition questions should not show unnecessary incident-response panels.

Practical incident-response questions may show more structured support.

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

It is not an official incident record, forensic report, legal assessment, or regulatory notification.

---

## Example Questions Panel

CyberLex Sweden includes an example questions panel below the main question input.

The purpose is to help users understand what kinds of questions the prototype can answer.

The panel can be shown or hidden with a Streamlit button.

Each example question is displayed with a button that lets the user fill the question input field automatically.

This is handled with Streamlit session state.

When the user clicks an example question, CyberLex:

1. stores the selected question in session state
2. fills the question input field with that question
3. hides the example questions panel
4. reruns the Streamlit app so the answer is generated

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

The knowledge base includes Swedish summaries and Swedish useful-question sections across several supported source files.

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
* it does not provide legal advice
* source material must be manually reviewed and updated
* the source audit checks local source structure, not live legal changes
* confidence labels describe local source matching only, not legal certainty
* source freshness labels describe stored local review dates only, not live legal currency
* detected topic labels describe question interpretation only, not legal classification
* the experimental search panel is for testing and does not replace the main answer system yet

---

## Future Development

Future technical improvements may include:

* continued Swedish source refinement
* more Swedish and EU legal sources
* vector search with ChromaDB or FAISS
* local embeddings using sentence-transformers
* AI-generated answers using a RAG design
* stronger citation formatting
* source update reminders
* live source review workflow
* optional retrieval mode comparison
* public deployment
* improved visual design
* stronger legal disclaimer and Terms of Use
* privacy policy improvements
* bilingual Swedish and English source expansion
* trademark and brand protection review if the project develops further

---

## Current Technical Status

CyberLex Sweden currently has:

* a working Streamlit interface
* a local Markdown knowledge base
* 13 source files checked by the source audit
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
* example question buttons
* bilingual interface support
* experimental retrieval sidebar
* experimental retrieval module in `app/vector_search.py`
* source audit script in `scripts/source_audit.py`
* metadata helper script in `scripts/add_missing_metadata.py`
* GitHub Actions source audit workflow
* improved Swedish routing for NIS2, GDPR, IMY, dataintrång, DORA, CRA, and EU attacks against information systems

The source-improvement phase is largely complete for the current prototype scope.

The next major technical step is true vector search, then later a RAG-based answer mode that remains mandatory-source-grounded.
