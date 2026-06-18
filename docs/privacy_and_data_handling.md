# Privacy and Data Handling

## Purpose

This document explains how the current CyberLex Sweden prototype handles user questions, local source files, case-library files, generated incident summaries, and sensitive information.

CyberLex Sweden is a local educational prototype.

It does not provide legal advice and should not be used as the sole basis for legal, compliance, regulatory, privacy, or security decisions.

---

## Current Processing Model

CyberLex Sweden currently runs locally as a Streamlit application.

In the current prototype:

* user questions are processed during the local Streamlit session
* answers are generated from local Markdown source files in the `data/` folder
* related case examples may be loaded from local Markdown files in the `cases/` folder
* no production database storage is implemented
* no user-account system is implemented
* no intentional analytics or telemetry is implemented by the app
* no live web browsing is used when answering questions
* no external AI API is required for the current rule-based prototype
* no production hosting environment is currently assumed

The app is designed for local testing, learning, demonstration, and portfolio use.

---

## Local-First Design

CyberLex Sweden is currently designed as a local-first prototype.

The current app reads local project files from the repository and generates answers during the active local session.

This means the current prototype is different from a hosted production service.

A hosted version would require a separate privacy and security review before real users or real user data are allowed.

Local-first does not mean risk-free.

Local machines can still create traces through browsers, terminals, screenshots, file downloads, sync tools, logs, backups, and Git history. Apparently computers enjoy hoarding evidence like tiny mechanical goblins.

---

## User Questions

User questions are used to:

* detect the question language
* detect the question topic
* search the local knowledge base
* select relevant source sections
* check whether related case examples should appear
* decide whether the question is practical incident-response triage
* decide whether SOC-style report download should appear
* decide whether refusal handling should appear
* generate a source-grounded answer

The current prototype does not intentionally save user questions to a production database.

However, local development environments can still create temporary or indirect traces, such as:

* terminal output
* browser cache
* Streamlit session data
* local logs
* downloaded files
* screenshots
* Git history if test data is committed by mistake
* operating system search indexes
* operating system logs
* backup or sync traces

This depends on how the app is run locally.

---

## Local Knowledge Base

CyberLex Sweden answers from local Markdown files stored in:

```text
data/
```

These files are educational summaries of selected legal, regulatory, authority, cybersecurity-law, and defensive incident-response topics.

The app does not verify live legal updates automatically when answering.

Source freshness labels describe local review dates only.

A source freshness label does not mean that CyberLex Sweden has checked the internet or confirmed that the law, authority guidance, or regulatory material is currently up to date.

---

## Local Case Library

CyberLex Sweden may show related case examples from local Markdown files stored in:

```text
cases/
```

The case library may include:

* authority decisions
* public incident examples
* case summaries
* fine or outcome notes where known
* learning notes
* related CyberLex topics
* official or reliable source links

Case examples are educational context only.

They are not fine predictions, legal assessments, or proof that a similar case would receive the same outcome.

Case-library files should not contain real confidential data unless the information is already public and appropriate to include.

---

## Incident Summaries

For selected practical incident-response questions, CyberLex Sweden can generate a downloadable SOC-style Markdown incident summary.

The generated summary may include:

* report metadata
* the original user question or reported event
* recommended first steps
* SOC triage support
* SOC action support
* SOC control checklist
* an incident log template
* evidence and log notes
* recovery reminders
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
* NIS2 or Swedish cybersecurity-law incident reports
* replacements for internal incident-response procedures
* replacements for professional incident-response support

---

## Downloaded Files

If the user downloads a generated Markdown incident summary, that file is controlled by the user's browser and local computer.

Downloaded files may remain in:

* the browser download folder
* temporary browser storage
* operating system file history
* backup folders
* cloud sync folders
* antivirus or endpoint-security logs
* screenshots or copied notes

Users should review downloaded files before sharing, committing, or uploading them anywhere.

Generated reports should use fictional, anonymized, or generalized examples during testing.

---

## Sensitive Information Warning

Users should avoid entering real sensitive information into the prototype.

Do not enter real:

* personal data
* credentials
* passwords
* access tokens
* API keys
* private keys
* customer data
* employee data
* student data
* confidential incident details
* sensitive security logs
* protected business information
* live exploit details
* information identifying real victims
* information identifying real systems
* information identifying real attackers
* information covered by confidentiality or security obligations

Use fictional, anonymized, or heavily generalized examples during testing.

Good test examples:

```text
A fictional customer database may have leaked.
```

```text
A test user clicked a suspicious link in a lab environment.
```

```text
A demo account showed a suspicious login from an unknown country.
```

Bad test examples:

```text
A real customer name, email, IP address, password, token, or incident log.
```

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
* consent management
* privacy policy acceptance flow
* audit logs suitable for regulated environments

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
* temporary files created during testing
* editor autosave behavior
* antivirus or endpoint-security tools

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
* generated reports containing real information
* screenshots containing names, emails, paths, tokens, or incident details

The project should use fictional or anonymized examples only.

Generated local files should be reviewed before committing.

Before committing, users should run:

```powershell
git status
```

This command shows which files are modified, staged, or untracked.

It helps prevent accidental commits of sensitive or unnecessary files, because Git has the moral restraint of a hungry servo-skull.

---

## Public Repository Warning

If the repository is public, anything committed may become visible to others.

Even if sensitive data is later deleted, it may remain in Git history unless the history is rewritten and all copies are controlled.

Users should avoid committing sensitive material in the first place.

Sensitive information should not be added to:

* Markdown files
* screenshots
* generated reports
* source files
* test data
* Git commit messages
* issue descriptions
* pull requests
* README examples

---

## External AI or API Use

The current rule-based CyberLex Sweden prototype does not require an external AI API.

If future versions add an external AI provider, API, hosted model, vector database, analytics service, or cloud storage service, the privacy position must be reviewed again.

Before using external services, the project should document:

* what data is sent
* why it is sent
* where it is processed
* whether it is stored
* how long it is retained
* who can access it
* whether it may be used for model training
* whether personal data or sensitive data is allowed
* what user notice or consent is needed
* what security controls are required

No real sensitive data should be sent to external services unless the legal, privacy, and security requirements are properly reviewed.

---

## Hosting and Deployment Warning

The current privacy position assumes local development and demonstration.

If CyberLex Sweden is deployed publicly or shared with real users, the project would need additional review before launch.

A public or hosted version should consider:

* privacy policy
* terms of use
* security review
* logging controls
* retention rules
* access controls
* abuse prevention
* rate limiting
* user notice
* incident-response process
* hosting provider review
* external service review
* handling of user-submitted data
* data deletion process
* backup and recovery rules

A public deployment should not happen with real user data until these areas are addressed.

---

## Current Privacy Position

The current privacy position is:

* CyberLex Sweden is a local educational prototype.
* It should be tested with fictional or anonymized examples only.
* It does not intentionally store user questions in a production database.
* It does not intentionally store generated incident summaries after download.
* It does not intentionally use analytics or telemetry.
* It does not use live web browsing for answers.
* It does not require an external AI API in the current rule-based version.
* It should not be used with real sensitive incident data.
* Any public or hosted version would need a separate privacy and security review.

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
* documented handling of downloaded files
* documented handling of case-library files
* documented handling of external AI or API providers
* documented incident process for a hosted version

---

## Final Note

CyberLex Sweden should be treated as a local educational prototype.

Users should not enter real sensitive information.

For real legal, compliance, privacy, or cybersecurity matters, users should rely on official sources, internal procedures, and qualified professionals.

CyberLex Sweden can support learning and structured exploration, but it should not become a bucket for real secrets. Humanity already has enough buckets on fire.
