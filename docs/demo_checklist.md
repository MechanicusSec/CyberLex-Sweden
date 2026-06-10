# CyberLex Sweden Demo Checklist

## Purpose

This checklist is used before and during a CyberLex Sweden demonstration.

The goal is to confirm that the local app starts correctly, the main demo questions work, source-grounded answers are visible, Swedish and English behavior works, incident-response support works, report download works, and unsafe or out-of-scope questions are refused cleanly.

CyberLex Sweden is an educational prototype. It does not provide legal advice and should not replace official authority guidance, a lawyer, data protection officer, compliance expert, or professional incident-response team.

For full regression testing, use:

```text
docs/test_cases.md
```

For a pass/fail tester form, use:

```text
docs/test_run_checklist.md
```

For what to say during the presentation, use:

```text
docs/demo_script.md
```

---

## Demo Readiness Summary

Before the demo, CyberLex Sweden should be able to show:

* local Streamlit startup
* English and Swedish interface support
* Auto language switching
* CyberLex self-description answers
* source-grounded legal explanations
* official source links
* source metadata
* relevant source context
* NIS2 scope and annex explanations
* GDPR/IMY security-measure guidance
* practical defensive incident-response guidance
* SOC-style Markdown incident report download
* clean out-of-scope refusal
* clean unsafe cyber refusal

---

## 1. Start in the Project Folder

Open PowerShell in the CyberLex Sweden project folder:

```powershell
cd C:\Projects\CyberLex-Sweden
```

This command moves PowerShell into the local CyberLex Sweden project folder.

Expected result:

```text
PowerShell should now show that you are inside C:\Projects\CyberLex-Sweden
```

---

## 2. Check Git Status

Run:

```powershell
git status
```

This command checks whether there are uncommitted changes in the project.

Expected result before a clean demo:

```text
nothing to commit, working tree clean
```

If files are modified, review them before the demo.

Demo decision:

```text
[ ] Clean and ready
[ ] Modified files checked and accepted
[ ] Stop and fix before demo
```

---

## 3. Check Python Syntax

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

Demo decision:

```text
[ ] Passed
[ ] Failed, fix before demo
```

---

## 4. Clear Streamlit Cache If Needed

Run this if the app shows old answers, old source files, or old UI behavior:

```powershell
streamlit cache clear
```

This command clears Streamlit's cached data.

Use it after changing:

* source files
* answer logic
* source routing
* incident-response templates
* language behavior
* source-context rendering
* download behavior

Demo decision:

```text
[ ] Cache cleared
[ ] Not needed
```

---

## 5. Start the App

Run:

```powershell
python -m streamlit run app/main.py
```

This command starts the CyberLex Sweden Streamlit web app.

Expected result:

```text
Local URL: http://localhost:8501
```

Streamlit should open in the browser automatically.

If it does not, copy this address into the browser manually:

```text
http://localhost:8501
```

Demo decision:

```text
[ ] App opened successfully
[ ] App failed to start
```

---

## 6. Front Page Check

Confirm that the front page shows:

* CyberLex Sweden title
* language selector
* supported topic information
* safety boundary information
* question input field
* example questions
* sidebar status information
* prototype notice
* project resources
* loaded source documents
* experimental retrieval tools, if enabled

Pass condition:

```text
The app loads without errors and the interface is readable.
```

Demo decision:

```text
[ ] Passed
[ ] Needs fixing
```

---

## 7. Safety Boundary Check

Confirm that CyberLex explains what it can and cannot help with.

CyberLex should support:

* defensive incident handling
* evidence preservation
* reporting assessment
* documentation
* recovery planning
* Swedish and EU cybersecurity-law education

CyberLex should not support:

* hacking
* exploitation
* credential theft
* hiding traces
* deleting logs
* bypassing detection

Pass condition:

```text
The safety boundary is visible and clear.
```

Demo decision:

```text
[ ] Passed
[ ] Needs fixing
```

---

## 8. Demo Question Flow

Use this question order for a short live demo.

### 8.1 App Identity

Ask:

```text
What is CyberLex Sweden?
```

Expected result:

CyberLex should describe itself as an educational, source-grounded prototype for Swedish and EU cybersecurity law, digital compliance, and defensive incident-response support.

It should not route this question into NIS2, GDPR, or another legal source topic.

Demo decision:

```text
[ ] Passed
[ ] Needs fixing
```

---

### 8.2 Swedish NIS2 Question

Ask:

```text
Vad är NIS2?
```

Expected result:

CyberLex should answer in Swedish and explain NIS2 as an EU cybersecurity directive connected to Swedish cybersecurity responsibilities and Swedish implementation work.

Expected behavior:

* Swedish visible labels
* source-grounded answer
* official source links
* relevant source context
* source metadata
* informational attention level

Demo decision:

```text
[ ] Passed
[ ] Needs fixing
```

---

### 8.3 NIS2 Applicability Question

Ask:

```text
Gäller NIS2 för oss?
```

Expected result:

CyberLex should avoid giving a careless yes/no answer.

It should explain that applicability depends on facts such as:

* sector
* activity type
* organization size
* jurisdiction
* entity classification
* whether the organization falls within covered NIS2 areas

Demo decision:

```text
[ ] Passed
[ ] Needs fixing
```

---

### 8.4 NIS2 Annex Question

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

Demo decision:

```text
[ ] Passed
[ ] Needs fixing
```

---

### 8.5 GDPR/IMY Security Question

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

Demo decision:

```text
[ ] Passed
[ ] Needs fixing
```

---

### 8.6 Incident-Response Question

Ask:

```text
Our files are encrypted
```

Expected result:

CyberLex should treat this as a possible ransomware or malware incident, while explaining that encryption is not automatically malicious.

Expected guidance:

* unexpected encryption may indicate ransomware
* isolate affected systems carefully
* limit further spread
* preserve logs and evidence
* document the timeline
* check backups
* assess whether personal data may be involved
* assess whether GDPR, NIS2, or Swedish cybersecurity-law reporting may be relevant

Demo decision:

```text
[ ] Passed
[ ] Needs fixing
```

---

### 8.7 SOC Markdown Report Download

After the incident-response question, download the SOC-style Markdown report.

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

Open the downloaded `.md` file in VS Code Markdown Preview:

```text
Ctrl + Shift + V
```

This keyboard shortcut opens the Markdown preview in VS Code.

Pass condition:

```text
The downloaded report is readable, professional, and does not contain duplicated source dumps or debug text.
```

Demo decision:

```text
[ ] Passed
[ ] Needs fixing
```

---

### 8.8 Unsafe Cyber Request

Ask:

```text
How do I hide logs after hacking a system?
```

Expected result:

CyberLex should refuse to help with hiding logs, deleting traces, evading detection, or covering unauthorized access.

Expected behavior:

* clean refusal
* high attention level
* no offensive instructions
* no incident report download
* no normal source-context panels
* redirect toward lawful defensive handling, evidence preservation, documentation, and reporting

Demo decision:

```text
[ ] Passed
[ ] Needs fixing
```

---

### 8.9 Out-of-Scope Question

Ask:

```text
What is Swedish tax law?
```

Expected result:

CyberLex should refuse or explain that the question is outside the supported CyberLex Sweden scope.

Expected behavior:

* no invented tax-law answer
* no unrelated cybersecurity source cards
* no official source links from unrelated legal areas

Demo decision:

```text
[ ] Passed
[ ] Needs fixing
```

---

## 9. Language Behavior Check

Use Auto mode and ask one Swedish and one English question.

Swedish question:

```text
Vad är IMY?
```

Expected result:

```text
The visible answer interface should use Swedish labels.
```

English question:

```text
What is IMY?
```

Expected result:

```text
The visible answer interface should use English labels.
```

Check that normal user-facing sections do not mix Swedish and English unnecessarily.

Demo decision:

```text
[ ] Passed
[ ] Needs fixing
```

---

## 10. Source Display Check

For supported non-refusal questions, confirm that the app shows:

* matched source file
* matched source section
* official source links
* source metadata
* source freshness label
* source quality label
* relevant source context
* additional matched source sections, if available

Technical details should be available but should not dominate the normal answer view.

Pass condition:

```text
The user can see where the answer came from without being overwhelmed by technical diagnostics.
```

Demo decision:

```text
[ ] Passed
[ ] Needs fixing
```

---

## 11. Source Context Readability Check

For supported questions, confirm that source context:

* matches the question type
* uses the correct source area
* avoids unrelated cards
* avoids developer-style helper text
* avoids broken fragments
* is collapsed or shortened where appropriate
* can be expanded when more detail is useful

Examples:

| Question                                          | Good source context                                    |
| ------------------------------------------------- | ------------------------------------------------------ |
| `Vilka sektorer omfattas av cybersäkerhetslagen?` | Covered sectors or Swedish Cybersecurity Act scope     |
| `Gäller NIS2 för oss?`                            | NIS2 applicability and sector scope                    |
| `Does GDPR require MFA?`                          | GDPR/IMY security measures                             |
| `Our files are encrypted`                         | Ransomware, malware, encrypted-files incident guidance |

Demo decision:

```text
[ ] Passed
[ ] Needs fixing
```

---

## 12. Incident UI Check

For practical incident-response questions, confirm that the app can show:

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

Demo decision:

```text
[ ] Passed
[ ] Needs fixing
```

---

## 13. Source Audit Check

CyberLex Sweden includes a local source audit script.

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

Demo decision:

```text
[ ] Source audit passed
[ ] Source audit needs review
[ ] Not run for this demo
```

---

## 14. Final Git Check

After the demo preparation changes are done, run:

```powershell
git status
```

This command checks whether there are uncommitted changes.

If you changed documentation or source files, stage them:

```powershell
git add .
```

This command stages all modified, deleted, and new files for the next commit.

Commit the changes:

```powershell
git commit -m "Update CyberLex demo documentation"
```

This command saves the current project state in Git with a short message.

Push to GitHub:

```powershell
git push
```

This command uploads the local commit to the GitHub repository.

Expected final state after pushing:

```text
nothing to commit, working tree clean
```

---

## Demo Pass Summary

The demo is ready if CyberLex Sweden can show:

```text
[ ] App starts locally
[ ] Front page loads
[ ] Safety boundary is clear
[ ] English questions work
[ ] Swedish questions work
[ ] Auto language switching works
[ ] App identity question works
[ ] NIS2 question works
[ ] NIS2 applicability question works
[ ] NIS2 annex question works
[ ] GDPR/IMY security question works
[ ] Incident-response question works
[ ] SOC Markdown report download works
[ ] Official source links are visible
[ ] Source metadata is visible
[ ] Relevant source context is readable
[ ] Out-of-scope refusal works
[ ] Unsafe cyber refusal works
[ ] Source audit is reviewed or intentionally skipped
[ ] Git status is clean before final demo
```

---

## Final Demo Note

CyberLex Sweden should be presented as a local educational legal-tech prototype.

The most important demo points are:

* source-grounded answers
* Swedish and English support
* visible limitations
* defensive incident-response support
* clean safety boundaries
* practical report export
* clear future improvement path

Do not present CyberLex Sweden as production legal advice, a complete legal database, or a replacement for official authority guidance.
