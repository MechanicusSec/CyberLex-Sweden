# CyberLex Sweden Final Report

## Project Title

CyberLex Sweden: A Source-Grounded Assistant Prototype for Swedish Cybersecurity Law, Digital Compliance, and Defensive Incident Response

## Student

CyberLex Sweden project author

## Project Type

Komvuxarbete / final school project with IT, network technician, cybersecurity, and digital compliance focus.

---

## Project Summary

CyberLex Sweden is a local educational prototype built as a Streamlit application. The project focuses on Swedish and EU cybersecurity law, digital compliance, GDPR, NIS2, DORA, the Cyber Resilience Act, Swedish cybercrime law, personal data breaches, selected case examples, and defensive incident-response learning.

The goal of the project was to create a source-grounded support tool that helps users search, understand, and review selected cybersecurity-law and incident-response information in a transparent way. Instead of using unsupported AI-generated legal answers, CyberLex Sweden uses a trusted local Markdown knowledge base, local case files, source routing, keyword-based retrieval, official source links, source metadata, case examples, and clear limitations.

The current prototype includes a working local Streamlit interface, Swedish and English support, source-grounded answers, Case Intelligence, related case examples, incident-response guidance, SOC-style Markdown incident report export, local source and case audits, automated tests, and GitHub Actions workflows.

CyberLex Sweden is an educational prototype. It does **not** provide legal advice and does not replace official authority guidance, qualified legal review, compliance review, a data protection officer, or professional incident-response support.

---

## Source Quality Policy

CyberLex Sweden follows a source-first design.

The project prioritizes:

* official Swedish authority sources
* official EU legal and regulatory sources
* official government or public-sector information
* defensive cybersecurity guidance
* clear source references
* readable official source links
* source dates and metadata
* source history and version notes
* refusal when no trusted local source exists

The guiding principle is:

```text
Better sources first. Better AI second.
```

This is important because legal, privacy, compliance, and cybersecurity topics can be risky if an application gives unsupported or unclear answers.

The source policy and source history are documented in:

```text
docs/source_policy.md
docs/source_history.md
```

---

## 1. Background

Cybersecurity law can be difficult to understand because relevant information is spread across many different places.

These sources can include:

* Swedish laws
* EU regulations and directives
* Swedish government agencies
* cybersecurity authorities
* data protection authorities
* public authority decisions
* official legal databases
* practical incident-response guidance

For IT students, network technician students, IT support staff, and smaller organizations, it can be difficult to quickly understand which rules may be relevant after a cyber incident or in a digital compliance situation.

A general chatbot may answer confidently without showing legal sources or separating legal guidance from historical case examples. That is risky for legal, compliance, privacy, and cybersecurity topics.

CyberLex Sweden was created to test a more transparent approach: answers should be based on selected local source material, and users should be able to see which source file and source section supported the answer.

---

## 2. Connection to Network Technician Education

CyberLex Sweden connects to the network technician and IT support area because modern network and IT work is not only about hardware, cabling, servers, and configuration. It also involves cybersecurity, incident handling, documentation, user guidance, privacy awareness, and understanding rules that affect IT environments.

The project demonstrates several skills relevant to a network technician direction:

* planning a technical project
* setting up and running a local application environment
* using Python, Streamlit, Git, GitHub, PowerShell, and VS Code
* organizing technical source files and documentation
* reading and using Swedish and English technical/legal source material
* documenting project work and technical decisions
* testing and troubleshooting a local application
* using version control and GitHub workflows
* understanding cybersecurity-law topics that may affect IT support work
* supporting defensive incident-response thinking
* creating structured incident documentation
* refusing unsafe cyber misuse requests

The project should therefore be understood as a cybersecurity-law and incident-response support prototype for IT and network support learning, not as a production legal-advice system.

---

## 3. Problem Description

The main problem is that cybersecurity-related legal information is often:

* spread across several authorities and legal sources
* written in complex legal or administrative language
* difficult to search without knowing exact legal terms
* risky to summarize incorrectly
* connected to overlapping legal frameworks such as GDPR, NIS2, DORA, CRA, and criminal law
* mixed with practical incident-response questions in real IT work

CyberLex Sweden tries to reduce this risk by using a local trusted knowledge base and by showing the source file, source section, official source links, source metadata, and limitations for supported answers.

The prototype does not try to replace a lawyer, court, authority, compliance specialist, data protection officer, or professional incident-response team.

---

## 4. Project Goal

The goal was to build a working local prototype that can:

* load trusted local knowledge base files
* search legal and cybersecurity information by topic
* split Markdown source files into searchable sections
* match user questions to relevant source sections
* route specific questions to stronger source files
* generate simple source-based answers
* show the source file and source section used
* display official source links and source metadata
* display source quality and freshness labels
* show practical explanations and assessment checklists
* support English, Swedish, and Auto language behavior
* support selected defensive incident-response scenarios
* generate SOC-style Markdown incident summaries
* show related case examples where relevant
* provide a Case Intelligence page for browsing cases
* provide Case Intelligence filters and comparison view
* refuse unsupported out-of-scope questions
* refuse unsafe cyber misuse requests
* audit local source files and case files
* run automated tests

---

## 5. Scope

The prototype covers selected Swedish and EU cybersecurity-law, digital compliance, case-library, and defensive incident-response topics.

The current legal and compliance scope includes:

* GDPR and personal data breach notification
* IMY and Swedish GDPR supervision
* GDPR core principles and security measures
* NIS2 and the Swedish Cybersecurity Act
* NIS2 sector scope and incident reporting
* Swedish cybercrime law and `dataintrång`
* EU attacks against information systems
* EU Cyber Resilience Act
* EU DORA
* selected digital compliance and cybersecurity-related legal topics

The case-library scope includes selected examples related to:

* GDPR risks
* Meta Pixel and tracking technologies
* profiling and marketing
* app data exposure
* wrong-recipient disclosures
* weak security measures
* public incident examples
* authority decisions and public outcomes where available

The incident-response scope includes selected defensive scenarios related to:

* suspicious email and phishing
* suspicious links
* suspicious login activity
* compromised accounts
* data leaks
* possible personal data breaches
* ransomware and malware
* encrypted files
* suspected hacking or intrusion

The prototype does not cover all Swedish law or all EU law. A question about Swedish tax law, for example, should be refused because it is outside the project scope.

---

## 6. Tools and Technologies

### Visual Studio Code

Visual Studio Code was used as the main editor for Python code, Markdown documentation, source files, case files, tests, and reports.

### Python

Python was used as the main programming language for the application, scripts, tests, and automation.

### Streamlit

Streamlit was used to create the local web interface. It provides the browser-based UI, input fields, sidebars, formatted answer sections, expanders, warnings, download buttons, and case browsing pages.

### Markdown

Markdown was used for the knowledge base, case library, documentation, logbook, and generated SOC-style incident reports.

### Git and GitHub

Git was used for version control. GitHub was used to store the project online, show project history, and run automation workflows.

### GitHub Actions

GitHub Actions was used for automated tests, source audit, and source watch workflows.

### Pytest

`pytest` was used for automated regression tests covering important logic such as routing, language detection, incident detection, SOC report generation, and source-context behavior.

---

## 7. Project Structure

The project is organized into several folders:

```text
CyberLex-Sweden/
├── .github/
│   └── workflows/
├── app/
│   ├── main.py
│   ├── routing.py
│   ├── incident_engine.py
│   ├── incident_reports.py
│   ├── source_loader.py
│   ├── source_context.py
│   ├── case_search.py
│   └── other app modules
├── cases/
│   └── local case-library Markdown files
├── data/
│   └── local Markdown knowledge base files
├── docs/
│   └── project documentation and generated reports
├── report/
│   └── final_report.md
├── screenshots/
├── scripts/
│   ├── source_audit.py
│   ├── source_watch.py
│   └── case_audit.py
├── source_snapshots/
├── tests/
├── README.md
└── requirements.txt
```

This structure separates application logic, source material, case examples, documentation, tests, scripts, and reports.

---

## 8. Knowledge Base

CyberLex Sweden uses local Markdown files as its trusted knowledge base.

The `data/` folder contains source material about:

* GDPR and personal data breaches
* IMY supervision and security measures
* NIS2 and incident reporting
* DORA
* Cyber Resilience Act
* Swedish cybercrime law and unauthorized access
* EU attacks against information systems
* defensive incident response

Each source file is structured with sections such as:

* topic
* main authority or legal source
* key idea
* important points
* practical explanation or checklist
* useful questions
* official source links
* source metadata
* disclaimer or limitation notes

This structure makes it easier for the app to search, display, audit, and update relevant source sections.

---

## 9. Case Library

CyberLex Sweden includes a separate local case library in the `cases/` folder.

The distinction is important:

```text
data/
= legal, regulatory, authority, cybersecurity, and defensive incident-response source material

cases/
= educational examples, authority decisions, public incident examples, outcomes, fines, learning notes, and related case context
```

The case library includes examples involving:

* Apoteket/Apohem Meta Pixel
* Avanza Meta Pixel
* Equality Ombudsman web form
* Kry Meta Pixel
* Miljödata data leak
* Region Skåne USB security case
* SL/WÅAB alcohol testing
* Sportadmin security breach
* Spotify access request
* Statens servicecenter breach notification
* Trygg-Hansa security deficiencies
* Indecap wrong-email customer data
* Klarna app data exposure
* Bonnier News profiling sanction

These cases are educational context only. They should not be treated as legal advice, fine predictions, or proof that a similar situation would produce the same result.

---

## 10. Application Functionality

The current application can:

1. Load Markdown source files from `data/`.
2. Load case files from `cases/`.
3. Extract official source links and metadata.
4. Split documents into searchable chunks.
5. Check whether a question belongs to the project scope.
6. Detect unsafe cyber misuse questions.
7. Search chunks using keyword matching, question intent, topic expansion, and source routing.
8. Generate simple source-based answers.
9. Display citation details, source links, metadata, quality labels, freshness labels, and confidence explanations.
10. Display detected topic labels, practical explanation cards, assessment checklists, and source context.
11. Display related cases where relevant.
12. Hide related cases for practical incident-response triage questions.
13. Provide defensive first-step guidance for selected incident scenarios.
14. Generate SOC-style Markdown report downloads for practical incident questions.
15. Refuse out-of-scope questions.
16. Refuse unsafe cyber misuse requests.
17. Provide a Case Intelligence page for browsing local case examples.
18. Provide Case Intelligence filters and comparison view.
19. Run local source, case, and source-watch checks.
20. Run automated tests locally and through GitHub Actions.

---

## 11. How the Application Works

The application follows this basic flow:

```text
User question
↓
Language selection or Auto language detection
↓
Scope and unsafe-request checks
↓
Topic and incident-response detection
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

The application is rule-based and source-grounded. It does not browse the web live during the answer flow and does not use an external AI API for answer generation.

---

## 12. Source Routing and Retrieval

Source routing was added to improve accuracy.

Some topics share similar terms, especially GDPR, NIS2, cybersecurity incidents, cybercrime, DORA, CRA, and data protection. Without routing, the app may choose the wrong source file.

Routing helps direct specific questions to the correct source.

Examples:

| Question type | Target source |
| --- | --- |
| What are the GDPR principles? | `gdpr_core_principles.md` |
| When must a personal data breach be reported? | `gdpr_personal_data_breach.md` |
| Does GDPR require MFA? | `imy_gdpr_security_measures.md` |
| What is NIS2? | `nis2_cybersecurity_law.md` |
| Does NIS2 apply to us? | `nis2_sector_scope_guidance.md` |
| What is dataintrång? | `cybercrime_dataintrang.md` |
| What is DORA? | `eu_dora_digital_operational_resilience.md` |
| What should we do if customer data leaked? | `cyber_incident_response_playbook.md` and GDPR breach material |

This makes the prototype more reliable than simple keyword matching alone.

---

## 13. Bilingual and Auto Language Support

CyberLex Sweden supports English, Swedish, and Auto language modes.

The app can display English or Swedish labels, limitation notices, topic labels, case summaries, source labels, and case sections where available.

Auto mode detects the active submitted question and chooses English or Swedish display logic based on the question.

Examples:

```text
Can Meta Pixel create GDPR risk?
→ English
```

```text
Kan Meta Pixel skapa GDPR-risk?
→ Swedish
```

This supports the project goal of making CyberLex Sweden useful in both Swedish and English contexts.

---

## 14. Case Intelligence and Related Cases

CyberLex Sweden includes related case support through:

```text
app/case_search.py
```

The Case Intelligence page allows users to browse local case files without asking a normal question.

It displays:

* case-library introduction
* case search
* case filters
* case count
* foldable case cards
* summaries
* learning notes
* outcomes or fines where known
* related topic badges
* official source links
* optional comparison table
* warning that outcomes and amounts are historical examples only

Related cases are shown below normal answers only when relevant.

They are mainly shown for legal, compliance, and case-library-style questions such as:

```text
Can Meta Pixel create GDPR risk?
Kan Meta Pixel skapa GDPR-risk?
Can an app bug expose customer data?
Kan ett appfel exponera kunduppgifter?
What can weak security measures cost?
Vad kan svaga säkerhetsåtgärder kosta?
Does profiling require consent?
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

## 15. Source, Case, and Test Automation

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

They cover core logic such as:

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

## 16. Incident-Response and SOC Report Support

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

The generated report is an educational documentation aid. It is not an official incident record, forensic report, legal assessment, breach notification, regulatory notification, or NIS2 incident report.

---

## 17. Testing

Testing was done through manual testing, local scripts, and automated tests.

Manual testing covered:

* app startup
* English, Swedish, and Auto language behavior
* example questions
* source-grounded answers
* source metadata and official links
* practical incident-response questions
* SOC-style report generation
* Case Intelligence page behavior
* case filters and comparison view
* related case behavior
* hidden related cases for urgent incident triage
* out-of-scope refusal
* unsafe cyber refusal

Automated tests were run with:

```powershell
python -m pytest
```

The expected current result is:

```text
50 passed
```

Audits can be run with:

```powershell
python scripts/source_watch.py
python scripts/source_audit.py
python scripts/case_audit.py
```

The source audit checks local source-file structure.

The case audit checks local case-file structure.

The source watch checks official source URLs and reports possible changes or failed checks.

---

## 18. Results

The project successfully produced a working local prototype.

The prototype can:

* answer selected cybersecurity-law questions using local trusted source files
* show source file, section, metadata, and official source links
* support Swedish and English display logic
* provide selected defensive incident-response guidance
* generate SOC-style Markdown reports for practical incident questions
* show related case examples where relevant
* browse case examples through Case Intelligence
* filter and compare case examples
* refuse out-of-scope questions
* refuse unsafe cyber misuse requests
* run local source and case audits
* run automated tests

This shows that CyberLex Sweden can provide a more controlled and transparent approach than a general chatbot for selected cybersecurity-law, digital compliance, and defensive incident-response topics.

---

## 19. Ethical, Legal, Privacy, and Security Considerations

Because CyberLex Sweden deals with legal and cybersecurity-related topics, it must not pretend to provide official legal advice.

The project includes disclaimers explaining that the answers are simplified and educational.

CyberLex Sweden should not provide instructions for committing cybercrime or hiding unauthorized activity.

The project is designed for lawful cybersecurity, education, legal awareness, compliance, defensive incident response, and source-based explanations.

Privacy and safety considerations include:

* the app is currently local
* no production database storage is implemented
* no user-account system is implemented
* no intentional analytics or telemetry is implemented by the app
* no external AI API is required for the current rule-based prototype
* users should avoid entering real sensitive incident data
* downloaded SOC-style reports are educational documentation aids
* case examples are not fine predictions
* source freshness labels are not legal currentness guarantees

The project includes user-facing policy documents:

* `docs/terms_of_use.md`
* `docs/privacy_and_data_handling.md`
* `docs/legal_disclaimer.md`

---

## 20. Limitations

The current prototype has several limitations:

* it only covers selected Swedish and EU cybersecurity-law topics
* it uses simplified educational summaries
* it does not use true vector search
* it does not use a full language model
* it does not use RAG answer generation
* it does not browse the web live during answers
* it does not provide legal advice
* it depends on the quality and completeness of the local knowledge base
* source material must be manually reviewed and updated
* it is a local prototype and is not publicly deployed
* the source audit checks local file structure, not live legal updates
* the case audit checks local case structure, not live legal or factual currentness
* the source freshness label is based on stored local review dates
* case examples are educational and should not be treated as fine predictions
* SOC-style reports are educational documentation aids, not official incident records
* the automated tests do not cover the full Streamlit UI

These limitations are acceptable for the current prototype stage.

The purpose is to demonstrate the concept, not to replace legal professionals, authorities, compliance specialists, or incident-response teams.

---

## 21. Future Improvements

Future improvements could include:

* adding more Swedish and EU legal sources
* adding more carefully labeled authority decisions and public incident examples
* improving Swedish and English source summaries
* adding true vector search with ChromaDB or FAISS
* using Python 3.12 or Python 3.11 for future AI dependency compatibility
* comparing vector search against current keyword/rule-based retrieval
* connecting a language model only after retrieval is reliable
* keeping answers grounded only in trusted local source material
* improving citation formatting and multi-source synthesis
* improving case comparison and filtering
* continuing to reduce large UI and routing logic in `app/main.py`
* improving visual design
* preparing deployment documentation
* reviewing privacy, safety, and legal requirements before any public deployment

---

## 22. Reflection

CyberLex Sweden shows that a useful educational assistant does not need to start with a full language model.

The most important design choice was to build the source structure first.

The local Markdown knowledge base, official source links, metadata, source history, audit reports, case library, refusal behavior, and tests make the prototype more transparent than a normal unsupported chatbot answer.

The project also showed that similar legal topics can easily be confused by search logic. For example, ransomware, NIS2, GDPR, DORA, CRA, and cybercrime can overlap in technical wording but still belong to different legal frameworks.

Source routing and rule-based retrieval were therefore important parts of the project.

The attempted vector-search planning also showed a practical software-development lesson: AI dependencies can be sensitive to Python versions and package compatibility. Pausing that work was better than destabilizing the working prototype.

That decision made the project more stable, which was more important than adding impressive but unreliable AI features.

---

## 23. Conclusion

CyberLex Sweden demonstrates how a focused source-grounded assistant can help users search and understand selected Swedish and EU cybersecurity-law topics.

The project uses a local trusted knowledge base, local case examples, source routing, rule-based search, source metadata, official source links, practical explanations, assessment checklists, Case Intelligence, defensive incident-response support, SOC-style Markdown report export, source/case audit scripts, automated tests, and safety refusals.

The result is a working educational prototype that is transparent, reviewable, and safer than a general unsupported chatbot for this type of topic.

CyberLex Sweden is not a finished legal product, but it provides a strong foundation for future development and demonstrates practical skills relevant to IT, network support, cybersecurity awareness, documentation, testing, and digital compliance.

---

## 24. Suggested Appendices

The following files can be used as appendices or supporting evidence:

* `README.md`
* `docs/project_overview.md`
* `docs/technical_design.md`
* `docs/source_list.md`
* `docs/source_policy.md`
* `docs/source_audit_report.md`
* `docs/source_watch_report.md`
* `docs/case_library/case_audit_report.md`
* `docs/test_cases.md`
* `docs/testing_and_demo.md`
* `docs/privacy_and_data_handling.md`
* `docs/legal_disclaimer.md`
* `docs/terms_of_use.md`
* selected screenshots from `screenshots/`
* GitHub commit history
* pytest output
