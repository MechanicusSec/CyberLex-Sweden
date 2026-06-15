# CyberLex Sweden Case Index

## Purpose

This file lists the current CyberLex Sweden case-library files.

The case library contains educational summaries of real authority decisions, court cases, and enforcement examples related to cybersecurity, GDPR, information leaks, data breaches, unauthorized access, tracking technology, security measures, and administrative fines.

CyberLex Sweden is an educational prototype. These summaries do not provide legal advice and do not replace the official decisions or qualified legal review.

---

## Current Case Library Status

Current status:

```text
Initial local case library created.
```

Current focus:

* Swedish GDPR decisions
* IMY authority decisions
* EDPB summaries
* data leaks
* information exposure
* tracking technology
* technical and organisational security measures
* administrative fines
* educational cost and risk context

---

## Current Case Files

| Case file                                        | Case topic                                       | Authority / source type | Fine or outcome                  | Main CyberLex use                                                             |
| ------------------------------------------------ | ------------------------------------------------ | ----------------------- | -------------------------------- | ----------------------------------------------------------------------------- |
| `cases/imy_avanza_bank_meta_pixel.md`            | Meta Pixel and customer data transfer            | IMY / EDPB              | SEK 15,000,000                   | Tracking technology, customer data, third-party transfer, GDPR security risk  |
| `cases/imy_trygg_hansa_security_deficiencies.md` | Security deficiencies and customer data exposure | IMY                     | SEK 35,000,000                   | Security measures, unauthorized access risk, customer data exposure           |
| `cases/imy_apoteket_apohem_meta_pixel.md`        | Meta Pixel and sensitive personal data           | IMY                     | SEK 37,000,000 and SEK 8,000,000 | Sensitive personal data, tracking tools, website data leakage                 |
| `cases/imy_equality_ombudsman_web_form.md`       | Web form and failed security measure             | IMY                     | SEK 100,000                      | Web form security, processor disclosure, failed control, smaller fine example |

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

---

## Case Use in CyberLex Sweden

The case library should later help CyberLex answer questions such as:

```text
Can tracking tools create GDPR risk?
What can weak GDPR security measures cost?
Can a web form cause a personal data breach?
What can happen if customer data is exposed online?
What kind of fines have Swedish organizations received?
Can accidental data transfer lead to a fine?
Why do technical and organisational measures matter?
What can a GDPR tracking incident cost?
```

CyberLex should use case references as supporting educational examples.

Cases should not replace the main legal source files in `data/`.

---

## Case Search Design

A future CyberLex version may search both:

```text
data/
cases/
```

Recommended future behavior:

1. User asks a question.
2. CyberLex answers from main legal/source files in `data/`.
3. CyberLex searches `cases/` for related case examples.
4. CyberLex shows a compact `Related cases` card.
5. User can expand a case summary for more detail.

Example display:

```text
Related case:
Avanza Bank and Meta Pixel
Authority: IMY
Year: 2024
Fine: SEK 15,000,000
Why relevant: Tracking technology transferred customer data to Meta.
```

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

CyberLex should not predict exact fines.

Safe wording:

```text
CyberLex does not predict fines. This is an educational risk context based on known factors and previous decisions.
```

---

## Important Limitations

The case library has important limits:

* Case summaries may be simplified.
* Fine amounts are case-specific.
* A similar incident may have a different outcome.
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
8. Avoid unsupported speculation.
9. Keep the disclaimer.
10. Later, add a case-retrieval test case.

---

## Current Development Note

The first version of the case library is local only.

It should not be pushed until the first case-library milestone is stable.

Recommended first milestone:

```text
Case library plan + template + first 4 case summaries + case index.
```

After that, CyberLex can add case search as a separate experimental feature.
