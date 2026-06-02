# CyberLex Sweden Technical Design

## Purpose

This document explains the technical design of the CyberLex Sweden prototype.

CyberLex Sweden is a local Streamlit application that answers questions about selected Swedish and EU cybersecurity law topics using a trusted local Markdown knowledge base.

The prototype does not use a full language model yet. Instead, it uses source-based search, question intent matching, rule-based answer generation, practical explanations, assessment checklists, detected topic labels, source quality labels, confidence explanations, and transparent source display.

---

## Application Architecture

The application is built with:

- Python
- Streamlit
- Local Markdown files
- Rule-based source search
- Source routing
- Topic keyword expansion
- Source confidence explanations
- Source quality labels
- Detected topic labels
- Source metadata extraction
- Citation display
- Bilingual interface support
- Practical explanation generation
- Topic-based assessment checklists

The main application file is:

```text
app/main.py
```

The local knowledge base is stored in:

```text
data/
```

The project documentation is stored in:

```text
docs/
```

---

## Main components

### Python

Python is the programming language used to build the application logic.

It handles:

- reading Markdown files
- splitting documents into searchable chunks
- scoring search results
- routing questions to source files
- expanding question terms
- detecting question topics
- detecting source quality labels
- generating answers
- generating practical explanations
- generating assessment checklists
- displaying results through Streamlit

### Streamlit

Streamlit is the Python framework used to create the CyberLex Sweden web interface.

It displays:

- the main page
- the sidebar
- the question input field
- answers
- citations
- detected topic cards
- source quality labels
- source metadata
- confidence explanations
- collapsible sections
- warnings and disclaimers

### Markdown knowledge base

CyberLex uses Markdown files in the `data/` folder as its trusted local knowledge base.

Each source file contains structured sections such as:

- topic
- key idea
- main authority
- important points
- practical explanation
- official source
- source date
- version notes
- disclaimer

This makes the source material easier to search, review, and update.

---

## Search and retrieval design

CyberLex searches the local knowledge base by:

1. Loading all Markdown files from `data/`.
2. Splitting each file into smaller chunks based on headings.
3. Cleaning the user question into searchable words.
4. Expanding important question terms with related legal and cybersecurity terms.
5. Matching question words against chunk text and section titles.
6. Applying score boosts for useful sections.
7. Applying score penalties for weak sections.
8. Routing clear questions to the most relevant source file.
9. Ranking results by relevance score.

The best match is used for the main answer, while additional matching sections are shown for transparency.

### Topic keyword expansion

CyberLex Sweden uses topic keyword expansion to improve local search matching.

The function `expand_question_terms(question)` adds related cybersecurity and legal terms when the user question contains important trigger words.

For example:

- `ransomware` can expand into terms such as cyber incident, incident reporting, personal data breach, GDPR, NIS2, security measures, and unauthorized access.
- `unauthorized access` can expand into terms such as dataintrång, cybercrime, illegal access, information system, and data intrusion.
- `DORA` can expand into terms such as digital operational resilience, financial sector, ICT risk, ICT incident, third-party ICT, and resilience testing.
- `NIS2` can expand into terms such as cybersecurity, incident reporting, essential entities, important entities, risk management, security measures, and MSB.

This makes the prototype better at finding relevant source sections even when the user does not use the exact same words as the Markdown knowledge files.

The expanded terms are added inside `search_chunks(question, chunks)` after the original question words are cleaned. Duplicate search terms are removed before scoring.

This is still rule-based search. It does not use a language model or vector database yet.

---

## Source routing

The function `get_target_source_file(question)` routes clear questions to a specific knowledge file.

For example:

- GDPR breach questions route to `gdpr_personal_data_breach.md`
- IMY questions route to `imy_gdpr_supervision.md`
- NIS2 incident reporting questions route to `nis2_incident_reporting.md`
- DORA questions route to `eu_dora_digital_operational_resilience.md`
- Dataintrång questions route to `cybercrime_dataintrang.md`

This improves accuracy by preventing similar words from matching the wrong source file.

---

## Detected topic labels

CyberLex Sweden displays a detected topic label above the citation details.

The function `detect_question_topic(question, language)` identifies a simple topic category from the user question.

Examples of detected topic labels include:

```text
Ransomware or malware incident
GDPR data breach
Cyber incident assessment
DORA and ICT risk
NIS2 and cybersecurity duties
Unauthorized access / dataintrång
Cyber Resilience Act and product security
GDPR and data protection
EU cybercrime and information systems
General cybersecurity law question
```

In Swedish mode, the topic labels are displayed in Swedish where relevant.

The detected topic label does not replace source matching. It is only a user-facing explanation of how CyberLex interpreted the question.

The detected topic card helps make the prototype easier to understand because the user can see the question category before reviewing the matched source, citation details, source metadata, limitation notice, and practical explanation.

The detected topic card uses a dedicated `topic-card` style in `app/main.py`.

---

## Source confidence explanations

CyberLex Sweden converts the numeric relevance score from local search into a human-readable source confidence explanation.

The function `generate_source_confidence(score, language)` returns both:

- a confidence level
- a short explanation of why the match should be treated as strong, moderate, or limited

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

The source confidence value does not represent legal certainty. It only explains how strongly the user question matched the selected local source section.

This helps users understand whether the answer is based on a strong source match or whether they should review the source context more carefully.

---

## Source quality labels

CyberLex Sweden displays a source quality label inside the citation details card.

The function `detect_source_quality(filename, language)` checks the matched knowledge file name and returns a short user-facing description of what type of source the local file is based on.

Examples:

```text
cybercrime_dataintrang.md
→ Swedish legal source / criminal-law topic

gdpr_personal_data_breach.md
→ IMY guidance and EU data protection source

gdpr_core_principles.md
→ EU data protection regulation source

imy_gdpr_supervision.md
→ Swedish supervisory authority source

nis2_incident_reporting.md
→ Swedish authority guidance and EU cybersecurity source

nis2_cybersecurity_law.md
→ Swedish authority guidance and EU cybersecurity source

eu_dora_digital_operational_resilience.md
→ EU digital operational resilience regulation source

eu_cyber_resilience_act.md
→ EU regulation source for digital product cybersecurity

eu_attacks_against_information_systems.md
→ EU directive source on attacks against information systems
```

The source quality label does not prove legal authority by itself. It only explains what kind of source category the local Markdown file represents.

This improves transparency because users can see whether the answer is based on Swedish legal material, Swedish authority guidance, EU regulation material, EU directive material, or a local educational summary based on trusted sources.

---

## CyberLex answer structure

CyberLex Sweden answers are designed to be source-grounded and transparent.

When a user asks an in-scope question, the app displays a structured answer with the following parts:

### 1. Short answer

The short answer gives a brief plain-language response to the user question.

This is generated by the rule-based answer function in `app/main.py`.

The short answer now includes more specific practical handling for different incident types, including:

- ransomware or malware incidents
- general cyber incidents
- GDPR/data breach questions
- unauthorized access questions
- DORA questions
- NIS2 questions

### 2. Detected topic

The detected topic card shows how CyberLex interpreted the question.

For example:

```text
Detected topic: Ransomware or malware incident
```

or:

```text
Detected topic: GDPR data breach
```

This card appears between the short answer and the citation details.

The purpose is to make the answer more understandable by showing the question category before the user reviews the matched source.

### 3. Citation details

The citation details show which local knowledge base file and section were used as the best match.

This includes:

- matched knowledge file
- matched section
- source quality
- relevance score
- source match confidence
- confidence explanation

The relevance score is the numeric score produced by CyberLex Sweden’s local search and ranking logic.

The source quality label explains what kind of source category the matched Markdown file represents, such as Swedish legal material, Swedish authority guidance, EU regulation material, EU directive material, or a local educational summary.

The source match confidence converts the numeric relevance score into a readable label:

- Very strong
- Strong
- Moderate
- Limited

This does not mean legal certainty. It only explains how strong the local source match is based on the current search logic.

The citation details are displayed as a styled card in the Streamlit interface.

The citation card shows the matched file, matched section, source quality, relevance score, source match confidence, and a short explanation of the confidence level.

This helps the user understand which source section CyberLex used first, what kind of source the local file is based on, and how strong the match appears to be.

### 4. Official source links

The official source links show trusted legal or authority-based sources connected to the matched knowledge file.

These links are stored inside the Markdown files in `data/` under the `## Official source` heading.

The source links use readable Markdown labels instead of raw URLs.

Example:

```markdown
[IMY: Personal data breach guidance](https://www.imy.se/)
```

Inside the Streamlit interface, official source links are displayed in a styled source card.

The source card makes the official sources easier to see and separates them from the answer text.

The application converts stored source links into clickable HTML links when displaying them inside the styled card.

This helps users review the official sources behind the answer.

### 5. Source metadata

CyberLex displays source metadata for the matched knowledge file.

This includes:

- source date
- version notes

The source date shows when the source material was last checked or added.

The version notes explain what kind of update or summary was added to the knowledge file.

The source metadata is displayed as a styled card in the Streamlit interface.

This helps users and reviewers see whether the answer is based on source material that has an update history and a documented review date.

The metadata does not guarantee that a source is still legally current. It is a transparency feature that helps show how the local knowledge base is maintained.

### 6. Important limitation

CyberLex displays an important limitation notice for each generated answer.

The limitation explains that CyberLex Sweden is an educational prototype and does not provide legal advice.

The limitation is displayed as a styled warning card in the Streamlit interface.

This makes the limitation more visible and separates it from the answer text.

The limitation card helps users understand that:

- the answer is generated from a simplified local knowledge base
- the project is educational
- the answer should not replace legal advice
- official authority guidance should be checked for important decisions

This is an important safety feature because CyberLex Sweden deals with legal and compliance-related topics.

### 7. CyberLex attention level

CyberLex displays an attention level for the answer.

The attention level is a simple educational signal based on the question topic and matched source sections.

Possible levels are:

- Normal
- Medium
- High

This is not a legal risk rating. It does not decide whether an organization has a legal obligation.

The purpose is to help users notice when a question may involve topics that require extra care, such as:

- personal data breaches
- incident reporting
- GDPR and NIS2 overlap
- DORA
- cybersecurity duties
- reporting timelines

The attention level is displayed as a styled card in the Streamlit interface.

The card uses CSS classes in `app/main.py` to show:

- a dark card background
- a left border indicating the attention level
- a bold level label
- a short reason
- a limitation note explaining that the level is not a legal risk rating

This makes the attention level easier to notice while keeping the wording cautious and educational.

### 8. Practical explanation

CyberLex displays a practical explanation for each generated answer.

The practical explanation gives the user a plain-language explanation of how the matched legal or authority-based source may be understood in practice.

This section is still rule-based and source-grounded. It does not use an external AI model.

The practical explanation is displayed as a styled card in the Streamlit interface.

The purpose is to make the answer easier to understand while keeping the source context visible.

The practical explanation should not be treated as legal advice. It is an educational explanation based on the matched knowledge source and the current prototype rules.

### 9. CyberLex assessment checklist

CyberLex displays a topic-based assessment checklist for each generated answer.

The checklist gives the user a structured way to review the issue raised by the question.

The checklist is rule-based and changes depending on the topic, such as:

- GDPR personal data breaches
- ransomware or malware incidents
- general cyber incidents
- NIS2 and cybersecurity incident reporting
- overlap between NIS2 and GDPR
- DORA
- dataintrång
- Cyber Resilience Act

The checklist is displayed inside a collapsible Streamlit expander.

Inside the expander, the checklist items are displayed in a styled checklist card.

This keeps the main answer page cleaner while still giving users practical review steps when they want more detail.

The checklist is educational and does not replace legal advice or official authority guidance.

### 10. Relevant source context

The relevant source context shows several matched source sections that support the answer.

This section is displayed inside a collapsible Streamlit expander so the page stays readable.

Each matched source section is displayed as a styled source context card.

Each context card shows:

- matched source file
- matched section
- relevance score
- short excerpt from the matched source section

The source context cards help users inspect the supporting source material without overwhelming the main answer.

This improves transparency because users can see which source sections CyberLex used as supporting context, not only the single best match.

### 11. Other matching source sections

CyberLex also lists other matching source sections ranked by relevance.

These are additional source sections found by the local search and ranking logic.

Each other matching source section shows:

- source file
- matched section
- relevance score

The other matching source sections are displayed as styled match cards in the Streamlit interface.

This makes the additional matches easier to scan and keeps the answer layout consistent with the citation, metadata, source context, checklist, and explanation cards.

This feature improves transparency because users can see not only the best match, but also other source sections that CyberLex considered relevant.

---

## Example questions panel

CyberLex Sweden includes an example questions panel below the main question input.

The purpose of this panel is to help users understand what kinds of questions the prototype can answer.

The panel can be shown or hidden with a Streamlit button.

Each example question is displayed with a button that lets the user fill the question input field automatically.

This is handled with Streamlit session state.

Streamlit session state is used to remember:

- the selected example question
- whether the example questions panel should be visible or hidden

When the user clicks an example question, CyberLex:

1. stores the selected question in session state
2. fills the question input field with that question
3. hides the example questions panel
4. reruns the Streamlit app so the answer is generated

Example English questions include:

- What is GDPR?
- What are the GDPR principles?
- When must a personal data breach be reported?
- Can an incident need to be reported under both NIS2 and GDPR?
- What should a company do after a ransomware attack?
- What should an organization check after a cyber incident?
- What should a company do after a data breach?
- What is NIS2?
- What is DORA?
- What is dataintrång?
- What is the Cyber Resilience Act?

In Swedish mode, the app displays Swedish example questions and Swedish button labels.

This improves usability by making the supported scope more visible and making it easier to test the prototype.

---

## Prototype version label

CyberLex Sweden displays a prototype version label in the sidebar.

The current displayed version is:

```text
Prototype version: 0.5
```

Version 0.5 represents the styled answer-card prototype. This version includes citation details, detected topic labels, source quality labels, official source links, source metadata, important limitation cards, attention level cards, practical explanation cards, assessment checklist cards, relevant source context cards, and other matching source section cards.

---

## Future AI mode sidebar note

CyberLex Sweden includes a small sidebar note called "Future AI mode".

The purpose of this note is to make the prototype status clear to users and reviewers.

The sidebar explains that the current version uses:

- local Markdown files
- source routing
- keyword ranking
- topic keyword expansion
- detected topic labels
- source quality labels
- source confidence explanations
- rule-based answers

It also explains that a future version may use:

- vector search
- RAG
- AI-generated answers based on trusted source material

This helps separate the current working prototype from the planned future AI version.

The current app does not use a full language model yet. It remains a local, rule-based, source-grounded prototype.

---

## Limitations

CyberLex Sweden is an educational prototype.

Current limitations include:

- It does not use a full language model yet.
- It does not browse the web live.
- It only answers from local Markdown sources.
- It only covers selected topics.
- It uses rule-based answers, explanations, attention levels, topic labels, source quality labels, confidence explanations, and checklists.
- It does not provide legal advice.
- Source material must be manually reviewed and updated.
- Confidence labels describe local source matching only, not legal certainty.
- Source quality labels describe the type of local source file, not a guarantee that the source is legally current.
- Detected topic labels describe question interpretation only, not a legal classification.

---

## Future development

Future improvements may include:

- better Swedish source summaries
- more Swedish and EU legal sources
- vector search with ChromaDB or FAISS
- AI-generated answers using a RAG design
- stronger citation formatting
- source update reminders
- public deployment
- improved visual design
- stronger legal disclaimer and Terms of Use
- clickable example questions using Streamlit session state