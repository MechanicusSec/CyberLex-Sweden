# CyberLex Sweden Case Library Plan

## Purpose

This document explains how CyberLex Sweden uses real authority decisions, court cases, and case-like enforcement examples as educational reference material.

The goal is to make CyberLex Sweden more useful for both school project work and possible future real-world development.

The case library helps users understand how cybersecurity, GDPR, data breaches, information leaks, unauthorized access, tracking technology, weak security measures, and digital compliance issues have been handled in real decisions.

CyberLex Sweden remains an educational prototype. It does not provide legal advice and does not predict legal outcomes.

---

## Current Status

The first working version of the case library has been implemented.

CyberLex Sweden currently includes:

* Markdown case files stored in `cases/`
* a case search module in `app/case_search.py`
* a Case Intelligence / authority decisions page in the Streamlit app
* related-case display under relevant answers
* case filtering in the user interface
* bilingual case display support
* language-aware official source display
* a case audit script
* a generated case audit report
* case learning notes in English and Swedish
* educational limitation text warning that historical outcomes are not fine predictions

The current case audit checks 8 case files.

---

## Why Add a Case Library?

CyberLex Sweden explains selected legal and cybersecurity topics from local source files.

A case library adds another layer:

```text
Legal rule or guidance + real decision example = better understanding
```

Cases can help show:

* what happened in real incidents
* what authority or court reviewed the issue
* what legal problem mattered
* what security weakness was important
* whether a fine, reprimand, or other outcome was issued
* what CyberLex users can learn from the case
* how similar legal or cybersecurity issues can be assessed differently depending on the facts

This makes CyberLex more realistic and useful than only showing abstract legal summaries.

---

## Case Library Scope

The first case library focuses on cases and authority decisions related to:

* GDPR personal data breaches
* data leaks
* information leaks
* unlawful disclosure of personal data
* insufficient security measures
* unauthorized access risk
* hacking or intrusion
* cyber attacks
* publication of leaked data
* use of tracking tools such as Meta Pixel where personal data was transferred
* web forms and analytics tools
* accidental disclosure by email
* app data exposure caused by technical or deployment errors
* supervisory investigations and public incident examples
* administrative fines
* reprimands
* cybersecurity-related compliance failures

The first version prioritizes Swedish and EU sources.

---

## Preferred Source Types

CyberLex Sweden should prioritize official or high-quality sources.

Preferred sources:

* IMY decisions and press releases
* IMY supervision pages
* EDPB summaries of national supervisory authority decisions
* Swedish court decisions where available and relevant
* EUR-Lex where EU legal context is needed
* official authority reports
* official cybersecurity authority guidance
* official company statements only as supporting context, not as the main legal source
* high-quality public reporting for public incident examples where no authority decision is available

Secondary sources may be used only for orientation, not as the main source, unless no official source is available. If a case is based partly on public reporting, CyberLex should label it clearly as a public incident or supervisory investigation example instead of presenting it as an authority decision.

---

## Current Case Files

The current case library includes these case files:

```text
cases/imy_apoteket_apohem_meta_pixel.md
cases/imy_avanza_bank_meta_pixel.md
cases/imy_equality_ombudsman_web_form.md
cases/imy_kry_meta_pixel.md
cases/klarna_app_data_exposure_2021.md
cases/imy_sportadmin_security_breach.md
cases/imy_trygg_hansa_security_deficiencies.md
cases/imy_wrong_email_customer_data.md
```

These files currently cover:

* Apoteket and Apohem Meta Pixel
* Avanza Bank and Meta Pixel
* Equality Ombudsman web form security case
* Kry Meta Pixel
* Klarna app data exposure 2021
* Sportadmin security breach
* Trygg-Hansa security deficiencies
* Wrong email customer data case

---

## Case File Location

Case files are stored in:

```text
cases/
```

Supporting case-library documentation is stored in:

```text
docs/case_library/
```

The generated case audit report is stored in:

```text
docs/case_library/case_audit_report.md
```

The case audit script is:

```text
scripts/case_audit.py
```

The case search module is:

```text
app/case_search.py
```

The main Streamlit case display is handled in:

```text
app/main.py
```

---

## Case File Template

Each case file should use a consistent structure so the app can search, display, and compare cases.

Recommended structure:

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

A short English educational summary of the case.

## Swedish short summary

A short Swedish educational summary of the case.

## What happened

What happened in plain English.

## Swedish what happened

What happened in plain Swedish.

## Legal issue

What legal or compliance issue was reviewed.

## Swedish legal issue

The same legal or compliance issue explained in Swedish.

## Decision or outcome

What the authority or court decided.

## Swedish decision or outcome

The decision or outcome explained in Swedish.

## Fine or cost

Fine amount, cost, or outcome if officially available.

CyberLex should not present this amount as a prediction for other cases.

## Swedish fine or cost

Fine amount, cost, or outcome explained in Swedish.

CyberLex ska inte presentera detta belopp som en förutsägelse för andra fall.

## Why it matters for CyberLex

Explain what CyberLex users can learn from this case.

## Swedish why it matters for CyberLex

Explain the educational value in Swedish.

## Learning note

Short English educational lesson from the case.

## Swedish learning note

Short Swedish educational lesson from the case.

## Similar CyberLex questions

- Example user question
- Example user question

## Related CyberLex topics

- GDPR
- IMY
- Personal data breach
- Security measures
- Incident response

## Swedish related CyberLex topics

- GDPR
- IMY
- Personuppgiftsincident
- Säkerhetsåtgärder
- Incidenthantering

## Official source

- [Official English or general source name](https://example.com)

## Swedish official source

- [Official Swedish source name](https://example.com)

If no Swedish source exists, use a clear label such as:

- [IMY - Officiell källa, engelsk IMY-sida](https://example.com)

## Case metadata

Source date: Last checked: YYYY-MM-DD

Version notes: Initial CyberLex Sweden educational case summary.

## Disclaimer

This is an educational case summary. It is not legal advice and does not replace the official decision, authority source, court judgment, or qualified legal review.
```

---

## Bilingual Case Display

CyberLex Sweden supports bilingual display for the Case Intelligence page.

The app can show:

* English case summaries in English mode
* Swedish case summaries in Swedish mode
* English fine or outcome sections in English mode
* Swedish fine or outcome sections in Swedish mode
* English related topic chips in English mode
* Swedish related topic chips in Swedish mode
* English and Swedish learning notes where available
* language-aware source links

The app uses fallback behavior when a section is missing.

For example:

* if `## Swedish short summary` exists, Swedish mode uses it
* if `## Swedish short summary` is missing, Swedish mode can fall back to `## Short summary`
* if `## Swedish official source` exists, Swedish mode uses it
* if no Swedish official source exists, the app can fall back to available official sources instead of hiding all source information

This keeps the interface clean while still preserving source transparency.

---

## Official Source Language Rules

Official source links should be handled carefully.

Recommended behavior:

```text
English mode -> show English or general official sources
Swedish mode -> show Swedish official sources when available
Auto mode -> show both English and Swedish official sources where available
```

If only one official source language exists, CyberLex may still show that source instead of leaving the source section empty.

This is especially important when an official authority only provides a source page in one language.

Case files should use:

```markdown
## Official source
```

for English or general official sources.

Case files should use:

```markdown
## Swedish official source
```

for Swedish official sources or Swedish-labeled official-source fallback entries.

---

## Case Selection Rules

A case should be added only if:

* it is relevant to CyberLex Sweden's scope
* it has an official or high-quality source
* the source can be cited clearly
* the case can be summarized without guessing
* the case teaches something useful about cybersecurity law, GDPR, data protection, incident response, or digital compliance
* the case can be presented with a clear educational limitation

A case should not be added if:

* the source is unclear
* the facts are too uncertain
* the source is only a random news article
* the topic is outside CyberLex Sweden's scope
* the summary would require legal speculation
* the case would make CyberLex appear to predict fines or legal outcomes

---

## Case Search and Related Cases

The app uses the case search module:

```text
app/case_search.py
```

The purpose of this module is to search the case library and find related authority decisions or enforcement examples.

The app can use related cases in two ways:

1. On the Case Intelligence page, where users can browse and filter all cases.
2. Under normal CyberLex answers, where related cases can support the main source-grounded answer.

Related cases should support the main answer, not replace legal sources.

A good related-case display should include:

* case title
* short summary
* fine or outcome
* learning note
* related CyberLex topics
* official source links
* educational limitation

The display should not suggest that a historic fine predicts a future fine.

---

## Case Intelligence Page

The Case Intelligence page allows users to browse authority decisions and case examples used by CyberLex Sweden as educational references.

The page should show:

* number of cases in the library
* number of visible cases after filtering
* search/filter field
* educational limitation warning
* expandable case cards
* summary
* fine or outcome
* related topics
* official source links

The page should support filtering by words such as:

```text
Meta Pixel
säkerhet
e-post
dataläcka
Darknet
Sportadmin
Avanza
Apoteket
Kry
Klarna
app
customer data
```

The page should respect the selected language mode.

---

## Case Audit System

CyberLex Sweden includes a case audit system.

The script is:

```text
scripts/case_audit.py
```

The script checks Markdown files in:

```text
cases/
```

It checks whether each case file has the required structure.

The generated report is:

```text
docs/case_library/case_audit_report.md
```

The case audit helps verify that case files include required headings and official-source information.

The audit does not browse the web and does not verify live legal currency.

It only checks local file structure and stored metadata.

---

## Risk and Cost Context

The case library can support risk and cost context.

CyberLex may explain possible cost areas such as:

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

Safe wording:

```text
CyberLex does not predict fines. This is educational risk context based on known factors and previous decisions.
```

Case amounts should be treated as historical examples from specific decisions, not as predictions.

---

## Future Fine and Risk Factors

A future risk model may consider:

* number of affected people
* type of personal data
* sensitive data involved
* children or protected identity information involved
* duration of the issue
* intentional or negligent behavior
* security measures in place
* whether the organization detected the issue itself
* whether the organization mitigated harm
* whether notification was delayed
* cooperation with the authority
* previous similar issues
* sector and organizational context
* whether the issue involved tracking technology or third-party tools
* whether the issue involved web forms, email mistakes, or weak access control

These factors should be explained as educational risk indicators, not as a legal fine calculator.

---

## Development Order

Original recommended order:

1. Create case library plan.
2. Create case file template.
3. Add first 3 case summaries.
4. Add source audit support for `cases/`.
5. Add case search as a separate experimental feature.
6. Add related-case display in the app.
7. Add educational risk and cost context.
8. Add test cases for case retrieval.
9. Consider future RAG only after case retrieval works reliably.

Current progress:

* case library plan created
* case files created
* case audit support added
* case search added
* related-case display added
* Case Intelligence page added
* bilingual case display added
* source-language display behavior improved
* manual regression tests added
* documentation updated
* case learning notes added
* Klarna app data exposure 2021 added as a public incident / supervisory investigation example

Remaining possible next steps:

* add more cases gradually
* improve exact source-language coverage where Swedish and English authority pages both exist
* refine case filtering and ranking
* add more structured case metadata if needed
* consider future RAG only after retrieval stays reliable

---

## Git Policy for This Feature

This work should stay local until a stable milestone is reached.

Recommended push points:

* after the case library plan and first case files are complete
* after case audit works
* after related-case search works
* after the app displays related cases cleanly
* after bilingual case display and test documentation are stable

Do not push every tiny edit.

This protects the project while it is still being actively improved.

---

## Final Note

The case library makes CyberLex Sweden more useful and realistic.

It should also stay careful, source-grounded, and educational.

Cases should help users understand real-world consequences, but CyberLex should not pretend to predict legal outcomes.

The current case-library implementation is a strong local milestone with 8 case files, including IMY-related decisions and one Klarna public app data exposure / supervisory investigation example. Future additions should still be added slowly and tested carefully.
