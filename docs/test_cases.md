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

---

## Test Case 23: Ransomware Incident Handling

### Question

```text
What should a company do after a ransomware attack?
```

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

The test results show that CyberLex Sweden can answer supported questions from trusted local knowledge files and refuse unsupported questions outside the project scope.