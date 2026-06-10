# CyberLex Sweden Product Roadmap

## Purpose

This roadmap explains how CyberLex Sweden could develop from a local school prototype into a more realistic legal-tech and cybersecurity compliance assistant.

The roadmap is not a promise that every feature will be built. It describes a realistic future development path.

CyberLex Sweden is currently an educational prototype. It does not provide legal advice and should not replace official authority guidance, a lawyer, data protection officer, compliance expert, or professional incident-response team.

---

## Current Prototype Status

CyberLex Sweden currently works as a local Streamlit application.

The current prototype includes:

* local Markdown knowledge base in `data/`
* source-based search and chunk ranking
* rule-based source routing
* source-grounded answer generation
* official source links
* source metadata
* source quality labels
* source freshness labels
* source confidence notes
* bilingual interface support for English and Swedish
* Auto language detection
* practical explanation cards
* CyberLex attention levels
* assessment checklist support
* relevant source context
* expandable source excerpts
* other matching source sections
* clickable example questions
* experimental retrieval sidebar
* defensive incident-response guidance
* SOC-style Markdown incident report export
* out-of-scope refusal behavior
* unsafe cyber refusal behavior
* local source audit script
* source audit report
* GitHub Actions source audit workflow
* manual test cases
* demo documentation
* technical design documentation
* legal/privacy/disclaimer drafts

The current system does not yet use:

* true vector search
* semantic embeddings
* ChromaDB
* FAISS
* full language-model answer generation
* RAG answer generation
* production database
* public deployment

The current version should be understood as a transparent, source-grounded educational prototype.

---

## Product Direction

CyberLex Sweden could develop in several possible directions:

* student portfolio project
* cybersecurity-law learning tool
* Swedish cyber law research assistant
* internal company knowledge assistant
* compliance support prototype
* bilingual Swedish/English legal-tech assistant
* future startup concept

The strongest direction is a focused source-grounded assistant for Swedish and EU cybersecurity law.

The product should stay narrow enough to remain trustworthy.

---

## Core Product Principles

Future development should follow these principles:

1. **Source grounding first**

   CyberLex should answer from trusted source material, not from general AI memory.

2. **Clear scope**

   CyberLex should stay focused on selected cybersecurity-law, data protection, digital compliance, cybercrime, and defensive incident-response topics.

3. **Visible limitations**

   CyberLex should always make clear that it is educational and not legal advice.

4. **Bilingual support**

   Swedish and English should both be treated as main languages.

5. **Safety boundaries**

   CyberLex should refuse unsafe cyber misuse requests.

6. **Source maintenance**

   Legal and cybersecurity sources must be reviewed and updated over time.

7. **Privacy awareness**

   A public version must handle user questions carefully and avoid unnecessary data storage.

---

## Completed Milestone: Local Source-Grounded Prototype

### Status

Completed for the current school project phase.

### Completed Features

* Streamlit web interface
* local Markdown knowledge base
* source loading
* chunk-based source search
* rule-based source routing
* source-grounded answers
* official source links
* source metadata
* source quality labels
* source freshness labels
* important limitation notices
* English and Swedish interface support
* Auto language detection
* example question buttons
* source context display
* practical explanation support
* assessment checklist support
* incident-response support
* SOC Markdown report export
* out-of-scope refusal
* unsafe cyber refusal
* source audit script
* source audit report
* documentation and test cases

### Why This Matters

This milestone proves that the project can answer selected questions from controlled local source material and show the user where the answer came from.

---

## Completed Milestone: Source and Retrieval Improvement

### Status

Completed for the current prototype phase.

### Completed Source Areas

CyberLex Sweden currently supports selected material related to:

* GDPR core principles
* GDPR personal data breach notification
* IMY and Swedish GDPR supervision
* GDPR/IMY security measures
* NIS2 and Swedish cybersecurity law
* NIS2 incident reporting
* NIS2 sector scope and applicability
* Swedish cybercrime and dataintrång
* DORA and digital operational resilience
* Cyber Resilience Act and product cybersecurity
* EU attacks against information systems
* defensive cyber incident response

### Completed Improvements

* source files cleaned and structured
* official source links improved
* source metadata standardized
* Swedish summaries added or improved
* source routing improved
* source context made more readable
* incident-response routing improved
* unsafe refusal behavior improved
* source audit workflow added

### Why This Matters

Better retrieval and better source structure make future AI features safer and more useful.

The design principle remains:

```text
Better sources first. Better AI second.
```

---

## Completed Milestone: Demo and Testing Readiness

### Status

Completed for final project preparation.

### Completed Documentation

* `docs/testing_and_demo.md`
* `docs/demo_script.md`
* `docs/demo_checklist.md`
* `docs/test_run_checklist.md`
* `docs/test_cases.md`

### Completed Testing Areas

* app startup
* English questions
* Swedish questions
* Auto language switching
* source routing
* official source links
* source metadata
* source context readability
* GDPR/IMY questions
* NIS2 questions
* DORA questions
* CRA questions
* cybercrime questions
* incident-response questions
* SOC Markdown report download
* out-of-scope refusal
* unsafe cyber refusal

### Why This Matters

The project can now be demonstrated and reviewed without relying only on the developer's memory, which is good because memory is just biological cache and humans keep proving why that is a terrible storage system.

---

## Phase 1: Source Expansion

### Status

Future improvement.

### Goal

Expand the trusted knowledge base while keeping source quality high.

### Possible Future Source Areas

* more IMY guidance
* more GDPR security guidance
* more NIS2 sector-specific material
* Swedish Cybersecurity Act updates
* DORA technical standards and guidance
* EU Cybersecurity Act
* ENISA certification material
* Protective Security Act, `säkerhetsskyddslagen`
* electronic communications security rules
* AI Act cybersecurity and compliance connections
* EDPB security and data protection guidance
* cybersecurity procurement guidance
* supplier and third-party security guidance
* Swedish public-sector cybersecurity guidance

### Requirements for New Source Files

Each new source file should include:

* topic
* main authority or legal source
* key idea
* important points
* cybersecurity connection
* useful questions
* Swedish summary where useful
* Swedish useful questions where useful
* official source links
* source metadata
* source date
* version notes
* disclaimer

### Success Criteria

This phase is successful when CyberLex can answer more supported questions without weakening source transparency or refusal behavior.

---

## Phase 2: Better Source Management

### Status

Partly completed.

### Completed Work

* source metadata
* source dates
* version notes
* source quality labels
* source freshness labels
* source audit script
* source audit report
* source policy
* source history
* GitHub Actions source audit workflow

### Planned Improvements

* source update checklist
* source categories
* source status values such as active, needs review, outdated
* source owner or reviewer field
* periodic review schedule
* link-checking process
* method for retiring outdated sources
* manual legal-currentness review process
* clearer high-priority source review routine

### Why This Matters

Legal and cybersecurity information changes over time.

The current source audit checks local file structure and metadata. It does not confirm live legal currency.

A more serious product would need stronger source review and update routines.

---

## Phase 3: Real Vector Search

### Status

Future technical phase.

### Goal

Improve retrieval quality beyond keyword matching and hand-written routing rules.

### Planned Improvements

* use a stable Python version such as Python 3.12 or Python 3.11
* add `sentence-transformers`
* generate embeddings for source chunks
* store chunk embeddings locally
* test ChromaDB or FAISS
* keep metadata attached to every chunk
* compare vector search results with current rule-based retrieval
* add a retrieval comparison mode
* add minimum confidence or similarity thresholds
* preserve source-grounded refusal behavior

### Related Document

The detailed implementation plan is stored in:

```text
docs/vector_search_plan.md
```

### Success Criteria

This phase is successful when CyberLex can find the correct source section even when the user does not use the exact same words as the source file.

---

## Phase 4: RAG and AI-Generated Answers

### Status

Future technical phase.

### Goal

Use AI to generate more natural answers while remaining grounded in trusted CyberLex source material.

### Important Rule

A future AI model should not answer legal or compliance questions from general memory.

It should only answer using retrieved CyberLex source chunks.

### Planned Improvements

* retrieve source chunks before answer generation
* pass source chunks into a language model
* generate clearer plain-language answers
* include citations and source metadata
* refuse unsupported questions
* prevent unsupported legal claims
* avoid unsafe cyber instructions
* keep disclaimers visible
* add multi-source synthesis
* add answer traceability to source chunks

### Related Document

The detailed AI/RAG plan is stored in:

```text
docs/ai_rag_plan.md
```

### Success Criteria

This phase is successful when answers become easier to read while still remaining cautious, source-grounded, and transparent.

---

## Phase 5: Code Structure and Maintainability

### Status

Future improvement.

### Goal

Make the codebase easier to maintain after the final project hand-in.

### Planned Refactor

The current `app/main.py` could later be split into smaller modules:

```text
app/ui.py
app/answer_engine.py
app/source_loader.py
app/source_context.py
app/incident_reports.py
app/language_utils.py
app/safety.py
```

### Why This Matters

The current app works, but the main file has become large.

Splitting the code later would make it easier to test, debug, and expand.

This should not be done right before hand-in unless there is enough time and low risk.

---

## Phase 6: User Experience and Visual Design

### Status

Partly completed.

### Completed Improvements

* cleaner main page
* supported topic information
* styled source metadata card
* styled limitation notice
* styled citation details
* styled official links
* styled source context
* styled attention levels
* collapsible source sections
* clickable example questions
* bilingual interface controls
* cleaner incident-response layout
* SOC Markdown report download

### Planned Improvements

* more polished visual identity
* better mobile layout
* better empty-state messages
* clearer onboarding text
* improved sidebar organization
* improved screenshot-ready design
* clearer explanation of prototype limitations
* better user-friendly names for source panels

### Success Criteria

This phase is successful when a new user can understand what CyberLex does without needing the developer to explain every panel.

---

## Phase 7: Public Deployment Preparation

### Status

Future phase.

### Goal

Prepare CyberLex Sweden for possible public deployment.

### Required Work Before Public Deployment

* review Terms of Use
* review Privacy Policy
* review Legal Disclaimer
* decide whether user questions are stored
* decide whether analytics are used
* decide whether external AI APIs are used
* add secure configuration handling
* avoid exposing secrets or API keys
* add deployment documentation
* add logging policy
* add security review checklist
* add abuse-prevention rules
* add rate limiting if public
* add contact/support information if public

### Possible Deployment Options

* Streamlit Community Cloud
* Render
* Railway
* Azure App Service
* AWS
* Hetzner
* Docker-based deployment

### Important Note

A public version must be treated differently from a local prototype.

A public version may process real user input, which creates privacy, security, and legal concerns.

### Success Criteria

This phase is successful when the app can be deployed safely with clear user-facing policies and no exposed secrets.

---

## Phase 8: Legal and Brand Protection

### Status

Future phase.

### Goal

Prepare CyberLex Sweden for possible long-term development as a brand or product.

### Possible Actions

* keep copyright notices
* avoid adding an open-source license unless intentionally chosen
* strengthen Terms of Use
* strengthen Privacy Policy
* strengthen Legal Disclaimer
* check for name conflicts
* consider registering the CyberLex Sweden name as a trademark
* consider logo and brand protection
* review whether public use requires legal review from a qualified lawyer

### Trademark Note

If CyberLex Sweden becomes a serious product, trademark protection may be useful for the name and brand identity.

This should be handled later, when the project has clearer long-term value.

### Success Criteria

This phase is successful when the project has a clear identity, ownership notice, and legal protection plan.

---

## Phase 9: Product Direction Decision

### Status

Future decision phase.

### Goal

Decide whether CyberLex Sweden should remain a portfolio project or become a real product concept.

### Questions to Answer

* Who is the target user?
* What problem does CyberLex solve better than existing sources?
* Should CyberLex answer only from official sources?
* Should CyberLex store user questions?
* Should CyberLex use a cloud language model?
* How should source updates be reviewed?
* What legal review is required before public use?
* Should CyberLex remain local/offline or become hosted?
* Which sectors should be prioritized first?
* How should Swedish and English support be maintained?

### Success Criteria

This phase is successful when the project has a clear long-term direction.

---

## Language Support Roadmap

### Current Support

CyberLex Sweden currently supports:

* English interface mode
* Swedish interface mode
* Auto language mode
* English user questions
* Swedish user questions
* English answer headings
* Swedish answer headings
* Swedish and English example questions
* Swedish source summaries in key knowledge files
* Swedish useful questions in many source files
* Swedish routing for supported topics

### Planned Improvements

* better Swedish answer wording
* better English explanations of Swedish legal terms
* more bilingual source summaries
* more Swedish legal terminology support
* more consistent bilingual source metadata
* better handling of mixed Swedish and English questions

### Success Criteria

Swedish and English should both feel like first-class language modes, not one real mode and one cursed translation layer.

---

## Risk Overview

| Risk                   | Explanation                                   | Mitigation                                                          |
| ---------------------- | --------------------------------------------- | ------------------------------------------------------------------- |
| Outdated legal sources | Laws and guidance can change                  | Use source review dates, source history, and manual review routines |
| Unsupported answers    | The system may answer without enough evidence | Use scope checks, source routing, and refusal behavior              |
| Wrong source match     | Similar legal topics may confuse retrieval    | Use routing, tests, and later vector search                         |
| Overreliance by users  | Users may treat answers as legal advice       | Keep disclaimers and Terms of Use clear                             |
| Privacy issues         | Public deployment may process user input      | Add privacy policy and avoid unnecessary storage                    |
| Cyber misuse           | Users may ask harmful cybercrime questions    | Refuse harmful or out-of-scope requests                             |
| False legal currency   | Users may assume sources are live-updated     | Explain that source audit does not verify live legal changes        |
| AI hallucination risk  | Future AI may generate unsupported statements | Require source-grounded RAG and refusal rules                       |
| Code complexity        | `app/main.py` may become hard to maintain     | Refactor into modules after hand-in                                 |

---

## Near-Term Roadmap

Before final hand-in, the near-term roadmap is:

1. Finish documentation cleanup.
2. Review source documentation.
3. Run source audit.
4. Run final manual smoke tests.
5. Confirm the demo flow works.
6. Confirm SOC Markdown report export works.
7. Check out-of-scope refusal.
8. Check unsafe cyber refusal.
9. Review README and final presentation material.
10. Commit and push the final clean version.

After hand-in, the roadmap is:

1. Refactor `app/main.py` into smaller modules.
2. Prepare Python 3.12 or 3.11 environment.
3. Add real vector search as a separate test mode.
4. Compare vector search against existing test cases.
5. Improve source update routines.
6. Expand Swedish and EU source coverage.
7. Consider RAG only after retrieval is reliable.
8. Review legal/privacy/disclaimer documents before any public deployment.

---

## Long-Term Vision

CyberLex Sweden could become a source-grounded assistant for Swedish and EU cybersecurity law.

A mature version should:

* rely on official and reviewed sources
* show citations clearly
* explain legal concepts in plain language
* refuse unsupported questions
* keep source history
* protect user privacy
* avoid harmful cybersecurity guidance
* support both Swedish and English as first-class languages
* maintain a strict difference between educational information and legal advice
* support future expansion into related compliance areas

---

## Summary

CyberLex Sweden has moved beyond a basic prototype.

The project now has a working local application, trusted knowledge files, source-grounded answers, source metadata, official source links, bilingual interface support, incident-response guidance, SOC Markdown report export, test cases, source audit support, and a realistic development roadmap.

The next major technical step is real vector search.

The long-term product direction should remain cautious: better sources first, better retrieval second, AI-generated answers only when source grounding is reliable.
