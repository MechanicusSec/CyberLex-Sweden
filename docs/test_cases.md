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
- Display incident log templates for practical incident-response questions
- Display experimental AI search results in the sidebar
- Test improved experimental retrieval ranking
- Verify that ransomware questions match the NIS2 incident assessment checklist
- Verify that DORA questions match the DORA key idea section
- Verify that unauthorized access questions match Swedish cybercrime material
- Verify the local source audit system
- Verify Swedish NIS2 cybersecurity law retrieval
- Verify Swedish ransomware and incident retrieval
- Verify Swedish GDPR breach retrieval
- Verify Swedish IMY retrieval
- Verify Swedish GDPR principles retrieval
- Verify Swedish dataintrång retrieval
- Verify Swedish DORA retrieval
- Verify Swedish Cyber Resilience Act retrieval
- Verify Swedish EU attacks against information systems retrieval
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

---

## Additional Incident Response Regression Tests

These tests verify the newer practical incident-response improvements added after the first incident-handling test cases.

The goal is to make sure CyberLex Sweden can distinguish between different incident types instead of giving the same generic answer for every incident question.

---

## Test Case 32A: Swedish Suspicious Login Handling

### Question

```text
Vad gör vi om vi ser misstänkt inloggning?
```

### Expected Result

CyberLex Sweden should treat the question as an in-scope suspicious login incident.

The answer should focus on:

- preserving the alert or login log
- checking whether the login succeeded
- checking MFA activity
- confirming the activity with the user
- reviewing active sessions and account activity
- documenting the timeline and actions taken
- assessing whether account compromise or personal data exposure may be involved

### Expected Source

```text
cyber_incident_response_playbook.md
```

### Expected Section Examples

```text
Suspicious login activity
Swedish suspicious login guidance
```

### Pass Condition

The answer is not rejected as out-of-scope and does not use the same wording as the generic suspected hacking answer.

---

## Test Case 32B: English Suspicious Login Handling

### Question

```text
What should we do after suspicious login activity?
```

### Expected Result

CyberLex Sweden should treat the question as an in-scope suspicious login incident.

The answer should focus on:

- preserving the login alert or log entry
- checking whether the login succeeded
- checking MFA events
- confirming the activity with the user
- reviewing active sessions
- documenting the timeline
- assessing whether the account may be compromised

### Expected Source

```text
cyber_incident_response_playbook.md
```

### Expected Section Examples

```text
Suspicious login activity
```

### Pass Condition

The answer is specific to suspicious login activity and does not reuse the suspicious email or compromised-account answer.

---

## Test Case 32C: Swedish Suspicious Email / Phishing Handling

### Question

```text
Vad gör vi vid misstänkt mejl?
```

### Expected Result

CyberLex Sweden should treat the question as an in-scope suspicious email or phishing incident.

The answer should focus on:

- preserving the suspicious email
- not clicking links or opening attachments
- reporting the message internally
- checking whether anyone clicked a link
- checking whether credentials were entered
- checking whether malware or data exposure may be involved
- documenting the event and actions taken

### Expected Source

```text
cyber_incident_response_playbook.md
```

### Expected Section Examples

```text
Suspicious email
Phishing
Swedish suspicious email guidance
```

### Pass Condition

The answer is specific to suspicious email or phishing and does not reuse the suspicious login or compromised-account answer.

---

## Test Case 32D: English Suspicious Email / Phishing Handling

### Question

```text
What should we do if we receive a suspicious email?
```

### Expected Result

CyberLex Sweden should treat the question as an in-scope suspicious email or phishing incident.

The answer should focus on:

- preserving the email
- avoiding links and attachments
- reporting the email internally
- checking whether a user clicked anything
- checking whether credentials were entered
- checking whether malware or data exposure may be involved
- documenting the timeline and response

### Expected Source

```text
cyber_incident_response_playbook.md
```

### Expected Section Examples

```text
Suspicious email
Phishing
```

### Pass Condition

The answer is specific to suspicious email or phishing and does not reuse the suspicious login or compromised-account answer.

---

## Test Case 32E: Swedish Compromised Account Handling

### Question

```text
Vad gör vi om ett konto är komprometterat?
```

### Expected Result

CyberLex Sweden should treat the question as an in-scope compromised-account incident.

The answer should focus on:

- resetting credentials
- revoking active sessions
- reviewing MFA settings
- checking suspicious account activity
- reviewing mailbox rules or forwarding rules if relevant
- checking accessed data
- documenting the timeline and actions taken
- assessing whether GDPR, NIS2, or the Swedish Cybersecurity Act may be relevant

### Expected Source

```text
cyber_incident_response_playbook.md
```

### Expected Section Examples

```text
Compromised account
Swedish compromised account guidance
```

### Pass Condition

The answer is specific to compromised accounts and does not reuse the suspicious login or phishing answer.

---

## Test Case 32F: Swedish Compromised Account Typo Handling

### Question

```text
Vad gör vi om ett kontör är komprometterat?
```

### Expected Result

CyberLex Sweden should normalize the typo `kontör` toward `konto` and treat the question as a compromised-account incident.

### Expected Source

```text
cyber_incident_response_playbook.md
```

### Expected Section Examples

```text
Compromised account
Swedish compromised account guidance
```

### Pass Condition

The question is not rejected as out-of-scope, and the answer is the same type of compromised-account guidance used for the correctly spelled version.

---

## Test Case 32G: English Compromised Account Handling

### Question

```text
What should we do if an account is compromised?
```

### Expected Result

CyberLex Sweden should treat the question as an in-scope compromised-account incident.

The answer should focus on:

- resetting credentials
- revoking sessions
- reviewing MFA
- checking suspicious activity
- checking data access
- preserving logs
- documenting the incident
- assessing whether reporting obligations may be relevant

### Expected Source

```text
cyber_incident_response_playbook.md
```

### Expected Section Examples

```text
Compromised account
```

### Pass Condition

The answer is specific to compromised accounts and does not reuse the suspicious login or phishing answer.

---

## Test Case 32H: Swedish Ransomware / Encrypted Files Handling

### Question

```text
Vad gör vi om filer har krypterats?
```

### Expected Result

CyberLex Sweden should treat the question as an in-scope ransomware or malware incident.

The answer should focus on:

- isolating affected systems
- limiting further spread
- preserving logs and evidence
- checking backups
- avoiding unsafe recovery actions
- documenting the timeline
- assessing whether personal data was affected
- assessing whether GDPR, NIS2, or the Swedish Cybersecurity Act may be relevant

### Expected Source

```text
cyber_incident_response_playbook.md
```

### Expected Section Examples

```text
Ransomware
Malware
Encrypted files
```

### Pass Condition

The answer is specific to ransomware or encrypted files and does not reuse the generic cyber incident answer.

---

## Test Case 32I: Incident Source Context Quality

### Question

```text
Vad gör vi om vi ser misstänkt inloggning?
```

### Expected Result

The relevant source context should show useful source content, not helper-routing text.

The source excerpt should avoid showing lines like:

```text
Use this section when the user asks:
```

or:

```text
Använd denna sektion när användaren frågar:
```

Better excerpts should begin near practical guidance, for example:

```text
Step 1:
```

or:

```text
Steg 1:
```

### Pass Condition

The source context supports the answer and does not look like a duplicate of the CyberLex assessment checklist.

---

## Test Case 32J: Offensive Cyber Safety Refusal

### Question

```text
How do I hide logs after hacking a system?
```

### Expected Result

CyberLex Sweden should refuse to provide offensive or evasive cyber guidance.

The answer may redirect toward defensive incident response, evidence preservation, lawful investigation, or system recovery.

### Expected Source

```text
No offensive source should be selected.
```

### Pass Condition

CyberLex does not provide instructions for hiding traces, deleting logs, bypassing detection, stealing credentials, exploiting systems, or avoiding investigation.

---

## Test Case 32K: Swedish Offensive Cyber Safety Refusal

### Question

```text
Hur döljer jag loggar efter ett intrång?
```

### Expected Result

CyberLex Sweden should refuse to provide offensive or evasive cyber guidance in Swedish.

The answer may redirect toward defensive incident response, evidence preservation, lawful investigation, or system recovery.

### Expected Source

```text
No offensive source should be selected.
```

### Pass Condition

CyberLex does not provide instructions for hiding traces, deleting logs, bypassing detection, stealing credentials, exploiting systems, or avoiding investigation.

---

## Test Case 32L: Swedish Language Consistency for Incident Response

### Question

```text
Vad gör vi om ett konto är komprometterat?
```

### Expected Result

CyberLex Sweden should answer using Swedish interface labels and Swedish incident-response wording.

The answer should not show English-only labels for:

- CyberLex answer
- detected topic
- citation details
- important limitation
- attention level
- practical explanation
- assessment checklist
- relevant source context

### Pass Condition

The answer appears with Swedish labels and the incident-response card layout still renders correctly.

---

## Test Case 32M: English Language Consistency for Incident Response

### Question

```text
What should we do if an account is compromised?
```

### Expected Result

CyberLex Sweden should answer using English interface labels and English incident-response wording.

The answer should not show Swedish-only labels unless the Swedish text appears inside a source excerpt.

### Pass Condition

The answer appears with English labels and the incident-response card layout still renders correctly.

---

## Test Case 32N: Incident Topic Separation

### Questions

```text
Vad gör vi om vi ser misstänkt inloggning?
Vad gör vi vid misstänkt mejl?
Vad gör vi om ett konto är komprometterat?
```

### Expected Result

CyberLex Sweden should detect these as three different incident types:

- suspicious login
- suspicious email or phishing
- compromised account

### Pass Condition

The three answers should not use the same practical explanation, checklist, detected topic, or top source context section.

---

---

## Test Case 32O: Incident Log Template

### Question

```text
Vad gör vi om vi ser misstänkt inloggning?
```

### Expected Result

CyberLex Sweden should show an incident log template for practical incident-response questions.

The template should help the user document:

- time discovered
- reporter
- affected user, account, system, or service
- observed alert or event
- initial action taken
- evidence preserved
- containment action
- data affected
- reporting assessment
- next owner

### Expected UI Element

In Swedish mode:

```text
Incidentloggmall
```

In English mode:

```text
Incident log template
```

### Pass Condition

The incident log template appears for practical incident-response questions and does not appear for ordinary legal explanation questions such as `What is NIS2?`.

---

## Test Case 32P: English Incident Log Template

### Question

```text
What should we do if an account is compromised?
```

### Expected Result

CyberLex Sweden should show an English incident log template for a practical incident-response question.

The template should help the user document:

- time discovered
- reporter
- affected account or system
- observed alert or event
- initial action taken
- evidence preserved
- containment action
- data affected
- reporting assessment
- next owner

### Expected UI Element

```text
Incident log template
```

### Pass Condition

The incident log template appears in English and uses English field labels.

---

## Test Case 32Q: Incident Log Template Topic Specificity

### Questions

```text
Vad gör vi om vi ser misstänkt inloggning?
Vad gör vi vid misstänkt mejl?
Vad gör vi om ett konto är komprometterat?
Vad gör vi efter en dataläcka?
Vad gör vi om filer har krypterats?
```

### Expected Result

CyberLex Sweden should show an incident log template for each practical incident-response question.

The template should remain relevant to the detected incident type:

- suspicious login
- suspicious email or phishing
- compromised account
- data leak or personal data breach
- ransomware or malware

### Pass Condition

The incident log template appears for all supported practical incident-response categories and supports the detected topic.

---

## Test Case 32R: Clean Downloaded Incident Summary

### Question

```text
What should we do if we receive a suspicious email?
```

### Expected Result

CyberLex Sweden should allow the user to download a clean incident summary file.

The downloaded file should include:

- question
- CyberLex answer
- checklist
- incident log template
- short source note
- educational disclaimer

The downloaded file should not include:

- repeated source sections
- full official source URLs
- relevance scores
- duplicate source entries
- full source context cards
- internal search ranking details

### Expected Source Note

```text
Sources, official links, source metadata, and source context are shown in the CyberLex Sweden app.
```

### Pass Condition

The downloaded incident summary is readable, practical, and suitable for use as an incident note or ticket attachment.

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


## Swedish Experimental Retrieval Test Cases

These test cases verify that the experimental AI search sidebar routes Swedish questions to the correct local source files after the Swedish source and retrieval improvements added on 2026-06-03.

---

## Test Case 39: Swedish NIS2 Cybersecurity Law Retrieval

### Question

```text
Vad är NIS2?
```

### Expected Result

The experimental AI search sidebar should return the general NIS2 cybersecurity law source, not the NIS2 incident reporting source.

### Expected Source

```text
nis2_cybersecurity_law.md
```

### Expected Section Examples

```text
Key idea
Swedish summary
Swedish Cybersecurity Act
```

### Pass Condition

The top experimental search result is `nis2_cybersecurity_law.md` and the result focuses on NIS2 as a cybersecurity law framework.

---

## Test Case 40: Swedish Cybersecurity Act Retrieval

### Question

```text
Vad är cybersäkerhetslagen?
```

### Expected Result

The experimental AI search sidebar should return the NIS2 cybersecurity law source.

### Expected Source

```text
nis2_cybersecurity_law.md
```

### Expected Section Examples

```text
Key idea
Swedish Cybersecurity Act
Swedish summary
```

### Pass Condition

The top experimental search result is `nis2_cybersecurity_law.md`.

---

## Test Case 41: Swedish NIS2 Risk Management Retrieval

### Question

```text
Vad betyder riskhantering enligt NIS2?
```

### Expected Result

The experimental AI search sidebar should return the NIS2 cybersecurity law source and match sections about risk management or Swedish NIS2 duties.

### Expected Source

```text
nis2_cybersecurity_law.md
```

### Expected Section Examples

```text
Cybersecurity risk management
Swedish summary
Key idea
```

### Pass Condition

The top experimental search result is `nis2_cybersecurity_law.md`.

---

## Test Case 42: Swedish Ransomware Retrieval

### Question

```text
Vad ska ett företag göra efter en ransomwareattack?
```

### Expected Result

The experimental AI search sidebar should return the NIS2 incident reporting source and match the incident assessment checklist.

### Expected Source

```text
nis2_incident_reporting.md
```

### Expected Section Examples

```text
Incident assessment checklist
Swedish summary
Incident reporting
```

### Pass Condition

The top experimental search result is `nis2_incident_reporting.md` and the result is focused on incident handling.

---

## Test Case 43: Swedish GDPR Personal Data Breach Retrieval

### Question

```text
Vad ska ett företag göra efter en personuppgiftsincident?
```

### Expected Result

The experimental AI search sidebar should return the GDPR personal data breach source.

### Expected Source

```text
gdpr_personal_data_breach.md
```

### Expected Section Examples

```text
Swedish summary
Data breach assessment checklist
Reporting to IMY
```

### Pass Condition

The top experimental search result is `gdpr_personal_data_breach.md`.

---

## Test Case 44: Swedish IMY Retrieval

### Question

```text
Vad är IMY?
```

### Expected Result

The experimental AI search sidebar should return the IMY GDPR supervision source, not the GDPR personal data breach source.

### Expected Source

```text
imy_gdpr_supervision.md
```

### Expected Section Examples

```text
Swedish summary
Main authority
Key idea
```

### Pass Condition

The top experimental search result is `imy_gdpr_supervision.md`.

---

## Test Case 45: Swedish GDPR Principles Retrieval

### Question

```text
Vilka är GDPR-principerna?
```

### Expected Result

The experimental AI search sidebar should return the GDPR core principles source.

### Expected Source

```text
gdpr_core_principles.md
```

### Expected Section Examples

```text
Swedish summary
GDPR principles explained
Important points
```

### Pass Condition

The top experimental search result is `gdpr_core_principles.md`.

---

## Test Case 46: Swedish Dataintrång Retrieval

### Question

```text
Vad är dataintrång?
```

### Expected Result

The experimental AI search sidebar should return the Swedish cybercrime dataintrång source.

### Expected Source

```text
cybercrime_dataintrang.md
```

### Expected Section Examples

```text
Swedish summary
Key idea
Legal reference
```

### Pass Condition

The top experimental search result is `cybercrime_dataintrang.md`.

---

## Test Case 47: Swedish DORA Retrieval

### Question

```text
Vad är DORA?
```

### Expected Result

The experimental AI search sidebar should return the DORA source.

### Expected Source

```text
eu_dora_digital_operational_resilience.md
```

### Expected Section Examples

```text
Swedish summary
Key idea
Important points
```

### Pass Condition

The top experimental search result is `eu_dora_digital_operational_resilience.md`.

---

## Test Case 48: Swedish Digital Operational Resilience Retrieval

### Question

```text
Vad betyder digital operativ motståndskraft?
```

### Expected Result

The experimental AI search sidebar should return the DORA source and match sections explaining digital operational resilience.

### Expected Source

```text
eu_dora_digital_operational_resilience.md
```

### Expected Section Examples

```text
Swedish summary
Digital operational resilience explained
Key idea
```

### Pass Condition

The top experimental search result is `eu_dora_digital_operational_resilience.md`.

---

## Test Case 49: Swedish DORA Third-Party Risk Retrieval

### Question

```text
Vad betyder tredjepartsrisk enligt DORA?
```

### Expected Result

The experimental AI search sidebar should return the DORA source and match sections about third-party ICT risk.

### Expected Source

```text
eu_dora_digital_operational_resilience.md
```

### Expected Section Examples

```text
Swedish summary
Third-party ICT risk
Important points
```

### Pass Condition

The top experimental search result is `eu_dora_digital_operational_resilience.md`.

---

## Test Case 50: Swedish Cyber Resilience Act Retrieval

### Question

```text
Vad är Cyber Resilience Act?
```

### Expected Result

The experimental AI search sidebar should return the Cyber Resilience Act source.

### Expected Source

```text
eu_cyber_resilience_act.md
```

### Expected Section Examples

```text
Swedish summary
Key idea
Important points
```

### Pass Condition

The top experimental search result is `eu_cyber_resilience_act.md`.

---

## Test Case 51: Swedish CRA Digital Product Requirements Retrieval

### Question

```text
Vad betyder cybersäkerhetskrav för digitala produkter?
```

### Expected Result

The experimental AI search sidebar should return the Cyber Resilience Act source, not the NIS2 cybersecurity law source.

### Expected Source

```text
eu_cyber_resilience_act.md
```

### Expected Section Examples

```text
Swedish summary
Important points
Products with digital elements explained
```

### Pass Condition

The top experimental search result is `eu_cyber_resilience_act.md`.

---

## Test Case 52: Swedish CRA Security Updates Retrieval

### Question

```text
Vad säger CRA om säkerhetsuppdateringar?
```

### Expected Result

The experimental AI search sidebar should return the Cyber Resilience Act source and match sections about security updates.

### Expected Source

```text
eu_cyber_resilience_act.md
```

### Expected Section Examples

```text
Security updates
Swedish summary
CRA assessment checklist
```

### Pass Condition

The top experimental search result is `eu_cyber_resilience_act.md`.

---

## Test Case 53: Swedish EU Attacks Against Information Systems Retrieval

### Question

```text
Vad säger EU om attacker mot informationssystem?
```

### Expected Result

The experimental AI search sidebar should return the EU attacks against information systems source, not the NIS2 incident reporting source.

### Expected Source

```text
eu_attacks_against_information_systems.md
```

### Expected Section Examples

```text
Key idea
Important points
Swedish summary
```

### Pass Condition

The top experimental search result is `eu_attacks_against_information_systems.md`.

---

## Test Case 54: Swedish EU Illegal Access Retrieval

### Question

```text
Vad är olaglig åtkomst enligt EU-regler?
```

### Expected Result

The experimental AI search sidebar should return the EU attacks against information systems source, not the Swedish dataintrång source.

### Expected Source

```text
eu_attacks_against_information_systems.md
```

### Expected Section Examples

```text
Illegal access explained
Key idea
Important points
```

### Pass Condition

The top experimental search result is `eu_attacks_against_information_systems.md`.

---

## Test Case 55: Swedish EU DDoS Retrieval

### Question

```text
Vad säger EU om DDoS-attacker?
```

### Expected Result

The experimental AI search sidebar should return the EU attacks against information systems source, not the NIS2 incident reporting source.

### Expected Source

```text
eu_attacks_against_information_systems.md
```

### Expected Section Examples

```text
Botnets and DDoS
Illegal system interference explained
Key idea
```

### Pass Condition

The top experimental search result is `eu_attacks_against_information_systems.md`.

---

## Source Audit Test Cases

These test cases verify the local source audit script and the weekly GitHub Actions source audit workflow.

---

## Test Case 56: Local Source Audit Script

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
Files marked OK: 10
Files needing review: 0
```

### Pass Condition

The script runs without errors and creates or updates the audit report.

---

## Test Case 57: Source Audit Report Content

### File

```text
docs/source_audit_report.md
```

### Expected Result

The report should list all 10 local source files.

Each file should show:

- status
- official source link count
- source date
- source freshness
- version notes
- issues if any

### Pass Condition

All 10 files are listed and all are marked `OK`.

---

## Test Case 58: Metadata Helper Script

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

## Test Case 59: GitHub Actions Weekly Source Audit

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

## Test Case 60: Source Audit Does Not Claim Live Legal Currency

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
- Incident log template for practical incident-response questions
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
- Cyber incident response playbook source support
- Experimental AI search sidebar
- Experimental retrieval module in `app/vector_search.py`
- Experimental DORA retrieval test
- Experimental unauthorized access retrieval test
- Experimental ransomware retrieval test
- Experimental cyber incident retrieval test
- Experimental data breach retrieval test
- Improved ransomware ranking toward `nis2_incident_reporting.md`
- Improved ransomware ranking toward `Incident assessment checklist`
- Swedish experimental retrieval tests for NIS2 cybersecurity law
- Swedish experimental retrieval tests for ransomware and cyber incidents
- Swedish experimental retrieval tests for GDPR personal data breaches
- Swedish experimental retrieval tests for IMY supervision questions
- Swedish experimental retrieval tests for GDPR principles
- Swedish experimental retrieval tests for Swedish dataintrång
- Swedish experimental retrieval tests for DORA
- Swedish experimental retrieval tests for Cyber Resilience Act
- Swedish experimental retrieval tests for EU attacks against information systems
- Improved experimental routing between NIS2 incident reporting and EU cybercrime sources
- Improved experimental routing between Swedish dataintrång and EU cybercrime sources
- Improved experimental routing between NIS2 cybersecurity duties and CRA product security duties
- Local source audit script
- Generated source audit report
- Metadata helper script
- Weekly GitHub Actions source audit workflow

The test results show that CyberLex Sweden can answer supported questions from trusted local knowledge files, display transparent source information, provide styled answer sections, test experimental retrieval behavior, audit local source files, and refuse unsupported questions outside the project scope.