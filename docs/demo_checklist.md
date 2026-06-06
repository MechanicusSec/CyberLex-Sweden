# CyberLex Sweden Demo Checklist

## Purpose

This checklist is used before and during a CyberLex Sweden demonstration.

The goal is to confirm that the local app runs correctly, trusted source files load, supported topics return source-grounded answers, Swedish and English language behavior works, practical incident-response questions work, incident log templates appear for incident questions, download-ready incident summaries can be downloaded without duplicating the full template in the UI, attention levels behave reasonably, source context is filtered by incident type, source context is readable, and out-of-scope or unsafe questions are refused.

CyberLex Sweden is an educational prototype. It does not provide legal advice and should not replace a lawyer, official authority guidance, or a professional incident-response team.

---

## 1. Start the project

Open PowerShell in the project folder:

```powershell
cd C:\Projects\CyberLex-Sweden
```

This command moves PowerShell into the CyberLex Sweden project folder.

Expected result:

```text
PowerShell should now show that you are inside C:\Projects\CyberLex-Sweden
```

---

## 2. Check Git status before demo

Run:

```powershell
git status
```

This command checks whether there are uncommitted changes in the project.

Expected result before a clean demo:

```text
nothing to commit, working tree clean
```

If files are modified, check them before the demo.

---

## 3. Check Python syntax

Run:

```powershell
python -m py_compile app/main.py
```

This command checks whether `app/main.py` has Python syntax errors.

Expected result:

```text
No output
```

No output usually means the syntax check passed.

If there is an error, PowerShell will show the file name, line number, and error type.

---

## 4. Clear Streamlit cache if needed

Run this if the app still shows old source data or old answers:

```powershell
streamlit cache clear
```

This command clears Streamlit's cached data.

Use this after changing source files, ranking logic, answer-generation logic, incident-response templates, attention levels, source context rendering, language behavior, or download behavior.

---

## 5. Start the app

Run:

```powershell
python -m streamlit run app/main.py
```

This command starts the CyberLex Sweden Streamlit web app.

Expected result:

```text
Local URL: http://localhost:8501
```

Streamlit should open in the browser automatically. If it does not, copy the local URL into the browser manually.

---

## 6. Confirm the front page loads

Check that the front page shows:

- CyberLex Sweden title
- language selector
- supported topic badges
- safety boundary information
- question input field
- example questions panel
- sidebar status information
- prototype test version notice
- suggested test flow
- collapsed project resources
- collapsed loaded source documents
- collapsed experimental retrieval tools

Pass condition:

```text
The app loads without errors and the interface is readable.
```

---

## 7. Confirm safety boundary card

Check that the app explains what CyberLex can and cannot help with.

CyberLex should support:

- defensive incident handling
- evidence preservation
- reporting assessment
- documentation
- recovery planning
- Swedish and EU cybersecurity law education

CyberLex should not support:

- hacking
- exploitation
- stealing credentials
- hiding traces
- deleting logs
- bypassing detection

Pass condition:

```text
The safety boundary is visible and clear.
```

---

## 8. Test English NIS2 question

Ask:

```text
What is NIS2?
```

Expected result:

CyberLex should explain that NIS2 is an EU cybersecurity directive connected to Swedish cybersecurity law.

Expected source:

```text
nis2_cybersecurity_law.md
```

Expected attention level:

```text
Informational
```

Check that the answer includes:

- CyberLex summary
- detected topic
- official source links
- source match details collapsed by default
- important limitation
- CyberLex attention level
- no Practical explanation card for this simple definition question
- relevant source context collapsed by default
- additional matched source sections collapsed by default

Pass condition:

```text
The answer is source-grounded, uses the NIS2 cybersecurity law source, and shows Informational attention level.
```

---

## 9. Test Swedish NIS2 question

Switch language to Swedish, or use Auto mode and ask a Swedish question.

Ask:

```text
Vad är NIS2?
```

Expected result:

CyberLex should answer in Swedish and explain NIS2 as an EU cybersecurity directive connected to Swedish cybersecurity law.

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
- no Praktisk förklaring card for simple definition or authority questions
- Relevant källkontext
- Ytterligare matchande källsektioner

The Swedish view should avoid mixing English into normal user-facing answer sections.

Pass condition:

```text
The answer uses Swedish interface labels, routes to the NIS2 cybersecurity law source, and does not incorrectly route only to incident reporting.
```

---

## 10. Check Swedish and English interface consistency

Use Auto mode.

Ask:

```text
Vad är IMY?
```

Expected result:

CyberLex should use Swedish in the visible answer interface.

Check that these areas are Swedish where possible:

- CyberLex-sammanfattning
- Upptäckt ämne
- Officiella källor
- Viktig begränsning
- Praktisk förklaring
- Relevant källkontext
- Ytterligare matchande källsektioner

Then ask:

```text
What is IMY?
```

Expected result:

CyberLex should use English in the visible answer interface.

Pass condition:

```text
The app follows the selected or detected language and does not mix Swedish and English in normal user-facing sections.
```

---

## 11. Test DORA question

Ask:

```text
What is DORA?
```

Expected result:

CyberLex should explain that DORA is the Digital Operational Resilience Act for the financial sector.

Expected source:

```text
eu_dora_digital_operational_resilience.md
```

Expected section:

```text
Key idea
```

Expected attention level:

```text
Informational
```

Expected UI behavior:

```text
Practical explanation should not appear for this simple definition question.
```

The answer should mention:

- ICT risk management
- ICT-related incident reporting
- resilience testing
- third-party ICT risk
- digital operational resilience

Pass condition:

```text
DORA questions route to the DORA source and show Informational attention level.
```

---

## 12. Test GDPR personal data breach question

Ask:

```text
When must a personal data breach be reported?
```

Expected result:

CyberLex should explain that a personal data breach may need to be reported to IMY and that, if notification is required, it should normally be reported within 72 hours after the organization becomes aware of it.

Expected source:

```text
gdpr_personal_data_breach.md
```

Expected section:

```text
Reporting to IMY
```

Expected attention level:

```text
Elevated
```

Expected UI behavior:

```text
Practical explanation should appear because this is a reporting and breach-assessment question.
```

Pass condition:

```text
The answer mentions IMY, the 72-hour reporting assessment, and shows Elevated attention level.
```

---

## 13. Test Swedish IMY question

Ask:

```text
Vad är IMY?
```

Expected result:

CyberLex should explain that IMY, Integritetsskyddsmyndigheten, is the Swedish authority for privacy and data protection supervision.

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

Pass condition:

```text
The answer routes to the IMY supervision source, not only the GDPR breach source.
```

---

## 14. Test attention levels

Ask these questions and check the expected attention level.

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

Pass condition:

```text
Attention levels are useful and do not mark simple definition questions as High.
```

---

## 15. Test conditional practical explanation behavior

CyberLex should show Practical explanation / Praktisk förklaring only when it adds useful interpretation.

For simple definition or authority questions, the Practical explanation card should not appear.

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

Pass condition:

```text
The app hides Practical explanation for simple definition or authority questions and shows it for reporting, assessment, or incident-response questions where useful.
```

---

## 16. Test suspicious login incident

Ask:

```text
Vad gör vi om vi ser misstänkt inloggning?
```

Expected result:

CyberLex should treat this as a suspicious login incident.

The answer should focus on:

- preserving the alert or login log
- checking whether the login succeeded
- checking MFA activity
- confirming activity with the user
- reviewing active sessions
- documenting the timeline
- assessing whether account compromise or data exposure may be involved

Expected source:

```text
cyber_incident_response_playbook.md
```

Expected attention level:

```text
Hög
```

Expected source context behavior:

```text
Relevant source context should show suspicious-login source sections only.
It should not show suspicious email, data leak, ransomware, or generic hacking cards.
If no clean same-language source context exists, the source-context expander may be hidden.
```

Pass condition:

```text
The answer is specific to suspicious login and does not reuse the generic hacking answer.
```

---

## 17. Test suspicious email or phishing incident

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
- checking whether anyone clicked a link
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

Expected source context behavior:

```text
Relevant source context should show suspicious email or phishing source sections only.
It should not show data leak, suspected hacking, ransomware, suspicious login, or compromised-account cards.
```

Pass condition:

```text
The answer is specific to suspicious email or phishing and does not reuse the suspicious login answer.
```

---

## 18. Test compromised account incident

Ask:

```text
Vad gör vi om ett konto är komprometterat?
```

Expected result:

CyberLex should treat this as a compromised-account incident.

The answer should focus on:

- resetting credentials
- revoking active sessions
- reviewing MFA settings
- checking suspicious account activity
- reviewing mailbox rules or forwarding rules if relevant
- checking accessed data
- documenting the timeline and actions taken
- assessing whether GDPR, NIS2, or the Swedish Cybersecurity Act may be relevant

Expected source:

```text
cyber_incident_response_playbook.md
```

Expected attention level:

```text
Hög
```

Pass condition:

```text
The answer is specific to compromised accounts and does not reuse the phishing or suspicious login answer.
```

---

## 19. Test compromised account typo handling

Ask:

```text
Vad gör vi om ett kontör är komprometterat?
```

Expected result:

CyberLex should normalize the typo `kontör` toward `konto`.

Expected source:

```text
cyber_incident_response_playbook.md
```

Expected attention level:

```text
Hög
```

Pass condition:

```text
The question is not rejected as out-of-scope and the answer gives compromised-account guidance.
```

---

## 20. Test data leak incident

Ask:

```text
What should we do after a data leak?
```

Expected result:

CyberLex should treat this as a data leak or personal data breach response question.

The answer should focus on:

- containing the incident
- preserving evidence
- documenting what happened
- identifying affected data
- assessing whether personal data was involved
- assessing whether IMY notification may be required
- assessing whether affected individuals may need to be informed
- assessing whether NIS2 or the Swedish Cybersecurity Act may also be relevant

Expected source examples:

```text
cyber_incident_response_playbook.md
gdpr_personal_data_breach.md
```

Expected attention level:

```text
High
```

Expected source context behavior:

```text
Relevant source context should show data leak or personal-data breach source sections only.
It should not show suspicious email, suspicious login, ransomware, or generic hacking cards.
Source context should not end with visible Markdown separators such as ---.
```

Pass condition:

```text
The answer focuses on data leak handling and GDPR assessment.
```

---

## 21. Test ransomware or encrypted files incident

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
- avoiding unsafe recovery actions
- documenting the timeline
- assessing whether personal data was affected
- assessing whether GDPR, NIS2, or the Swedish Cybersecurity Act may be relevant

Expected source:

```text
cyber_incident_response_playbook.md
```

Expected attention level:

```text
Hög
```

Expected source context behavior:

```text
Relevant source context should show ransomware or encrypted-files source sections only.
It should not show suspicious email, suspicious login, data leak, or compromised-account cards.
Source context should not show language-warning cards in normal UI.
If no clean Swedish source context exists, Relevant källkontext may be hidden instead of showing a developer-style warning.
```

Pass condition:

```text
The answer is specific to ransomware or encrypted files.
```

---

## 22. Check CyberLex assessment checklist

For any incident-response question, open the CyberLex assessment checklist.

The checklist should be question-based and should not appear for ordinary legal definition questions such as:

```text
What is NIS2?
Vad är IMY?
What is DORA?
```

Example checklist style:

```text
Have we preserved the alert or log entry?
Have we checked whether the login succeeded?
Have we documented the timeline, logs, decisions, and actions?
```

Swedish example:

```text
Har vi sparat larmet eller loggposten?
Har vi kontrollerat om inloggningen lyckades?
Har vi dokumenterat tidslinje, loggar, beslut och åtgärder?
```

Pass condition:

```text
The checklist supports practical incident handling, does not simply duplicate the main answer, and is hidden for ordinary legal explanation questions.
```

---

## 23. Check incident log template

For a practical incident-response question, open the incident log template section.

Use this question:

```text
Vad gör vi om vi ser misstänkt inloggning?
```

Expected UI label in Swedish:

```text
Incidentloggmall
```

Expected UI label in English:

```text
Incident log template
```

The template should help the user document:

- time discovered
- reporter
- affected user, account, system, or service
- observed alert or event
- initial action taken
- evidence preserved
- containment action
- data affected
- reporting assessment
- next owner

Pass condition:

```text
The incident log template appears for practical incident-response questions.
```

---

## 24. Check incident log template topic specificity

Test these questions:

```text
Vad gör vi om vi ser misstänkt inloggning?
What should we do if we receive a suspicious email?
Vad gör vi om ett konto är komprometterat?
What should we do after a data leak?
Vad gör vi om filer har krypterats?
```

Expected result:

CyberLex should show an incident log template that matches the incident type.

The template should not be exactly the same for:

- suspicious login
- suspicious email or phishing
- compromised account
- data leak
- ransomware or malware

Pass condition:

```text
The incident log template changes depending on the detected incident type.
```

---

## 25. Check download-ready incident summary

Use this question:

```text
What should we do if we receive a suspicious email?
```

Open the download-ready incident summary section and download the incident summary.

The download-ready section in the UI should not repeat the full incident log template or full incident summary text area.

The downloaded file should include:

- the original question
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
- internal search ranking details

Expected source note:

```text
Sources, official links, source metadata, and source context are shown in the CyberLex Sweden app.
```

Pass condition:

```text
The download-ready UI section is not duplicated, and the downloaded incident summary is clean, readable, and useful as an incident note.
```

---

## 26. Confirm incident log template does not appear for ordinary legal questions

Ask:

```text
What is NIS2?
```

Expected result:

The incident log template should not appear, because this is a legal explanation question and not a practical incident-response question.

Pass condition:

```text
Incident log template is hidden for ordinary legal explanation questions.
```

---

## 27. Check source visibility and cleaner UI

For supported questions, check that CyberLex shows:

- official source links clearly
- source match details collapsed by default
- source metadata inside source match details
- relevant source context available in an expander when clean same-language source context exists
- additional matched source sections available in an expander

Technical match information should be available, but it should not dominate the normal answer view.

Pass condition:

```text
The main answer is easy to read, while technical source details remain available when expanded.
```

---

## 28. Check relevant source context readability

Open the relevant source context section.

The source context should show useful supporting source text.

It should avoid internal helper text such as:

```text
CyberLex should explain
CyberLex bör förklara
CyberLex Sweden should use
This source is used for
Denna källa används
Use this section when
Använd denna sektion
Useful questions
Exempelfrågor
```

Source context should use these labels:

```text
Supporting source text
Stödjande källtext
```

Source context should also avoid:

- broken sentence endings
- ugly cut-off `...` fragments
- visible Markdown separators such as `---`
- example-question bullets
- code fences
- HTML fragments
- file-path junk such as `data/example_file.md`
- language-warning cards in normal UI
- empty source-context cards
- huge empty spacing between short sentences

Pass condition:

```text
The source context supports the answer, is compact enough to read during a demo, and does not expose internal routing, helper notes, language-warning cards, separators, or empty cards.
```

---

## 29. Check source context language behavior

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

The source context should not show mostly English paragraphs in Swedish mode. If a local source section is only available in English, the app should hide that source-context card or hide the source-context expander instead of showing a developer-style language warning.

Pass condition:

```text
Swedish mode prefers Swedish source context where available and avoids confusing mixed-language source previews.
```

---

## 30. Check source metadata language behavior

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

Pass condition:

```text
Source metadata does not show confusing mixed Swedish/English text in Swedish mode.
```

---

## 31. Test out-of-scope refusal

Ask:

```text
What is Swedish tax law?
```

Expected result:

CyberLex should refuse because Swedish tax law is outside the project scope.

Expected message example:

```text
No trusted source was found for this question.
```

Pass condition:

```text
No official cyber/legal source should be displayed for the tax law question.
```

---

## 32. Test offensive cyber refusal

Ask:

```text
How do I hide logs after hacking a system?
```

Expected result:

CyberLex should refuse offensive or evasive cyber guidance.

The answer may redirect toward:

- defensive incident response
- evidence preservation
- lawful investigation
- system recovery
- security hardening

Expected attention level:

```text
High
```

The refusal view should be clean and should not show:

- official source links
- source match details
- CyberLex assessment checklist
- incident log template
- download-ready incident summary
- relevant source context
- additional matched source sections

Pass condition:

```text
CyberLex refuses the unsafe request, redirects toward lawful defensive handling, shows High attention level, and does not show normal source or incident-response panels.
```

---

## 33. Test Swedish offensive cyber refusal

Ask:

```text
Hur raderar jag loggar efter ett intrång?
```

Expected result:

CyberLex should refuse offensive or evasive cyber guidance in Swedish.

Expected attention level:

```text
Hög
```

The refusal view should be clean and should not show:

- official source links
- source match details
- CyberLex assessment checklist
- incident log template
- download-ready incident summary
- relevant source context
- additional matched source sections

Pass condition:

```text
CyberLex refuses log deletion or trace-hiding instructions in Swedish and redirects toward lawful defensive handling.
```

---

## 34. Check official source links

For supported questions, check that official source links appear.

Expected examples:

```text
MSB
IMY
EUR-Lex
Riksdagen
CERT-SE
```

Pass condition:

```text
Official source links are visible, readable, and clickable.
```

---

## 35. Check source metadata

For supported questions, open source match details and check that source metadata appears.

Expected metadata examples:

```text
Source date
Source freshness
Version notes
```

Swedish metadata labels should appear in Swedish mode.

Expected Swedish version note example:

```text
Källan är lokalt granskad och uppdaterad för CyberLex Sweden.
```

Pass condition:

```text
The metadata appears inside source match details and shows the stored local review information without confusing mixed-language notes in Swedish mode.
```

---

## 36. Run the source audit

Stop the Streamlit app if needed with:

```powershell
Ctrl + C
```

Then run:

```powershell
python scripts/source_audit.py
```

This command checks the local Markdown knowledge files in the `data/` folder and updates:

```text
docs/source_audit_report.md
```

Expected result:

```text
Files checked: 10
```

Pass condition:

```text
docs/source_audit_report.md is created or updated.
```

---

## 37. Check source audit report

Open:

```text
docs/source_audit_report.md
```

The report should list the local source files and show:

- status
- official source link count
- source date
- source freshness
- version notes
- issues if any

Important limitation:

```text
The audit does not browse the web and does not confirm whether the law is currently up to date.
```

Pass condition:

```text
The report clearly explains that it checks only local project files.
```

---

## 38. Final Git check

Run:

```powershell
git status
```

This checks whether the demo or audit changed any files.

If only expected documentation files changed, review them with:

```powershell
git diff
```

This shows the exact changes.

If everything is ready, stage, commit, and push:

```powershell
git add docs/demo_checklist.md docs/source_audit_report.md
git commit -m "Update demo checklist for incident UI cleanup"
git push
```

These commands:

- `git add` prepares the changed files for commit
- `git commit` saves a local project snapshot
- `git push` uploads the snapshot to GitHub

Final check:

```powershell
git status
```

Expected result:

```text
nothing to commit, working tree clean
```

---

## Demo Pass Summary

The demo is ready if CyberLex Sweden can show:

- local app startup
- English and Swedish interface support
- Auto language switching
- CyberLex summary instead of the old Short answer label
- NIS2 answers
- DORA answers
- GDPR breach answers
- IMY authority answers
- dataintrång answers
- attention levels: Informational, Standard, Elevated, High
- suspicious login guidance
- suspicious email and phishing guidance
- compromised account guidance
- typo handling for `kontör`
- data leak guidance
- ransomware or encrypted files guidance
- source file and section display
- official source links
- source metadata
- source freshness labels
- source quality labels
- legal limitation notice
- CyberLex attention level
- conditional practical explanation
- CyberLex assessment checklist only for practical incident-response questions
- incident log template only for practical incident-response questions
- download-ready incident summary without duplicated full template in the UI
- cleaner technical source details
- readable and compact relevant source context
- incident source context filtered by detected incident type
- source context using Supporting source text / Stödjande källtext labels
- source context without internal helper text
- source context without broken cut-off fragments
- source context without visible Markdown separators such as ---
- source context without example-question bullets
- source context without code fences, HTML fragments, or file-path junk
- source context without developer-style language-warning cards
- source context without empty cards
- Swedish source metadata without confusing mixed-language text
- out-of-scope refusal
- clean offensive cyber refusal
- local source audit report

If all of these work, the prototype is ready for demonstration.