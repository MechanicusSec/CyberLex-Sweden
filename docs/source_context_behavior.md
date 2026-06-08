# Source Context Behavior

CyberLex Sweden is designed to show where answers come from without overwhelming the user.

This document explains how source matching, routing, official links, metadata, relevant source context, source-card language, and incident-context behavior should work.

---

## Source-Based Search

CyberLex uses a local Markdown knowledge base stored in the `data/` folder.

When a user asks a question, the app searches local source chunks and tries to find relevant source sections.

Source-based search means:

- the app searches the local knowledge base
- the app selects relevant source chunks
- the answer is generated from supported local material
- the app does not browse the web live when answering

---

## Official Source Links

Official source links are different from source-based search.

Official source links are links stored inside the matched Markdown source file. They point to authorities, legal texts, or official guidance used when creating the local source summary.

Examples may include:

- IMY
- MSB or MCF
- CERT-SE
- EUR-Lex
- EDPB
- CISA, where used for defensive incident-response reference material

Official source links help users check the original source material.

---

## Source Metadata

Source metadata describes the local source file.

It can include:

- source date
- local review date
- version notes
- source freshness label
- source quality label

Source freshness labels describe when the local CyberLex source file was reviewed. They do not guarantee that the law or official guidance is currently up to date.

---

## Relevant Source Context

Relevant source context shows supporting source text that CyberLex used or considered useful for the answer.

It should help users understand:

- which source area supported the answer
- which source section was used
- what supporting text was available
- why the answer is grounded in the local knowledge base

Source context should be collapsed by default when it is detailed.

---

## User-Friendly Source Context

Source context should avoid developer-style noise.

It should not show:

- internal helper notes
- visible Markdown separators such as `---`
- example-question bullets
- empty source-context cards
- code fences
- HTML fragments
- file-path junk
- broken mid-sentence fragments
- confusing language warnings
- raw relevance-score details in normal user view

Technical diagnostics can still show deeper details when explicitly enabled.

---

## Language-Aware Source Context Labels

Source-context labels should follow the active answer language.

In Swedish mode, source context should use Swedish labels such as:

- `Relevant källkontext`
- `Källområde`
- `Använd sektion`
- `Källtyp`
- `Stödjande källtext`
- `Praktisk förklaring`
- `Svarsstöd`

In English mode, source context should use English labels such as:

- `Relevant source context`
- `Source area`
- `Used section`
- `Source type`
- `Supporting source text`
- `Practical explanation`
- `Answer guidance`

For example, a Swedish question such as:

```text
Gäller NIS2 för oss?
```

should show source-context sections such as:

```text
Praktisk förklaring
Svarsstöd
```

It should not show the raw English section label `Practical explanation` as the visible card title or used-section value in Swedish mode.

---

## Incident-Type Source Filtering

For practical incident-response questions, source context should match the incident type.

Examples:

| Question type | Preferred source context |
|---|---|
| suspicious email or phishing | suspicious email/phishing sections |
| suspicious login | suspicious login sections |
| compromised account | compromised account sections |
| data leak | data leak or personal data breach sections |
| ransomware or encrypted files | ransomware or malware sections |
| suspected hacking or intrusion | hacking, intrusion, containment, evidence preservation sections |

CyberLex should avoid showing unrelated incident cards.

---

## Incident Statement Detection and Fallback Avoidance

Users often report incidents as short statements rather than neat questions.

Examples:

```text
Kunddata kan ha läckt
Kund data kan ha läckt
Customer data may have leaked
Våra filer har krypterats
Our files are encrypted
```

CyberLex should treat these as practical incident-response inputs when they fall inside the supported cybersecurity scope.

For supported incident statements, CyberLex should not fall back to a generic summary such as:

```text
CyberLex Sweden found a relevant trusted source section, but this prototype cannot yet generate a detailed legal explanation for this question.
```

or the Swedish equivalent.

Instead, the answer should provide topic-specific guidance and relevant source context.

---

## Data Leak and Customer Data Source Filtering

Data-leak questions should connect to data-leak, personal data breach, GDPR, and IMY source context.

Examples:

| User question | Preferred source context |
|---|---|
| Kunddata kan ha läckt | suspected data leak / personal data breach guidance |
| Kund data kan ha läckt | suspected data leak / personal data breach guidance |
| Customer data may have leaked | suspected data leak / personal data breach guidance |
| What should we assess after a personal data breach? | personal data breach assessment |

The answer should guide the user to:

- contain the incident
- preserve evidence
- identify what data may have leaked
- check whether personal data is involved
- assess risk to individuals' rights and freedoms
- assess whether IMY notification may be needed within 72 hours
- assess whether affected individuals need to be informed if the risk is high
- document the timeline, facts, decisions, and uncertainty

---

## Ransomware and Encrypted Files Source Filtering

Encrypted files can be normal in ordinary IT.

However, in a cybersecurity incident context, unexpected encrypted files should be treated as a possible ransomware or malware incident until proven otherwise.

Examples:

| User question | Preferred source context |
|---|---|
| Våra filer har krypterats | ransomware or malware sections |
| Vad gör vi om filer har krypterats? | ransomware or malware sections |
| Our files are encrypted | ransomware or malware sections |
| Files are encrypted | ransomware or malware sections |
| Our files have been encrypted | ransomware or malware sections |
| Encrypted files | ransomware or malware sections |

The answer should guide the user to:

- isolate affected systems
- stop further spread
- preserve logs, ransom notes, screenshots, filenames, timestamps, and alerts
- avoid wiping or reinstalling systems before evidence is preserved
- check backups before restore
- assess whether data was also stolen or exposed
- assess GDPR/IMY and NIS2/Swedish Cybersecurity Act reporting relevance
- document the timeline, facts, actions, and uncertainty

---

## NIS2 Sector Scope Source Filtering

For NIS2 sector-scope questions, source context should match the subtype.

Examples:

| User question | Preferred source context |
|---|---|
| Which sectors are covered? | Covered sectors |
| Vilka sektorer omfattas av cybersäkerhetslagen? | Omfattade sektorer |
| Does NIS2 apply to us? | Practical explanation / answer guidance |
| Gäller NIS2 för oss? | Praktisk förklaring / svarsstöd |
| Are municipalities covered? | Public administration, municipalities and regions |
| Omfattas kommuner av cybersäkerhetslagen? | Offentlig förvaltning, kommuner och regioner |
| Are small companies covered? | Size assessment |
| Do we need to register? | Registration |

This keeps different NIS2 questions from showing the same generic source cards.

---

## GDPR and IMY Source Filtering

For GDPR and IMY questions, source context should distinguish between:

- GDPR principles
- IMY supervision
- personal data breach notification
- GDPR security measures
- technical and organizational measures
- EDPB/IMY security guidance
- incident-response overlap

Examples:

| User question | Preferred source context |
|---|---|
| What is IMY? | IMY supervision |
| Vad säger IMY om säkerhetsåtgärder? | IMY GDPR security measures |
| Does GDPR require MFA? | GDPR security measures |
| Does GDPR require encryption? | GDPR security measures |
| What should we assess after a personal data breach? | Personal data breach assessment |
| How does GDPR connect to incident response? | GDPR/IMY/EDPB incident-response guidance |

CyberLex should avoid showing hacking or generic incident-response cards for purely GDPR security-measure questions unless the user asks about an actual incident.

---

## Source Context Length and Readability

Source context should be useful but not overwhelming.

Long checklists and long source sections may be shortened in normal user view when needed.

Preferred behavior:

- show the most relevant part of the source text
- prefer one to three useful source cards
- avoid repeating near-identical source cards
- avoid very long source dumps in normal view
- keep full technical details behind diagnostics when needed

If source text is shortened, the app may show a user-friendly note such as:

```text
Excerpt shortened for readability.
```

or in Swedish:

```text
Utdraget har förkortats för läsbarhet.
```

---

## Technical Diagnostics

Technical diagnostics can show deeper information such as:

- matched file
- matched section
- relevance score
- source match confidence
- additional matched sections
- technical retrieval behavior

Diagnostics are useful for developers and testers, but they should not dominate the normal user interface.

Diagnostics should stay hidden by default.

---

## Current Source Context Goal

The current source context goal is:

- show enough supporting source text to make the answer trustworthy
- avoid overwhelming normal users
- keep developer diagnostics separate
- keep source cards tied to the question type
- avoid repeated or unrelated source sections
- make official source links easy to find
- keep legal and incident-response answers grounded in local trusted source material
- localize source-context labels according to Swedish or English mode
- avoid generic fallback summaries for supported incident-response statements
- treat unexpected encrypted files as a possible ransomware or malware incident in cybersecurity context
- treat customer-data leak statements as possible data-leak or personal-data-breach incidents
