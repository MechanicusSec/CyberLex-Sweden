# CyberLex Sweden

CyberLex Sweden is a final school project and educational legal-tech prototype focused on Swedish and EU cybersecurity law, cyber incident response, GDPR, NIS2, DORA, the Cyber Resilience Act, cybercrime, data protection, and digital compliance.

The project works as a local AI-style assistant that helps users search selected cybersecurity-law and incident-response topics through a trusted local Markdown knowledge base. It uses source-based search, source routing, structured CyberLex summary answers, official source links, source metadata, source freshness labels, topic labels, CyberLex attention levels, practical explanations, incident-response checklists, cleaned relevant source context, cleaner collapsed source details, Swedish/English interface handling, and an experimental retrieval panel.

CyberLex Sweden does **not** provide legal advice. It is built for learning, demonstration, and portfolio use.

---

## Project Purpose

Cybersecurity law and incident response can be difficult to understand because relevant information is spread across many different sources, including:

- Swedish law
- EU regulations and directives
- Swedish government agencies
- cybersecurity authorities
- data protection authorities
- financial-sector cybersecurity rules
- product cybersecurity rules
- incident reporting guidance
- practical security-response procedures

CyberLex Sweden explores how a focused, source-grounded assistant can help users find relevant cybersecurity-law and incident-response information in a safer and more transparent way.

The main design goal is simple:

```text
Better sources first. Better AI second.
```

The prototype should show where an answer comes from, what source section was matched, what practical steps may be relevant, and what limitations apply.

---

## Current Prototype Status

CyberLex Sweden currently runs as a local Streamlit application.

The current version is a source-grounded, rule-based prototype. It does not yet use a full language model, live web browsing, or production vector search.

Completed major improvements include:

- Local Markdown knowledge base
- Source-based search and chunk ranking
- Source routing for supported legal and incident-response topics
- English and Swedish interface support
- Auto language switching improvements
- Swedish retrieval improvements
- Swedish metadata display cleanup
- Structured CyberLex summary cards
- Source match details
- Official source links
- Source metadata display
- Source quality labels
- Source freshness labels
- Source match confidence labels
- Detected topic labels
- CyberLex attention levels: Informational, Standard, Elevated, and High
- Cleaner test-run interface
- Collapsed sidebar project resources and loaded source documents
- Collapsed experimental retrieval tools
- Cleaner source match details for normal users
- Practical explanation cards
- Topic-based assessment checklists for practical incident-response questions
- Cleaned relevant source context cards
- Additional matched source section cards
- Source context cleanup to avoid internal helper text, broken cut-off fragments, code fences, HTML fragments, and file-path junk
- Example question panel
- Practical incident-response guidance
- Incident log templates for practical incident-response questions
- Copy-ready incident summaries
- Clean downloadable incident summary files
- Defensive cyber safety boundary
- Out-of-scope refusal handling
- Offensive cyber request refusal
- Experimental AI search sidebar
- Local source audit script
- Weekly GitHub Actions source audit workflow
- Manual test documentation
- Demo checklist documentation
- Practical test-run checklist documentation
- Product roadmap
- Technical design documentation
- Source update history

Vector search was investigated and documented, but the implementation is paused for now because the local Python/package setup needs a stable Python version for AI dependencies.

---

## Supported Topics

CyberLex Sweden currently focuses on selected Swedish and EU cybersecurity-law topics and defensive cyber incident-response topics.

Supported legal and compliance areas include:

- GDPR and personal data breach notification in Sweden
- IMY and Swedish GDPR supervision
- GDPR core principles
- NIS2 and the Swedish Cybersecurity Act
- NIS2 incident reporting
- Swedish cybercrime law and dataintrång
- EU attacks against information systems
- EU Cyber Resilience Act
- EU DORA, the Digital Operational Resilience Act
- Digital compliance and cybersecurity-related legal topics

Supported practical incident-response areas include:

- Suspected hacking or intrusion
- Suspicious login activity
- Suspicious email and phishing
- Compromised accounts
- Data leaks
- Personal data breach response
- Ransomware and malware
- Encrypted files
- Evidence preservation
- Incident documentation
- Reporting assessment
- Recovery planning

Out-of-scope questions, such as Swedish tax law, should be refused by the application.

Unsafe cyber requests, such as hacking, stealing credentials, hiding logs, deleting traces, or bypassing detection, should also be refused or redirected toward defensive guidance.

---

## Safety Boundary

CyberLex Sweden is designed for defensive, educational, and compliance-oriented use.

CyberLex Sweden can help with:

- Understanding selected cybersecurity-law topics
- Understanding selected EU cybersecurity regulations and directives
- Defensive incident-response steps
- Evidence preservation
- Documentation and timeline building
- GDPR/IMY reporting assessment
- NIS2 and Swedish Cybersecurity Act reporting assessment
- Recovery planning
- Source-grounded learning

CyberLex Sweden must not help with:

- Hacking systems
- Exploiting vulnerabilities
- Stealing credentials
- Hiding traces
- Deleting logs
- Bypassing detection
- Evading investigation
- Performing unauthorized access

This boundary is part of the project design.

---

## Knowledge Base Sources

The local knowledge base is stored in the `data/` folder.

Current source files:

```text
data/cybercrime_dataintrang.md
data/cyber_incident_response_playbook.md
data/eu_attacks_against_information_systems.md
data/eu_cyber_resilience_act.md
data/eu_dora_digital_operational_resilience.md
data/gdpr_core_principles.md
data/gdpr_personal_data_breach.md
data/imy_gdpr_supervision.md
data/nis2_cybersecurity_law.md
data/nis2_incident_reporting.md
```

Each knowledge file is designed to include:

- topic
- main authority or legal source
- key idea
- important points
- practical explanation or checklist where useful
- cybersecurity connection
- useful questions
- official source links
- source metadata
- disclaimer

The application does not browse the web live when answering. It answers only from the local trusted source files.

---

## Current Features

The current prototype can:

- load local Markdown knowledge base files
- split source documents into searchable chunks
- match user questions to relevant source sections
- route specific questions to the most relevant source file
- generate simple source-based CyberLex summary answers
- display structured source match details
- display the matched source file and section
- display official source links connected to the matched file
- display source metadata, including source date and version notes
- simplify Swedish source metadata so confusing mixed-language version notes are not shown in the Swedish UI
- display source quality labels
- display source freshness labels
- display source match confidence
- display detected topic labels
- show CyberLex attention levels for different question types
- use calmer attention levels for ordinary legal explanation questions
- keep technical source match details available but collapsed by default
- keep project resources and loaded source documents available but collapsed in the sidebar
- show matched source excerpts and supporting source context
- clean source context so internal helper notes, code fences, HTML fragments, and file-path junk do not appear in normal user-facing excerpts
- keep source context excerpts compact and avoid broken mid-sentence cut-offs
- show practical explanations
- show topic-based assessment checklists for practical incident-response questions
- show other matching source sections
- support English and Swedish interface labels
- improve Auto language behavior so Swedish questions can switch visible answer sections to Swedish
- provide example questions
- handle practical incident-response questions
- display incident log templates for practical incident-response questions
- generate copy-ready incident summaries
- download clean incident summary files for use as incident notes or ticket attachments
- distinguish suspicious login, phishing, compromised account, data leak, and ransomware questions
- normalize some Swedish typo variants, such as `kontör` toward `konto`
- refuse out-of-scope questions
- refuse or redirect unsafe offensive cyber requests
- display legal disclaimers
- run a local source audit
- run a weekly GitHub Actions source audit workflow

---

## Test-Run Readiness

CyberLex Sweden has been cleaned up for a first practical test run.

The test-run interface is designed to keep the normal user view readable while still preserving transparency. Main answers now use the **CyberLex summary** label instead of the older **Short answer** wording. Detected topics, official source links, limitations, attention levels, and practical explanations are shown clearly. More technical details, such as source match details, source metadata, relevant source context, additional matched sections, sidebar project resources, loaded source documents, and experimental retrieval tools, remain available but are collapsed by default.

Recent test-run cleanup focused on language consistency and source-context readability. Swedish questions should use Swedish visible answer labels where possible, Auto mode should follow the detected question language more consistently, source metadata should avoid confusing mixed-language notes in Swedish mode, and source context cards should avoid internal helper text, broken cut-off fragments, code fences, HTML fragments, and file-path junk.

CyberLex attention levels are used as educational signals, not legal risk ratings:

| Attention level | Intended use |
|---|---|
| Informational | Basic legal or authority explanation questions, such as `What is NIS2?`, `What is DORA?`, or `Vad är IMY?` |
| Standard | General legal or compliance questions that need source-grounded explanation but are not urgent incident-response questions |
| Elevated | Reporting, breach assessment, GDPR/NIS2 overlap, and regulatory-duty questions |
| High | Practical incident-response questions and unsafe/offensive cyber requests that must be refused or redirected |

The practical test-run checklist is stored in:

```text
docs/test_run_checklist.md
```

This checklist is intended to help another tester run the prototype without needing developer guidance.

---

## Practical Incident Response Support

CyberLex Sweden includes a practical incident-response playbook for defensive guidance.

The playbook supports questions such as:

```text
What should I do if I suspect hacking?
What should we do after suspicious login activity?
What should we do if we receive a suspicious email?
What should we do if an account is compromised?
What should we do after a data leak?
What should we do if files are encrypted by ransomware?
Vad ska jag göra om jag misstänker intrång?
Vad gör vi om vi ser misstänkt inloggning?
Vad gör vi vid misstänkt mejl?
Vad gör vi om ett konto är komprometterat?
Vad gör vi om ett kontör är komprometterat?
Vad gör vi efter en dataläcka?
Vad gör vi om filer har krypterats?
```

The app should provide practical first steps, such as:

- preserve alerts, logs, and evidence
- avoid unsafe actions that destroy evidence
- contain the incident
- check affected accounts, systems, and data
- document the timeline
- assess whether personal data was involved
- assess whether GDPR/IMY reporting may be relevant
- assess whether NIS2 or the Swedish Cybersecurity Act may be relevant
- escalate to internal security teams, CERT-SE, legal, or official authorities when appropriate

CyberLex Sweden can also generate a clean downloadable incident summary for practical incident-response questions. The downloaded summary includes the original question, recommended first steps, checklist, incident log template, short source note, and educational disclaimer. It avoids full source dumps, relevance scores, duplicate source sections, and long official URLs because those details are already shown inside the app.

The incident-response guidance is educational and defensive. It is not a replacement for a professional incident-response team.

---

## Experimental AI Search

CyberLex Sweden includes an experimental AI search panel in the sidebar. For test runs, this panel is collapsed by default so it does not distract from the main user experience.

This panel uses:

```text
app/vector_search.py
```

Despite the file name, the current experimental search is still rule-based. It does not yet use embeddings, ChromaDB, FAISS, or a full language model.

The experimental search is used to test retrieval ranking before future vector search or RAG integration.

It currently uses:

- Markdown chunking
- keyword matching
- useful-section boosts
- weak-section penalties
- topic-specific routing rules
- source-specific score boosts and penalties

Example Swedish retrieval tests now supported:

| Question | Expected source |
|---|---|
| `Vad är NIS2?` | `nis2_cybersecurity_law.md` |
| `Vad ska ett företag göra efter en ransomwareattack?` | `nis2_incident_reporting.md` or `cyber_incident_response_playbook.md` |
| `Vad gör vi om vi ser misstänkt inloggning?` | `cyber_incident_response_playbook.md` |
| `Vad gör vi vid misstänkt mejl?` | `cyber_incident_response_playbook.md` |
| `Vad gör vi om ett konto är komprometterat?` | `cyber_incident_response_playbook.md` |
| `Vad är IMY?` | `imy_gdpr_supervision.md` |
| `Vad är DORA?` | `eu_dora_digital_operational_resilience.md` |
| `Vad betyder cybersäkerhetskrav för digitala produkter?` | `eu_cyber_resilience_act.md` |
| `Vad säger EU om attacker mot informationssystem?` | `eu_attacks_against_information_systems.md` |
| `Vad är olaglig åtkomst enligt EU-regler?` | `eu_attacks_against_information_systems.md` |

---

## Source Audit System

CyberLex Sweden includes a local source audit script:

```text
scripts/source_audit.py
```

The script checks the Markdown files in `data/` for required source structure, including:

- official source section
- official source links
- source metadata section
- source date
- source freshness label
- version notes

It generates:

```text
docs/source_audit_report.md
```

The expected result should match the current number of source files in the `data/` folder.

The audit does **not** browse the web and does **not** confirm whether the law is currently up to date. It only checks the local project files.

A weekly GitHub Actions workflow also exists for source auditing:

```text
.github/workflows/source-audit.yml
```

---

## Tools and Technologies

| Tool | Purpose |
|---|---|
| Python | Main programming language used to build the app |
| Streamlit | Creates the local web interface |
| Markdown | Used for documentation and local knowledge base files |
| Git | Tracks project changes and commit history |
| GitHub | Stores the project online |
| GitHub Actions | Runs the weekly source audit workflow |
| VS Code | Code editor used during development |
| PowerShell | Used to run local commands on Windows |

---

## Project Structure

```text
CyberLex-Sweden
├── .github
│   └── workflows
│       └── source-audit.yml
├── app
│   ├── main.py
│   └── vector_search.py
├── data
│   ├── cybercrime_dataintrang.md
│   ├── cyber_incident_response_playbook.md
│   ├── eu_attacks_against_information_systems.md
│   ├── eu_cyber_resilience_act.md
│   ├── eu_dora_digital_operational_resilience.md
│   ├── gdpr_core_principles.md
│   ├── gdpr_personal_data_breach.md
│   ├── imy_gdpr_supervision.md
│   ├── nis2_cybersecurity_law.md
│   └── nis2_incident_reporting.md
├── docs
│   ├── ai_rag_plan.md
│   ├── demo_checklist.md
│   ├── legal_disclaimer.md
│   ├── privacy_policy.md
│   ├── product_roadmap.md
│   ├── project_overview.md
│   ├── project_plan.md
│   ├── source_audit_report.md
│   ├── source_list.md
│   ├── source_policy.md
│   ├── source_update_history.md
│   ├── technical_design.md
│   ├── terms_of_use.md
│   ├── test_cases.md
│   ├── test_run_checklist.md
│   └── vector_search_plan.md
├── report
│   └── final_report.md
├── screenshots
├── scripts
│   ├── add_missing_metadata.py
│   └── source_audit.py
├── sources
├── .gitignore
├── COPYRIGHT.md
├── README.md
└── requirements.txt
```

---

## How to Run Locally

### 1. Open the project folder

```powershell
cd C:\Projects\CyberLex-Sweden
```

This moves PowerShell into the CyberLex Sweden project folder.

### 2. Create a virtual environment if needed

```powershell
python -m venv .venv
```

This creates an isolated Python environment for the project.

### 3. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

This activates the local Python environment.

You should see:

```text
(.venv)
```

at the start of the terminal line.

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

This installs the Python packages listed in `requirements.txt`.

### 5. Check Python syntax

```powershell
python -m py_compile app/main.py
```

This checks whether the main app file has Python syntax errors.

If the command gives no output, the syntax check usually passed.

### 6. Start the app

```powershell
python -m streamlit run app/main.py
```

This starts CyberLex Sweden locally in the browser.

Expected local address:

```text
http://localhost:8501
```

---

## Useful Commands

Run the app:

```powershell
python -m streamlit run app/main.py
```

Run the source audit:

```powershell
python scripts/source_audit.py
```

Run the experimental retrieval module:

```powershell
python app/vector_search.py
```

Check Python syntax for the main app:

```powershell
python -m py_compile app/main.py
```

Check Python syntax for the experimental retrieval module:

```powershell
python -m py_compile app/vector_search.py
```

Clear Streamlit cache:

```powershell
streamlit cache clear
```

Check Git status:

```powershell
git status
```

---

## Documentation

Additional project documentation is available in the `docs/` folder.

Important documents include:

- `docs/project_overview.md` - project overview and background
- `docs/project_plan.md` - project plan and schedule
- `docs/source_list.md` - trusted source list
- `docs/source_policy.md` - source quality policy
- `docs/source_update_history.md` - source update history and knowledge base change log
- `docs/source_audit_report.md` - generated local source audit report
- `docs/test_cases.md` - manual and experimental retrieval test cases
- `docs/demo_checklist.md` - demo preparation and presentation checklist
- `docs/test_run_checklist.md` - practical checklist for running a first test pass
- `docs/technical_design.md` - application architecture and technical design
- `docs/product_roadmap.md` - product roadmap and future development plan
- `docs/vector_search_plan.md` - vector search plan
- `docs/ai_rag_plan.md` - future RAG plan
- `docs/terms_of_use.md` - draft terms of use
- `docs/privacy_policy.md` - draft privacy policy
- `docs/legal_disclaimer.md` - legal disclaimer for educational use

---

## Testing and Demo

Manual test cases are documented in:

```text
docs/test_cases.md
```

The demo checklist is documented in:

```text
docs/demo_checklist.md
```

The practical test-run checklist is documented in:

```text
docs/test_run_checklist.md
```

This checklist is intended for a first external or semi-external test run. It covers startup, core legal questions, Swedish and English questions, practical incident-response questions, incident log templates, clean downloaded incident summaries, refusal behavior, source visibility, source audit checks, and tester feedback.

The current test coverage includes:

- core knowledge base tests
- UI card layout tests
- source metadata tests
- official source link tests
- incident-response tests
- suspicious login tests
- suspicious email and phishing tests
- compromised account tests
- data leak tests
- ransomware and malware tests
- incident log template tests
- clean downloaded incident summary tests
- attention-level tests
- cleaner test-run UI checks
- collapsed technical source detail checks
- practical test-run checklist
- Swedish and English language consistency tests
- Auto language switching tests
- source context readability tests
- source metadata language consistency tests
- offensive cyber refusal tests
- out-of-scope refusal tests
- experimental retrieval tests
- source audit tests

---

## Important Limitations

CyberLex Sweden is an educational prototype.

Current limitations:

- It does not provide legal advice.
- It does not replace official authority guidance.
- It does not replace a qualified lawyer or professional compliance review.
- It does not replace a professional incident-response team.
- It does not browse the web live.
- It only answers from local Markdown source files.
- It covers selected cybersecurity-law and incident-response topics only.
- The current answers are rule-based.
- The experimental AI search is not real vector search yet.
- Source freshness labels describe stored local review dates only.
- The source audit checks file structure, not live legal currency.
- Incident-response guidance is simplified for educational use.
- Downloaded incident summaries are documentation aids and do not replace internal incident-response records, legal review, or official reporting.
- Attention levels are educational signals and do not replace legal, regulatory, or incident-response risk assessment.
- Some local source sections are fuller in English than Swedish, so continued bilingual source expansion is still needed.

For serious legal, regulatory, compliance, or security decisions, official sources and qualified professionals should be checked.

---

## Future Improvements

Planned or possible improvements include:

- Improve the professional formatting of downloaded incident summaries
- Add optional prepared-by, organization, date/time, and incident ID fields to downloaded summaries
- Add fuller Swedish source sections to the Markdown knowledge base so Swedish source context can rely on real Swedish source text rather than fallback notes
- Add copy/export features for broader non-incident answers, checklists, and sources
- Add more specific attention-level explanations per incident type
- Continue refining the cleaner test-run interface after user feedback
- Improve source context selection further so the most useful explanatory sections appear first
- Revisit vector search using Python 3.12 or another stable AI-compatible environment
- Add embeddings with `sentence-transformers`
- Add ChromaDB or FAISS
- Compare keyword search with vector search
- Add RAG-style answer generation
- Keep answers grounded only in trusted local source material
- Add more Swedish and EU cybersecurity-law sources
- Improve source update workflows
- Improve visual design
- Prepare public deployment documentation
- Strengthen Terms of Use, Privacy Policy, and Legal Disclaimer
- Continue bilingual Swedish and English source expansion
- Consider trademark and brand protection if the project develops further

---

## Disclaimer

CyberLex Sweden is a school project and educational prototype.

It provides simplified information from selected local source summaries and official source links. It is not legal advice, does not guarantee legal accuracy or currentness, and should not be used as the sole basis for legal, compliance, or security decisions.

For real incidents, legal questions, regulatory reporting, or compliance decisions, users should check official sources and contact qualified professionals.
