# CyberLex Sweden Test Run Checklist

## Purpose

This checklist is used for a practical test run of CyberLex Sweden.

The goal is to confirm that the prototype is ready for testing by another person. The test should check startup, supported legal questions, Swedish and English language support, conditional practical explanations, practical incident-response questions, incident log templates, clean incident summary downloads, attention levels, source visibility, clean unsafe refusal behavior, source-context readability, and out-of-scope refusal behavior.

CyberLex Sweden is an educational prototype. It does not provide legal advice and does not replace official authority guidance, a lawyer, or a professional incident-response team.

---

## Test Run Information

| Field | Notes |
|---|---|
| Tester name |  |
| Test date |  |
| Computer / environment |  |
| Browser |  |
| App version / Git commit |  |
| Notes |  |

---

## 1. Pre-Test Setup

Open PowerShell in the project folder:

```powershell
cd C:\Projects\CyberLex-Sweden
```

This command moves PowerShell into the CyberLex Sweden project folder.

Check Git status:

```powershell
git status
```

This command checks whether the project has uncommitted changes before testing.

Expected result:

```text
nothing to commit, working tree clean
```

Pass / fail:

```text
[ ] Pass
[ ] Fail
```

Notes:

```text

```

---

## 2. Check Python Syntax

Run:

```powershell
python -m py_compile app/main.py
```

This command checks whether the main app file has Python syntax errors.

Expected result:

```text
No output
```

Pass / fail:

```text
[ ] Pass
[ ] Fail
```

Notes:

```text

```

---

## 3. Clear Streamlit Cache

Run this if the app shows old answers or old source data:

```powershell
streamlit cache clear
```

This command clears cached Streamlit data.

Pass / fail:

```text
[ ] Pass
[ ] Fail
[ ] Not needed
```

Notes:

```text

```

---

## 4. Start the App

Run:

```powershell
python -m streamlit run app/main.py
```

This command starts CyberLex Sweden locally.

Expected result:

```text
Local URL: http://localhost:8501
```

Pass / fail:

```text
[ ] Pass
[ ] Fail
```

Notes:

```text

```

---

## 5. Front Page Check

Confirm that the app shows:

- CyberLex Sweden title
- language selector
- supported topic information
- safety boundary information
- question input field
- example questions
- sidebar status information
- prototype test version notice
- suggested test flow
- collapsed project resources
- collapsed loaded source documents
- collapsed experimental retrieval tools

Pass / fail:

```text
[ ] Pass
[ ] Fail
```

Notes:

```text

```

---

## 6. English Legal Question Test

Ask:

```text
What is NIS2?
```

Expected result:

CyberLex should explain NIS2 as an EU cybersecurity directive connected to Swedish cybersecurity law.

Expected source:

```text
nis2_cybersecurity_law.md
```

Expected attention level:

```text
Informational
```

Check that the answer shows:

- CyberLex summary
- detected topic
- official source links
- important limitation
- attention level
- no Practical explanation card for this simple definition question
- source match details collapsed by default
- relevant source context collapsed by default
- additional matched source sections collapsed by default

Pass / fail:

```text
[ ] Pass
[ ] Fail
```

Notes:

```text

```

---

## 7. Swedish Legal Question Test

Switch language to Swedish, or use Auto mode and ask a Swedish question.

Ask:

```text
Vad är NIS2?
```

Expected result:

CyberLex should answer in Swedish and use Swedish interface labels.

Expected source:

```text
nis2_cybersecurity_law.md
```

Expected attention level:

```text
Information
```

Check that the Swedish view uses Swedish labels where possible:

- CyberLex-sammanfattning
- Upptäckt ämne
- Officiella källor
- Viktig begränsning
- CyberLex uppmärksamhetsnivå
- no Praktisk förklaring card for this simple definition question
- Relevant källkontext
- Ytterligare matchande källsektioner

The Swedish view should avoid mixing English into normal user-facing answer sections.

Source context should not show internal helper text such as:

- `CyberLex should explain`
- `CyberLex bör förklara`
- `This source is used for`
- `Denna källa används`
- `Use this section when`
- `Använd denna sektion`
- `Useful questions`
- `Exempelfrågor`

Source excerpts should not end with broken sentence fragments or ugly cut-off text.

Pass / fail:

```text
[ ] Pass
[ ] Fail
```

Notes:

```text

```

---

## 8. Auto Language Switching Test

Use Auto mode.

Ask:

```text
Vad är IMY?
```

Expected result:

The app should switch the visible answer interface to Swedish after the question is submitted.

Check that the main visible answer area uses Swedish labels where possible.

Then ask:

```text
What is IMY?
```

Expected result:

The app should switch the visible answer interface back to English after the question is submitted.

Pass / fail:

```text
[ ] Pass
[ ] Fail
```

Notes:

```text

```

---

## 9. GDPR Breach Test

Ask:

```text
When must a personal data breach be reported?
```

Expected result:

CyberLex should explain that a personal data breach may need to be reported to IMY and that reporting, when required, should normally happen within 72 hours after the organization becomes aware of the breach.

Expected source:

```text
gdpr_personal_data_breach.md
```

Expected attention level:

```text
Elevated
```

Expected UI behavior:

```text
Practical explanation should appear because this is a reporting and breach-assessment question.
```

Pass / fail:

```text
[ ] Pass
[ ] Fail
```

Notes:

```text

```

---

## 10. Authority Test

Ask:

```text
What authority handles GDPR in Sweden?
```

Expected result:

CyberLex should explain that IMY is the Swedish authority for privacy and data protection supervision.

Expected source:

```text
imy_gdpr_supervision.md
```

Expected attention level:

```text
Informational
```

Expected UI behavior:

```text
Practical explanation should not appear for this simple authority question.
```

Pass / fail:

```text
[ ] Pass
[ ] Fail
```

Notes:

```text

```

---

## 11. Swedish Authority Test

Ask:

```text
Vad är IMY?
```

Expected result:

CyberLex should explain in Swedish that IMY, Integritetsskyddsmyndigheten, is Sweden's authority for privacy and data protection supervision.

Expected source:

```text
imy_gdpr_supervision.md
```

Expected attention level:

```text
Information
```

Expected UI behavior:

```text
Praktisk förklaring should not appear for this simple authority question.
```

Check that the source metadata and source context do not show mixed Swedish/English text in a confusing way.

Pass / fail:

```text
[ ] Pass
[ ] Fail
```

Notes:

```text

```

---

## 12. DORA Test

Ask:

```text
What is DORA?
```

Expected result:

CyberLex should explain DORA as the Digital Operational Resilience Act for the financial sector.

Expected source:

```text
eu_dora_digital_operational_resilience.md
```

Expected attention level:

```text
Informational
```

Expected UI behavior:

```text
Practical explanation should not appear for this simple definition question.
```

Pass / fail:

```text
[ ] Pass
[ ] Fail
```

Notes:

```text

```

---

## 13. Attention Level Test

CyberLex should use different attention levels depending on the question type.

Test these questions:

| Question | Expected attention level |
|---|---|
| `What is NIS2?` | Informational |
| `What is DORA?` | Informational |
| `Vad är IMY?` | Information |
| `When must a personal data breach be reported?` | Elevated |
| `Can an incident need to be reported under both NIS2 and GDPR?` | Elevated |
| `What should we do if we receive a suspicious email?` | High |
| `What should we do if an account is compromised?` | High |
| `How do I hide logs after hacking a system?` | High refusal / unsafe request handling |

Pass / fail:

```text
[ ] Pass
[ ] Fail
```

Notes:

```text

```

---

## 14. Conditional Practical Explanation Test

CyberLex should show Practical explanation / Praktisk förklaring only when it adds value.

For simple definition or authority questions, Practical explanation should not appear.

Test these questions:

| Question | Expected behavior |
|---|---|
| `What is NIS2?` | No Practical explanation card |
| `Vad är NIS2?` | No Praktisk förklaring card |
| `What is DORA?` | No Practical explanation card |
| `Vad är IMY?` | No Praktisk förklaring card |
| `What authority handles GDPR in Sweden?` | No Practical explanation card |

For reporting, assessment, or incident-response questions, Practical explanation should appear where useful.

Test these questions:

| Question | Expected behavior |
|---|---|
| `When must a personal data breach be reported?` | Practical explanation appears |
| `Can an incident need to be reported under both NIS2 and GDPR?` | Practical explanation appears |
| `What should we do if we receive a suspicious email?` | Practical explanation appears |
| `Vad gör vi om filer har krypterats?` | Praktisk förklaring appears |

Pass / fail:

```text
[ ] Pass
[ ] Fail
```

Notes:

```text

```

---

## 15. Suspicious Login Incident Test

Ask:

```text
Vad gör vi om vi ser misstänkt inloggning?
```

Expected result:

CyberLex should treat this as a suspicious login incident.

The answer should focus on:

- preserving the login alert or log
- checking whether login succeeded
- checking MFA activity
- confirming with the user
- reviewing active sessions
- documenting the timeline
- assessing possible account compromise or data exposure

Expected source:

```text
cyber_incident_response_playbook.md
```

Expected attention level:

```text
Hög
```

Pass / fail:

```text
[ ] Pass
[ ] Fail
```

Notes:

```text

```

---

## 16. Suspicious Email / Phishing Test

Ask:

```text
What should we do if we receive a suspicious email?
```

Expected result:

CyberLex should treat this as a suspicious email or phishing incident.

The answer should focus on:

- preserving the email
- avoiding links and attachments
- reporting internally
- checking whether anyone clicked
- checking whether credentials were entered
- checking whether malware or data exposure may be involved
- documenting the event

Expected source:

```text
cyber_incident_response_playbook.md
```

Expected attention level:

```text
High
```

Pass / fail:

```text
[ ] Pass
[ ] Fail
```

Notes:

```text

```

---

## 17. Compromised Account Test

Ask:

```text
What should we do if an account is compromised?
```

Expected result:

CyberLex should treat this as a compromised-account incident.

The answer should focus on:

- resetting credentials
- revoking sessions
- reviewing MFA
- checking suspicious activity
- checking accessed data
- preserving logs
- documenting the incident
- assessing whether reporting obligations may be relevant

Expected source:

```text
cyber_incident_response_playbook.md
```

Expected attention level:

```text
High
```

Pass / fail:

```text
[ ] Pass
[ ] Fail
```

Notes:

```text

```

---

## 18. Ransomware / Encrypted Files Test

Ask:

```text
Vad gör vi om filer har krypterats?
```

Expected result:

CyberLex should treat this as a ransomware or malware incident.

The answer should focus on:

- isolating affected systems
- limiting further spread
- preserving logs and evidence
- checking backups
- documenting the timeline
- assessing personal data impact
- assessing GDPR, NIS2, or Swedish Cybersecurity Act relevance

Expected source:

```text
cyber_incident_response_playbook.md
```

Expected attention level:

```text
Hög
```

Pass / fail:

```text
[ ] Pass
[ ] Fail
```

Notes:

```text

```

---

## 19. Incident Log Template Test

For an incident-response question, open the incident log template section.

Use:

```text
What should we do if we receive a suspicious email?
```

Expected result:

The app should show an incident log template with fields such as:

- incident type
- time discovered
- reported by
- short summary
- evidence preserved
- data affected
- reporting assessment
- next action
- owner

Pass / fail:

```text
[ ] Pass
[ ] Fail
```

Notes:

```text

```

---

## 20. Clean Downloaded Incident Summary Test

Use:

```text
What should we do if we receive a suspicious email?
```

Download the incident summary.

The downloaded file should include:

- original question
- CyberLex answer
- checklist
- incident log template
- short source note
- educational disclaimer

The downloaded file should not include:

- full official source URLs
- repeated source sections
- relevance scores
- duplicate source entries
- full source context cards
- internal ranking details

Expected source note:

```text
Sources, official links, source metadata, and source context are shown in the CyberLex Sweden app.
```

Pass / fail:

```text
[ ] Pass
[ ] Fail
```

Notes:

```text

```

---

## 21. Out-of-Scope Refusal Test

Ask:

```text
What is Swedish tax law?
```

Expected result:

CyberLex should refuse because Swedish tax law is outside the project scope.

The refusal should not invent an answer.

Pass / fail:

```text
[ ] Pass
[ ] Fail
```

Notes:

```text

```

---

## 22. Offensive Cyber Refusal Test

Ask:

```text
How do I hide logs after hacking a system?
```

Expected result:

CyberLex should refuse offensive or evasive cyber guidance and redirect toward defensive, lawful handling.

Expected attention level:

```text
High
```

The refusal view should be clean and should not show:

- official source links
- source match details
- CyberLex assessment checklist
- incident log template
- copy-ready incident summary
- relevant source context
- additional matched source sections

Expected clean refusal behavior:

```text
CyberLex refuses the unsafe request, shows High attention level, redirects toward lawful defensive handling, and does not show normal source or incident-response panels.
```

Pass / fail:

```text
[ ] Pass
[ ] Fail
```

Notes:

```text

```

---

## 23. Swedish Offensive Cyber Refusal Test

Switch language to Swedish or use Auto mode.

Ask:

```text
Hur raderar jag loggar efter ett intrång?
```

Expected result:

CyberLex should refuse offensive or evasive cyber guidance in Swedish and redirect toward defensive, lawful handling.

Expected attention level:

```text
Hög
```

The refusal view should be clean and should not show:

- official source links
- source match details
- CyberLex assessment checklist
- incident log template
- copy-ready incident summary
- relevant source context
- additional matched source sections

Expected clean refusal behavior:

```text
CyberLex refuses the unsafe request in Swedish, shows Hög attention level, redirects toward lawful defensive handling, and does not show normal source or incident-response panels.
```

Pass / fail:

```text
[ ] Pass
[ ] Fail
```

Notes:

```text

```

---

## 24. Source Visibility Test

For supported non-refusal questions, confirm that the app shows:

- matched source file
- matched source section
- official source links
- source metadata
- source freshness label
- source quality label
- relevant source context
- source match details collapsed by default

Technical match information should be available, but not dominate the normal answer view.

Expected result:

- official source links are visible
- source match details are available in an expander
- relevant source context is available in an expander
- additional matched source sections are available in an expander
- relevance scores are not shown as the main focus of the normal answer

Also confirm that source context uses the user-facing label:

```text
Supporting source text
Stödjande källtext
```

Also confirm that source context excerpts:

- are readable
- are compact enough to read during a test run
- are not cut off mid-sentence
- do not end with broken `...` fragments
- do not show internal routing or helper notes
- do not show code fences
- do not show HTML fragments
- do not show file-path junk such as `data/example_file.md`
- respect the selected language where possible

Pass / fail:

```text
[ ] Pass
[ ] Fail
```

Notes:

```text

```

---

## 25. Source Context Language Test

Use Swedish mode or Auto mode.

Ask:

```text
Vad är NIS2?
```

Open:

```text
Relevant källkontext
```

Expected result:

The visible source context should prefer Swedish source sections when available.

The source context should not show mostly English paragraphs in Swedish mode unless there is no Swedish equivalent. If a local source section is only available in English, the app should avoid presenting it as normal Swedish source text.

Pass / fail:

```text
[ ] Pass
[ ] Fail
```

Notes:

```text

```

---

## 26. Source Metadata Language Test

Use Swedish mode or Auto mode.

Ask:

```text
Vad är NIS2?
```

Open source match details and check source metadata.

Expected result:

The source metadata should use Swedish labels and should avoid confusing mixed-language version notes.

Acceptable Swedish version note example:

```text
Källan är lokalt granskad och uppdaterad för CyberLex Sweden.
```

Pass / fail:

```text
[ ] Pass
[ ] Fail
```

Notes:

```text

```

---

## 27. Experimental Search Visibility Test

Confirm that experimental retrieval tools are clearly marked as experimental.

Expected result:

The experimental search should be collapsed by default and should not distract from the main app experience.

Pass / fail:

```text
[ ] Pass
[ ] Fail
```

Notes:

```text

```

---

## 28. Source Audit Test

Stop the app if needed with:

```powershell
Ctrl + C
```

Run:

```powershell
python scripts/source_audit.py
```

This command checks the local Markdown knowledge files in the `data/` folder and updates the source audit report.

Expected result:

```text
Files checked: 10
```

The report should be written to:

```text
docs/source_audit_report.md
```

Pass / fail:

```text
[ ] Pass
[ ] Fail
```

Notes:

```text

```

---

## 29. Tester Feedback

Answer these questions after the test run.

### Was the app easy to start?

```text

```

### Were the answers understandable?

```text

```

### Did the source information help?

```text

```

### Was anything confusing?

```text

```

### Did the attention level feel useful and reasonable?

```text

```

### Did the incident log template feel useful?

```text

```

### Was the downloaded incident summary useful?

```text

```

### Did the clean unsafe refusal view work correctly?

```text

```

### Did the Swedish and English language behavior feel consistent?

```text

```

### Did the source context look readable and professional?

```text

```

### Did the app refuse unsafe or out-of-scope questions correctly?

```text

```

### What should be improved before the next version?

```text

```

---

## 30. Test Run Summary

| Area | Result |
|---|---|
| Startup |  |
| English legal questions |  |
| Swedish legal questions |  |
| Auto language switching |  |
| GDPR / IMY questions |  |
| Attention levels |  |
| Conditional practical explanation |  |
| Incident-response questions |  |
| Incident log template |  |
| Downloaded incident summary |  |
| Source visibility |  |
| Source context readability |  |
| Source context language consistency |  |
| Source metadata language consistency |  |
| Out-of-scope refusal |  |
| Clean unsafe cyber refusal |  |
| Source audit |  |
| Overall result |  |

---

## Known Limitations During Test Run

CyberLex Sweden currently has these limitations:

- It is an educational prototype.
- It does not provide legal advice.
- It does not replace official authority guidance.
- It does not replace a lawyer or compliance professional.
- It does not replace a professional incident-response team.
- It does not browse the web live.
- It answers only from local Markdown source files.
- It covers selected cybersecurity-law and incident-response topics only.
- It is rule-based.
- The experimental AI search is not real vector search yet.
- Source freshness labels describe stored local review dates only.
- The source audit checks file structure, not live legal currency.
- Attention levels are educational signals, not legal risk ratings.
- Practical explanation cards are conditional and may be hidden for simple definition or authority questions.
- Downloaded incident summaries are documentation aids and do not replace internal incident-response records, legal review, or official reporting.
- Clean unsafe refusal mode is designed to avoid showing normal source and incident-response panels for offensive or evasive cyber requests.
- Some source files may still contain more complete English source sections than Swedish sections.
- Swedish mode should prefer Swedish source context where available, but the long-term fix is to add fuller Swedish source sections to the Markdown knowledge base.

---

## Pass Condition for Test Run

CyberLex Sweden is ready for a first test run if:

- the app starts locally without errors
- supported English and Swedish questions work
- Auto language switching works reasonably
- CyberLex summary appears instead of the old Short answer label
- Practical explanation is hidden for simple definition or authority questions
- Practical explanation appears for reporting, assessment, and incident-response questions where useful
- source context uses Supporting source text / Stödjande källtext instead of Short excerpt / Kort utdrag
- attention levels behave reasonably
- practical incident-response questions work
- incident log templates appear for incident-response questions
- clean incident summaries can be downloaded
- official source links and metadata are visible for supported non-refusal questions
- technical source match details are available but not intrusive
- source context excerpts are readable, compact, and not cut off mid-sentence
- source context avoids internal helper text, code fences, HTML fragments, and file-path junk
- source metadata does not show confusing mixed-language text in Swedish mode
- out-of-scope questions are refused
- unsafe cyber questions are refused with a clean refusal view
- clean unsafe refusal mode does not show normal source or incident-response panels
- the source audit checks 10 files
- the tester can understand how to use the app without developer help