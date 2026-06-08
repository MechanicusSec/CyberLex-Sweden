# Privacy and Data Handling

CyberLex Sweden is a local educational prototype. This document explains how the current prototype handles user questions, local source files, incident summaries, and sensitive information.

CyberLex Sweden does **not** provide legal advice and should not be used as the sole basis for legal, compliance, regulatory, or security decisions.

---

## Current Processing Model

CyberLex Sweden currently runs locally as a Streamlit application.

In the current prototype:

- user questions are processed during the local Streamlit session
- answers are generated from local Markdown source files in the data/ folder
- no production database storage is implemented
- no user-account system is implemented
- no intentional analytics or telemetry is implemented by the app
- no live web browsing is used when answering questions

The app is designed for local testing, learning, demonstration, and portfolio use.

---

## User Questions

User questions are used to:

- detect the question language
- detect the question topic
- search the local knowledge base
- select relevant source sections
- generate a source-grounded summary
- decide whether practical guidance, incident templates, or refusal handling should appear

The prototype does not intentionally save user questions to a database.

However, users should remember that local development environments can still produce runtime output, terminal logs, browser cache, or Streamlit session data. This depends on how the app is run locally.

---

## Local Knowledge Base

CyberLex Sweden answers from local Markdown files stored in the data/ folder.

These files are written as educational summaries of selected legal, regulatory, authority, and incident-response topics.

The app does not verify live legal updates automatically when answering. Source freshness labels describe local review dates only.

---

## Incident Summaries

For selected practical incident-response questions, CyberLex Sweden can generate a downloadable incident summary.

The generated incident summary is intended as a documentation aid for learning and testing. It may include:

- the original question
- recommended first steps
- an incident checklist
- an incident log template
- a source note
- an educational disclaimer

The app does not intentionally store downloaded summaries after generating them. The downloaded file is created for the user.

Users should not treat the generated summary as an official incident record, legal assessment, regulatory report, or replacement for internal incident-response procedures.

---

## Sensitive Information Warning

Users should avoid entering real sensitive information into the prototype.

Do **not** enter real:

- personal data
- credentials
- passwords
- access tokens
- private keys
- customer data
- employee data
- confidential incident details
- security logs containing sensitive information
- protected business information
- live exploit details
- information that could identify real victims, systems, or attackers

Use fictional or anonymized examples during testing.

---

## GDPR and Data Protection Note

CyberLex Sweden discusses GDPR and personal data breach topics, but it is not itself a production GDPR compliance system.

The prototype does not currently include:

- a data processing register
- role-based access control
- user authentication
- production logging controls
- retention rules
- deletion workflows
- data subject request workflows
- processor/subprocessor management
- production security review

Those would be needed before using a similar system with real users or real personal data.

---

## Local Development Considerations

Because CyberLex Sweden is currently run locally, data handling depends partly on the local machine and development environment.

Users should consider:

- terminal output
- local browser cache
- Streamlit session behavior
- downloaded files saved by the browser
- Git history if test data is accidentally committed
- screenshots used in documentation
- local operating system logs
- backup or sync tools such as OneDrive

Do not commit real sensitive incident examples to GitHub.

---

## Current Privacy Position

The current privacy position is:

- CyberLex Sweden is a local educational prototype.
- It should be tested with fictional or anonymized examples only.
- It does not intentionally store user questions or incident summaries in a production database.
- It does not intentionally use analytics or telemetry.
- It should not be used with real sensitive incident data.

---

## Future Improvements

Possible future privacy improvements include:

- clearer in-app privacy notice
- optional local-only mode explanation in the interface
- explicit test-data warning near the question input
- configurable logging behavior
- export/delete controls for generated summaries
- public deployment privacy review
- stronger Terms of Use and Privacy Policy
- security review before any production or public use