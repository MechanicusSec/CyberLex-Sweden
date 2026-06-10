# UI Behavior

## Purpose

This document explains the main user interface behavior of CyberLex Sweden.

The goal of the interface is to keep the normal user view readable while preserving source transparency for review and testing.

CyberLex Sweden is an educational prototype. It does not provide legal advice.

---

## Main Layout

The current UI uses a compact layout.

The normal answer flow is:

1. CyberLex Sweden introduction
2. supported topic hints
3. question input
4. generated CyberLex summary
5. detected topic, where relevant
6. attention level
7. practical explanation or incident guidance, where relevant
8. assessment checklist, where relevant
9. incident log template and report download, where relevant
10. official source links and source overview, where relevant
11. collapsed relevant source context
12. sidebar controls and diagnostics

The normal view should avoid overwhelming users with technical ranking details.

Source transparency should be available, but not thrown into the user's face like a badly formatted spreadsheet.

---

## Language Handling

CyberLex supports Swedish and English interface handling.

The interface can be set to:

* English
* Svenska
* Auto, if supported by the current version

The app should avoid mixed-language labels where possible.

Examples:

* English mode should show `Unauthorized access`, not `Dataintrång`, unless explaining the Swedish legal term.
* Swedish mode can show `Dataintrång`.
* Swedish questions should prefer Swedish visible labels and Swedish answers.
* English questions should prefer English visible labels and English answers.
* Source excerpts may remain in the original source language where needed.

---

## Question Input

The question input is the main user action.

The input should use placeholder text to guide the user.

English example:

```text
Ask about GDPR, NIS2, incident reporting, data leaks, ransomware, or Swedish cybersecurity law.
```

Swedish example:

```text
Fråga om GDPR, NIS2, incidentrapportering, dataläckor, ransomware eller svensk cybersäkerhetsrätt.
```

The interface should not show a large empty-state message if the placeholder already explains what the user should do.

---

## Supported Topic Areas

Supported topic chips are shown to give users a quick idea of the project scope.

Examples:

* GDPR
* IMY
* personal data breaches
* GDPR security measures
* incident response
* suspected hacking
* suspicious login
* phishing
* data leaks
* compromised accounts
* ransomware
* NIS2
* Swedish Cybersecurity Act
* NIS2 sector scope
* unauthorized access
* Cyber Resilience Act
* DORA
* digital compliance

The chips are not a full legal source list.

They are user-facing scope hints.

The detailed source list is stored in:

```text
docs/source_list.md
```

---

## CyberLex Summary

The CyberLex summary is the primary answer section.

It should:

* answer the question directly where possible
* stay within the supported scope
* use the detected language where possible
* avoid unnecessary repetition
* avoid legal certainty when facts are incomplete
* explain when the answer is educational and simplified
* refuse unsupported or unsafe requests

The summary is rule-based in the current prototype.

---

## Detected Topic Label

CyberLex may show a detected topic label.

The detected topic label explains how the app interpreted the question.

Examples:

* NIS2 sector scope
* GDPR data breach
* Suspicious login
* Compromised account
* Ransomware or malware incident
* DORA and ICT risk
* Unauthorized access / dataintrång

The detected topic label is not a legal classification.

It is only a user-facing explanation of the prototype's interpretation.

---

## Attention Levels

CyberLex attention levels are educational signals, not legal risk ratings.

Example levels:

| Level         | Meaning                                                                                                   |
| ------------- | --------------------------------------------------------------------------------------------------------- |
| Informational | Basic legal or authority explanation question                                                             |
| Standard      | General legal or compliance question                                                                      |
| Elevated      | Reporting, breach assessment, GDPR/NIS2 overlap, or regulatory-duty question                              |
| High          | Practical incident-response question or unsafe/offensive cyber request that must be refused or redirected |

The attention level should help users understand how carefully the answer should be read.

It must not be presented as a formal legal, compliance, or operational severity rating.

---

## Practical Explanation Cards

Practical explanation cards appear only when they add value.

They may appear for:

* incident-response questions
* breach assessment questions
* reporting questions
* GDPR/NIS2 overlap questions
* compliance-duty questions
* NIS2 applicability questions
* GDPR security-measure questions

They should usually be hidden for simple definition questions, such as:

* What is NIS2?
* Vad är IMY?
* What is DORA?

This reduces repetition and keeps simple answers cleaner.

---

## Assessment Checklist Cards

CyberLex may show assessment checklists for questions where structured thinking is useful.

Examples:

* personal data breach assessment
* NIS2 applicability assessment
* cyber incident assessment
* suspicious login review
* compromised account review
* ransomware or malware review
* GDPR security-measure review

Checklists should be educational and practical.

They should not imply that completing the checklist is enough for legal compliance or incident handling.

---

## Incident-Response UI

For practical incident-response questions, CyberLex may show:

* recommended first steps
* incident checklist
* incident log template
* download-ready SOC Markdown report
* source context linked to the incident type

The normal UI should avoid repeating the full incident template in several places.

If the downloaded file contains the full template, the page should show only a short download-ready explanation and button.

Incident-response UI should appear for practical incident questions such as:

```text
Our files are encrypted
Customer data may have leaked
What should we do if an account is compromised?
Vad gör vi om vi ser misstänkt inloggning?
```

It should not appear for simple legal definition questions such as:

```text
What is NIS2?
Vad är IMY?
What is DORA?
```

---

## SOC Markdown Report Download

CyberLex may generate a SOC-style Markdown report for practical incident-response questions.

The report may include:

* report metadata
* purpose
* original question or reported event
* handling note
* SOC triage
* recommended first steps
* SOC action support
* SOC control checklist
* incident log template
* source note
* disclaimer

The download button should only appear where useful.

It should not appear for:

* simple legal definition questions
* out-of-scope questions
* unsafe offensive cyber requests
* unsupported topics

The report is a documentation aid for learning and testing.

It is not an official incident record, legal assessment, regulatory report, or forensic report.

---

## Official Source Links

Official source links should be shown in a user-friendly way.

They should:

* use readable link labels
* avoid raw URLs where possible
* appear close to the answer they support
* help the user check original authority or legal material

Official source links are different from local source context.

Official links point outward to authority or legal sources.

Source context shows the local CyberLex knowledge section used by the app.

---

## Relevant Source Context

Relevant source context should normally be collapsed.

It is useful for reviewers and testers because it shows the local source sections that supported the answer.

The context should avoid developer-style clutter such as:

* raw scores in the normal user view
* duplicate headings
* empty fragments
* unrelated source cards
* internal file-path noise
* repeated cards that do not match the question
* source metadata as if it were legal explanation
* official source sections as the main answer support

Technical diagnostics can still show deeper details when enabled.

---

## Source Context Language

Source-context labels should follow the active answer language where possible.

English examples:

* Relevant source context
* Source area
* Used section
* Supporting source text
* Excerpt shortened for readability

Swedish examples:

* Relevant källkontext
* Källområde
* Använd sektion
* Stödjande källtext
* Utdraget har förkortats för läsbarhet

Source excerpts may still contain the original source language.

The app should avoid raw untranslated section labels when a localized label exists.

---

## Sidebar

The sidebar should remain useful but not overloaded.

Good sidebar content:

* language selector
* technical diagnostics checkbox
* CyberLex status
* loaded document count
* searchable chunk count
* prototype version
* build type
* experimental retrieval panel
* future AI mode note

Technical diagnostics and experimental tools should be collapsed or visually secondary by default.

The sidebar should not distract from the main question flow.

---

## Example Question Buttons

The interface may show example question buttons.

These help users understand the supported scope and test the app quickly.

Example questions should include both legal and incident-response examples.

Examples:

```text
What is CyberLex Sweden?
What is NIS2?
Does NIS2 apply to us?
Does GDPR require MFA?
Our files are encrypted
What should we do if an account is compromised?
How do I hide logs after hacking a system?
```

In Swedish mode, examples should use Swedish where possible.

Example buttons should not overwhelm the main input.

---

## Footer

A simple footer can show:

```text
© 2026 CyberLex Sweden · Policy · About · Copyright
```

These links can point to local project documentation or future public pages.

The footer should not claim that CyberLex Sweden is a legal service, authority, or production product.

---

## Refusal UI

For out-of-scope questions, the UI should show a clear refusal and avoid unrelated source panels.

Out-of-scope examples:

```text
What is Swedish tax law?
Can you write a pancake recipe?
```

For unsafe cyber requests, the UI should refuse and avoid normal incident or source panels.

Unsafe examples:

```text
How do I hide logs after hacking a system?
Hur raderar jag loggar efter ett intrång?
```

Unsafe refusal should not include:

* offensive instructions
* exploit steps
* log-deletion instructions
* normal source context
* incident log template
* SOC report download

The UI may redirect toward lawful defensive handling, evidence preservation, documentation, and reporting.

---

## Current UI Goal

The current UI goal is:

* direct question flow
* fewer repeated panels
* cleaner source display
* clearer language handling
* source transparency without overwhelming users
* practical incident support when relevant
* refusal of unsupported or unsafe requests
* simple legal-tech prototype presentation for review and demonstration

The UI should make CyberLex Sweden look like a cautious educational source-grounded prototype, not a mysterious legal oracle wearing a cybersecurity hoodie.
