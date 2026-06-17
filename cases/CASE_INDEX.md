# CyberLex Sweden Case Index

## Purpose

This file lists the current CyberLex Sweden case-library files.

The case library contains educational summaries of real authority decisions, court cases, enforcement examples, public incidents, and supervisory investigation examples related to cybersecurity, GDPR, information leaks, data breaches, unauthorized access, tracking technology, security measures, and administrative fines.

CyberLex Sweden is an educational prototype. These summaries do not provide legal advice and do not replace the official decisions, official authority material, or qualified legal review.

---

## Current Case Library Status

Current status:

```text
Local 8-case library created.
```

Current focus:

* Swedish GDPR decisions
* IMY authority decisions
* EDPB summaries
* public incident examples
* supervisory investigation examples
* data leaks
* information exposure
* tracking technology
* technical and organisational security measures
* administrative fines
* educational cost and risk context

Important distinction:

```text
Most cases are IMY-related authority decisions or decision summaries.
The Klarna app data exposure case is a public incident / supervisory investigation example, not an IMY administrative fine case.
```

---

## Current Case Files

| Case file                                        | Case topic                                          | Authority / source type                             | Fine or outcome                                         | Main CyberLex use                                                                           |
| ------------------------------------------------ | --------------------------------------------------- | --------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `cases/imy_apoteket_apohem_meta_pixel.md`        | Meta Pixel and sensitive personal data              | IMY                                                 | SEK 37,000,000 and SEK 8,000,000                        | Sensitive personal data, tracking tools, website data leakage, third-party transfer         |
| `cases/imy_avanza_bank_meta_pixel.md`            | Meta Pixel and customer data transfer               | IMY / EDPB                                          | SEK 15,000,000                                          | Tracking technology, customer data, third-party transfer, GDPR security risk                |
| `cases/imy_equality_ombudsman_web_form.md`       | Web form and failed security measure                | IMY                                                 | SEK 100,000                                             | Web form security, processor disclosure, failed control, smaller fine example               |
| `cases/imy_kry_meta_pixel.md`                    | Meta Pixel and healthcare-related tracking risk     | IMY / EDPB                                          | Reprimand / corrective outcome                          | Tracking technology, healthcare context, sensitive data risk, GDPR security measures        |
| `cases/imy_sportadmin_security_breach.md`        | Security breach affecting children and young people | IMY                                                 | Administrative fine / security breach outcome           | Large-scale breach, children’s data, incident response, publication risk, security controls |
| `cases/imy_trygg_hansa_security_deficiencies.md` | Security deficiencies and customer data exposure    | IMY                                                 | SEK 35,000,000                                          | Security measures, unauthorized access risk, customer data exposure, access control         |
| `cases/imy_wrong_email_customer_data.md`         | Customer data sent to the wrong email recipient     | IMY / authority decision example                    | Case-specific outcome                                   | Accidental disclosure, email handling, confidentiality, personal data breach risk           |
| `cases/klarna_app_data_exposure_2021.md`         | Klarna app data exposure incident                   | Public incident / supervisory investigation example | No confirmed IMY fine stored for this specific incident | App bug, customer data exposure, account/session separation, supervisory and trust risk     |

---

## Case Topic Tags

The current case library supports these topic tags:

* GDPR
* IMY
* EDPB
* Personal data breach
* Security measures
* Technical and organisational measures
* Sensitive personal data
* Customer data
* Data leak
* Information leak
* Tracking technology
* Meta Pixel
* Website analytics
* Web form security
* Data processor
* Unauthorized access risk
* Administrative fine
* Incident response
* Privacy by design
* Public incident
* Supervisory investigation
* App security
* App bug
* Customer account exposure
* Session handling
* Account separation
* Financial app risk
* Children’s data
* Healthcare-related privacy risk
* Accidental disclosure
* Email disclosure

---

## Case Use in CyberLex Sweden

The case library helps CyberLex answer questions such as:

```text
Can tracking tools create GDPR risk?
What can weak GDPR security measures cost?
Can a web form cause a personal data breach?
What can happen if customer data is exposed online?
What kind of fines have Swedish organizations received?
Can accidental data transfer lead to a fine?
Why do technical and organisational measures matter?
What can a GDPR tracking incident cost?
Can an app bug expose customer data?
Can users see other users' data because of an app error?
Can a short app incident still create GDPR or supervisory risk?
Kan ett appfel exponera kunduppgifter?
Kan användare se andra användares uppgifter?
Vad kan hända om kunddata exponeras i en app?
```

CyberLex should use case references as supporting educational examples.

Cases should not replace the main legal source files in `data/`.

---

## Case Search Design

CyberLex can search both:

```text
data/
cases/
```

Recommended behavior:

1. User asks a question.
2. CyberLex answers from main legal/source files in `data/`.
3. CyberLex searches `cases/` for related case examples.
4. CyberLex shows a compact `Related cases` card.
5. User can expand a case summary for more detail.
6. CyberLex shows learning notes when available.

Example display:

```text
Related case:
Avanza Bank and Meta Pixel
Authority: IMY
Year: 2024
Fine: SEK 15,000,000
Why relevant: Tracking technology transferred customer data to Meta.
```

Example display for public incident:

```text
Related case:
Klarna app data exposure 2021
Source type: Public incident / supervisory investigation example
Outcome: No confirmed IMY fine stored for this specific incident
Why relevant: A short app bug exposed customer data and created privacy, confidentiality, trust, and supervisory risk.
```

---

## Learning Notes

Case files may include:

```markdown
## Learning note

## Swedish learning note
```

Learning notes are used to explain the educational lesson from each case.

They should help users understand:

* why the case matters
* what kind of risk the case shows
* what CyberLex can learn from the case
* how similar incidents may connect to GDPR, security measures, incident response, or supervisory risk

Learning notes should stay educational and should not give legal advice.

---

## Fine and Cost Context

The case library can support future cost and risk context.

CyberLex may later show educational fine/cost information such as:

* official fine amount from the case
* affected people, if available
* type of data involved
* whether sensitive personal data was involved
* whether the issue involved weak security measures
* whether the issue involved tracking tools or third parties
* whether the incident was accidental, negligent, or linked to insufficient controls
* possible cost categories beyond fines
* business trust impact
* investigation and remediation cost categories

CyberLex should not predict exact fines.

Safe wording:

```text
CyberLex does not predict fines. This is educational risk context based on known factors and previous decisions or public incidents.
```

---

## Important Limitations

The case library has important limits:

* Case summaries may be simplified.
* Fine amounts are case-specific.
* A similar incident may have a different outcome.
* Public incidents are not always authority decisions.
* Public reporting should not be treated as a confirmed fine or final legal assessment.
* Authority decisions depend on facts, evidence, timing, mitigation, cooperation, and legal assessment.
* CyberLex does not predict court outcomes or administrative fines.
* CyberLex does not provide legal advice.
* Official sources should always be checked.

---

## Future Case Candidates

Possible future cases to add:

* more IMY personal data breach decisions
* more Swedish cybercrime or unauthorized access judgments
* ransomware-related authority decisions
* public-sector personal data breach cases
* healthcare or school data leak cases
* EU or EDPB case summaries on security measures
* DORA-related future enforcement cases when available
* NIS2-related future enforcement cases when Swedish practice develops
* more public app or platform incident examples
* supplier and processor-related security cases

---

## Maintenance Rules

When a new case is added:

1. Add a new Markdown file in `cases/`.
2. Use `cases/CASE_TEMPLATE.md`.
3. Add official source links.
4. Add case metadata.
5. Add the case to this index.
6. Add useful CyberLex questions.
7. Add related CyberLex topic tags.
8. Add a learning note.
9. Add a Swedish learning note.
10. Avoid unsupported speculation.
11. Do not describe public incidents as authority fines unless an official decision confirms it.
12. Keep the disclaimer.
13. Run the case audit script.
14. Later, add or update a case-retrieval test case.

---

## Current Development Note

The case library is currently local-first.

The user prefers not to push to GitHub too often while development is active.

Current Git policy:

```text
Commit locally at stable milestones.
Push only occasionally when a sensible milestone is ready.
```

Recommended current milestone:

```text
8-case library + learning notes + documentation + case index.
```

After this, CyberLex can continue improving case search ranking, especially for app exposure questions related to the Klarna case.
