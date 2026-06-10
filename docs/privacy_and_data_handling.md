# Privacy and Data Handling

## Purpose

This document explains how the current CyberLex Sweden prototype handles user questions, local source files, generated incident summaries, and sensitive information.

CyberLex Sweden is a local educational prototype.

It does not provide legal advice and should not be used as the sole basis for legal, compliance, regulatory, or security decisions.

---

## Current Processing Model

CyberLex Sweden currently runs locally as a Streamlit application.

In the current prototype:

* user questions are processed during the local Streamlit session
* answers are generated from local Markdown source files in the `data/` folder
* no production database storage is implemented
* no user-account system is implemented
* no intentional analytics or telemetry is implemented by the app
* no live web browsing is used when answering questions
* no external AI API is required for the current rule-based prototype

The app is designed for local testing, learning, demonstration, and portfolio use.

---

## User Questions

User questions are used to:

* detect the question language
* detect the question topic
* search the local knowledge base
* select relevant source sections
* generate a source-grounded answer
* decide whether practical guidance, incident templates, report download, or refusal handling should appear

The current prototype does not intentionally save user questions to a production database.

However, local development environments can still create temporary or indirect traces, such as:

* terminal output
* browser cache
* Streamlit session data
* local logs
* downloaded files
* screenshots
* Git history if test data is committed by mistake
* operating system or backup/sync traces

This depends on how the app is run locally.

---

## Local Knowledge Base

CyberLex Sweden answers from local Markdown files stored in:

```text
data/
```

These files are educational summaries of selected legal, regulatory, authority, and defensive incident-response topics.

The app does not verify live legal updates automatically when answering.

Source freshness labels describe local review dates only.

A source freshness label does not mean that CyberLex has checked the internet or confirmed that the law is currently up to date.

---

## Incident Summaries

For selected practical incident-response questions, CyberLex Sweden can generate a downloadable SOC-style Markdown incident summary.

The generated summary may include:

* report metadata
* the original user question or reported event
* recommended first steps
* SOC triage support
* an incident checklist
* an incident log template
* a short source note
* an educational disclaimer

The current prototype does not intentionally store downloaded summaries after generating them.

The downloaded file is created for the user and is handled by the user's browser and local machine.

Users should not treat generated summaries as:

* official incident records
* legal assessments
* regulatory reports
* forensic reports
* breach notifications
* replacements for internal incident-response procedures
* replacements for professional incident-response support

---

## Sensitive Information Warning

Users should avoid entering real sensitive information into the prototype.

Do not enter real:

* personal data
* credentials
* passwords
* access tokens
* private keys
* customer data
* employee data
* confidential incident details
* sensitive security logs
* protected business information
* live exploit details
* information identifying real victims
* information identifying real systems
* information identifying real attackers
* information covered by confidentiality or security obligations

Use fictional, anonymized, or heavily generalized examples during testing.

---

## GDPR and Data Protection Note

CyberLex Sweden discusses GDPR and personal data breach topics, but it is not itself a production GDPR compliance system.

The current prototype does not include:

* a data processing register
* role-based access control
* user authentication
* production logging controls
* retention rules
* deletion workflows
* data subject request workflows
* processor or subprocessor management
* production security review
* formal DPIA support
* official breach-notification submission
* access logs designed for regulated production use

Those would need to be considered before using a similar system with real users or real personal data.

---

## Local Development Considerations

Because CyberLex Sweden is currently run locally, data handling depends partly on the local machine and development environment.

Users should consider:

* terminal output
* local browser cache
* Streamlit session behavior
* downloaded files saved by the browser
* screenshots used in documentation
* Git history
* local operating system logs
* backup or sync tools such as OneDrive
* files accidentally added to GitHub

Do not commit real sensitive incident examples to GitHub.

Do not include real sensitive data in screenshots, reports, demos, or test cases.

---

## GitHub and Repository Considerations

If the CyberLex Sweden repository is public or shared, users should avoid committing:

* real personal data
* real incident data
* credentials
* tokens
* private keys
* logs from real environments
* real customer information
* real employee information
* confidential security details

The project should use fictional or anonymized examples only.

Generated local files should be reviewed before committing.

---

## Current Privacy Position

The current privacy position is:

* CyberLex Sweden is a local educational prototype.
* It should be tested with fictional or anonymized examples only.
* It does not intentionally store user questions in a production database.
* It does not intentionally store generated incident summaries after download.
* It does not intentionally use analytics or telemetry.
* It does not use live web browsing for answers.
* It should not be used with real sensitive incident data.

---

## Future Privacy Improvements

Possible future privacy improvements include:

* clearer in-app privacy notice
* visible local-only mode explanation
* explicit test-data warning near the question input
* configurable logging behavior
* export and delete controls for generated summaries
* retention rules if storage is added
* authentication and authorization if user accounts are added
* public deployment privacy review
* stronger Terms of Use and Privacy Policy
* security review before production or public use
* review of any external AI API or hosting provider before use
* clear statement about whether user questions are stored

---

## Final Note

CyberLex Sweden should be treated as a local educational prototype.

Users should not enter real sensitive information.

For real legal, compliance, privacy, or cybersecurity matters, users should rely on official sources, internal procedures, and qualified professionals.
