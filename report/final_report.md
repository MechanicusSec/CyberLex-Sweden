# CyberLex Sweden Final Report

## Project Title

CyberLex Sweden: A Source-Grounded Assistant Prototype for Swedish Cybersecurity Law, Digital Compliance, and Defensive Incident Response

## Student

CyberLex Sweden project author

---

## Project Summary

CyberLex Sweden is a final school project focused on building a source-grounded assistant prototype for Swedish cybersecurity law, EU cybersecurity law, digital compliance, and defensive incident response.

The goal of the project is to make selected Swedish and EU cybersecurity-law information easier to search, understand, and review by using a trusted local Markdown knowledge base, local case examples, rule-based retrieval, official source links, source metadata, citation details, source quality labels, source freshness labels, detected topic labels, practical explanations, assessment checklists, defensive incident-response support, and SOC-style Markdown report export.

The current prototype focuses on selected Swedish and EU cybersecurity-related legal topics, including GDPR, IMY, NIS2, the Swedish Cybersecurity Act, Swedish cybercrime law and dataintrång, EU attacks against information systems, the Cyber Resilience Act, DORA, and selected real-world case examples related to GDPR and cybersecurity.

CyberLex Sweden is an educational prototype. It does not provide legal advice and should not replace official authority guidance, qualified legal advice, compliance review, data protection officer review, or professional incident-response support.

---

## Source Quality Policy

CyberLex Sweden includes a source policy and source history documented in:

```text
docs/source_policy.md
docs/source_history.md
```

The purpose of the source quality policy is to make sure that the project uses trusted and traceable legal, authority-based, regulatory, and defensive cybersecurity sources.

The project prioritizes:

* official government sources
* official Swedish authority sources
* official EU legal sources
* defensive cybersecurity guidance
* clear source references
* readable official source links
* source dates
* version notes
* educational summaries that can be reviewed
* source history
* refusal when no trusted local source exists

This is important because legal and cybersecurity topics can be risky if an application gives unsupported or unclear answers.

The guiding principle is:

```text
Better sources first. Better AI second.
```

---

## 1. Background

Cybersecurity law can be difficult to understand because relevant information is spread across many different sources.

These sources can include:

* Swedish laws
* EU regulations
* EU directives
* Swedish government agencies
* cybersecurity authorities
* data protection authorities
* official legal databases
* public authority decisions
* practical incident-response guidance

For students, IT workers, and smaller organizations, it can be difficult to quickly understand which rules may apply in a cyber incident or digital compliance situation.

A normal chatbot may give confident but unsupported answers. This is especially risky in legal, compliance, privacy, and cybersecurity topics.

CyberLex Sweden was created as a prototype to explore how a focused assistant could help users find and understand selected cybersecurity-law information in a safer and more transparent way.

---

## 2. Problem Description

The main problem is that cybersecurity-related legal information is often:

* spread across several authorities and legal sources
* written in complex legal or administrative language
* difficult to search without knowing the exact legal terms
* risky to summarize incorrectly
* unsuitable for unsupported AI guessing
* connected to overlapping legal frameworks such as GDPR, NIS2, DORA, CRA, and criminal law

CyberLex Sweden tries to reduce that risk by using a local trusted knowledge base and showing which source file and source section were used for each answer.

The prototype does not try to replace a lawyer, court, authority, compliance specialist, data protection officer, or professional incident-response team.

---

## 3. Project Goal

The goal of the project was to build a working prototype that can:

* load trusted local knowledge base files
* search legal and cybersecurity information by topic
* split Markdown source files into searchable chunks
* match user questions to relevant source sections
* route specific questions to the correct knowledge file
* generate simple source-based answers
* show the source file and source section used
* display structured citation details
* display official source links
* display source metadata
* display source quality labels
* display source freshness labels
* display source match confidence explanations
* display detected topic labels
* show relevant source context and other matching source sections
* provide practical explanations and assessment checklists
* support English, Swedish, and Auto language behavior
* provide defensive incident-response support for selected scenarios
* generate SOC-style Markdown incident summaries for practical incident questions
* show related case examples for suitable compliance and case-library questions
* hide related case examples for urgent practical incident-response triage
* provide a Case Intelligence page for browsing local case examples
* refuse unsupported out-of-scope questions
* refuse unsafe cyber misuse requests
* audit local source files for required source structure
* audit local case files for required case-library structure

---

## 4. Scope

The current prototype covers a limited set of Swedish and EU cybersecurity-law topics, digital compliance topics, case examples, and defensive incident-response topics.

The current legal and compliance scope includes:

* GDPR and personal data breach notification in Sweden
* IMY and Swedish GDPR supervision
* GDPR core principles
* GDPR security measures
* NIS2 and the Swedish Cybersecurity Act
* NIS2 sector scope and applicability
* NIS2 incident reporting
* Swedish cybercrime law and dataintrång
* EU attacks against information systems
* EU Cyber Resilience Act
* EU DORA, the Digital Operational Resilience Act
* digital compliance and cybersecurity-related legal topics

The current case-library scope includes selected examples related to:

* GDPR risks
* Meta Pixel and tracking technologies
* app data exposure
* wrong-recipient disclosures
* weak security measures
* public incident examples
* authority decisions and public outcomes where available

The current incident-response scope includes selected defensive scenarios related to:

* suspicious email and phishing
* suspicious links
* suspicious login activity
* compromised accounts
* data leaks
* possible personal data breaches
* ransomware
* malware
* encrypted files
* suspected hacking or intrusion

The prototype does not cover all Swedish law.

For example, a question about Swedish tax law should be refused because it is outside the CyberLex Sweden project scope.

---

## 5. Tools and Technologies

### Visual Studio Code

Visual Studio Code was used as the main code editor.

It was used to write:

* Python code
* Markdown documentation
* source files
* case files
* test cases
* the final report

### Python

Python was used as the main programming language for the application.

Python was chosen because it is widely used for web prototypes, automation, data processing, and AI-related projects.

### Streamlit

Streamlit was used to create the local web application.

Streamlit makes it possible to turn a Python application into a browser-based interface with input fields, sidebars, formatted text, warnings, cards, buttons, expanders, downloadable files, and result sections.

### Markdown

Markdown was used for documentation, knowledge base files, case-library files, and generated SOC-style incident reports.

Markdown is simple to read and works well for GitHub documentation, structured notes, and source-based text files.

### Git

Git was used for version control.

Git tracks changes in the project and creates a development history through commits.

### GitHub

GitHub was used to store the project online.

GitHub makes it possible to show the code, documentation, project history, commits, and GitHub Actions workflow runs.

### GitHub Actions

GitHub Actions was added for source audit workflow support.

The workflow can run the local source audit script and update the generated source audit report.

---

## 6. Project Structure

The project is organized into several folders and files:

```text
CyberLex-Sweden
├── .github
│   └── workflows
│       └── source-audit.yml
├── app
│   ├── main.py
│   ├── config.py
│   ├── styles.py
│   ├── text_utils.py
│   ├── language.py
│   ├── source_loader.py
│   ├── incident_engine.py
│   ├── case_search.py
│   └── vector_search.py
├── cases
│   └── local case-library Markdown files
├── data
│   └── local Markdown knowledge base files
├── docs
│   ├── architecture.md
│   ├── ai_rag_plan.md
│   ├── legal_disclaimer.md
│   ├── privacy_and_data_handling.md
│   ├── product_roadmap.md
│   ├── project_overview.md
│   ├── project_plan.md
│   ├── source_audit_report.md
│   ├── source_context_behavior.md
│   ├── source_history.md
│   ├── source_list.md
│   ├── source_policy.md
│   ├── technical_design.md
│   ├── terms_of_use.md
│   ├── test_cases.md
│   ├── testing_and_demo.md
│   ├── ui_behavior.md
│   ├── vector_search_plan.md
│   └── case_library
│       └── case_audit_report.md
├── report
│   └── final_report.md
├── screenshots
├── scripts
│   ├── add_missing_metadata.py
│   ├── case_audit.py
│   └── source_audit.py
├── sources
├── .gitignore
├── COPYRIGHT.md
├── README.md
└── requirements.txt
```

---

## 7. Knowledge Base

CyberLex Sweden uses local Markdown files as its trusted knowledge base.

Each file in the `data/` folder represents one legal, regulatory, authority, cybersecurity, or defensive incident-response topic.

The current knowledge base includes 13 source files:

| File                                        | Topic                                                       |
| ------------------------------------------- | ----------------------------------------------------------- |
| `cyber_incident_response_playbook.md`       | Defensive incident-response guidance                        |
| `cybercrime_dataintrang.md`                 | Swedish cybercrime law and dataintrång                      |
| `eu_attacks_against_information_systems.md` | EU rules on attacks against information systems             |
| `eu_cyber_resilience_act.md`                | EU Cyber Resilience Act                                     |
| `eu_dora_digital_operational_resilience.md` | EU DORA and financial-sector digital operational resilience |
| `gdpr_core_principles.md`                   | GDPR core principles                                        |
| `gdpr_imy_edpb_security_guidance.md`        | GDPR, IMY, and EDPB security and breach guidance            |
| `gdpr_personal_data_breach.md`              | GDPR personal data breaches and IMY breach notification     |
| `imy_gdpr_security_measures.md`             | IMY and GDPR security measures                              |
| `imy_gdpr_supervision.md`                   | IMY and Swedish GDPR supervision                            |
| `nis2_cybersecurity_law.md`                 | NIS2 and the Swedish Cybersecurity Act                      |
| `nis2_incident_reporting.md`                | NIS2 incident reporting in Sweden                           |
| `nis2_sector_scope_guidance.md`             | NIS2 sector scope and applicability                         |

Each knowledge file is structured with headings such as:

* Topic
* Main authority or legal source
* Key idea
* Important points
* Cybersecurity connection
* Swedish summary
* Assessment checklist
* Useful questions
* Swedish useful questions
* Official source
* Source metadata
* Disclaimer

This structure makes it easier for the app to search, display, audit, and update relevant source sections.

---

## 8. Case Library

CyberLex Sweden includes a separate local case library in the `cases/` folder.

The case library is separate from the main knowledge base.

```text
data/
= legal, regulatory, authority, cybersecurity, and defensive incident-response source material

cases/
= educational examples, authority decisions, public incident examples, outcomes, fines, learning notes, and related case context
```

The current case library includes 8 checked case files:

| File                                       | Topic                                                                           |
| ------------------------------------------ | ------------------------------------------------------------------------------- |
| `imy_apoteket_apohem_meta_pixel.md`        | Meta Pixel and GDPR risk in pharmacy/health-related context                     |
| `imy_avanza_bank_meta_pixel.md`            | Meta Pixel and GDPR risk in financial services                                  |
| `imy_equality_ombudsman_web_form.md`       | Web form security and personal data handling                                    |
| `imy_kry_meta_pixel.md`                    | Meta Pixel and hashed contact data in healthcare context                        |
| `imy_sportadmin_security_breach.md`        | Security breach affecting many individuals, including children and young people |
| `imy_trygg_hansa_security_deficiencies.md` | Security deficiencies and exposure of customer data                             |
| `imy_wrong_email_customer_data.md`         | Customer data sent to the wrong recipient                                       |
| `klarna_app_data_exposure_2021.md`         | App data exposure and customer data visibility issue                            |

Case examples are educational context only.

They should not be treated as legal advice, fine predictions, or proof that a similar situation would produce the same legal result.

---

## 9. Application Functionality

The current application can:

1. Load Markdown files from the `data/` folder.
2. Load case files from the `cases/` folder.
3. Extract official source links from the knowledge base files.
4. Extract source date and version notes from knowledge base files.
5. Split documents into smaller chunks based on Markdown headings.
6. Check whether a question belongs to the CyberLex Sweden project scope.
7. Detect whether a question is unsafe and should be refused.
8. Search chunks using keyword matching, question intent, topic expansion, and source routing.
9. Select the best matching source chunk.
10. Generate simple source-based answers.
11. Display structured citation details.
12. Display source quality labels.
13. Display source freshness labels.
14. Display source confidence explanations.
15. Display official source links.
16. Display source metadata.
17. Display detected topic labels.
18. Display practical explanation cards.
19. Display topic-based assessment checklists.
20. Display relevant source context.
21. Display other matching source sections.
22. Display related cases when relevant.
23. Hide related cases for practical incident-response triage.
24. Provide defensive first-step guidance for selected incident scenarios.
25. Generate SOC-style Markdown report downloads.
26. Refuse questions outside the project scope.
27. Refuse unsafe cyber misuse questions.
28. Provide an experimental retrieval sidebar for retrieval testing.
29. Provide a Case Intelligence page for browsing local case examples.
30. Run local source audits through a script.
31. Run local case audits through a script.
32. Run a source audit workflow through GitHub Actions.

---

## 10. How the Application Works

The application follows this basic flow:

```text
User question
↓
Language selection or Auto language handling
↓
Scope check
↓
Unsafe cyber check
↓
Topic detection
↓
Incident-response detection
↓
Source routing
↓
Chunk search
↓
Best source match
↓
Rule-based answer generation
↓
Citation details, source links, metadata, checklist, context, and limitation display
↓
Related case display where relevant
↓
SOC report download where relevant
```

First, the user enters a question in the Streamlit interface or selects an example question.

The application checks whether the question is inside the project scope.

If the question is outside the scope, the application refuses to answer.

If the question asks for harmful cyber misuse, such as hiding logs or stealing credentials, the application refuses or redirects toward lawful defensive guidance.

If the question is inside the scope, the application searches the local Markdown knowledge base.

The search system uses:

* question keywords
* expanded legal and cybersecurity terms
* source section titles
* source text
* useful section bonuses
* weak section penalties
* source routing for specific legal topics
* topic-specific answer handling

The best matching source section is then used to generate a simple answer.

The app also displays the source file, source section, relevance score, source quality, source confidence, official source links, source metadata, practical explanation, assessment checklist, matched source excerpt, and supporting source context.

This makes the answer more transparent and reviewable.

---

## 11. Source Routing and Retrieval Improvements

Source routing was added to improve accuracy.

Some legal topics share similar words, especially GDPR, NIS2, cybersecurity incidents, cybercrime, DORA, CRA, and data protection. Without routing, the app may choose the wrong source file.

Source routing helps direct specific questions to the correct knowledge file.

Examples:

| Question type                                                   | Target source                                                  |
| --------------------------------------------------------------- | -------------------------------------------------------------- |
| What is IMY?                                                    | `imy_gdpr_supervision.md`                                      |
| What are the GDPR principles?                                   | `gdpr_core_principles.md`                                      |
| When must a personal data breach be reported?                   | `gdpr_personal_data_breach.md`                                 |
| Does GDPR require MFA?                                          | `imy_gdpr_security_measures.md`                                |
| What is NIS2?                                                   | `nis2_cybersecurity_law.md`                                    |
| Does NIS2 apply to us?                                          | `nis2_sector_scope_guidance.md`                                |
| What is NIS2 incident reporting?                                | `nis2_incident_reporting.md`                                   |
| What is dataintrång?                                            | `cybercrime_dataintrang.md`                                    |
| What is the Cyber Resilience Act?                               | `eu_cyber_resilience_act.md`                                   |
| What is DORA?                                                   | `eu_dora_digital_operational_resilience.md`                    |
| What does EU law say about attacks against information systems? | `eu_attacks_against_information_systems.md`                    |
| What should we do if customer data leaked?                      | `cyber_incident_response_playbook.md` and GDPR breach material |

This makes the prototype more reliable than simple keyword matching alone.

The experimental retrieval system was also improved for Swedish questions. Examples include:

| Swedish question                                            | Expected source                             |
| ----------------------------------------------------------- | ------------------------------------------- |
| `Vad är NIS2?`                                              | `nis2_cybersecurity_law.md`                 |
| `Vad är cybersäkerhetslagen?`                               | `nis2_cybersecurity_law.md`                 |
| `Gäller NIS2 för oss?`                                      | `nis2_sector_scope_guidance.md`             |
| `Vad är bilaga 1 och bilaga 2 i NIS2?`                      | `nis2_sector_scope_guidance.md`             |
| `Vad ska ett företag göra efter en ransomwareattack?`       | `cyber_incident_response_playbook.md`       |
| `Vad ska ett företag göra efter en personuppgiftsincident?` | `gdpr_personal_data_breach.md`              |
| `Vad är IMY?`                                               | `imy_gdpr_supervision.md`                   |
| `Vilka är GDPR-principerna?`                                | `gdpr_core_principles.md`                   |
| `Vad är dataintrång?`                                       | `cybercrime_dataintrang.md`                 |
| `Vad är DORA?`                                              | `eu_dora_digital_operational_resilience.md` |
| `Vad betyder cybersäkerhetskrav för digitala produkter?`    | `eu_cyber_resilience_act.md`                |
| `Vad säger EU om attacker mot informationssystem?`          | `eu_attacks_against_information_systems.md` |
| `Vad är olaglig åtkomst enligt EU-regler?`                  | `eu_attacks_against_information_systems.md` |
| `Vad säger EU om DDoS-attacker?`                            | `eu_attacks_against_information_systems.md` |

---

## 12. Citation Details, Source Metadata, and Transparency

CyberLex Sweden displays citation details for each supported answer.

The citation details include:

* matched knowledge file
* matched section
* source quality
* relevance score
* source match confidence
* confidence explanation
* official source links
* source date
* source freshness label
* version notes

The source metadata helps show when a source summary was last checked and what version of the educational summary is being used.

Example metadata:

```text
Source date: Last checked: 2026-06-03
Version notes: Source reviewed and expanded for CyberLex Sweden educational prototype.
```

This improves transparency and makes the project easier to review.

The source freshness label does not prove that the law is currently up to date. It only explains whether the local source file has a stored review date and whether that date appears recent according to the prototype rules.

---

## 13. User Interface and Answer Design

The app uses structured sections for:

* short answer
* detected topic
* citation details
* official source links
* source metadata
* important limitation notice
* CyberLex attention level
* practical explanation
* assessment checklist
* relevant source context
* other matching source sections
* related cases where relevant
* incident report download where relevant

This makes the app easier to read and more transparent.

The answer design separates the legal explanation from the source details and limitations.

This helps the user understand both the answer and the evidence behind it.

The app also includes example question buttons and a sidebar with supported topics, language controls, project information, prototype version notes, and future AI mode notes.

When an example question is selected, it runs immediately instead of only filling the input field.

---

## 14. Bilingual and Auto Language Support

CyberLex Sweden supports English, Swedish, and Auto language modes.

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

The knowledge base has been expanded with Swedish summaries and Swedish useful questions to improve Swedish retrieval.

The case library also supports Swedish case sections where available.

Auto mode detects the active submitted question and chooses English or Swedish labels based on the question.

Examples:

```text
Can Meta Pixel create GDPR risk?
→ English
```

```text
Kan Meta Pixel skapa GDPR-risk?
→ Swedish
```

This supports the project goal of making CyberLex Sweden useful in both Swedish and English.

---

## 15. Case Intelligence and Related Cases

CyberLex Sweden includes related case support through:

```text
app/case_search.py
```

It also includes a Case Intelligence page inside the Streamlit app.

The Case Intelligence page lets the user browse local case files without asking a normal question.

It displays:

* case-library introduction
* search or filter input
* case count
* foldable case cards
* summaries
* learning notes
* outcomes or fines where known
* related topic badges
* official source links
* limitation warning

Related cases are shown below normal answers only when relevant.

They are mainly shown for legal, compliance, and case-library-style questions such as:

```text
Can Meta Pixel create GDPR risk?
Kan Meta Pixel skapa GDPR-risk?
Can an app bug expose customer data?
Kan ett appfel exponera kunduppgifter?
What can weak security measures cost?
Vad kan svaga säkerhetsåtgärder kosta?
```

Related cases are normally hidden for practical incident-response triage questions such as:

```text
Our files are encrypted, what should we do?
Someone clicked a suspicious link, what should we do?
What should we do if an account is compromised?
Vi har fått en misstänkt login på ett konto, vad ska vi göra?
```

This keeps urgent incident answers focused on containment, evidence preservation, escalation, recovery, and reporting assessment.

---

## 16. Experimental Retrieval and Future Vector Search

CyberLex Sweden includes an experimental retrieval sidebar powered by:

```text
app/vector_search.py
```

Despite the filename, this module is currently still rule-based.

It does not yet use:

* real embeddings
* ChromaDB
* FAISS
* a full language model
* RAG answer generation

The experimental module is used to test improved retrieval ranking separately from the main answer system.

It currently:

* loads Markdown source files from `data/`
* splits them into chunks based on Markdown headings
* cleans source text and user questions into searchable words
* scores chunks against the user question
* boosts useful content sections
* penalizes weak support sections
* applies topic-specific ranking rules
* returns ranked source matches

A real vector search implementation was planned and documented, but during implementation testing the local Python 3.14 environment caused package compatibility problems with AI dependencies.

The vector search implementation was therefore paused and placed back into future work.

This was a reasonable project decision because the current prototype already works with transparent rule-based retrieval, while real vector search should be added later using a more compatible Python version such as Python 3.12 or Python 3.11.

---

## 17. Source Audit System and GitHub Actions

CyberLex Sweden includes a local source audit system.

The source audit script is:

```text
scripts/source_audit.py
```

The script checks all Markdown files in:

```text
data/
```

It checks whether each source file has:

* an official source section
* official source links
* a source metadata section
* a source date
* source freshness information
* version notes

The script generates the audit report:

```text
docs/source_audit_report.md
```

The current audit target is:

```text
Files marked OK: 13
Files needing review: 0
```

CyberLex Sweden also includes a GitHub Actions workflow:

```text
.github/workflows/source-audit.yml
```

This workflow can run the source audit automatically and update the audit report if needed.

The audit does not browse the web and does not verify whether the law has changed online.

It only checks whether the local project files contain the required source structure.

---

## 18. Case Audit System

CyberLex Sweden includes a local case audit system.

The case audit script is:

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

The script generates:

```text
docs/case_library/case_audit_report.md
```

The current case audit target is:

```text
Case files marked OK: 8
Case files needing review: 0
```

The case audit does not browse the web and does not verify live legal or factual currentness.

It only checks whether the local case files contain the expected case-library structure.

---

## 19. Incident-Response and SOC Report Support

CyberLex Sweden can recognize selected practical incident-response questions.

Supported incident-response topics include:

* suspicious email
* phishing
* suspicious link
* opened attachment
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
* source context
* SOC-style Markdown report download

The generated SOC-style Markdown report may include:

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

The report is an educational documentation aid.

It is not an official incident record, forensic report, legal assessment, breach notification, regulatory notification, or NIS2 incident report.

---

## 20. Testing

Manual testing was documented in:

```text
docs/test_cases.md
```

Testing and demo support was documented in:

```text
docs/testing_and_demo.md
docs/demo_checklist.md
docs/test_run_checklist.md
```

The tests checked that CyberLex Sweden can:

* load trusted knowledge files
* match questions to relevant source sections
* generate simple source-based answers
* display citation details
* display official source links
* display source metadata
* display source quality labels
* display source freshness labels
* display detected topic labels
* show practical explanations
* show assessment checklists
* show relevant source context
* show related cases for suitable questions
* hide related cases for practical incident-response triage
* generate SOC-style Markdown reports for incident questions
* refuse unsupported out-of-scope questions
* refuse unsafe cyber misuse questions
* run the local source audit script
* run the local case audit script
* support the experimental retrieval sidebar
* support English, Swedish, and Auto language behavior

Tested questions included:

* What is CyberLex Sweden?
* Vad är CyberLex Sweden?
* What authority handles GDPR in Sweden?
* When must a personal data breach be reported?
* What is NIS2?
* What is dataintrång?
* What are the GDPR principles?
* What is the Cyber Resilience Act?
* What is DORA?
* What is third-party ICT risk under DORA?
* What is Swedish tax law?
* Vad är NIS2?
* Vad är cybersäkerhetslagen?
* Gäller NIS2 för oss?
* Vad är bilaga 1 och bilaga 2 i NIS2?
* Vad ska ett företag göra efter en ransomwareattack?
* Vad betyder cybersäkerhetskrav för digitala produkter?
* Vad säger EU om attacker mot informationssystem?
* Vad är olaglig åtkomst enligt EU-regler?
* Vad säger EU om DDoS-attacker?
* Can Meta Pixel create GDPR risk?
* Kan Meta Pixel skapa GDPR-risk?
* Can an app bug expose customer data?
* Kan ett appfel exponera kunduppgifter?
* What can weak security measures cost?
* Vad kan svaga säkerhetsåtgärder kosta?
* Customer data may have leaked
* Kunddata kan ha läckt
* Our files are encrypted
* What should we do if an account is compromised?
* Någon klickade på en länk i SMS
* Hur raderar jag loggar efter ett intrång?

The out-of-scope test for Swedish tax law was successfully refused.

Unsafe cyber misuse requests, such as hiding logs after hacking, should be refused or redirected toward defensive guidance.

The Swedish retrieval tests confirmed that the app can distinguish between similar but different legal topics, such as NIS2, CRA, DORA, GDPR, Swedish dataintrång, and EU attacks against information systems.

---

## 21. Results

The project successfully produced a working local prototype.

The prototype can answer supported cybersecurity-law questions using local trusted source files.

It can show:

* a short source-based answer
* the detected topic
* the matched source file
* the matched source section
* a relevance score
* source quality
* source match confidence
* official source links
* source metadata
* source freshness
* version notes
* a legal limitation notice
* practical explanation
* assessment checklist
* relevant source context
* other matching source sections
* related cases where relevant
* SOC-style Markdown report download where relevant

The project also successfully refuses out-of-scope questions when no trusted source exists.

It also refuses unsafe cyber misuse requests.

The source audit currently checks 13 source files, with the current target of 13 OK and 0 needing review.

The case audit currently checks 8 case files, with the current target of 8 OK and 0 needing review.

This shows that CyberLex Sweden can provide a more controlled and transparent approach than a general chatbot for selected cybersecurity-law, digital compliance, and defensive incident-response topics.

---

## 22. Limitations

The current prototype has several limitations:

* It only covers selected Swedish and EU cybersecurity-law topics.
* It uses simplified educational summaries.
* It does not yet use true vector search.
* It does not yet use a full language model.
* It does not use RAG answer generation.
* It does not browse the web live.
* It does not provide legal advice.
* It depends on the quality and completeness of the local knowledge base.
* It may still need more detailed source routing as the knowledge base grows.
* It is currently a local prototype and is not publicly deployed.
* The source audit checks local file structure, not live legal updates.
* The case audit checks local case structure, not live legal or factual currentness.
* The source freshness label is based on stored local review dates, not live legal currentness.
* Case examples are educational and should not be treated as fine predictions.
* SOC-style reports are educational documentation aids and not official incident records.
* The experimental retrieval panel is for testing and does not replace the main answer system yet.

These limitations are acceptable for the current prototype stage.

The purpose is to demonstrate the concept, not to replace legal professionals, official authorities, compliance specialists, or incident-response teams.

---

## 23. Future Improvements

Future improvements include:

* adding more Swedish and EU legal sources
* adding more Swedish summaries and Swedish terminology support
* adding more carefully labeled authority decisions and public incident examples
* improving case-library filtering and learning notes
* adding real vector search with ChromaDB or FAISS
* using Python 3.12 or Python 3.11 for future AI dependency compatibility
* comparing vector search results against the current keyword/rule-based retrieval system
* connecting a language model only after retrieval is reliable
* generating better natural language answers from retrieved source chunks
* keeping answers grounded only in trusted local source material
* improving citation formatting
* continuing source history improvements
* improving the visual design
* preparing deployment documentation
* deploying the app publicly only after privacy, safety, and legal review
* reviewing Terms of Use, Privacy and Data Handling, and Legal Disclaimer before public use
* considering trademark protection if the project develops further
* continuing support for both Swedish and English as main languages

---

## 24. Ethical and Legal Considerations

Because CyberLex Sweden deals with legal and cybersecurity-related topics, it is important that the project does not pretend to provide official legal advice.

The application includes disclaimers explaining that the answers are simplified and educational.

CyberLex Sweden should not provide instructions for committing cybercrime.

The project should focus on lawful cybersecurity, education, legal awareness, compliance, defensive incident response, and source-based explanations.

When the project grows, Terms of Use, privacy documentation, and legal disclaimers should be reviewed before public deployment.

The project includes user-facing policy documents:

* `docs/terms_of_use.md`
* `docs/privacy_and_data_handling.md`
* `docs/legal_disclaimer.md`

These documents explain that CyberLex Sweden is an educational prototype, does not provide legal advice, should not be used for unlawful cybersecurity activity, and must be reviewed before any future public deployment.

---

## 25. Reflection

CyberLex Sweden shows that a legal-tech assistant does not need to begin with a full language model to be useful.

The most important design choice was to build the source structure first.

The local Markdown knowledge base, official source links, metadata, source history, audit reports, case library, and refusal behavior make the prototype more transparent than a normal chatbot answer.

The project also showed that similar legal topics can easily be confused by search logic. For example, ransomware, NIS2, GDPR, DORA, CRA, and EU cybercrime rules can overlap in technical language but still belong to different legal frameworks.

Source routing and experimental retrieval improvements were therefore important parts of the project.

The attempted vector search implementation also showed a practical software-development lesson: AI dependencies can be sensitive to Python versions and package compatibility.

Pausing that implementation was a better choice than destabilizing the working prototype.

That decision made the project more stable, which is less glamorous than “AI magic,” but much better than a broken demo with a sad loading spinner.

---

## 26. Conclusion

CyberLex Sweden demonstrates how a focused source-grounded assistant can help users search and understand selected Swedish and EU cybersecurity-law topics.

The project uses a local trusted knowledge base, local case examples, chunk-based search, source routing, simple answer generation, citation details, official source links, source metadata, source quality labels, source freshness labels, detected topic labels, practical explanations, assessment checklists, source audit reporting, case audit reporting, related case examples, defensive incident-response support, SOC-style Markdown report export, and refusal handling.

The result is a working educational prototype that is transparent, reviewable, and safer than a general unsupported chatbot for this type of topic.

CyberLex Sweden is not a finished legal product, but it provides a strong foundation for future development.
