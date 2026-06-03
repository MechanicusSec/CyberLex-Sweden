# CyberLex Sweden Test Cases

## Purpose

This document contains manual test cases for the CyberLex Sweden prototype.

The goal is to verify that the application can:

- Load trusted knowledge base files
- Search source material by chunks
- Match user questions to relevant source sections
- Generate simple source-based answers
- Show the source file and source section used
- Show official source links connected to the matched knowledge file
- Show source metadata such as source date and version notes
- Show source quality labels
- Show source freshness labels
- Avoid unsupported answers when no trusted source exists
- Display styled answer cards introduced in prototype version 0.5
- Handle practical cyber incident questions with more specific short answers
- Display detected topic labels for supported question categories
- Display experimental AI search results in the sidebar
- Test improved experimental retrieval ranking
- Verify that ransomware questions match the NIS2 incident assessment checklist
- Verify that DORA questions match the DORA key idea section
- Verify that unauthorized access questions match Swedish cybercrime material
- Verify the local source audit system
- Verify the weekly GitHub Actions source audit workflow

---

## Test Environment

The tests were performed locally using:

- Windows 11
- Visual Studio Code
- Python virtual environment
- Streamlit
- Local Markdown knowledge base files in the `data/` folder
- Local scripts in the `scripts/` folder
- GitHub Actions workflow in `.github/workflows/`

Application command:

```powershell
streamlit run app/main.py
```

Alternative application command:

```powershell
python -m streamlit run app/main.py
```

Source audit command:

```powershell
python scripts/source_audit.py
```

Experimental search module command:

```powershell
python app/vector_search.py
```

---

## Core Knowledge Base Test Cases

These test cases verify that CyberLex Sweden can answer supported questions from trusted local Markdown source files.

---

## Test Case 1: GDPR Authority

### Question

```text
What authority handles GDPR in Sweden?
```

### Expected Result

CyberLex Sweden should explain that GDPR and personal data protection in Sweden are handled by IMY, Integritetsskyddsmyndigheten.

### Expected Source

```text
imy_gdpr_supervision.md
```

### Expected Section

```text
Main authority
```

### Expected Official Source Link

```text
https://www.imy.se/en/
```

### Expected Source Metadata

```text
Source date: Last checked: 2026-06-03
Version notes: Source reviewed and cleaned for CyberLex Sweden educational prototype.
```

### Result

Passed.

### Notes

The system should route authority questions about GDPR supervision to the IMY supervision source. This is more accurate than routing broad authority questions to the personal data breach source.

---

## Test Case 2: Personal Data Breach Reporting

### Question

```text
When must a personal data breach be reported?
```

### Expected Result

CyberLex Sweden should explain that a personal data breach may need to be reported to IMY and that, if notification is required, it should normally be reported within 72 hours after the organization becomes aware of it.

### Expected Source

```text
gdpr_personal_data_breach.md
```

### Expected Section

```text
Reporting to IMY
```

### Expected Official Source Link

```text
https://www.imy.se/en/organisations/forms-and-e-services/notification-of-a-personal-data-breach/
```

### Expected Source Metadata

```text
Source date: Last checked: 2026-06-03
Version notes: Source reviewed and cleaned for CyberLex Sweden educational prototype.
```

### Result

Passed.

### Notes

The system correctly matches the question to the GDPR personal data breach reporting source and displays source traceability.

---

## Test Case 3: NIS2

### Question

```text
What is NIS2?
```

### Expected Result

CyberLex Sweden should explain that NIS2 is an EU cybersecurity directive connected to Swedish cybersecurity law. The answer should mention cybersecurity risk management, security measures, and incident reporting for covered organizations.

### Expected Source

```text
nis2_cybersecurity_law.md
```

### Expected Section

```text
Key idea
```

### Expected Official Source Link

```text
https://www.msb.se/
```

### Expected Source Metadata

```text
Source date: Last checked: 2026-06-03
Version notes: Source reviewed for CyberLex Sweden educational prototype.
```

### Result

Passed.

### Notes

The system correctly matches general NIS2 questions to the NIS2 cybersecurity law source.

---

## Test Case 4: Dataintrång

### Question

```text
What is dataintrång?
```

### Expected Result

CyberLex Sweden should explain that dataintrång means data intrusion under Swedish criminal law and is connected to unauthorized access to, or interference with, data or information systems.

### Expected Source

```text
cybercrime_dataintrang.md
```

### Expected Section

```text
Key idea
```

### Expected Official Source Link

```text
https://www.riksdagen.se/
```

### Expected Source Metadata

```text
Source date: Last checked: 2026-06-03
Version notes: Source reviewed for CyberLex Sweden educational prototype.
```

### Result

Passed.

### Notes

The system correctly matches the question to the Swedish cybercrime source and shows official legal source links.

---

## Test Case 5: Out-of-Scope Question

### Question

```text
What is Swedish tax law?
```

### Expected Result

CyberLex Sweden should refuse to answer because Swedish tax law is outside the project scope.

### Expected Message

```text
No trusted source was found for this question.
```

### Expected Source

```text
No source should be selected.
```

### Expected Official Source Link

```text
No official source link should be displayed.
```

### Expected Source Metadata

```text
No source metadata should be displayed.
```

### Result

Passed.

### Notes

The system correctly refuses the question because Swedish tax law is outside the CyberLex Sweden scope.

---

## Test Case 6: GDPR Core Principles

### Question

```text
What are the GDPR principles?
```

### Expected Result

CyberLex Sweden should explain that GDPR includes principles such as lawfulness, fairness and transparency, purpose limitation, data minimisation, accuracy, storage limitation, integrity and confidentiality, and accountability.

### Expected Source

```text
gdpr_core_principles.md
```

### Expected Section

```text
Important points
```

### Expected Official Source Link

```text
https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng
```

### Expected Source Metadata

```text
Source date: Last checked: 2026-06-03
Version notes: Source reviewed for CyberLex Sweden educational prototype.
```

### Result

Passed.

### Notes

The system correctly matches the question to the GDPR core principles source file.

---

## Test Case 7: EU Attacks Against Information Systems

### Question

```text
What is the EU law about attacks against information systems?
```

### Expected Result

CyberLex Sweden should explain that Directive 2013/40/EU concerns attacks against information systems and covers topics such as illegal access, system interference, data interference, and cooperation between authorities.

### Expected Source

```text
eu_attacks_against_information_systems.md
```

### Expected Section

```text
Key idea
```

### Expected Official Source Link

```text
https://eur-lex.europa.eu/eli/dir/2013/40/oj/eng
```

### Expected Source Metadata

```text
Source date: Last checked: 2026-06-03
Version notes: Source reviewed for CyberLex Sweden educational prototype.
```

### Result

Passed.

### Notes

The system correctly matches the question to the EU attacks against information systems source file.

---

## Test Case 8: Cyber Resilience Act

### Question

```text
What is the Cyber Resilience Act?
```

### Expected Result

CyberLex Sweden should explain that the Cyber Resilience Act is an EU regulation about cybersecurity requirements for products with digital elements.

### Expected Source

```text
eu_cyber_resilience_act.md
```

### Expected Section

```text
Key idea
```

### Expected Official Source Link

```text
https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
```

### Expected Source Metadata

```text
Source date: Last checked: 2026-06-03
Version notes: Source reviewed for CyberLex Sweden educational prototype.
```

### Result

Passed.

### Notes

The system correctly matches the question to the Cyber Resilience Act source file.

---

## Test Case 9: DORA

### Question

```text
What is DORA?
```

### Expected Result

CyberLex Sweden should explain that DORA, the Digital Operational Resilience Act, is an EU regulation for the financial sector. The answer should mention ICT risk management, ICT-related incident reporting, resilience testing, third-party ICT risk, and digital operational resilience.

### Expected Source

```text
eu_dora_digital_operational_resilience.md
```

### Expected Section

```text
Key idea
```

### Expected Official Source Link

```text
https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng
```

### Expected Source Metadata

```text
Source date: Last checked: 2026-06-03
Version notes: Source reviewed for CyberLex Sweden educational prototype.
```

### Result

Passed.

### Notes

The system correctly matches the question to the DORA knowledge file and displays citation details, official source links, source metadata, and source context.

---

## Test Case 10: DORA Third-Party ICT Risk

### Question

```text
What is third-party ICT risk under DORA?
```

### Expected Result

CyberLex Sweden should explain that third-party ICT risk under DORA concerns risks connected to ICT third-party service providers, such as cloud services, software providers, outsourced ICT services, and other external technology providers.

### Expected Source

```text
eu_dora_digital_operational_resilience.md
```

### Expected Section

```text
Third-party ICT risk
```

### Expected Official Source Link

```text
https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng
```

### Expected Source Metadata

```text
Source date: Last checked: 2026-06-03
Version notes: Source reviewed for CyberLex Sweden educational prototype.
```

### Result

Passed.

### Notes

The system correctly routes the question to the DORA source and matches the third-party ICT risk section.

---

## Test Case 11: DORA Relationship with NIS2 and GDPR

### Question

```text
How is DORA connected to NIS2 and GDPR?
```

### Expected Result

CyberLex Sweden should explain that DORA, NIS2, and GDPR are different legal frameworks but can overlap. DORA focuses on digital operational resilience in the financial sector, NIS2 focuses on cybersecurity requirements for covered entities, and GDPR focuses on personal data protection.

### Expected Source

```text
eu_dora_digital_operational_resilience.md
```

### Expected Section

```text
Relationship with NIS2 and GDPR
```

### Expected Official Source Link

```text
https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng
```

### Expected Source Metadata

```text
Source date: Last checked: 2026-06-03
Version notes: Source reviewed for CyberLex Sweden educational prototype.
```

### Result

Passed.

### Notes

The system correctly matches the DORA relationship question to the DORA source and displays traceability information.

---

## Prototype Version 0.5 UI Test Cases

These test cases verify the styled answer layout introduced in prototype version 0.5.

The purpose is to confirm that CyberLex Sweden displays source-grounded answers clearly, consistently, and with visible separation between the answer, sources, limitations, practical guidance, and supporting context.

---

## Test Case 12: Citation Details Card

### Question

```text
When must a personal data breach be reported?
```

### Expected Result

CyberLex Sweden should display a citation details card showing:

- matched knowledge file
- matched section
- source quality
- relevance score
- source match confidence
- confidence explanation

### Pass Condition

The citation details are visible and displayed as a styled card.

---

## Test Case 13: Official Source Links Card

### Question

```text
When must a personal data breach be reported?
```

### Expected Result

CyberLex Sweden should display official source links connected to the matched knowledge file.

### Pass Condition

The official source links are visible, readable, and clickable.

---

## Test Case 14: Source Metadata Card

### Question

```text
What is NIS2?
```

### Expected Result

CyberLex Sweden should display source metadata, including source date, source freshness, and version notes if available.

### Pass Condition

The source metadata appears in a styled card.

---

## Test Case 15: Important Limitation Card

### Question

```text
What is GDPR?
```

### Expected Result

CyberLex Sweden should display an important limitation notice explaining that the app is educational and does not provide legal advice.

### Pass Condition

The limitation is visible and displayed as a warning-style card.

---

## Test Case 16: CyberLex Attention Level Card

### Question

```text
Can an incident need to be reported under both NIS2 and GDPR?
```

### Expected Result

CyberLex Sweden should display a CyberLex attention level card.

The attention level should explain why the question may require extra care.

### Pass Condition

The attention level card is visible and includes:

- level
- reason
- limitation note

---

## Test Case 17: Practical Explanation Card

### Question

```text
What should a company do after a ransomware attack?
```

### Expected Result

CyberLex Sweden should display a practical explanation based on the matched source context.

### Pass Condition

The practical explanation appears in a styled card and does not replace the legal limitation notice.

---

## Test Case 18: Assessment Checklist Expander

### Question

```text
When must a personal data breach be reported?
```

### Expected Result

CyberLex Sweden should display a CyberLex assessment checklist inside a collapsible expander.

### Pass Condition

The checklist can be opened and contains relevant review points.

---

## Test Case 19: Relevant Source Context Cards

### Question

```text
What is the difference between GDPR and NIS2?
```

### Expected Result

CyberLex Sweden should display relevant source context inside a collapsible expander.

Each source context item should show:

- source file
- matched section
- relevance score
- excerpt

### Pass Condition

The source context cards are visible inside the expander and the excerpts are readable.

---

## Test Case 20: Other Matching Source Section Cards

### Question

```text
What is DORA?
```

### Expected Result

CyberLex Sweden should display other matching source sections ranked by relevance.

### Pass Condition

The other matching sections appear as styled cards and do not break the answer layout.

---

## Test Case 21: Swedish Interface Card Layout

### Question

```text
När måste en personuppgiftsincident rapporteras?
```

### Expected Result

CyberLex Sweden should answer using Swedish interface labels and show the same source-grounded card structure.

### Pass Condition

The answer appears with Swedish labels and the styled cards still render correctly.

---

## Test Case 22: Example Question Panel

### Action

Open the example questions panel and click an example question.

### Expected Result

CyberLex Sweden should:

1. Fill the question input with the selected example question.
2. Hide the example question panel.
3. Generate an answer for the selected question.

### Pass Condition

The selected example question works without manually typing it.

---

## Test Case 23: Detected Topic Card

### Question

```text
What should a company do after a ransomware attack?
```

### Expected Result

CyberLex Sweden should display a detected topic card between the short answer and the citation details.

The detected topic should explain how CyberLex interpreted the question.

### Expected Topic

```text
Ransomware or malware incident
```

### Pass Condition

The detected topic card is visible and shows a topic label that matches the question category.

---

## Test Case 23B: Source Quality Label

### Question

```text
What should a company do after a ransomware attack?
```

### Expected Result

CyberLex Sweden should display a source quality label inside the citation details card.

The source quality label should explain what type of source the matched local knowledge file is based on.

### Expected Source

```text
nis2_incident_reporting.md
```

### Expected Source Quality

```text
Swedish authority guidance and EU cybersecurity source
```

### Pass Condition

The citation details card includes a visible source quality row, and the label matches the type of source used by the matched knowledge file.

---

## Test Case 23C: Source Freshness Label

### Question

```text
What should a company do after a ransomware attack?
```

### Expected Result

CyberLex Sweden should display a source freshness label inside the source metadata card.

The source freshness label should explain whether the matched local knowledge file has a recent stored review date.

### Expected Source

```text
nis2_incident_reporting.md
```

### Expected Source Date

```text
Last checked: 2026-06-03
```

### Expected Source Freshness

```text
Recently checked
```

### Pass Condition

The source metadata card includes a visible source freshness row, and the label is based on the stored source date in the matched knowledge file.

---

## Improved Incident Handling Test Cases

These test cases verify topic keyword expansion, improved cyber incident handling, improved unauthorized access wording, separated practical short answers, and separated assessment checklists.

---

## Test Case 24: Ransomware Incident Handling

### Question

```text
What should a company do after a ransomware attack?
```

### Expected Result

CyberLex Sweden should treat ransomware as an in-scope cybersecurity incident question.

The answer should explain that an organization should contain the incident, preserve evidence, document what happened, assess whether personal data was affected, and consider whether GDPR or NIS2 incident reporting may be relevant.

### Expected Source

```text
nis2_incident_reporting.md
```

### Expected Section

```text
Incident assessment checklist
```

### Pass Condition

The question is not rejected as out-of-scope, and CyberLex displays a source-grounded answer with citation details, official source links, source metadata, limitation notice, attention level, practical explanation, and assessment checklist.

---

## Test Case 25: Cyber Incident Checklist Handling

### Question

```text
What should an organization check after a cyber incident?
```

### Expected Result

CyberLex Sweden should treat the question as an in-scope cyber incident question.

The answer should explain that the organization may need to assess incident containment, documentation, personal data impact, service impact, preserved evidence, and whether NIS2 or GDPR reporting could be relevant.

### Expected Source

```text
nis2_incident_reporting.md
```

### Expected Section

```text
Incident assessment checklist
```

### Pass Condition

CyberLex matches a relevant incident reporting source and displays the styled answer cards correctly.

---

## Test Case 26: Unauthorized Access English Answer

### Question

```text
Is unauthorized access illegal in Sweden?
```

### Expected Result

CyberLex Sweden should explain in English that unauthorized access to an information system may be illegal in Sweden.

The answer may mention the Swedish offence `dataintrång`, but the English explanation should come first.

### Expected Source

```text
cybercrime_dataintrang.md
```

### Expected Section

```text
Key idea
```

### Pass Condition

The answer starts with English wording and does not begin directly with the Swedish term `Dataintrång`.

---

## Test Case 27: Ransomware Practical Short Answer

### Question

```text
What should a company do after a ransomware attack?
```

### Expected Result

CyberLex Sweden should give a ransomware-specific practical answer.

The answer should explain that the organization should:

- isolate affected systems
- limit further spread
- preserve logs and evidence
- document the timeline
- assess whether personal data was affected
- assess whether GDPR notification to IMY may be required
- assess whether NIS2 or Swedish Cybersecurity Act reporting may be relevant

### Expected Source

```text
nis2_incident_reporting.md
```

### Expected Section

```text
Incident assessment checklist
```

### Pass Condition

The answer should mention ransomware or malware handling and should not use the exact same short answer as the general cyber incident test.

---

## Test Case 28: General Cyber Incident Practical Short Answer

### Question

```text
What should an organization check after a cyber incident?
```

### Expected Result

CyberLex Sweden should give a general cyber incident assessment answer.

The answer should explain that the organization should check:

- what happened
- which systems and data were affected
- whether personal data was involved
- whether the incident may be reportable
- the timeline
- technical impact
- decisions and actions taken
- which legal frameworks were assessed, such as GDPR, NIS2, or the Swedish Cybersecurity Act

### Expected Source

```text
nis2_incident_reporting.md
```

### Expected Section

```text
Incident assessment checklist
```

### Pass Condition

The answer should be a general assessment answer and should not use the exact same wording as the ransomware answer.

---

## Test Case 29: Data Breach Practical Short Answer

### Question

```text
What should a company do after a data breach?
```

### Expected Result

CyberLex Sweden should give a GDPR/data breach-specific practical answer.

The answer should explain that the organization should:

- contain the incident
- preserve relevant evidence
- document what happened
- assess whether personal data was affected
- assess whether the breach creates a risk to individuals' rights and freedoms
- assess whether notification to IMY is required within 72 hours
- assess whether affected individuals may need to be informed if the risk is high

### Expected Source

```text
gdpr_personal_data_breach.md
```

### Expected Section

```text
Reporting to IMY
```

### Pass Condition

The answer should focus on GDPR/data breach handling and should not use the same wording as the ransomware or general cyber incident answer.

---

## Test Case 30: Ransomware Assessment Checklist

### Question

```text
What should a company do after a ransomware attack?
```

### Expected Result

CyberLex Sweden should display a ransomware-specific assessment checklist.

The checklist should include review points such as:

- isolate affected systems
- limit further spread
- preserve logs and technical evidence
- document the timeline, discovery, impact, and actions taken
- check whether backups exist and are unaffected
- assess whether personal data was affected
- assess whether GDPR notification to IMY may be relevant
- assess whether NIS2 or Swedish Cybersecurity Act reporting may be relevant

### Pass Condition

The checklist is clearly focused on ransomware or malware handling and is different from the general cyber incident checklist.

---

## Test Case 31: General Cyber Incident Assessment Checklist

### Question

```text
What should an organization check after a cyber incident?
```

### Expected Result

CyberLex Sweden should display a general cyber incident assessment checklist.

The checklist should include review points such as:

- identify what happened and when it was discovered
- identify affected systems, accounts, services, and data
- assess technical impact and severity
- assess whether personal data was involved
- check whether the incident may be reportable
- assess whether GDPR, NIS2, or the Swedish Cybersecurity Act may be relevant
- document timeline, technical impact, decisions, and actions taken
- compare the assessment with official sources and internal incident response procedures

### Pass Condition

The checklist is clearly focused on general cyber incident assessment and is different from the ransomware checklist.

---

## Test Case 32: Data Breach Assessment Checklist

### Question

```text
What should a company do after a data breach?
```

### Expected Result

CyberLex Sweden should display a GDPR/data breach-specific assessment checklist.

The checklist should include review points such as:

- contain the incident
- preserve relevant evidence
- identify what personal data may have been affected
- assess whether the breach may create risk to individuals' rights and freedoms
- check when the organization became aware of the breach
- assess whether notification to IMY is required within 72 hours
- assess whether affected individuals may need to be informed if the risk is high
- document the decision, timeline, actions, and sources

### Pass Condition

The checklist is clearly focused on GDPR/data breach handling and is different from the ransomware and general cyber incident checklists.

---

## Experimental AI Search Test Cases

These test cases verify the experimental AI search sidebar and the experimental retrieval module in `app/vector_search.py`.

The experimental search does not replace the main CyberLex answer system yet.

It is used to test retrieval ranking and source-section matching before future vector search or RAG features are added.

---

## Test Case 33: Experimental Search Sidebar Visibility

### Action

Open CyberLex Sweden in Streamlit and check the sidebar.

### Expected Result

The sidebar should show an experimental AI search section.

### Pass Condition

The sidebar includes an input field for experimental search testing and explains that the feature does not replace the main CyberLex answer yet.

---

## Test Case 34: Experimental Search DORA Retrieval

### Question

```text
What is DORA?
```

### Expected Result

The experimental AI search sidebar should return DORA source material as the top match.

### Expected Source

```text
eu_dora_digital_operational_resilience.md
```

### Expected Section

```text
Key idea
```

### Pass Condition

The top experimental search result is the DORA file and the `Key idea` section.

---

## Test Case 35: Experimental Search Unauthorized Access Retrieval

### Question

```text
Is unauthorized access illegal in Sweden?
```

### Expected Result

The experimental AI search sidebar should return the Swedish cybercrime source as the top match.

### Expected Source

```text
cybercrime_dataintrang.md
```

### Expected Section

```text
Key idea
```

### Pass Condition

The top experimental search result is the cybercrime dataintrång source and the `Key idea` section.

---

## Test Case 36: Experimental Search Ransomware Retrieval

### Question

```text
What should a company do after a ransomware attack?
```

### Expected Result

The experimental AI search sidebar should return the NIS2 incident reporting source as the top match.

### Expected Source

```text
nis2_incident_reporting.md
```

### Expected Section

```text
Incident assessment checklist
```

### Pass Condition

The top experimental search result is the NIS2 incident reporting file and the `Incident assessment checklist` section.

---

## Test Case 37: Experimental Search Cyber Incident Retrieval

### Question

```text
What should an organization check after a cyber incident?
```

### Expected Result

The experimental AI search sidebar should return the NIS2 incident reporting source as the top match.

### Expected Source

```text
nis2_incident_reporting.md
```

### Expected Section

```text
Incident assessment checklist
```

### Pass Condition

The top experimental search result is the NIS2 incident reporting file and a relevant cyber incident assessment section.

---

## Test Case 38: Experimental Search Data Breach Retrieval

### Question

```text
What should a company do after a data breach?
```

### Expected Result

The experimental AI search sidebar should return the GDPR personal data breach source as a top match.

### Expected Source

```text
gdpr_personal_data_breach.md
```

### Expected Section

```text
Reporting to IMY
```

### Pass Condition

The experimental search result includes the GDPR breach source and a relevant reporting or cybersecurity connection section.

---

## Source Audit Test Cases

These test cases verify the local source audit script and the weekly GitHub Actions source audit workflow.

---

## Test Case 39: Local Source Audit Script

### Command

```powershell
python scripts/source_audit.py
```

### Expected Result

The script should check all Markdown files in the `data/` folder and generate:

```text
docs/source_audit_report.md
```

### Expected Summary

```text
Files marked OK: 9
Files needing review: 0
```

### Pass Condition

The script runs without errors and creates or updates the audit report.

---

## Test Case 40: Source Audit Report Content

### File

```text
docs/source_audit_report.md
```

### Expected Result

The report should list all 9 local source files.

Each file should show:

- status
- official source link count
- source date
- source freshness
- version notes
- issues if any

### Pass Condition

All 9 files are listed and all are marked `OK`.

---

## Test Case 41: Metadata Helper Script

### Command

```powershell
python scripts/add_missing_metadata.py
```

### Expected Result

The script should check the Markdown files in the `data/` folder and add a `## Source metadata` section only if it is missing.

### Pass Condition

The script should not duplicate metadata sections in files that already have them.

### Notes

This script is mainly a maintenance helper and does not need to be run every week.

---

## Test Case 42: GitHub Actions Weekly Source Audit

### Action

Open GitHub Actions and run the workflow manually.

### Expected Workflow

```text
Weekly Source Audit
```

### Expected Result

The workflow should:

1. Check out the repository.
2. Set up Python.
3. Run `python scripts/source_audit.py`.
4. Update `docs/source_audit_report.md`.
5. Commit the updated report if changes are found.

### Pass Condition

The workflow run finishes with status `Success`.

---

## Test Case 43: Source Audit Does Not Claim Live Legal Currency

### Action

Read the generated source audit report.

### Expected Result

The report should clearly explain that it does not browse the web and does not confirm whether the law is currently up to date.

### Pass Condition

The report states that it only checks the local project files.

---

## Test Summary

The current prototype successfully demonstrates:

- Local source loading
- Chunk-based document search
- Intent-based source ranking
- Source routing for clearer topic matching
- Simple source-based answers
- Source file and section display
- Official source link display
- Source quality label in citation details
- Human-readable source quality labels for Swedish legal sources, Swedish authority guidance, EU regulations, EU directives, and local educational summaries
- Source freshness label in source metadata
- Human-readable freshness labels based on stored local source review dates
- Source metadata display
- Legal disclaimer display
- Out-of-scope question refusal
- Styled citation details card
- Styled official source links card
- Styled source metadata card
- Styled important limitation card
- CyberLex attention level card
- Practical explanation card
- Assessment checklist expander
- Relevant source context cards
- Other matching source section cards
- Swedish interface card layout
- Clickable example question panel behavior
- Detected topic card
- Human-readable topic labels for ransomware, GDPR data breach, DORA, NIS2, GDPR, unauthorized access, and general cyber law questions
- Topic keyword expansion
- Improved ransomware handling
- Improved cyber incident handling
- Improved unauthorized access English answer wording
- Separated practical short answers for ransomware, cyber incidents, and data breaches
- Separated assessment checklists for ransomware, cyber incidents, and data breaches
- Experimental AI search sidebar
- Experimental retrieval module in `app/vector_search.py`
- Experimental DORA retrieval test
- Experimental unauthorized access retrieval test
- Experimental ransomware retrieval test
- Experimental cyber incident retrieval test
- Experimental data breach retrieval test
- Improved ransomware ranking toward `nis2_incident_reporting.md`
- Improved ransomware ranking toward `Incident assessment checklist`
- Local source audit script
- Generated source audit report
- Metadata helper script
- Weekly GitHub Actions source audit workflow

The test results show that CyberLex Sweden can answer supported questions from trusted local knowledge files, display transparent source information, provide styled answer sections, test experimental retrieval behavior, audit local source files, and refuse unsupported questions outside the project scope.