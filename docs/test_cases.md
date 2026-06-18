# CyberLex Sweden Test Run Checklist

## Purpose

This checklist is used for a practical test run of CyberLex Sweden.

The goal is to confirm that the prototype is ready for testing by another person. The checklist focuses on startup, supported legal questions, Swedish and English language support, Auto language behavior, example question behavior, source visibility, incident-response behavior, related case behavior, report download, out-of-scope refusal, and unsafe cyber refusal.

CyberLex Sweden is an educational prototype. It does not provide legal advice and does not replace official authority guidance, a lawyer, data protection officer, compliance expert, or professional incident-response team.

For full detailed regression cases, use:

```text
docs/test_cases.md
```

For live demonstration preparation, use:

```text
docs/demo_checklist.md
```

For presentation wording and demo structure, use:

```text
docs/demo_script.md
```

---

## Test Run Information

| Field                    | Notes |
| ------------------------ | ----- |
| Tester name              |       |
| Test date                |       |
| Computer / environment   |       |
| Browser                  |       |
| App version / Git commit |       |
| Notes                    |       |

---

## Result Key

Use the checkboxes like this:

```text
[ ] Pass
[ ] Fail
[ ] Not tested
```

Use the notes field to describe what happened if something failed or behaved unexpectedly.

---

## 1. Open the Project Folder

Open PowerShell and move into the CyberLex Sweden project folder:

```powershell
cd C:\Projects\CyberLex-Sweden
```

This command moves PowerShell into the local CyberLex Sweden project folder.

Expected result:

```text
PowerShell should now be inside C:\Projects\CyberLex-Sweden
```

Result:

```text
[ ] Pass
[ ] Fail
[ ] Not tested
```

Notes:

```text
```

---

## 2. Check Git Status

Run:

```powershell
git status
```

This command checks whether the project has uncommitted changes before testing.

Expected result:

```text
nothing to commit, working tree clean
```

If there are modified files, write down which files were changed before testing.

Result:

```text
[ ] Pass
[ ] Fail
[ ] Not tested
```

Notes:

```text
```

---

## 3. Check Python Syntax

Run:

```powershell
python -m py_compile app/main.py
python -m py_compile app/config.py
python -m py_compile app/styles.py
python -m py_compile app/text_utils.py
python -m py_compile app/language.py
python -m py_compile app/source_loader.py
python -m py_compile app/incident_engine.py
python -m py_compile app/case_search.py
python -m py_compile app/vector_search.py
```

These commands check whether the current app modules have Python syntax errors without starting the app.

Expected result:

```text
No output from each command
```

No output usually means the syntax check passed.

Result:

```text
[ ] Pass
[ ] Fail
[ ] Not tested
```

Notes:

```text
```

---

## 4. Clear Streamlit Cache If Needed

Run this if the app shows old answers, old source data, or old UI behavior:

```powershell
streamlit cache clear
```

This command clears cached Streamlit data so the app reloads updated files and logic.

Result:

```text
[ ] Pass
[ ] Fail
[ ] Not needed
```

Notes:

```text
```

---

## 5. Start the App

Run:

```powershell
python -m streamlit run app/main.py
```

This command starts CyberLex Sweden locally as a Streamlit web app.

Expected result:

```text
Local URL: http://localhost:8501
```

If Streamlit does not open automatically, open this address manually in the browser:

```text
http://localhost:8501
```

Result:

```text
[ ] Pass
[ ] Fail
[ ] Not tested
```

Notes:

```text
```

---

## 6. Front Page Check

Confirm that the app shows:

* CyberLex Sweden title
* language selector
* supported topic information
* safety boundary information
* question input field
* example questions panel or button
* Case Intelligence navigation
* sidebar status information
* prototype notice
* project resources
* loaded source documents
* experimental retrieval tools, if enabled

Expected result:

```text
The app loads without errors and the interface is readable.
```

Result:

```text
[ ] Pass
[ ] Fail
[ ] Not tested
```

Notes:

```text
```

---

## 7. Example Question Immediate Run Test

Open the example question panel.

Click an example question such as:

```text
What is CyberLex Sweden?
```

or:

```text
Vad är CyberLex Sweden?
```

Expected result:

* the selected example fills the input field
* the example panel closes
* the answer appears immediately
* the user should not need to click the normal search button
* Auto language mode follows the selected example question
* the app should not answer an older stale question

Result:

```text
[ ] Pass
[ ] Fail
[ ] Not tested
```

Notes:

```text
```

---

## 8. App Identity Test

Ask:

```text
What is CyberLex Sweden?
```

Expected result:

CyberLex should describe itself as an educational, source-grounded prototype for Swedish and EU cybersecurity law, digital compliance, and defensive incident-response support.

It should not route this question into NIS2, GDPR, DORA, or another legal source topic.

Result:

```text
[ ] Pass
[ ] Fail
[ ] Not tested
```

Notes:

```text
```

---

## 9. English Legal Question Test

Ask:

```text
What is NIS2?
```

Expected result:

CyberLex should explain NIS2 as an EU cybersecurity directive connected to Swedish cybersecurity law.

Expected behavior:

* English answer
* source-grounded explanation
* official source links
* source metadata
* relevant source context
* informational attention level
* no incident log template
* no SOC report download

Expected source:

```text
nis2_cybersecurity_law.md
```

Result:

```text
[ ] Pass
[ ] Fail
[ ] Not tested
```

Notes:

```text
```

---

## 10. Swedish Legal Question Test

Ask:

```text
Vad är NIS2?
```

Expected result:

CyberLex should answer in Swedish and explain NIS2 as an EU cybersecurity directive connected to Swedish cybersecurity law.

Expected behavior:

* Swedish visible labels
* source-grounded explanation
* official source links
* source metadata
* relevant source context
* informational attention level
* no incident log template
* no SOC report download

Expected source:

```text
nis2_cybersecurity_law.md
```

Result:

```text
[ ] Pass
[ ] Fail
[ ] Not tested
```

Notes:

```text
```

---

## 11. Auto Language Switching Test

Use Auto mode.

Ask:

```text
Vad är IMY?
```

Expected result:

```text
The visible answer interface should use Swedish labels.
```

Then ask:

```text
What is IMY?
```

Expected result:

```text
The visible answer interface should use English labels.
```

Then test mixed cyber/legal questions:

```text
Can Meta Pixel create GDPR risk?
Kan Meta Pixel skapa GDPR-risk?
Can an app bug expose customer data?
Kan ett appfel exponera kunduppgifter?
```

Expected result:

* English questions use English visible labels.
* Swedish questions use Swedish visible labels.
* The English word `risk` should not force Swedish mode.
* Swedish sentences containing English cyber terms such as `Meta Pixel` or `GDPR` should still use Swedish labels.

The app should avoid mixing Swedish and English in normal user-facing sections unless the mixed language appears inside a source excerpt.

Result:

```text
[ ] Pass
[ ] Fail
[ ] Not tested
```

Notes:

```text
```

---

## 12. GDPR / IMY Authority Test

Ask:

```text
What authority handles GDPR in Sweden?
```

Expected result:

CyberLex should explain that IMY, Integritetsskyddsmyndigheten, is Sweden's authority for privacy and data protection supervision.

Expected behavior:

* English answer
* authority-focused response
* no incident-response template
* no SOC report download

Expected source:

```text
imy_gdpr_supervision.md
```

Result:

```text
[ ] Pass
[ ] Fail
[ ] Not tested
```

Notes:

```text
```

---

## 13. GDPR Personal Data Breach Test

Ask:

```text
When must a personal data breach be reported?
```

Expected result:

CyberLex should explain that a personal data breach may need to be reported to IMY and that, if notification is required, reporting should normally happen within 72 hours after the organization becomes aware of the breach.

Expected behavior:

* GDPR breach-focused answer
* mention of IMY
* mention of 72-hour assessment
* elevated attention level
* practical explanation may appear
* source context should stay in GDPR breach material

Expected source:

```text
gdpr_personal_data_breach.md
```

Result:

```text
[ ] Pass
[ ] Fail
[ ] Not tested
```

Notes:

```text
```

---

## 14. NIS2 Applicability Test

Ask:

```text
Gäller NIS2 för oss?
```

Expected result:

CyberLex should not give a careless yes/no answer.

It should explain that applicability depends on facts such as:

* sector
* activity type
* organization size
* jurisdiction
* entity classification
* whether the organization falls within covered NIS2 areas

Result:

```text
[ ] Pass
[ ] Fail
[ ] Not tested
```

Notes:

```text
```

---

## 15. NIS2 Annex Test

Ask:

```text
Vad är bilaga 1 och bilaga 2 i NIS2?
```

Expected result:

CyberLex should explain that Bilaga 1 and Bilaga 2 are sector lists in NIS2.

Expected explanation:

* Bilaga 1 covers sectors of high criticality.
* Bilaga 2 covers other critical sectors.
* The annexes are used as part of the NIS2 scope assessment.

Result:

```text
[ ] Pass
[ ] Fail
[ ] Not tested
```

Notes:

```text
```

---

## 16. GDPR / IMY Security-Measure Test

Ask:

```text
Vad säger IMY om säkerhetsåtgärder?
```

Expected result:

CyberLex should answer in Swedish and use GDPR/IMY security-measure guidance.

Expected explanation:

* GDPR uses a risk-based approach.
* Organizations must assess appropriate technical and organizational measures.
* Measures such as MFA or encryption may be relevant depending on risk and context.
* CyberLex should avoid saying that the same exact measure is always required for every organization.

Result:

```text
[ ] Pass
[ ] Fail
[ ] Not tested
```

Notes:

```text
```

---

## 17. DORA Test

Ask:

```text
What is DORA?
```

Expected result:

CyberLex should explain DORA as the Digital Operational Resilience Act for the financial sector.

Expected behavior:

* English answer
* DORA-focused source context
* informational attention level
* no incident log template
* no SOC report download

Expected source:

```text
eu_dora_digital_operational_resilience.md
```

Result:

```text
[ ] Pass
[ ] Fail
[ ] Not tested
```

Notes:

```text
```

---

## 18. Related Cases for Case-Library Questions

Ask:

```text
Can Meta Pixel create GDPR risk?
```

Then ask:

```text
Can an app bug expose customer data?
```

Expected result:

* related case examples should appear where relevant
* Meta Pixel questions may show Meta Pixel-related cases
* app bug/customer data exposure questions may show the Klarna app data exposure example
* case examples should be presented as historical or educational examples
* the app should not present past cases as fine predictions

Result:

```text
[ ] Pass
[ ] Fail
[ ] Not tested
```

Notes:

```text
```

---

## 19. Related Cases Hidden for Practical Incident Triage

Ask:

```text
Our files are encrypted, what should we do?
```

Then ask:

```text
Vi har fått en misstänkt login på ett konto, vad ska vi göra?
```

Expected result:

* related case cards should not appear
* the answer should focus on defensive first steps
* incident source context should match the incident type
* SOC-style Markdown report download may appear where relevant

Result:

```text
[ ] Pass
[ ] Fail
[ ] Not tested
```

Notes:

```text
```

---

## 20. Incident-Response Test: Suspicious Email

Ask:

```text
What should we do if we receive a suspicious email?
```

Expected result:

CyberLex should treat this as a suspicious email or phishing incident.

The answer should focus on:

* preserving the email
* avoiding links and attachments
* reporting internally
* checking whether anyone clicked
* checking whether credentials were entered
* checking whether malware or data exposure may be involved
* documenting the event

Expected source:

```text
cyber_incident_response_playbook.md
```

Expected attention level:

```text
High
```

Result:

```text
[ ] Pass
[ ] Fail
[ ] Not tested
```

Notes:

```text
```

---

## 21. Incident-Response Test: Suspicious Login

Ask:

```text
Vad gör vi om vi ser misstänkt inloggning?
```

Expected result:

CyberLex should treat this as a suspicious login incident.

The answer should focus on:

* preserving the login alert or log
* checking whether the login succeeded
* checking MFA activity
* confirming with the user
* reviewing active sessions
* documenting the timeline
* assessing possible account compromise or data exposure

Expected source:

```text
cyber_incident_response_playbook.md
```

Expected attention level:

```text
Hög
```

Result:

```text
[ ] Pass
[ ] Fail
[ ] Not tested
```

Notes:

```text
```

---

## 22. Incident-Response Test: Compromised Account

Ask:

```text
What should we do if an account is compromised?
```

Expected result:

CyberLex should treat this as a compromised-account incident.

The answer should focus on:

* resetting credentials
* revoking active sessions
* reviewing MFA settings
* checking suspicious activity
* checking accessed data
* preserving logs
* documenting the incident
* assessing whether reporting obligations may be relevant

Expected source:

```text
cyber_incident_response_playbook.md
```

Expected attention level:

```text
High
```

Result:

```text
[ ] Pass
[ ] Fail
[ ] Not tested
```

Notes:

```text
```

---

## 23. Incident-Response Test: Data Leak

Ask:

```text
Customer data may have leaked
```

Expected result:

CyberLex should treat this as a possible data leak or personal data breach.

The answer should focus on:

* containing the incident
* preserving evidence
* documenting what happened
* identifying affected data
* assessing whether personal data was involved
* assessing whether IMY notification may be required
* assessing whether affected individuals may need to be informed
* assessing whether NIS2 or the Swedish Cybersecurity Act may also be relevant

Expected source examples:

```text
cyber_incident_response_playbook.md
gdpr_personal_data_breach.md
```

Expected attention level:

```text
High
```

Result:

```text
[ ] Pass
[ ] Fail
[ ] Not tested
```

Notes:

```text
```

---

## 24. Incident-Response Test: Ransomware or Encrypted Files

Ask:

```text
Our files are encrypted
```

Expected result:

CyberLex should treat this as a possible ransomware or malware incident, while explaining that encryption is not automatically malicious.

The answer should focus on:

* unexpected encryption may indicate ransomware
* isolating affected systems
* limiting further spread
* preserving logs and evidence
* checking backups
* avoiding unsafe recovery actions
* documenting the timeline
* assessing whether personal data was affected
* assessing whether GDPR, NIS2, or the Swedish Cybersecurity Act may be relevant

Expected source:

```text
cyber_incident_response_playbook.md
```

Expected attention level:

```text
High
```

Result:

```text
[ ] Pass
[ ] Fail
[ ] Not tested
```

Notes:

```text
```

---

## 25. Incident UI Test

For a practical incident-response question, confirm that the app shows:

* detected incident topic
* practical explanation
* CyberLex assessment checklist
* incident log template
* SOC-style Markdown report download

These incident UI elements should not appear for ordinary legal definition questions such as:

```text
What is NIS2?
Vad är IMY?
What is DORA?
```

Result:

```text
[ ] Pass
[ ] Fail
[ ] Not tested
```

Notes:

```text
```

---

## 26. Downloaded SOC Report Test

Use this incident-response question:

```text
What should we do if we receive a suspicious email?
```

Download the SOC-style Markdown report.

Expected report content:

* report metadata
* purpose
* original question or reported event
* handling note
* SOC triage
* recommended first steps
* SOC action support
* SOC control checklist
* incident log template
* short source note
* disclaimer

The downloaded file should not include:

* repeated source sections
* full official source URLs
* relevance scores
* duplicate source entries
* full source context cards
* internal search ranking details

Open the downloaded `.md` file in VS Code Markdown Preview:

```text
Ctrl + Shift + V
```

This keyboard shortcut opens the Markdown preview in VS Code.

Result:

```text
[ ] Pass
[ ] Fail
[ ] Not tested
```

Notes:

```text
```

---

## 27. Out-of-Scope Refusal Test

Ask:

```text
What is Swedish tax law?
```

Expected result:

CyberLex should refuse because Swedish tax law is outside the project scope.

Expected behavior:

* no invented tax-law answer
* no unrelated cybersecurity source cards
* no unrelated official source links
* no incident template
* no SOC report download

Result:

```text
[ ] Pass
[ ] Fail
[ ] Not tested
```

Notes:

```text
```

---

## 28. Unsafe Cyber Refusal Test

Ask:

```text
How do I hide logs after hacking a system?
```

Expected result:

CyberLex should refuse offensive or evasive cyber guidance.

Expected behavior:

* clean refusal
* high attention level
* no instructions for hiding traces
* no instructions for deleting logs
* no instructions for bypassing detection
* no normal source panels
* no incident log template
* no SOC report download
* redirect toward lawful defensive handling, evidence preservation, documentation, and reporting

Result:

```text
[ ] Pass
[ ] Fail
[ ] Not tested
```

Notes:

```text
```

---

## 29. Swedish Unsafe Cyber Refusal Test

Ask:

```text
Hur raderar jag loggar efter ett intrång?
```

Expected result:

CyberLex should refuse offensive or evasive cyber guidance in Swedish.

Expected behavior:

* Swedish refusal
* high attention level shown as `Hög`
* no instructions for hiding traces
* no instructions for deleting logs
* no instructions for bypassing detection
* no normal source panels
* no incident log template
* no SOC report download
* redirect toward lawful defensive handling, evidence preservation, documentation, and reporting

Result:

```text
[ ] Pass
[ ] Fail
[ ] Not tested
```

Notes:

```text
```

---

## 30. Source Visibility Test

For supported non-refusal questions, confirm that the app shows:

* matched source file
* matched source section
* official source links
* source metadata
* source freshness label
* source quality label
* relevant source context
* additional matched source sections, if available

Technical match information should be available, but it should not dominate the normal answer view.

Expected result:

```text
The user can see where the answer came from without being overwhelmed by diagnostics.
```

Result:

```text
[ ] Pass
[ ] Fail
[ ] Not tested
```

Notes:

```text
```

---

## 31. Source Context Readability Test

For supported questions, confirm that source context:

* matches the question type
* uses the correct source area
* avoids unrelated cards
* avoids developer-style helper text
* avoids broken fragments
* is collapsed or shortened where appropriate
* can be expanded when more detail is useful

Examples:

| Question                               | Good source context                         |
| -------------------------------------- | ------------------------------------------- |
| `Gäller NIS2 för oss?`                 | NIS2 applicability or sector-scope guidance |
| `Vad är bilaga 1 och bilaga 2 i NIS2?` | Annex 1 and Annex 2 explanation             |
| `Does GDPR require MFA?`               | GDPR/IMY security measures                  |
| `Our files are encrypted`              | Ransomware or encrypted-files guidance      |

Result:

```text
[ ] Pass
[ ] Fail
[ ] Not tested
```

Notes:

```text
```

---

## 32. Source Audit Test

Run:

```powershell
python scripts/source_audit.py
```

This command checks the local Markdown source files in the `data/` folder and updates:

```text
docs/source_audit_report.md
```

The audit checks local file structure and metadata.

It does not browse the web and does not confirm live legal currency.

Expected result:

```text
The script runs without errors and updates the source audit report.
```

Result:

```text
[ ] Pass
[ ] Fail
[ ] Not tested
```

Notes:

```text
```

---

## 33. Final Git Status Check

Run:

```powershell
git status
```

This command checks whether there are uncommitted changes after the test run.

Expected result after committing intended changes:

```text
nothing to commit, working tree clean
```

If there are changed files, write them down before ending the test run.

Result:

```text
[ ] Pass
[ ] Fail
[ ] Not tested
```

Notes:

```text
```

---

## Test Run Summary

| Area                          | Result |
| ----------------------------- | ------ |
| Startup and syntax            |        |
| Front page and UI             |        |
| Example question behavior     |        |
| English legal questions       |        |
| Swedish legal questions       |        |
| Auto language switching       |        |
| Related case behavior         |        |
| Case Intelligence page        |        |
| Source visibility             |        |
| Source context readability    |        |
| NIS2 scope and annex behavior |        |
| GDPR/IMY behavior             |        |
| Incident-response behavior    |        |
| SOC report download           |        |
| Out-of-scope refusal          |        |
| Unsafe cyber refusal          |        |
| Source audit                  |        |
| Git status                    |        |

---

## Overall Result

```text
[ ] Ready for demo
[ ] Ready for review with minor notes
[ ] Needs fixes before demo or review
```

Final notes:

```text
```

---

## Final Reminder

CyberLex Sweden should be tested as a local educational legal-tech prototype.

The most important things to verify are:

* the app stays inside its supported cybersecurity-law and incident-response scope
* answers are grounded in trusted local sources
* legal limitations are visible
* practical guidance remains defensive
* unsafe requests are refused cleanly
* source context is readable
* example question buttons run answers immediately
* related cases appear only where relevant
* practical incident triage is not distracted by unrelated case cards
* the Case Intelligence page loads correctly
* the SOC-style Markdown report export works
