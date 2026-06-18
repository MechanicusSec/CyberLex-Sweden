# UI Behavior

## Purpose

This document explains the main user interface behavior of CyberLex Sweden.

The goal of the interface is to keep the normal user view readable while preserving source transparency for review and testing.

CyberLex Sweden is an educational prototype. It does not provide legal advice.

---

## Current Behavior Summary

The current UI behavior includes:

* English, Swedish, and Auto language modes
* example questions that run immediately when selected
* synchronized visible input and submitted question state
* source-grounded answer display
* collapsed relevant source context
* practical incident-response panels only where useful
* related cases only for relevant compliance or case-library questions
* hidden related-case section for practical incident-response triage questions
* Case Intelligence page for browsing local case examples

---

## Main Layout

The current UI uses a compact layout.

The normal answer flow is:

1. CyberLex Sweden introduction
2. supported topic hints
3. question input
4. optional example question panel
5. generated CyberLex summary
6. detected topic, where relevant
7. attention level
8. practical explanation or incident guidance, where relevant
9. assessment checklist, where relevant
10. incident log template and report download, where relevant
11. official source links and source overview, where relevant
12. related cases, only where relevant
13. collapsed relevant source context
14. sidebar controls and diagnostics

The normal view should avoid overwhelming users with technical ranking details.

Source transparency should be available, but not thrown into the user's face like a badly formatted spreadsheet.

---

## Language Handling

CyberLex supports Swedish and English interface handling.

The interface can be set to:

* English
* Svenska
* Auto

In Auto mode, the app detects the visible active question and decides whether the answer flow should use English or Swedish.

Examples:

```text
Can Meta Pixel create GDPR risk?
→ English
```

```text
Kan Meta Pixel skapa GDPR-risk?
→ Svenska
```

```text
What is NIS2?
→ English
```

```text
Vad är NIS2?
→ Svenska
```

The app should avoid mixed-language labels where possible.

Examples:

* English mode should show `Unauthorized access`, not `Dataintrång`, unless explaining the Swedish legal term.
* Swedish mode can show `Dataintrång`.
* Swedish questions should prefer Swedish visible labels and Swedish answers.
* English questions should prefer English visible labels and English answers.
* Source excerpts may remain in the original source language where needed.

Auto language detection is rule-based. It has been improved for mixed cybersecurity/legal questions, but it is not a full translation system.

---

## Question Input

The question input is the main user action.

The input should use placeholder text to guide the user.

The visible input field, the submitted question, and the selected example question should stay synchronized through Streamlit session state.

The user should be able to submit a question by:

* typing a question and pressing Enter
* typing a question and clicking the search button
* selecting an example question

The app should avoid answering an older stale question when the input field shows a newer question.

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

For practical incident-response triage, CyberLex should not show related case examples by default. The answer should stay focused on what the user should do next.

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

## Related Case Display

CyberLex may show related cases and incident examples for questions where case-library context is useful.

Related cases may appear for questions such as:

```text
Can Meta Pixel create GDPR risk?
Kan Meta Pixel skapa GDPR-risk?
Can an app bug expose customer data?
Kan ett appfel exponera kunduppgifter?
What can weak security measures cost?
Vad kan svaga säkerhetsåtgärder kosta?
```

The related case section should help users connect general legal or compliance topics to historical examples, authority decisions, public incident examples, or educational case notes.

Related cases should not be shown for practical incident-response triage questions such as:

```text
Our files are encrypted, what should we do?
Vi har fått en misstänkt login på ett konto, vad ska vi göra?
Someone clicked a suspicious link, what should we do?
Någon klickade på en misstänkt länk, vad gör vi?
```

For practical incident questions, the UI should focus on:

* immediate defensive first steps
* containment
* evidence preservation
* incident checklist
* source context
* SOC-style report download

Historical cases can be useful, but they should not distract from urgent incident triage. Apparently even software needs bedside manner.

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

For practical incident-response questions, source context should be filtered to the detected incident type where possible.

Examples:

* suspicious-login questions should avoid showing ransomware or phishing source cards
* suspicious-link questions should avoid showing generic hacking source cards
* ransomware questions should avoid showing suspicious-login cards
* data-leak questions should focus on data-leak or breach response context

For NIS2 sector-scope questions, source context should prefer the most relevant subtype, such as covered sectors, municipality scope, registration, annexes, or essential/important entities.

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

## Case Intelligence Page

CyberLex includes a Case Intelligence page for browsing the local case library.

The Case Intelligence page should show:

* case-library introduction
* search or filter input
* total case count
* shown case count
* limitation warning about historical outcomes
* foldable case cards
* summaries
* learning notes, where available
* fines, costs, or outcomes, where available
* related topic badges
* official source links

The page should support Swedish and English display where the case files include bilingual sections.

Historical cases and public incidents must not be presented as predictions of legal outcome, fine size, or regulatory decision.

---

## Sidebar

The sidebar should remain useful but not overloaded.

Good sidebar content:

* page navigation, such as Ask CyberLex and Case Intelligence
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

The interface can show an example questions panel.

These examples help users understand the supported scope and test the app quickly.

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

When the user clicks an example question, CyberLex should:

1. fill the question input field
2. store the same question as the submitted active question
3. hide the example question panel
4. rerun the app
5. show the answer immediately

The user should not need to click the normal search button after selecting an example question.

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
* example questions that run answers immediately
* fewer repeated panels
* cleaner source display
* clearer Auto language handling
* source transparency without overwhelming users
* related cases only when relevant
* practical incident support when relevant
* refusal of unsupported or unsafe requests
* simple legal-tech prototype presentation for review and demonstration

The UI should make CyberLex Sweden look like a cautious educational source-grounded prototype, not a mysterious legal oracle wearing a cybersecurity hoodie.
