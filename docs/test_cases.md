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
- Avoid unsupported answers when no trusted source exists
- Display styled answer cards introduced in prototype version 0.5
- Handle practical cyber incident questions with more specific short answers
- Display detected topic labels for supported question categories

---

## Test Environment

The tests were performed locally using:

- Windows 11
- Visual Studio Code
- Python virtual environment
- Streamlit
- Local Markdown knowledge base files in the `data/` folder

Application command:

```powershell
streamlit run app/main.py
```

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
gdpr_personal_data_breach.md
```

### Expected Section

```text
Main authority
```

### Expected Official Source Link

```text
https://www.imy.se/en/organisations/forms-and-e-services/notification-of-a-personal-data-breach/
```

### Expected Source Metadata

```text
Source date: Last checked: 2026-05-30
Version notes: Initial educational summary added for CyberLex Sweden.
```

### Result

Passed.

### Notes

The system correctly matched the question to the GDPR source and displayed the source file, source section, official source link, and source metadata.

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
Source date: Last checked: 2026-05-30
Version notes: Initial educational summary added for CyberLex Sweden.
```

### Result

Passed.

### Notes

The system correctly matched the question to the reporting section and displayed the source metadata.

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
https://www.msb.se/sv/amnesomraden/informationssakerhet-cybersakerhet-och-sakra-kommunikationer/krav-och-regler-inom-informationssakerhet-och-cybersakerhet/nis-direktivet/det-har-ar-nis2-direktivet/
```

### Expected Source Metadata

```text
Source date: Last checked: 2026-05-30
Version notes: Initial educational summary added for CyberLex Sweden.
```

### Result

Passed.

### Notes

The system correctly matched the question to the NIS2 knowledge file and displayed official source links and metadata.

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
https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/brottsbalk-1962700_sfs-1962-700/
```

### Expected Source Metadata

```text
Source date: Last checked: 2026-05-30
Version notes: Initial educational summary added for CyberLex Sweden.
```

### Result

Passed.

### Notes

The system correctly matched the question to the cybercrime source and showed official legal source links.

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

The system correctly refused the question because it was outside the CyberLex Sweden scope.

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
Source date: Last checked: 2026-05-30
Version notes: Initial educational summary added for CyberLex Sweden.
```

### Result

Passed.

### Notes

The system correctly matched the question to the GDPR core principles knowledge file and showed official source links and metadata.

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
Source date: Last checked: 2026-05-30
Version notes: Initial educational summary added for CyberLex Sweden.
```

### Result

Passed.

### Notes

The system correctly matched the question to the EU attacks against information systems source file and displayed source traceability.

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
Source date: Last checked: 2026-05-30
Version notes: Initial educational summary added for CyberLex Sweden.
```

### Result

Passed.

### Notes

The system correctly matched the question to the Cyber Resilience Act source file and displayed the official source link and source metadata.

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
Source date: Last checked: 2026-05-31
Version notes: Initial educational summary added for CyberLex Sweden.
```

### Result

Passed.

### Notes

The system correctly matched the question to the DORA knowledge file and displayed citation details, official source links, source metadata, and the matched source excerpt.

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
Source date: Last checked: 2026-05-31
Version notes: Initial educational summary added for CyberLex Sweden.
```

### Result

Passed.

### Notes

The system correctly routed the question to the DORA source and matched the third-party ICT risk section.

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
Source date: Last checked: 2026-05-31
Version notes: Initial educational summary added for CyberLex Sweden.
```

### Result

Passed.

### Notes

The system correctly matched the DORA relationship question to the DORA source and displayed traceability information.

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
- relevance score
- source match confidence

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

CyberLex Sweden should display source metadata, including source date and version notes if available.

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
Relationship with GDPR breach reporting
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

The answer should explain that the organization may need to assess incident containment, documentation, personal data impact, and whether NIS2 or GDPR reporting could be relevant.

### Expected Source

```text
nis2_incident_reporting.md
```

### Expected Section

```text
Relationship with GDPR breach reporting
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
Practical explanation
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
Relationship with GDPR breach reporting
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
Relationship with GDPR breach reporting
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

## Test Summary

The current prototype successfully demonstrates:

- Local source loading
- Chunk-based document search
- Intent-based source ranking
- Source routing for clearer topic matching
- Simple source-based answers
- Source file and section display
- Official source link display
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

The test results show that CyberLex Sweden can answer supported questions from trusted local knowledge files, display transparent source information, provide styled answer sections, and refuse unsupported questions outside the project scope.