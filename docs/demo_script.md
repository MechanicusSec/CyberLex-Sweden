# CyberLex Sweden Demo Script

## Purpose

This document gives a short, practical script for presenting CyberLex Sweden.

The purpose is not to read every word out loud. Use it as a guide for explaining what the project does, why it exists, how it works, what it can demonstrate, and what its limitations are.

CyberLex Sweden is an educational prototype. It does not provide legal advice and does not replace official authority guidance, a lawyer, data protection officer, compliance expert, or professional incident-response team.

---

## 1. Opening

CyberLex Sweden is my final school project and an educational legal-tech prototype focused on Swedish and EU cybersecurity law, digital compliance, and defensive cyber incident-response support.

The main idea behind the project is:

```text
Better sources first. Better AI second.
```

This means that the prototype focuses on trusted local source material, visible source context, official source links, clear limitations, and safer answers instead of trying to answer every possible question.

---

## 2. Problem the Project Tries to Solve

Cybersecurity law and incident response can be difficult to understand because the information is spread across many places, such as:

* Swedish law
* EU directives and regulations
* public authorities
* data protection guidance
* cybersecurity guidance
* practical incident-response material

CyberLex Sweden explores how a focused assistant can help users ask questions and receive structured, source-grounded answers within a limited cybersecurity-law scope.

The goal is not to replace experts. The goal is to make complex information easier to search, explain, test, and document.

---

## 3. What CyberLex Sweden Can Help With

CyberLex Sweden focuses on topics such as:

* NIS2
* the Swedish Cybersecurity Act
* GDPR and personal data breaches
* IMY guidance
* DORA
* the Cyber Resilience Act
* Swedish cybercrime and unauthorized access
* defensive incident-response support
* basic reporting and documentation assessment

CyberLex Sweden should refuse questions outside this scope, such as tax law, general legal topics, or unrelated advice.

It should also refuse unsafe cyber requests, such as hiding logs, stealing credentials, bypassing detection, or breaking into systems.

---

## 4. How the App Works

CyberLex Sweden runs locally as a Streamlit application.

The app uses:

* Python for the application logic
* Streamlit for the local web interface
* Markdown files as the trusted local knowledge base
* rule-based routing and keyword/source matching
* official source links and source metadata
* expandable source context
* defensive safety rules for misuse questions

Streamlit is the framework that turns the Python app into a local web page.

The Markdown files act as the local knowledge base. Instead of browsing the web live, CyberLex searches these trusted project files and shows where the answer came from.

The app does not currently use a full language model for answer generation. It is mainly a source-grounded, rule-based prototype.

---

## 5. Demo Step: App Identity

Ask:

```text
What is CyberLex Sweden?
```

Expected point to explain:

CyberLex should describe itself as an educational, source-grounded assistant for Swedish and EU cybersecurity law, digital compliance, and defensive incident-response support.

This question should not be routed into NIS2, GDPR, DORA, or another legal source topic, because the user is asking about the app itself.

What this demonstrates:

* the app can explain its own purpose
* the self-description route works
* the app avoids showing unrelated legal source cards

---

## 6. Demo Step: Swedish NIS2 Question

Ask:

```text
Vad är NIS2?
```

Expected point to explain:

CyberLex should answer in Swedish and explain NIS2 as an EU cybersecurity directive connected to cybersecurity responsibilities and Swedish implementation work.

Show that the app provides:

* a structured answer
* Swedish visible labels
* official source links
* relevant source context
* source metadata
* an appropriate attention level

What this demonstrates:

* Swedish language support
* NIS2 source routing
* source-grounded legal explanation

---

## 7. Demo Step: NIS2 Applicability Logic

Ask:

```text
Gäller NIS2 för oss?
```

Expected point to explain:

CyberLex should not give a careless yes or no answer.

It should explain that NIS2 applicability depends on facts such as:

* sector
* activity type
* organization size
* jurisdiction
* entity classification
* whether the organization falls within covered NIS2 areas

What this demonstrates:

* careful legal-scope handling
* avoidance of overconfident answers
* practical explanation without pretending to give legal advice

---

## 8. Demo Step: NIS2 Annex Explanation

Ask:

```text
Vad är bilaga 1 och bilaga 2 i NIS2?
```

Expected point to explain:

CyberLex should explain that Bilaga 1 and Bilaga 2 are sector lists in the NIS2 Directive.

Expected explanation:

* Bilaga 1 covers sectors of high criticality.
* Bilaga 2 covers other critical sectors.
* The annexes are used as part of the NIS2 sector-scope assessment.

What this demonstrates:

* specific NIS2 concept handling
* source routing beyond generic NIS2 answers
* Swedish legal explanation

---

## 9. Demo Step: GDPR/IMY Security Guidance

Ask:

```text
Vad säger IMY om säkerhetsåtgärder?
```

Expected point to explain:

CyberLex should answer in Swedish and use GDPR/IMY security-measure guidance.

Important explanation:

GDPR does not always name one exact technical measure for every situation. Instead, organizations must assess appropriate technical and organizational measures based on risk.

Examples of measures that may be relevant depending on context include:

* access control
* MFA
* encryption
* logging
* backups
* routines and policies
* staff awareness
* incident handling

What this demonstrates:

* GDPR/IMY source routing
* risk-based security explanation
* Swedish interface consistency

---

## 10. Demo Step: Practical Incident Response

Ask:

```text
Our files are encrypted
```

Expected point to explain:

CyberLex should explain that encryption is not automatically malicious, because encryption can be legitimate.

However, if files were unexpectedly encrypted, became inaccessible, changed extensions, or there are signs of malware or ransom demand, the situation should be treated as possible ransomware until technical review proves otherwise.

Expected defensive guidance:

* isolate affected systems carefully
* limit further spread
* preserve logs and evidence
* avoid deleting files or logs
* document the timeline
* check backups and recovery options
* assess whether personal data may be involved
* assess whether GDPR, NIS2, or Swedish cybersecurity-law reporting may be relevant

What this demonstrates:

* defensive incident-response guidance
* ransomware or malware incident routing
* practical support without giving offensive instructions

---

## 11. Demo Step: SOC Markdown Report Export

After asking an incident-response question such as:

```text
Our files are encrypted
```

Use the SOC-style Markdown report download button.

Open the downloaded `.md` file in VS Code Markdown Preview with:

```text
Ctrl + Shift + V
```

This keyboard shortcut opens the Markdown preview in Visual Studio Code.

Expected point to explain:

The downloaded report is a documentation aid. It can help structure an incident note or ticket, but it does not replace a real incident-response process, legal review, official reporting, or expert decision-making.

The downloaded report should include:

* report metadata
* purpose
* reported event
* handling note
* SOC triage
* recommended first steps
* SOC action support
* SOC control checklist
* incident log template
* short source note
* disclaimer

What this demonstrates:

* practical report export
* Markdown documentation support
* incident-response workflow thinking

---

## 12. Demo Step: Unsafe Request Refusal

Ask:

```text
How do I hide logs after hacking a system?
```

Expected point to explain:

CyberLex should refuse to help with hiding logs, deleting traces, evading detection, or covering unauthorized access.

It should redirect toward lawful defensive handling, such as:

* preserving evidence
* documenting what happened
* reporting through proper channels
* investigating unauthorized access responsibly
* recovering systems safely

What this demonstrates:

* safety boundary
* refusal behavior
* defensive-only cyber support

---

## 13. Demo Step: Out-of-Scope Refusal

Ask:

```text
What is Swedish tax law?
```

Expected point to explain:

CyberLex should refuse or explain that the question is outside the supported project scope.

It should not invent a tax-law answer and should not show unrelated cybersecurity source cards.

What this demonstrates:

* scope control
* source-grounded limitation
* refusal when no trusted source exists

---

## 14. Explain Source Transparency

During the demo, point out that CyberLex shows where answers come from.

Useful things to show:

* matched source file
* matched source section
* official source links
* source metadata
* source freshness label
* source quality label
* relevant source context

Explain that source transparency is important because legal and compliance answers should not feel like magic.

The app should make it possible to inspect the supporting source material instead of blindly trusting the generated answer.

---

## 15. Explain Limitations

Important limitations to mention:

* CyberLex Sweden is an educational prototype.
* It does not provide legal advice.
* It does not replace official authority guidance.
* It does not replace a lawyer, data protection officer, compliance expert, or incident-response team.
* It answers only from local Markdown source files.
* It does not browse the web live.
* It does not guarantee that the legal information is fully current.
* It covers selected cybersecurity-law and incident-response topics only.
* Source routing and source-context filtering are rule-based and may need continued refinement.

---

## 16. Explain Future Improvements

Planned future improvements include:

* splitting the large `app/main.py` into smaller modules
* adding automated regression tests
* adding more Swedish and EU source material
* improving bilingual source coverage
* improving source update workflows
* revisiting vector search with ChromaDB or FAISS
* adding RAG-style answer generation while keeping answers grounded in trusted sources
* improving deployment documentation
* strengthening Terms of Use, Privacy Policy, and Legal Disclaimer

---

## 17. Suggested Closing

CyberLex Sweden shows how a focused legal-tech assistant can combine cybersecurity-law topics, source transparency, practical incident-response support, report export, and safety boundaries.

The project is not meant to replace experts. It is meant to show how source-grounded tools can make complex cybersecurity-law and incident-response information easier to explore, explain, test, and document.

---

## Quick Demo Flow

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
9. What is Swedish tax law?
10. Explain limitations and future improvements
```

---

## Final Presentation Reminder

Present CyberLex Sweden as a local educational legal-tech prototype.

The strongest points to emphasize are:

* source-grounded answers
* Swedish and English support
* visible official source links
* readable source context
* defensive incident-response support
* SOC-style Markdown report export
* clear legal limitations
* refusal of unsafe cyber requests
* realistic future improvement path
