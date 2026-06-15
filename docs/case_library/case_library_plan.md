# CyberLex Sweden Case Library Plan

## Purpose

This document explains how CyberLex Sweden will use real authority decisions, court cases, and case-like enforcement examples as educational reference material.

The goal is to make CyberLex Sweden more useful for both school project work and possible future real-world development.

The case library should help users understand how cybersecurity, GDPR, data breaches, information leaks, unauthorized access, and digital compliance issues have been handled in real decisions.

CyberLex Sweden remains an educational prototype. It does not provide legal advice.

---

## Why Add a Case Library?

CyberLex Sweden currently explains selected legal and cybersecurity topics from local source files.

A case library adds another layer:

```text
Legal rule or guidance + real decision example = better understanding
```

Cases can help show:

* what happened in real incidents
* what authority or court reviewed the issue
* what legal problem mattered
* what security weakness was important
* whether a fine or other consequence was issued
* what CyberLex users can learn from the case

This makes CyberLex more realistic and useful than only showing abstract legal summaries.

---

## Case Library Scope

The first case library should focus on cases and authority decisions related to:

* GDPR personal data breaches
* data leaks
* information leaks
* unlawful disclosure of personal data
* insufficient security measures
* unauthorized access
* hacking or intrusion
* ransomware or malware incidents
* use of tracking tools such as Meta Pixel where personal data was transferred
* administrative fines
* cybersecurity-related compliance failures

The first version should prioritize Swedish and EU sources.

---

## Preferred Source Types

CyberLex Sweden should prioritize official or high-quality sources.

Preferred sources:

* IMY decisions and press releases
* EDPB summaries of national supervisory authority decisions
* Swedish court decisions where available and relevant
* EUR-Lex where EU legal context is needed
* official authority reports
* official cybersecurity authority guidance

Secondary sources may be used only for orientation, not as the main source, unless no official source is available.

---

## First Case Candidates

Good first case candidates include:

1. Avanza Bank and Meta Pixel

   Topic: transfer of customer data to Meta through Meta Pixel.

   Why useful: shows how tracking technology, financial data, GDPR security, and unlawful transfer can create serious compliance risk.

2. Swedish insurance company security case

   Topic: insufficient security measures and personal data exposure.

   Why useful: connects directly to GDPR security measures, access control, and security weakness assessment.

3. SL and WÅAB administrative fines

   Topic: processing personal data related to employee sobriety tests.

   Why useful: shows that even lower fines can matter and that GDPR applies to workplace processing and sensitive contexts.

4. Apoteket and Apohem Meta Pixel fines

   Topic: transfer of sensitive personal data to Meta through website tracking.

   Why useful: strong example of data leakage through tracking technology in a sensitive sector.

5. Equality Ombudsman web form case

   Topic: insufficient security measures in a web form.

   Why useful: simple case example for security measures, web forms, and personal data exposure.

---

## Case File Location

Case files should be stored in:

```text
cases/
```

Example filenames:

```text
cases/imy_avanza_bank_meta_pixel.md
cases/imy_insurance_company_security_measures.md
cases/imy_sl_waab_employee_sobriety_tests.md
cases/imy_apoteket_apohem_meta_pixel.md
cases/imy_equality_ombudsman_web_form.md
```

Each file should use a consistent structure so the app can later search, display, and compare cases.

---

## Case File Template

Each case file should use this structure:

```markdown
# Case title

## Case type

IMY decision / court case / EDPB summary / authority decision / other

## Jurisdiction

Sweden / EU / other

## Year

YYYY

## Authority or court

Name of authority or court

## Topic

Short topic labels.

## Short summary

A short educational summary of the case.

## What happened

What happened in plain language.

## Legal issue

What legal or compliance issue was reviewed.

## Decision or outcome

What the authority or court decided.

## Fine or cost

Fine amount, cost, or outcome if officially available.

If no fine amount is available, write:

No official fine amount included in this source summary.

## Why it matters for CyberLex

Explain what CyberLex users can learn from this case.

## Similar CyberLex questions

- Example user question
- Example user question

## Related CyberLex topics

- GDPR
- IMY
- Personal data breach
- Security measures
- Incident response
- NIS2
- DORA
- Dataintrång

## Official source

- [Official source name](https://example.com)

## Case metadata

Source date: Last checked: YYYY-MM-DD

Version notes: Initial CyberLex Sweden educational case summary.

## Disclaimer

This is an educational case summary. It is not legal advice and does not replace the official decision, authority source, court judgment, or qualified legal review.
```

---

## Case Selection Rules

A case should be added only if:

* it is relevant to CyberLex Sweden's scope
* it has an official or high-quality source
* the source can be cited clearly
* the case can be summarized without guessing
* the case teaches something useful about cybersecurity law, GDPR, data protection, incident response, or digital compliance

A case should not be added if:

* the source is unclear
* the facts are too uncertain
* the source is only a random news article
* the topic is outside CyberLex Sweden's scope
* the summary would require legal speculation

---

## How Cases Should Be Used Later

In a future app version, CyberLex could show related cases after the main source-grounded answer.

Example:

```text
Related cases:
- Avanza Bank and Meta Pixel
- Apoteket and Apohem Meta Pixel
```

The case display should include:

* case title
* authority or court
* year
* topic
* short summary
* fine or outcome
* official source link
* educational limitation

Cases should support the answer, not replace legal sources.

---

## Risk and Cost Context

The case library can support future risk and cost context.

CyberLex may later explain possible cost areas such as:

* administrative fines
* legal review
* incident response
* forensic investigation
* customer or data subject notification
* downtime
* remediation work
* reputation damage
* internal investigation
* authority communication

CyberLex should not predict exact fines.

A safe wording is:

```text
CyberLex does not predict fines. This is an educational risk context based on known factors and previous decisions.
```

---

## Future Fine and Risk Factors

A future risk model may consider:

* number of affected people
* type of personal data
* sensitive data involved
* duration of the issue
* intentional or negligent behavior
* security measures in place
* whether the organization detected the issue itself
* whether the organization mitigated harm
* whether notification was delayed
* cooperation with the authority
* previous similar issues
* sector and organizational context

These factors should be explained as educational risk indicators, not as a legal fine calculator.

---

## Development Order

Recommended order:

1. Create case library plan.
2. Create case file template.
3. Add first 3 case summaries.
4. Add source audit support for `cases/`.
5. Add case search as a separate experimental feature.
6. Add related-case display in the app.
7. Add educational risk and cost context.
8. Add test cases for case retrieval.
9. Consider future RAG only after case retrieval works reliably.

---

## Git Policy for This Feature

This work should stay local until a stable milestone is reached.

Recommended push points:

* after the case library plan and first case files are complete
* after case audit works
* after related-case search works
* after the app displays related cases cleanly

Do not push every tiny edit.

---

## Final Note

The case library should make CyberLex Sweden more useful and realistic.

It should also stay careful, source-grounded, and educational.

Cases should help users understand real-world consequences, but CyberLex should not pretend to predict legal outcomes.
