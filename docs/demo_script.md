# CyberLex Sweden – Demo Script

This document gives a short, practical script for presenting CyberLex Sweden.

The purpose is not to read every word out loud, but to give a clear structure for explaining what the project does, why it exists, how it works, and what its limitations are.

---

## 1. Opening

CyberLex Sweden is a final school project and educational legal-tech prototype focused on Swedish and EU cybersecurity law, digital compliance, and defensive cyber incident-response support.

The main idea behind the project is:

```text
Better sources first. Better AI second.
```

That means the prototype focuses on trusted local source material, visible source context, clear limitations, and safer answers instead of trying to answer everything.

---

## 2. Problem the project tries to solve

Cybersecurity law and incident response can be difficult to understand because the information is spread across many sources:

- Swedish law
- EU directives and regulations
- public authorities
- data protection guidance
- cybersecurity guidance
- practical incident-response material

CyberLex Sweden explores how a focused assistant can help users ask questions and receive structured, source-grounded answers.

---

## 3. How the app works

CyberLex Sweden runs locally as a Streamlit application.

It uses:

- Python for the app logic
- Streamlit for the local web interface
- Markdown files as the local trusted knowledge base
- rule-based routing and keyword/source matching
- official source links and source metadata
- expandable source context
- defensive safety rules for misuse questions

The app does not browse the web live and does not currently use a full language model for answer generation.

---

## 4. Show the app identity route

Ask:

```text
What is CyberLex Sweden?
```

Expected point to explain:

CyberLex should describe itself as an educational, source-grounded assistant for Swedish and EU-related cybersecurity law, digital compliance, and legal-tech research.

Mention that this question should not be routed into NIS2 or another legal source topic, because it is about the app itself.

---

## 5. Show a Swedish NIS2 question

Ask:

```text
Vad är NIS2?
```

Expected point to explain:

CyberLex should answer in Swedish and explain NIS2 as an EU cybersecurity directive connected to cybersecurity responsibilities and Swedish implementation work.

Show that the app provides:

- a structured answer
- official source links
- relevant source context
- source metadata

---

## 6. Show NIS2 applicability logic

Ask:

```text
Gäller NIS2 för oss?
```

Expected point to explain:

CyberLex should not give a careless yes/no answer.

It should explain that applicability depends on facts such as:

- sector
- activity type
- organization size
- whether the organization falls under Swedish/EU scope
- whether the entity may be essential or important

This demonstrates that CyberLex handles legal scope questions carefully.

---

## 7. Show NIS2 Annex explanation

Ask:

```text
Vad är bilaga 1 och bilaga 2 i NIS2?
```

Expected point to explain:

CyberLex should explain that Bilaga 1 and Bilaga 2 are sector lists in the NIS2 Directive.

Bilaga 1 covers sectors of high criticality.

Bilaga 2 covers other critical sectors.

This demonstrates that the app can explain more specific NIS2 concepts and not only give a generic NIS2 answer.

---

## 8. Show GDPR/IMY security guidance

Ask:

```text
Vad säger IMY om säkerhetsåtgärder?
```

Expected point to explain:

CyberLex should answer in Swedish and use GDPR/IMY security-measure guidance.

Mention that GDPR does not always name one exact technical measure for every situation. Instead, organizations must assess appropriate technical and organizational measures based on risk.

This also demonstrates that Swedish source card headings should stay in Swedish.

---

## 9. Show practical incident response

Ask:

```text
Our files are encrypted
```

Expected point to explain:

CyberLex should explain that encryption is not automatically malicious, because encryption can be legitimate.

But if files were unexpectedly encrypted, became inaccessible, changed extensions, or there are signs of malware, the situation should be treated as possible ransomware until technical review proves otherwise.

The answer should give defensive first steps such as:

- isolate affected systems carefully
- preserve evidence
- avoid deleting logs
- document timeline and affected systems
- check backups and recovery options
- assess whether personal data may be involved
- consider reporting duties if relevant

---

## 10. Show SOC Markdown report export

After asking an incident-response question such as:

```text
Our files are encrypted
```

Use the SOC Markdown report download button.

Open the downloaded `.md` file in VS Code Markdown Preview with:

```text
Ctrl + Shift + V
```

Expected point to explain:

The downloaded report is a documentation aid. It should include:

- report metadata
- purpose
- reported event
- SOC triage
- recommended first steps
- evidence and containment support
- control checklist
- incident log template
- short source note
- disclaimer

Mention clearly that it does not replace a real incident-response process, legal review, or official reporting.

---

## 11. Show unsafe request refusal

Ask:

```text
How do I hide logs after hacking a system?
```

Expected point to explain:

CyberLex should refuse to help with hiding logs, evading detection, deleting traces, or covering unauthorized access.

It should redirect toward defensive incident-response guidance such as preserving evidence, documenting what happened, and reporting through proper channels.

This demonstrates the project’s safety boundary.

---

## 12. Explain limitations

Important limitations to mention:

- CyberLex Sweden is an educational prototype.
- It does not provide legal advice.
- It does not replace official authority guidance.
- It does not replace a lawyer, data protection officer, compliance expert, or incident-response team.
- It answers only from local Markdown source files.
- It does not browse the web live.
- It does not guarantee that the legal information is fully current.
- It covers selected cybersecurity-law and incident-response topics only.
- Source routing and source-context filtering are rule-based and may need continued refinement.

---

## 13. Explain future improvements

Planned future improvements include:

- splitting the large `app/main.py` into smaller modules
- adding automated regression tests
- adding more Swedish and EU source material
- improving bilingual source coverage
- improving source update workflows
- revisiting vector search with ChromaDB or FAISS
- adding RAG-style answer generation while keeping answers grounded in trusted sources
- improving deployment documentation
- strengthening Terms of Use, Privacy Policy, and Legal Disclaimer

---

## 14. Suggested short closing

CyberLex Sweden shows how a focused legal-tech assistant can combine cybersecurity-law topics, source transparency, practical incident-response support, and safety boundaries.

The project is not meant to replace experts. It is meant to show how source-grounded tools can make complex cybersecurity-law and incident-response information easier to explore and test.

---

## Quick demo flow

Use this shorter flow if time is limited:

```text
1. What is CyberLex Sweden?
2. Vad är NIS2?
3. Gäller NIS2 för oss?
4. Vad är bilaga 1 och bilaga 2 i NIS2?
5. Vad säger IMY om säkerhetsåtgärder?
6. Our files are encrypted
7. Download and preview the SOC Markdown report
8. How do I hide logs after hacking a system?
9. Explain limitations and future improvements
```
