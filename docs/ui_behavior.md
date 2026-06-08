# UI Behavior

This document explains the main user interface behavior of CyberLex Sweden.

The goal of the interface is to keep the normal user view readable while still preserving source transparency for review and testing.

---

## Main Layout

The current UI uses a compact layout:

1. CyberLex Sweden introduction
2. question input
3. generated CyberLex summary
4. attention level
5. optional practical explanation or incident guidance
6. official source links and source overview where relevant
7. collapsed relevant source context
8. sidebar controls and diagnostics

The normal view should avoid overwhelming users with technical ranking details.

---

## Language Handling

CyberLex supports Swedish and English interface handling.

The interface can be set to:

- English
- Svenska
- Auto, if supported by the current version

The app should avoid mixed-language labels where possible.

Examples:

- English mode should show Unauthorized access, not Dataintrång.
- Swedish mode can show Dataintrång.
- Swedish questions should prefer Swedish visible labels and Swedish answers.
- English questions should prefer English visible labels and English answers.

---

## Question Input

The question input is the main user action.

The input should use placeholder text to guide the user.

English example:

Ask about GDPR, NIS2, incident reporting, data leaks, ransomware, or Swedish cybersecurity law.

Swedish example:

Fråga om GDPR, NIS2, incidentrapportering, dataläckor, ransomware eller svensk cybersäkerhetsrätt.

The interface should not show a large empty-state message if the placeholder already explains what the user should do.

---

## Supported Topic Areas

Supported topic chips are shown to give users a quick idea of the project scope.

Examples:

- GDPR
- IMY
- Personal data breaches
- Incident response
- Suspected hacking
- Data leaks
- Compromised accounts
- NIS2
- Swedish Cybersecurity Act
- Unauthorized access
- EU Cyber Resilience Act
- DORA
- Digital compliance

The chips are not a full legal source list. They are user-facing scope hints.

---

## CyberLex Summary

The CyberLex summary is the primary answer section.

It should:

- answer the question directly where possible
- stay within the supported scope
- use the detected language where possible
- avoid unnecessary repetition
- avoid giving legal certainty when the facts are incomplete
- make clear when the answer is educational and simplified

The summary is rule-based in the current prototype.

---

## Attention Levels

CyberLex attention levels are educational signals, not legal risk ratings.

Informational means a basic legal or authority explanation question.

Standard means a general legal or compliance question.

Elevated means a reporting, breach assessment, GDPR/NIS2 overlap, or regulatory-duty question.

High means a practical incident-response question or an unsafe/offensive cyber request that must be refused or redirected.

The attention level should help users understand how carefully the answer should be read.

---

## Practical Explanation Cards

Practical explanation cards appear only when they add value.

They may appear for:

- incident-response questions
- breach assessment questions
- reporting questions
- GDPR/NIS2 overlap questions
- compliance-duty questions

They should usually be hidden for simple definition questions, such as:

- What is NIS2?
- Vad är IMY?
- What is DORA?

This reduces repetition and keeps simple answers cleaner.

---

## Incident-Response UI

For practical incident-response questions, CyberLex may show:

- recommended first steps
- incident checklist
- incident log template
- download-ready incident summary
- source context linked to the incident type

The normal UI should avoid repeating the full incident template in several places. If the downloaded file contains the full template, the page should show only a short download-ready explanation and button.

---

## Official Source Links

Official source links should be shown in a user-friendly way.

They should:

- use readable link labels
- avoid raw URLs where possible
- appear close to the answer they support
- help the user check original authority or legal material

Official source links are different from the local source context. The official links point outward to authority or legal sources, while the source context shows the local CyberLex knowledge section used by the app.

---

## Relevant Source Context

Relevant source context should normally be collapsed.

It is useful for reviewers and testers because it shows the local source sections that supported the answer.

The context should avoid developer-style clutter such as:

- raw scores in the normal user view
- duplicate headings
- empty fragments
- unrelated source cards
- internal file-path noise
- repeated cards that do not match the question

Technical diagnostics can still show deeper details when enabled.

---

## Sidebar

The sidebar should remain useful but not overloaded.

Good sidebar content:

- language selector
- technical diagnostics checkbox
- CyberLex status
- loaded document count
- searchable chunk count
- prototype version
- build type

Technical diagnostics and experimental tools should be collapsed or hidden by default.

The sidebar should not distract from the main question flow.

---

## Footer

A simple footer can show:

© 2026 CyberLex Sweden · Policy · About · Copyright

These links can point to local project documentation or future public pages.

---

## Current UI Goal

The current UI goal is:

- direct question flow
- fewer repeated panels
- cleaner source display
- clearer language handling
- source transparency without overwhelming users
- practical incident support when relevant
- simple legal-tech prototype presentation for review and demonstration
