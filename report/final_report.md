# CyberLex Sweden Final Report

## Project Title

CyberLex Sweden: An AI-Style Assistant Prototype for Swedish Cybersecurity Law and Digital Compliance

## Student

Robert Banderby

---

## Project Summary

CyberLex Sweden is a final school project focused on building an AI-style assistant prototype for Swedish cybersecurity law and digital compliance.

The goal of the project is to make selected Swedish and EU cybersecurity-law information easier to search, understand, and review by using a trusted local Markdown knowledge base, source-based retrieval, simple answer generation, official source links, source metadata, citation details, source quality labels, source freshness labels, detected topic labels, practical explanations, and assessment checklists.

The current prototype focuses on selected Swedish and EU cybersecurity-related legal topics, including GDPR, IMY, NIS2, the Swedish Cybersecurity Act, Swedish cybercrime law and dataintrång, EU attacks against information systems, the Cyber Resilience Act, and DORA.

CyberLex Sweden is an educational prototype. It does not provide official legal advice and should not replace official authority guidance, qualified legal advice, or professional compliance review.

---

## Source Quality Policy

CyberLex Sweden includes a source policy and a source update history documented in:

```text
docs/source_policy.md
docs/source_update_history.md
```

The purpose of the source quality policy is to make sure that the project uses trusted and traceable legal or authority-based sources.

The project prioritizes:

- official government sources
- official Swedish authority sources
- official EU legal sources
- clear source references
- readable official source links
- source dates
- version notes
- educational summaries that can be reviewed
- source update history
- refusal when no trusted local source exists

This is important because legal and cybersecurity topics can be risky if an application gives unsupported or unclear answers.

---

## 1. Background

Cybersecurity law can be difficult to understand because relevant information is spread across many different sources.

These sources can include:

- Swedish laws
- EU regulations
- EU directives
- Swedish government agencies
- cybersecurity authorities
- data protection authorities
- official legal databases

For students, IT workers, and smaller organizations, it can be difficult to quickly understand which rules may apply in a cyber incident or digital compliance situation.

A normal chatbot may give confident but unsupported answers. This is especially risky in legal and compliance topics.

CyberLex Sweden was created as a prototype to explore how an AI-style assistant could help users find and understand selected cybersecurity-law information in a safer and more transparent way.

---

## 2. Problem Description

The main problem is that cybersecurity-related legal information is often:

- spread across several authorities and legal sources
- written in complex legal or administrative language
- difficult to search without knowing the exact legal terms
- risky to summarize incorrectly
- unsuitable for unsupported AI guessing
- connected to overlapping legal frameworks such as GDPR, NIS2, DORA, CRA, and criminal law

CyberLex Sweden tries to reduce that risk by using a local trusted knowledge base and showing which source file and source section were used for each answer.

The prototype does not try to replace a lawyer, court, authority, or official legal source.

---

## 3. Project Goal

The goal of the project was to build a working prototype that can:

- load trusted local knowledge base files
- search legal and cybersecurity information by topic
- split Markdown source files into searchable chunks
- match user questions to relevant source sections
- route specific questions to the correct knowledge file
- generate simple source-based answers
- show the source file and source section used
- display structured citation details
- display official source links
- display source metadata
- display source quality labels
- display source freshness labels
- display source match confidence explanations
- display detected topic labels
- show relevant source context and other matching source sections
- provide practical explanations and assessment checklists
- support both English and Swedish interface labels
- refuse unsupported out-of-scope questions
- audit the local source files for required source structure

---

## 4. Scope

The current prototype covers a limited set of Swedish and EU cybersecurity-law topics.

The current scope includes:

- GDPR and personal data breach notification in Sweden
- IMY and Swedish GDPR supervision
- GDPR core principles
- NIS2 and the Swedish Cybersecurity Act
- NIS2 incident reporting
- Swedish cybercrime law and dataintrång
- EU attacks against information systems
- EU Cyber Resilience Act
- EU DORA, the Digital Operational Resilience Act
- digital compliance and cybersecurity-related legal topics

The prototype does not cover all Swedish law.

For example, a question about Swedish tax law should be refused because it is outside the CyberLex Sweden project scope.

---

## 5. Tools and Technologies

### Visual Studio Code

Visual Studio Code was used as the main code editor.

It was used to write:

- Python code
- Markdown documentation
- source files
- test cases
- the final report

### Python

Python was used as the main programming language for the application.

Python was chosen because it is widely used for web prototypes, automation, data processing, and AI-related projects.

### Streamlit

Streamlit was used to create the local web application.

Streamlit makes it possible to turn a Python script into a browser-based interface with input fields, sidebars, formatted text, warnings, cards, buttons, expanders, and result sections.

### Markdown

Markdown was used for documentation and knowledge base files.

Markdown is simple to read and works well for GitHub documentation, structured notes, and source-based text files.

### Git

Git was used for version control.

Git tracks changes in the project and creates a development history through commits.

### GitHub

GitHub was used to store the project online.

GitHub makes it possible to show the code, documentation, project history, commits, and GitHub Actions workflow runs.

### GitHub Actions

GitHub Actions was added for a weekly source audit workflow.

The workflow runs the local source audit script and can update the generated source audit report.

---

## 6. Project Structure

The project is organized into several folders:

```text
CyberLex-Sweden
├── app
│   ├── main.py
│   └── vector_search.py
├── data
│   ├── cybercrime_dataintrang.md
│   ├── eu_attacks_against_information_systems.md
│   ├── eu_cyber_resilience_act.md
│   ├── eu_dora_digital_operational_resilience.md
│   ├── gdpr_core_principles.md
│   ├── gdpr_personal_data_breach.md
│   ├── imy_gdpr_supervision.md
│   ├── nis2_cybersecurity_law.md
│   └── nis2_incident_reporting.md
├── docs
│   ├── ai_rag_plan.md
│   ├── legal_disclaimer.md
│   ├── privacy_policy.md
│   ├── product_roadmap.md
│   ├── project_overview.md
│   ├── project_plan.md
│   ├── source_audit_report.md
│   ├── source_list.md
│   ├── source_policy.md
│   ├── source_update_history.md
│   ├── technical_design.md
│   ├── terms_of_use.md
│   ├── test_cases.md
│   └── vector_search_plan.md
├── report
│   └── final_report.md
├── screenshots
├── scripts
│   ├── add_missing_metadata.py
│   └── source_audit.py
├── sources
│   └── notes
├── .github
│   └── workflows
│       └── source-audit.yml
├── .gitignore
├── COPYRIGHT.md
├── README.md
└── requirements.txt
```

---

## 7. Knowledge Base

CyberLex Sweden uses local Markdown files as its trusted knowledge base.

Each file in the `data` folder represents one legal or regulatory topic.

The current knowledge base includes:

| File | Topic |
|---|---|
| `gdpr_personal_data_breach.md` | GDPR personal data breaches and IMY breach notification |
| `imy_gdpr_supervision.md` | IMY and Swedish GDPR supervision |
| `gdpr_core_principles.md` | GDPR core principles |
| `nis2_cybersecurity_law.md` | NIS2 and the Swedish Cybersecurity Act |
| `nis2_incident_reporting.md` | NIS2 incident reporting in Sweden |
| `cybercrime_dataintrang.md` | Swedish cybercrime law and dataintrång |
| `eu_attacks_against_information_systems.md` | EU rules on attacks against information systems |
| `eu_cyber_resilience_act.md` | EU Cyber Resilience Act |
| `eu_dora_digital_operational_resilience.md` | EU DORA and financial-sector digital operational resilience |

Each knowledge file is structured with headings such as:

- Topic
- Main authority or legal source
- Key idea
- Important points
- Cybersecurity connection
- Swedish summary
- Assessment checklist
- Useful questions
- Swedish useful questions
- Official source
- Source metadata
- Disclaimer

This structure makes it easier for the app to search, display, audit, and update relevant source sections.

---

## 8. Application Functionality

The current application can:

1. Load Markdown files from the `data` folder.
2. Extract official source links from the knowledge base files.
3. Extract source date and version notes from knowledge base files.
4. Split documents into smaller chunks based on Markdown headings.
5. Check whether a question belongs to the CyberLex Sweden project scope.
6. Search chunks using keyword matching, question intent, topic expansion, and source routing.
7. Select the best matching source chunk.
8. Generate simple source-based answers.
9. Display structured citation details.
10. Display source quality labels.
11. Display source freshness labels.
12. Display source confidence explanations.
13. Display official source links.
14. Display source metadata.
15. Display detected topic labels.
16. Display practical explanation cards.
17. Display topic-based assessment checklists.
18. Display relevant source context.
19. Display other matching source sections.
20. Refuse questions outside the project scope.
21. Provide an experimental AI search sidebar for retrieval testing.
22. Run local source audits through a script.
23. Run a weekly source audit workflow through GitHub Actions.

---

## 9. How the Application Works

The application follows this basic flow:

```text
User question
↓
Language selection or auto language handling
↓
Scope check
↓
Topic detection
↓
Source routing
↓
Chunk search
↓
Best source match
↓
Rule-based answer generation
↓
Citation details, source links, metadata, checklist, and context display
```

First, the user enters a question in the Streamlit interface.

The application checks whether the question is inside the project scope.

If the question is outside the scope, the application refuses to answer.

If the question is inside the scope, the application searches the local Markdown knowledge base.

The search system uses:

- question keywords
- expanded legal and cybersecurity terms
- source section titles
- source text
- useful section bonuses
- weak section penalties
- source routing for specific legal topics
- topic-specific answer handling

The best matching source section is then used to generate a simple answer.

The app also displays the source file, source section, relevance score, source quality, source confidence, official source links, source metadata, practical explanation, assessment checklist, matched source excerpt, and supporting source context.

This makes the answer more transparent and reviewable.

---

## 10. Source Routing and Retrieval Improvements

Source routing was added to improve accuracy.

Some legal topics share similar words, especially GDPR, NIS2, cybersecurity incidents, cybercrime, DORA, CRA, and data protection. Without routing, the app may choose the wrong source file.

Source routing helps direct specific questions to the correct knowledge file.

Examples:

| Question type | Target source |
|---|---|
| What is IMY? | `imy_gdpr_supervision.md` |
| What are the GDPR principles? | `gdpr_core_principles.md` |
| When must a personal data breach be reported? | `gdpr_personal_data_breach.md` |
| What is NIS2? | `nis2_cybersecurity_law.md` |
| What is NIS2 incident reporting? | `nis2_incident_reporting.md` |
| What is dataintrång? | `cybercrime_dataintrang.md` |
| What is the Cyber Resilience Act? | `eu_cyber_resilience_act.md` |
| What is DORA? | `eu_dora_digital_operational_resilience.md` |
| What does EU law say about attacks against information systems? | `eu_attacks_against_information_systems.md` |

This makes the prototype more reliable than simple keyword matching alone.

The experimental retrieval system was also improved for Swedish questions. Examples include:

| Swedish question | Expected source |
|---|---|
| `Vad är NIS2?` | `nis2_cybersecurity_law.md` |
| `Vad är cybersäkerhetslagen?` | `nis2_cybersecurity_law.md` |
| `Vad ska ett företag göra efter en ransomwareattack?` | `nis2_incident_reporting.md` |
| `Vad ska ett företag göra efter en personuppgiftsincident?` | `gdpr_personal_data_breach.md` |
| `Vad är IMY?` | `imy_gdpr_supervision.md` |
| `Vilka är GDPR-principerna?` | `gdpr_core_principles.md` |
| `Vad är dataintrång?` | `cybercrime_dataintrang.md` |
| `Vad är DORA?` | `eu_dora_digital_operational_resilience.md` |
| `Vad betyder cybersäkerhetskrav för digitala produkter?` | `eu_cyber_resilience_act.md` |
| `Vad säger EU om attacker mot informationssystem?` | `eu_attacks_against_information_systems.md` |
| `Vad är olaglig åtkomst enligt EU-regler?` | `eu_attacks_against_information_systems.md` |
| `Vad säger EU om DDoS-attacker?` | `eu_attacks_against_information_systems.md` |

---

## 11. Citation Details, Source Metadata, and Transparency

CyberLex Sweden displays citation details for each supported answer.

The citation details include:

- matched knowledge file
- matched section
- source quality
- relevance score
- source match confidence
- confidence explanation
- official source links
- source date
- source freshness label
- version notes

The source metadata helps show when a source summary was last checked and what version of the educational summary is being used.

Example metadata:

```text
Source date: Last checked: 2026-06-03
Version notes: Source reviewed and expanded for CyberLex Sweden educational prototype.
```

This improves transparency and makes the project easier to review.

The source freshness label does not prove that the law is currently up to date. It only explains whether the local source file has a stored review date and whether that date appears recent according to the prototype rules.

---

## 12. User Interface and Answer Design

Prototype version 0.5 improved the interface and answer layout.

The app now uses styled sections for:

- short answer
- detected topic
- citation details
- official source links
- source metadata
- important limitation notice
- CyberLex attention level
- practical explanation
- assessment checklist
- relevant source context
- other matching source sections

This makes the app easier to read and more transparent.

The answer design separates the legal explanation from the source details and limitations. This helps the user understand both the answer and the evidence behind it.

The app also includes example question buttons and a sidebar with supported topics, language controls, project information, prototype version, and future AI mode notes.

---

## 13. Bilingual Support

CyberLex Sweden supports both English and Swedish interface modes.

The app can display:

- English labels
- Swedish labels
- English example questions
- Swedish example questions
- English limitation text
- Swedish limitation text
- English topic labels
- Swedish topic labels
- English source-confidence labels
- Swedish source-confidence labels
- English freshness labels
- Swedish freshness labels

The knowledge base has also been expanded with Swedish summaries and Swedish useful questions to improve Swedish retrieval.

This supports the project goal of making CyberLex Sweden useful in both Swedish and English.

---

## 14. Experimental AI Search

CyberLex Sweden includes an experimental AI search sidebar powered by:

```text
app/vector_search.py
```

Despite the filename, this module is currently still rule-based. It does not yet use real embeddings, ChromaDB, FAISS, or a full language model.

The experimental module is used to test improved retrieval ranking separately from the main answer system.

It currently:

- loads Markdown source files from `data/`
- splits them into chunks based on Markdown headings
- cleans source text and user questions into searchable words
- scores chunks against the user question
- boosts useful content sections
- penalizes weak support sections
- applies topic-specific ranking rules
- returns ranked source matches

A real vector search implementation was planned and documented, but during implementation testing the local Python 3.14 environment caused package compatibility problems with AI dependencies. The vector search implementation was therefore paused and placed back into future work.

This was a reasonable project decision because the current prototype already works with transparent rule-based retrieval, while real vector search should be added later using a more compatible Python version such as Python 3.12.

---

## 15. Source Audit System and GitHub Actions

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

- an official source section
- official source links
- a source metadata section
- a source date
- source freshness information
- version notes

The script generates the audit report:

```text
docs/source_audit_report.md
```

The current audit goal is:

```text
Files marked OK: 9
Files needing review: 0
```

CyberLex Sweden also includes a GitHub Actions workflow:

```text
.github/workflows/source-audit.yml
```

This workflow can run the source audit automatically and update the audit report if needed.

The audit does not browse the web and does not verify whether the law has changed online. It only checks whether the local project files contain the required source structure.

---

## 16. Testing

Manual testing was documented in:

```text
docs/test_cases.md
```

The tests checked that CyberLex Sweden can:

- load trusted knowledge files
- match questions to relevant source sections
- generate simple source-based answers
- display citation details
- display official source links
- display source metadata
- display source quality labels
- display source freshness labels
- display detected topic labels
- show practical explanations
- show assessment checklists
- show relevant source context
- refuse unsupported questions
- run the local source audit script
- support the experimental AI search sidebar

Tested questions included:

- What authority handles GDPR in Sweden?
- When must a personal data breach be reported?
- What is NIS2?
- What is dataintrång?
- What are the GDPR principles?
- What is the Cyber Resilience Act?
- What is DORA?
- What is third-party ICT risk under DORA?
- What is Swedish tax law?
- Vad är NIS2?
- Vad är cybersäkerhetslagen?
- Vad ska ett företag göra efter en ransomwareattack?
- Vad betyder cybersäkerhetskrav för digitala produkter?
- Vad säger EU om attacker mot informationssystem?
- Vad är olaglig åtkomst enligt EU-regler?
- Vad säger EU om DDoS-attacker?

The out-of-scope test for Swedish tax law was successfully refused.

The Swedish retrieval tests confirmed that the experimental retrieval system can distinguish between similar but different legal topics, such as NIS2, CRA, DORA, GDPR, Swedish dataintrång, and EU attacks against information systems.

---

## 17. Results

The project successfully produced a working local prototype.

The prototype can answer supported cybersecurity-law questions using local trusted source files.

It can show:

- a short source-based answer
- the detected topic
- the matched source file
- the matched source section
- a relevance score
- source quality
- source match confidence
- official source links
- source metadata
- source freshness
- version notes
- a legal limitation notice
- practical explanation
- assessment checklist
- relevant source context
- other matching source sections

The project also successfully refuses out-of-scope questions when no trusted source exists.

This shows that CyberLex Sweden can provide a more controlled and transparent approach than a general chatbot for selected cybersecurity-law topics.

---

## 18. Limitations

The current prototype has several limitations:

- It only covers selected Swedish and EU cybersecurity-law topics.
- It uses simplified educational summaries.
- It does not yet use true vector search.
- It does not yet use a full language model.
- It does not browse the web live.
- It does not provide legal advice.
- It depends on the quality and completeness of the local knowledge base.
- It may still need more detailed source routing as the knowledge base grows.
- It is currently a local prototype and is not publicly deployed.
- The source audit checks local file structure, not live legal updates.
- The source freshness label is based on stored local review dates, not live legal currentness.
- The experimental AI search panel is for testing and does not replace the main answer system yet.

These limitations are acceptable for the current prototype stage.

The purpose is to demonstrate the concept, not to replace legal professionals or official authorities.

---

## 19. Future Improvements

Future improvements include:

- adding more Swedish and EU legal sources
- adding more Swedish summaries and Swedish terminology support
- adding real vector search with ChromaDB or FAISS
- using Python 3.12 for future AI dependency compatibility
- comparing vector search results against the current keyword/rule-based retrieval system
- connecting a language model only after retrieval is reliable
- generating better natural language answers from retrieved source chunks
- improving citation formatting
- continuing source update history improvements
- improving the visual design
- preparing deployment documentation
- deploying the app publicly only after privacy, safety, and legal review
- reviewing Terms of Use, Privacy Policy, and Legal Disclaimer before public use
- considering trademark protection if the project develops further
- continuing support for both Swedish and English as main languages

---

## 20. Ethical and Legal Considerations

Because CyberLex Sweden deals with legal and cybersecurity-related topics, it is important that the project does not pretend to provide official legal advice.

The application includes disclaimers explaining that the answers are simplified and educational.

CyberLex Sweden should not provide instructions for committing cybercrime.

The project should focus on lawful cybersecurity, education, legal awareness, compliance, and source-based explanations.

When the project grows, Terms of Use and a Privacy Policy should be reviewed before public deployment.

The project includes draft user-facing policy documents:

- `docs/terms_of_use.md`
- `docs/privacy_policy.md`
- `docs/legal_disclaimer.md`

These documents explain that CyberLex Sweden is an educational prototype, does not provide legal advice, should not be used for unlawful cybersecurity activity, and must be reviewed before any future public deployment.

---

## 21. Reflection

CyberLex Sweden shows that a legal-tech assistant does not need to begin with a full language model to be useful.

The most important design choice was to build the source structure first. The local Markdown knowledge base, official source links, metadata, source update history, audit report, and refusal behavior make the prototype more transparent than a normal chatbot answer.

The project also showed that similar legal topics can easily be confused by search logic. For example, ransomware, NIS2, GDPR, DORA, CRA, and EU cybercrime rules can overlap in technical language but still belong to different legal frameworks. Source routing and experimental retrieval improvements were therefore important parts of the project.

The attempted vector search implementation also showed a practical software-development lesson: AI dependencies can be sensitive to Python versions and package compatibility. Pausing that implementation was a better choice than destabilizing the working prototype.

---

## 22. Conclusion

CyberLex Sweden demonstrates how a focused AI-style assistant can help users search and understand selected Swedish and EU cybersecurity-law topics.

The project uses a local trusted knowledge base, chunk-based search, source routing, simple answer generation, citation details, official source links, source metadata, source quality labels, source freshness labels, detected topic labels, practical explanations, assessment checklists, source audit reporting, and out-of-scope refusal.

The result is a working educational prototype that is transparent, reviewable, and safer than a general unsupported chatbot for this type of topic.

CyberLex Sweden is not a finished legal product, but it provides a strong foundation for future development.

