# CyberLex Sweden Source Policy

## Purpose

This document defines how CyberLex Sweden should handle legal, cybersecurity, compliance, and defensive incident-response sources.

Because CyberLex Sweden deals with legal and cybersecurity-related information, the system must avoid unsupported answers and should rely on trusted source material only.

The goal is to make the project safer, more transparent, easier to evaluate, and easier to maintain.

CyberLex Sweden is an educational prototype. It does not provide legal advice.

---

## Main Rule

CyberLex Sweden should only answer questions when it can match the question to trusted source material in the local knowledge base.

If no trusted source is found, the system should refuse to answer confidently.

Example refusal:

```text
No trusted source was found for this question. CyberLex Sweden only covers selected Swedish and EU cybersecurity law, cybercrime, GDPR, NIS2, incident reporting, DORA, the Cyber Resilience Act, EU attacks against information systems, data protection, and related digital compliance topics.
```

The system should not:

* invent legal answers
* guess legal obligations
* answer legal questions from general memory
* claim legal certainty without source support
* answer outside the project scope

---

## Trusted Source Categories

CyberLex Sweden should prioritize sources from the following categories:

* official Swedish legal sources
* official Swedish authority sources
* official EU legal sources
* official EU agency or institution sources
* official cybersecurity authority guidance
* official data protection authority guidance
* defensive incident-response guidance from trusted authorities
* documented educational summaries based on trusted sources

Examples of trusted sources include:

* Sveriges Riksdag
* IMY, Integritetsskyddsmyndigheten
* MSB, Myndigheten för samhällsskydd och beredskap
* CERT-SE
* EUR-Lex
* European Commission
* European Banking Authority, EBA
* European Insurance and Occupational Pensions Authority, EIOPA
* European Securities and Markets Authority, ESMA
* European Data Protection Board, EDPB

CyberLex Sweden may use other sources later, but official sources should normally be preferred.

---

## Local Knowledge Base Policy

CyberLex Sweden currently answers from local Markdown files in:

```text
data/
```

The current local source audit checks 13 source files:

```text
data/cyber_incident_response_playbook.md
data/cybercrime_dataintrang.md
data/eu_attacks_against_information_systems.md
data/eu_cyber_resilience_act.md
data/eu_dora_digital_operational_resilience.md
data/gdpr_core_principles.md
data/gdpr_imy_edpb_security_guidance.md
data/gdpr_personal_data_breach.md
data/imy_gdpr_security_measures.md
data/imy_gdpr_supervision.md
data/nis2_cybersecurity_law.md
data/nis2_incident_reporting.md
data/nis2_sector_scope_guidance.md
```

The current audit result is:

```text
Files marked OK: 12
Files needing review: 1
```

The file currently needing review is:

```text
data/gdpr_imy_edpb_security_guidance.md
```

Reason:

```text
Missing Official source section, official source links, Source metadata section, source date, and version notes.
```

Recommended action:

This file should be fixed or removed before final hand-in.

If it duplicates `data/imy_gdpr_security_measures.md`, it should probably be removed after confirming that the app does not depend on it.

The app should treat Markdown files as controlled educational summaries.

The app should not treat them as complete legal sources. They are simplified project files based on official or trusted source material.

---

## Required Source File Structure

Each source file in `data/` should include these sections where relevant:

* `## Topic`
* `## Main authority`
* `## Main legal source`
* `## Key idea`
* `## Important points`
* practical or cybersecurity connection
* useful questions
* `## Official source`
* `## Source metadata`
* `## Disclaimer`

The exact headings may vary slightly depending on the source, but the file should always clearly show:

* what the source topic is
* which authority or legal source it is based on
* what the key idea is
* which questions it supports
* which official links support the content
* when the file was last checked
* what changed in the file
* that the material is educational and not legal advice

---

## Official Source Links

Each source file should include an `## Official source` section.

Official sources should use readable Markdown links when possible.

Preferred format:

```markdown
## Official source

- [Source name](https://example.com)
```

Raw URLs may work technically, but readable Markdown links are easier to review and easier to display in the app.

Official links should point to primary sources when possible.

Examples:

* EUR-Lex pages for EU regulations and directives
* IMY guidance pages for GDPR and personal data breach topics
* MSB pages for NIS2 and Swedish cybersecurity guidance
* Riksdag pages for Swedish law
* CERT-SE pages for defensive incident-response support
* EDPB pages for GDPR guidance

---

## Source Metadata

Each source file should include a `## Source metadata` section.

Preferred format:

```markdown
## Source metadata

Source date: Last checked: 2026-06-10

Version notes: Source reviewed for CyberLex Sweden educational prototype.
```

The source date shows when the local source summary was last checked or reviewed.

The version notes explain what was added, cleaned, or changed.

Source metadata improves transparency, but it does not prove that the law is currently up to date.

---

## Source Freshness Labels

CyberLex Sweden may display source freshness labels based on the stored source date.

Examples:

```text
Last checked: 2026-06-08
→ Recently checked
```

```text
No source date stored
→ No review date stored
```

```text
Older stored review date
→ Review recommended
```

These labels are transparency indicators only.

They do not check the internet and do not confirm current legal validity.

---

## Source Quality Labels

CyberLex Sweden may display source quality labels based on the matched local source file.

Examples:

```text
cybercrime_dataintrang.md
→ Swedish legal source / criminal-law topic
```

```text
imy_gdpr_supervision.md
→ Swedish supervisory authority source
```

```text
imy_gdpr_security_measures.md
→ Swedish authority guidance on GDPR security measures
```

```text
eu_dora_digital_operational_resilience.md
→ EU digital operational resilience regulation source
```

```text
eu_cyber_resilience_act.md
→ EU regulation source for digital product cybersecurity
```

```text
eu_attacks_against_information_systems.md
→ EU directive source on attacks against information systems
```

```text
cyber_incident_response_playbook.md
→ Defensive incident-response guidance
```

The source quality label explains the type of source category.

It is not a guarantee of legal completeness or current legal validity.

---

## Source Audit Policy

CyberLex Sweden includes a local source audit script:

```text
scripts/source_audit.py
```

The source audit checks Markdown source files in:

```text
data/
```

It checks for:

* official source section
* official source links
* source metadata section
* source date
* source freshness
* version notes

The audit report is written to:

```text
docs/source_audit_report.md
```

Current audit result:

```text
Files marked OK: 12
Files needing review: 1
```

The source audit is a structure check.

It does not browse the web and does not verify that laws, regulations, or authority guidance are currently up to date.

This distinction must stay clear in documentation and user-facing explanations.

---

## GitHub Actions Source Audit Policy

CyberLex Sweden includes a GitHub Actions workflow:

```text
.github/workflows/source-audit.yml
```

The workflow runs the local source audit automatically on a schedule and can also be started manually from GitHub Actions.

The workflow is intended to:

1. check out the repository
2. set up Python
3. run `python scripts/source_audit.py`
4. update `docs/source_audit_report.md`
5. commit the updated report if needed

This workflow helps keep the audit report updated, but it does not perform live legal review.

The workflow should not be described as confirming that legal sources are current.

---

## Refusal Behavior

CyberLex Sweden should refuse questions that are outside its trusted source scope.

Examples of out-of-scope areas:

* Swedish tax law
* family law
* medical advice
* investment advice
* unrelated political questions
* general trivia
* recipes
* unrelated homework questions
* cybercrime instructions
* harmful security abuse instructions

The refusal should be clear and should explain the project scope.

The system should not provide instructions for:

* committing cybercrime
* bypassing security
* stealing credentials
* exploiting systems without authorization
* hiding activity
* deleting traces
* evading detection
* maintaining unauthorized access

CyberLex Sweden may explain legal concepts such as unauthorized access, dataintrång, DDoS, botnets, misuse of tools, and incident reporting in an educational and lawful context.

---

## Defensive Cyber Guidance Policy

CyberLex Sweden may provide defensive incident-response guidance for supported incidents.

Supported incident-response topics include:

* suspicious emails
* phishing
* clicked links
* opened attachments
* entered credentials
* suspicious login activity
* suspicious MFA activity
* compromised accounts
* suspected hacking
* malware
* ransomware
* encrypted files
* customer data leaks
* possible personal data breaches

Defensive guidance should focus on:

* containment
* evidence preservation
* documentation
* internal reporting
* escalation
* recovery planning
* GDPR/IMY assessment where relevant
* NIS2 or Swedish cybersecurity-law assessment where relevant

It should not provide offensive instructions.

---

## Source-Grounding Rule for Future AI or RAG

If CyberLex Sweden later adds a language model or RAG mode, the AI should not answer freely from general model memory.

Future AI-generated answers should use retrieved source chunks from the trusted local knowledge base.

A future AI answer should normally include:

1. short answer
2. plain-language explanation
3. citation details
4. official source links
5. source metadata
6. important limitation
7. refusal if no trusted source supports the answer

The system should not generate legal claims that are not supported by retrieved source material.

The rule is:

```text
No trusted source, no answer.
```

---

## Supported Source Topics

CyberLex Sweden currently supports selected questions about:

* GDPR core principles
* GDPR personal data breaches
* GDPR/IMY security measures
* IMY and Swedish GDPR supervision
* NIS2 and Swedish cybersecurity law
* NIS2 incident reporting
* NIS2 sector scope and entity classification
* ransomware and cyber incident assessment
* defensive incident response
* Swedish cybercrime law and dataintrång
* EU attacks against information systems
* Cyber Resilience Act
* DORA and digital operational resilience
* overlap between cybersecurity incidents and data protection duties

CyberLex Sweden does not cover all Swedish law or all EU digital regulation.

---

## Source History Policy

Source updates should be documented in:

```text
docs/source_history.md
```

The source history should describe:

* which file was updated
* what was changed
* why it was changed
* what result or test case confirmed the update
* whether retrieval logic was changed

This helps reviewers understand how the knowledge base developed over time.

Older references to `docs/source_update_history.md` should be replaced with `docs/source_history.md`.

---

## Version Control Policy

Source file changes should be committed to Git with clear messages.

Good commit messages include:

```text
Improve Swedish DORA source support
Improve Swedish CRA source support
Update source history with EU attacks support
Update source list with current knowledge base
Update source policy for current audit status
```

The purpose is to make the project history understandable.

Generated or temporary files should not be committed unless intentionally included.

Examples that should normally not be committed:

* `.venv/`
* `__pycache__/`
* `.streamlit/cache/`
* generated vector index files
* temporary test files
* downloaded model files

---

## Future Source Review Workflow

Future versions of CyberLex Sweden may improve source review by adding:

* source owners or reviewers
* source status labels such as active, needs review, outdated, retired
* automated link checking
* scheduled source review reminders
* separate review dates for each official link
* source change detection
* live legal update review workflow
* better distinction between Swedish law, EU law, and authority guidance
* source-to-chunk metadata for future vector search or RAG

These improvements would make the source system stronger if CyberLex Sweden becomes public or more product-like.

---

## Important Limitation

This source policy defines how CyberLex Sweden should handle local project sources.

It does not make CyberLex Sweden a legal authority.

It does not prove that any law, regulation, or authority guidance is currently up to date.

For important legal, compliance, regulatory, or cybersecurity decisions, users should check official sources and qualified professional advice.

CyberLex Sweden remains an educational prototype.
