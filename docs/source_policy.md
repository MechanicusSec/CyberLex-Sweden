# CyberLex Sweden Source Policy

## Purpose

This document defines how CyberLex Sweden should handle legal and cybersecurity sources.

Because CyberLex Sweden deals with legal and cybersecurity-related information, the system must avoid unsupported answers and should rely on trusted source material only.

The goal is to make the project safer, more transparent, easier to evaluate, and easier to maintain.

CyberLex Sweden is an educational prototype. It does not provide legal advice.

---

## Main rule

CyberLex Sweden should only answer questions when it can match the question to trusted source material in the local knowledge base.

If no trusted source is found, the system should refuse to answer confidently.

Example refusal:

```text
No trusted source was found for this question. CyberLex Sweden only covers Swedish cybersecurity law, cybercrime, GDPR, NIS2, incident reporting, data protection, EU cybersecurity law, and related digital compliance topics.
```

The system should not invent legal answers, guess legal obligations, or answer from general memory.

---

## Trusted source categories

CyberLex Sweden should prioritize sources from the following categories:

- official Swedish legal sources
- official Swedish authority sources
- official EU legal sources
- official EU agency or institution sources
- official cybersecurity authority guidance
- official data protection authority guidance
- documented educational summaries based on trusted sources

Examples of trusted sources include:

- Sveriges Riksdag
- IMY, Integritetsskyddsmyndigheten
- MSB, Myndigheten för samhällsskydd och beredskap
- EUR-Lex
- European Commission
- European Banking Authority, EBA
- European Insurance and Occupational Pensions Authority, EIOPA
- European Securities and Markets Authority, ESMA
- European Data Protection Board, EDPB

CyberLex Sweden may use other sources later, but official sources should normally be preferred.

---

## Local knowledge base policy

CyberLex Sweden currently answers from local Markdown files in:

```text
data/
```

The current local knowledge base includes:

```text
data/cybercrime_dataintrang.md
data/eu_attacks_against_information_systems.md
data/eu_cyber_resilience_act.md
data/eu_dora_digital_operational_resilience.md
data/gdpr_core_principles.md
data/gdpr_personal_data_breach.md
data/imy_gdpr_supervision.md
data/nis2_cybersecurity_law.md
data/nis2_incident_reporting.md
```

The app should treat these Markdown files as controlled educational summaries.

The app should not treat them as complete legal sources. They are simplified project files based on official source material.

---

## Required source file structure

Each source file in `data/` should include these sections where relevant:

- `## Topic`
- `## Main authority`
- `## Main legal source`
- `## Key idea`
- `## Important points`
- practical or cybersecurity connection
- useful questions
- `## Official source`
- `## Source metadata`
- `## Disclaimer`

The exact headings may vary slightly depending on the source, but the file should always clearly show:

- what the source topic is
- which authority or legal source it is based on
- what the key idea is
- which questions it supports
- which official links support the content
- when the file was last checked
- what changed in the file
- that the material is educational and not legal advice

---

## Official source links

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

- EUR-Lex pages for EU regulations and directives
- IMY guidance pages for GDPR and personal data breach topics
- MSB pages for NIS2 and Swedish cybersecurity guidance
- Riksdag pages for Swedish law

---

## Source metadata

Each source file should include a `## Source metadata` section.

Preferred format:

```markdown
## Source metadata

Source date: Last checked: 2026-06-03

Version notes: Source reviewed for CyberLex Sweden educational prototype.
```

The source date shows when the local source summary was last checked or reviewed.

The version notes explain what was added, cleaned, or changed.

Source metadata improves transparency, but it does not prove that the law is currently up to date.

---

## Source freshness labels

CyberLex Sweden may display source freshness labels based on the stored source date.

Examples:

```text
Last checked: 2026-06-03
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

## Source quality labels

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

The source quality label explains the type of source category. It is not a guarantee of legal completeness or current legal validity.

---

## Source audit policy

CyberLex Sweden includes a local source audit script:

```text
scripts/source_audit.py
```

The source audit checks Markdown source files in:

```text
data/
```

It checks for:

- official source section
- official source links
- source metadata section
- source date
- source freshness
- version notes

The audit report is written to:

```text
docs/source_audit_report.md
```

The expected current audit result is:

```text
Files marked OK: 9
Files needing review: 0
```

The source audit is a structure check. It does not browse the web and does not verify that laws or authority guidance are currently up to date.

This distinction must stay clear in documentation and user-facing explanations.

---

## GitHub Actions source audit policy

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

## Refusal behavior

CyberLex Sweden should refuse questions that are outside its trusted source scope.

Examples of out-of-scope areas:

- Swedish tax law
- family law
- medical advice
- investment advice
- unrelated political questions
- general trivia
- cybercrime instructions
- harmful security abuse instructions

The refusal should be clear, polite, and explain the project scope.

The system should not provide instructions for committing cybercrime, bypassing security, stealing credentials, exploiting systems without authorization, or hiding activity.

CyberLex Sweden may explain legal concepts such as unauthorized access, dataintrång, DDoS, botnets, misuse of tools, and incident reporting in an educational and lawful context.

---

## Source-grounding rule for future AI or RAG

If CyberLex Sweden later adds a language model or RAG mode, the AI should not answer freely from general model memory.

Future AI-generated answers should use retrieved source chunks from the trusted local knowledge base.

A future AI answer should normally include:

1. a short answer
2. a plain-language explanation
3. citation details
4. official source links
5. an important limitation
6. a refusal if no trusted source supports the answer

The system should not generate legal claims that are not supported by retrieved source material.

---

## Supported source topics

CyberLex Sweden currently supports selected questions about:

- GDPR core principles
- GDPR personal data breaches
- IMY and Swedish GDPR supervision
- NIS2 and Swedish cybersecurity law
- NIS2 incident reporting
- ransomware and cyber incident assessment
- Swedish cybercrime law and dataintrång
- EU attacks against information systems
- Cyber Resilience Act
- DORA and digital operational resilience
- overlap between cybersecurity incidents and data protection duties

CyberLex Sweden does not cover all Swedish law or all EU digital regulation.

---

## Source update history

Source updates should be documented in:

```text
docs/source_update_history.md
```

The source update history should describe:

- which file was updated
- what was changed
- why it was changed
- what result or test case confirmed the update
- whether retrieval logic was changed

This helps reviewers understand how the knowledge base developed over time.

---

## Version control policy

Source file changes should be committed to Git with clear messages.

Good commit messages include:

```text
Improve Swedish DORA source support
Improve Swedish CRA source support
Update source history with EU attacks support
Update source list with current knowledge base
```

The purpose is to make the project history understandable.

Generated or temporary files should not be committed unless intentionally included.

Examples that should normally not be committed:

- `.venv/`
- cache folders
- generated vector index files
- temporary test files
- downloaded model files

---

## Future source review workflow

Future versions of CyberLex Sweden may improve source review by adding:

- source owners or reviewers
- source status labels such as active, needs review, outdated, retired
- automated link checking
- scheduled source review reminders
- separate review dates for each official link
- source change detection
- live legal update review workflow
- better distinction between Swedish law, EU law, and authority guidance
- source-to-chunk metadata for future vector search or RAG

These improvements would make the source system stronger if CyberLex Sweden becomes public or more product-like.

---

## Important limitation

This source policy defines how CyberLex Sweden should handle local project sources.

It does not make CyberLex Sweden a legal authority.

It does not prove that any law, regulation, or authority guidance is currently up to date.

For important legal, compliance, or cybersecurity decisions, users should check official sources and qualified professional advice.

CyberLex Sweden remains an educational prototype.
