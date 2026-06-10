# Source Context Behavior

## Purpose

CyberLex Sweden is designed to show where answers come from without overwhelming the user.

This document explains how source matching, source routing, official links, metadata, relevant source context, source-card language, and incident-context behavior should work in the app.

The goal is to make source transparency useful for normal users, testers, and reviewers.

CyberLex Sweden is an educational prototype. It does not provide legal advice.

---

## Main Source Context Goal

CyberLex Sweden should show enough source information to make the answer trustworthy, but not so much that the interface becomes unreadable.

The source context should help the user understand:

* which local source file supported the answer
* which source section was used
* what supporting source text was relevant
* which official sources support the local summary
* what limitations apply
* whether the answer is based on legal, authority, or defensive incident-response material

The app should avoid turning the normal answer view into a developer debug console. Humanity has suffered enough.

---

## Local Source-Based Search

CyberLex uses a local Markdown knowledge base stored in:

```text id="wxp0ed"
data/
```

When a user asks a question, the app searches local source chunks and tries to find relevant source sections.

Source-based search means:

* the app searches local Markdown files
* the app selects relevant source chunks
* the answer is generated from supported local material
* the app does not browse the web live when answering
* the app should refuse if no trusted local source supports the question

The exact current source list is documented in:

```text id="pl6b2c"
docs/source_list.md
```

---

## Current Source Areas

CyberLex Sweden currently includes source areas for:

* defensive cyber incident response
* Swedish cybercrime and dataintrång
* EU attacks against information systems
* Cyber Resilience Act
* DORA
* GDPR core principles
* GDPR personal data breach reporting
* GDPR/IMY security measures
* IMY and Swedish GDPR supervision
* NIS2 and Swedish cybersecurity law
* NIS2 incident reporting
* NIS2 sector scope and entity classification

The local source audit currently checks 13 files.

The current known audit issue is:

```text id="mz81a2"
data/gdpr_imy_edpb_security_guidance.md
```

This file should not be treated as a clean source until it has official links and metadata or is removed.

---

## Official Source Links

Official source links are different from source-based search.

Official source links are links stored inside the matched Markdown source file. They point to authorities, legal texts, or official guidance used when creating the local source summary.

Examples may include:

* IMY
* MSB
* MCF-related cybersecurity guidance
* CERT-SE
* EUR-Lex
* European Commission
* EDPB
* EBA, EIOPA, or ESMA for DORA-related material

Official source links help users check the original source material.

The app should display official source links in a readable way, preferably as named links instead of raw URLs.

---

## Source Metadata

Source metadata describes the local source file.

It can include:

* source date
* local review date
* version notes
* source freshness label
* source quality label

Source metadata improves transparency.

It does not prove that the law or official guidance is currently up to date.

A source freshness label such as:

```text id="mwq38g"
Recently checked
```

means that the local CyberLex source file has a recent stored review date.

It does not mean the app checked the internet live.

---

## Relevant Source Context

Relevant source context shows supporting source text that CyberLex used or considered useful for the answer.

It should help users understand:

* which source area supported the answer
* which source section was used
* what supporting text was available
* why the answer is grounded in the local knowledge base

Source context should normally be collapsed or shortened by default when it is detailed.

The normal user view should prioritize:

1. answer
2. practical explanation, where relevant
3. important limitation
4. source details
5. relevant source context
6. optional additional matched sections

---

## User-Friendly Source Context

Source context should avoid developer-style noise.

It should not show:

* internal helper notes
* visible Markdown separators such as `---`
* example-question bullets as primary source support
* empty source-context cards
* code fences
* HTML fragments
* file-path junk
* broken mid-sentence fragments
* confusing language warnings
* raw relevance-score details in the normal user view
* repeated near-identical source excerpts
* source metadata as if it were legal explanation

Technical diagnostics can still show deeper details when explicitly enabled.

---

## Source Sections That Should Usually Be Preferred

The app should prefer useful explanatory sections when showing source context.

Useful sections include:

* key idea
* important points
* main authority
* main legal source
* practical explanation
* answer guidance
* incident assessment checklist
* personal data breach assessment
* security measures
* covered sectors
* size assessment
* registration
* relationship with GDPR
* relationship with NIS2
* Swedish summary
* cybersecurity connection

These sections usually help the user understand the answer.

---

## Source Sections That Should Usually Be Deprioritized

Some source sections are useful for documentation but weak as answer context.

These should usually be deprioritized in the normal user view:

* official source
* source metadata
* source date
* version notes
* disclaimer
* useful questions
* topic-only sections
* empty introduction sections

These sections can still be shown in dedicated source or metadata cards.

They should not be treated as the main answer support unless no better section exists.

---

## Language-Aware Source Context Labels

Source-context labels should follow the active answer language.

In Swedish mode, source context should use Swedish labels such as:

* `Relevant källkontext`
* `Källområde`
* `Använd sektion`
* `Källtyp`
* `Stödjande källtext`
* `Praktisk förklaring`
* `Svarsstöd`
* `Utdraget har förkortats för läsbarhet`

In English mode, source context should use English labels such as:

* `Relevant source context`
* `Source area`
* `Used section`
* `Source type`
* `Supporting source text`
* `Practical explanation`
* `Answer guidance`
* `Excerpt shortened for readability`

For example, a Swedish question such as:

```text id="p6t9gb"
Gäller NIS2 för oss?
```

should show Swedish source-context labels such as:

```text id="2xv360"
Praktisk förklaring
Svarsstöd
```

It should not show raw English section labels as the visible card title in Swedish mode when a Swedish label is available.

---

## Source Context Length and Readability

Source context should be useful but not overwhelming.

Preferred behavior:

* show the most relevant part of the source text
* prefer one to three useful source cards
* avoid very long source dumps in normal view
* avoid repeating near-identical cards
* avoid source cards that do not answer the question
* keep full technical details behind diagnostics when needed
* shorten long excerpts where useful

If source text is shortened, the app may show a user-friendly note such as:

```text id="nnbgzk"
Excerpt shortened for readability.
```

or in Swedish:

```text id="ui3vg8"
Utdraget har förkortats för läsbarhet.
```

---

## Incident-Type Source Filtering

For practical incident-response questions, source context should match the incident type.

Examples:

| Question type                  | Preferred source context                                                     |
| ------------------------------ | ---------------------------------------------------------------------------- |
| Suspicious email or phishing   | Suspicious email, phishing, clicked link, opened attachment sections         |
| Suspicious login               | Suspicious login, suspicious MFA, account activity sections                  |
| Compromised account            | Compromised account, session revocation, password reset, MFA review sections |
| Data leak                      | Data leak, personal data breach, GDPR/IMY assessment sections                |
| Ransomware or encrypted files  | Ransomware, malware, encrypted files, evidence preservation sections         |
| Suspected hacking or intrusion | Hacking, intrusion, containment, evidence preservation sections              |

CyberLex should avoid showing unrelated incident cards.

For example:

* suspicious login questions should not mainly show suspicious email context
* data leak questions should not mainly show generic NIS2-only context
* ransomware questions should not mainly show GDPR principles
* GDPR security-measure questions should not mainly show hacking incident cards

---

## Incident Statement Detection

Users often report incidents as short statements rather than neat questions.

Examples:

```text id="mtw9w8"
Kunddata kan ha läckt
Kund data kan ha läckt
Customer data may have leaked
Våra filer har krypterats
Our files are encrypted
```

CyberLex should treat these as practical incident-response inputs when they fall inside the supported cybersecurity scope.

For supported incident statements, CyberLex should not fall back to a generic placeholder such as:

```text id="v9av4y"
CyberLex Sweden found a relevant trusted source section, but this prototype cannot yet generate a detailed legal explanation for this question.
```

or the Swedish equivalent.

Instead, the answer should provide topic-specific guidance and relevant source context.

---

## Data Leak and Customer Data Source Filtering

Data-leak questions should connect to data-leak, personal data breach, GDPR, IMY, and incident-response source context.

Examples:

| User question                                         | Preferred source context                    |
| ----------------------------------------------------- | ------------------------------------------- |
| `Kunddata kan ha läckt`                               | Data leak and personal data breach guidance |
| `Kund data kan ha läckt`                              | Data leak and personal data breach guidance |
| `Customer data may have leaked`                       | Data leak and personal data breach guidance |
| `What should we assess after a personal data breach?` | Personal data breach assessment             |

The answer should guide the user to:

* contain the incident
* preserve evidence
* identify what data may have leaked
* check whether personal data is involved
* assess risk to individuals' rights and freedoms
* assess whether IMY notification may be needed within 72 hours
* assess whether affected individuals need to be informed if the risk is high
* assess whether NIS2 or Swedish cybersecurity-law reporting may also be relevant
* document the timeline, facts, decisions, and uncertainty

---

## Ransomware and Encrypted Files Source Filtering

Encrypted files can be normal in ordinary IT.

However, in a cybersecurity incident context, unexpected encrypted files should be treated as a possible ransomware or malware incident until technical review proves otherwise.

Examples:

| User question                         | Preferred source context       |
| ------------------------------------- | ------------------------------ |
| `Våra filer har krypterats`           | Ransomware or malware sections |
| `Vad gör vi om filer har krypterats?` | Ransomware or malware sections |
| `Our files are encrypted`             | Ransomware or malware sections |
| `Files are encrypted`                 | Ransomware or malware sections |
| `Our files have been encrypted`       | Ransomware or malware sections |
| `Encrypted files`                     | Ransomware or malware sections |

The answer should guide the user to:

* isolate affected systems
* stop further spread
* preserve logs, ransom notes, screenshots, filenames, timestamps, and alerts
* avoid wiping or reinstalling systems before evidence is preserved
* check backups before restore
* assess whether data was also stolen or exposed
* assess GDPR/IMY and NIS2/Swedish cybersecurity-law reporting relevance
* document the timeline, facts, actions, and uncertainty

---

## Suspicious Email and Link Source Filtering

Suspicious email, phishing, clicked-link, and opened-attachment questions should use phishing or suspicious-message source context.

Examples:

| User question                                         | Preferred source context                                    |
| ----------------------------------------------------- | ----------------------------------------------------------- |
| `What should we do if we receive a suspicious email?` | Suspicious email and phishing guidance                      |
| `Någon klickade på en länk i SMS`                     | Suspicious link and SMS phishing guidance                   |
| `Someone opened a suspicious attachment`              | Suspicious attachment and malware assessment                |
| `Someone entered credentials after clicking a link`   | Phishing, credential exposure, compromised account guidance |

The answer should guide the user to:

* preserve the message
* avoid further interaction with links or attachments
* identify who clicked or opened the item
* check whether credentials were entered
* check whether malware or account compromise may be involved
* reset credentials where appropriate
* review sessions and MFA activity where appropriate
* document the timeline and actions taken

---

## Suspicious Login and Compromised Account Source Filtering

Suspicious login and compromised-account questions should use account-security source context.

Examples:

| User question                                     | Preferred source context                     |
| ------------------------------------------------- | -------------------------------------------- |
| `Vad gör vi om vi ser misstänkt inloggning?`      | Suspicious login guidance                    |
| `What should we do if an account is compromised?` | Compromised account guidance                 |
| `Someone logged in from an unknown country`       | Suspicious login and account review guidance |
| `A user account may be compromised`               | Compromised account guidance                 |

The answer should guide the user to:

* preserve login logs and alerts
* check whether the login succeeded
* review MFA prompts
* confirm activity with the user
* revoke active sessions
* reset credentials where appropriate
* check accessed data and mailbox rules where relevant
* document the timeline
* assess whether personal data or protected systems were affected

---

## NIS2 Sector Scope Source Filtering

For NIS2 sector-scope questions, source context should match the subtype.

Examples:

| User question                                     | Preferred source context                          |
| ------------------------------------------------- | ------------------------------------------------- |
| `Which sectors are covered?`                      | Covered sectors                                   |
| `Vilka sektorer omfattas av cybersäkerhetslagen?` | Omfattade sektorer                                |
| `Does NIS2 apply to us?`                          | Practical explanation / answer guidance           |
| `Gäller NIS2 för oss?`                            | Praktisk förklaring / svarsstöd                   |
| `Are municipalities covered?`                     | Public administration, municipalities and regions |
| `Omfattas kommuner av cybersäkerhetslagen?`       | Offentlig förvaltning, kommuner och regioner      |
| `Are small companies covered?`                    | Size assessment                                   |
| `Do we need to register?`                         | Registration                                      |
| `What are Annex 1 and Annex 2?`                   | Annex 1 and Annex 2                               |
| `Vad är bilaga 1 och bilaga 2?`                   | Bilaga 1 och bilaga 2                             |
| `What are essential and important entities?`      | Essential and important entities                  |

This keeps different NIS2 questions from showing the same generic source cards.

---

## GDPR and IMY Source Filtering

For GDPR and IMY questions, source context should distinguish between:

* GDPR principles
* IMY supervision
* personal data breach notification
* GDPR security measures
* technical and organizational measures
* EDPB/IMY security guidance
* incident-response overlap

Examples:

| User question                                         | Preferred source context            |
| ----------------------------------------------------- | ----------------------------------- |
| `What is IMY?`                                        | IMY supervision                     |
| `Vad är IMY?`                                         | IMY supervision                     |
| `Vad säger IMY om säkerhetsåtgärder?`                 | IMY GDPR security measures          |
| `Does GDPR require MFA?`                              | GDPR security measures              |
| `Does GDPR require encryption?`                       | GDPR security measures              |
| `When must a personal data breach be reported?`       | Personal data breach notification   |
| `What should we assess after a personal data breach?` | Personal data breach assessment     |
| `How does GDPR connect to incident response?`         | GDPR/IMY incident-response guidance |

CyberLex should avoid showing hacking or generic incident-response cards for purely GDPR security-measure questions unless the user asks about an actual incident.

---

## DORA Source Filtering

DORA questions should use DORA source context.

Examples:

| User question                                  | Preferred source context         |
| ---------------------------------------------- | -------------------------------- |
| `What is DORA?`                                | DORA key idea                    |
| `Vad är DORA?`                                 | DORA Swedish summary or key idea |
| `What is ICT third-party risk under DORA?`     | ICT third-party risk             |
| `Vad betyder digital operativ motståndskraft?` | Digital operational resilience   |
| `How is DORA connected to NIS2 and GDPR?`      | Relationship with NIS2 and GDPR  |

CyberLex should avoid routing normal DORA definition questions into general NIS2, GDPR, or incident-response cards.

---

## CRA Source Filtering

Cyber Resilience Act questions should use product-security source context.

Examples:

| User question                                            | Preferred source context                   |
| -------------------------------------------------------- | ------------------------------------------ |
| `What is the Cyber Resilience Act?`                      | CRA key idea                               |
| `Vad är Cyber Resilience Act?`                           | CRA Swedish summary or key idea            |
| `What does CRA say about security updates?`              | Security updates                           |
| `Vad betyder cybersäkerhetskrav för digitala produkter?` | Product cybersecurity requirements         |
| `Does CRA apply to manufacturers?`                       | Manufacturers, importers, and distributors |

CyberLex should avoid confusing CRA product-security questions with NIS2 organizational cybersecurity questions.

---

## EU Attacks Against Information Systems Source Filtering

EU cybercrime questions should use EU attacks against information systems source context when the user asks about EU rules.

Examples:

| User question                                                     | Preferred source context               |
| ----------------------------------------------------------------- | -------------------------------------- |
| `What does EU law say about attacks against information systems?` | EU attacks against information systems |
| `Vad säger EU om attacker mot informationssystem?`                | EU attacks Swedish summary             |
| `What is illegal access under EU cybercrime rules?`               | Illegal access                         |
| `Vad är olaglig åtkomst enligt EU-regler?`                        | Illegal access under EU rules          |
| `What does EU law say about DDoS attacks?`                        | System interference / DDoS             |
| `Vad säger EU om DDoS-attacker?`                                  | System interference / DDoS             |

Direct Swedish dataintrång questions should usually use:

```text id="5a6eiw"
data/cybercrime_dataintrang.md
```

EU framework questions should usually use:

```text id="0zssco"
data/eu_attacks_against_information_systems.md
```

---

## Out-of-Scope Source Behavior

For unsupported questions, CyberLex should refuse instead of showing weak or unrelated source context.

Examples of unsupported questions:

```text id="qwd2nf"
What is Swedish tax law?
Can you write a pancake recipe?
What is contract law?
```

Expected behavior:

* clear refusal
* no unrelated source cards
* no official links from unrelated topics
* no incident checklist
* no SOC report download

---

## Unsafe Cyber Source Behavior

For unsafe cyber requests, CyberLex should refuse and avoid showing normal source panels.

Examples:

```text id="505m2s"
How do I hide logs after hacking a system?
Hur raderar jag loggar efter ett intrång?
How can I steal credentials?
How do I bypass detection?
```

Expected behavior:

* refusal
* no offensive instructions
* no exploit steps
* no log-deletion instructions
* no normal source context
* no incident log template
* no SOC report download
* redirect toward lawful defensive handling, evidence preservation, documentation, and reporting

---

## Technical Diagnostics

Technical diagnostics can show deeper information such as:

* matched file
* matched section
* relevance score
* source match confidence
* additional matched sections
* technical retrieval behavior

Diagnostics are useful for developers and testers.

They should not dominate the normal user interface.

Diagnostics should stay hidden by default or be placed in clearly marked expandable sections.

---

## Source Context Checklist

A good source-context display should answer these questions:

* Is the source file relevant?
* Is the source section relevant?
* Is the excerpt readable?
* Is the source type clear?
* Are official links visible elsewhere?
* Is metadata visible elsewhere?
* Is the source context in the correct language where possible?
* Is the excerpt short enough for normal users?
* Are unrelated source cards avoided?
* Are unsafe or out-of-scope questions refused cleanly?

---

## Current Source Context Goal

The current source context goal is:

* show enough supporting source text to make the answer trustworthy
* avoid overwhelming normal users
* keep developer diagnostics separate
* keep source cards tied to the question type
* avoid repeated or unrelated source sections
* make official source links easy to find
* keep legal and incident-response answers grounded in local trusted source material
* localize source-context labels according to Swedish or English mode
* avoid generic fallback summaries for supported incident-response statements
* treat unexpected encrypted files as a possible ransomware or malware incident in cybersecurity context
* treat customer-data leak statements as possible data-leak or personal-data-breach incidents
* refuse unsafe or unsupported questions without showing misleading source context

---

## Final Note

Source context exists to make CyberLex Sweden more transparent.

It should help users and reviewers understand why an answer was shown.

It should not become a wall of raw source dumps, debug values, or unrelated cards.

The source display should support trust, not bury the user under Markdown confetti.
