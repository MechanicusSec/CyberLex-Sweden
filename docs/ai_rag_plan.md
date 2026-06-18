# CyberLex Sweden AI and RAG Plan

## Purpose

This document explains how CyberLex Sweden could later use AI and Retrieval-Augmented Generation, also called RAG.

CyberLex Sweden is currently a local source-grounded educational prototype. It searches trusted Markdown source files, matches related case examples, and generates rule-based answers.

A future AI version could make answers more natural, flexible, and easier to read. However, because CyberLex Sweden deals with cybersecurity law, GDPR, NIS2, DORA, cybercrime, incident reporting, the Cyber Resilience Act, real-world case examples, and digital compliance, AI answers must remain source-grounded.

CyberLex Sweden should not provide legal advice and should not answer legal or compliance questions without trusted source material.

---

## Current System

The current CyberLex Sweden prototype uses:

* local Markdown files in `data/`
* local case-library files in `cases/`
* keyword-based search
* source routing
* chunk ranking
* topic keyword expansion
* rule-based answer generation
* related case matching
* Case Intelligence page
* English mode
* Swedish mode
* Auto language mode
* official source links
* source metadata
* source quality labels
* source freshness labels
* source confidence explanations
* detected topic labels
* practical explanation cards
* topic-based assessment checklists
* relevant source context
* defensive incident-response guidance
* SOC-style Markdown report export for practical incident questions
* out-of-scope refusal
* unsafe cyber refusal
* an experimental retrieval sidebar

This makes the current system transparent, testable, and suitable for an educational prototype.

The current app does not use:

* a full language model
* true semantic vector search
* ChromaDB
* FAISS
* RAG answer generation
* live web browsing for legal answers
* an external AI API

---

## Current Source-Grounded Design

CyberLex Sweden answers are based on selected local source files.

The local knowledge base is stored in:

```text
data/
```

The local case library is stored in:

```text
cases/
```

The exact current source list should be checked in:

```text
docs/source_list.md
```

Each source file should include:

* topic
* main authority or legal source
* key idea
* important points
* official source links
* source metadata
* source date
* version notes
* disclaimer

Case files should include educational case context, outcome or fine notes where known, related CyberLex questions, learning notes, and official or reliable source links where possible.

The current source audit checks local source-file structure and metadata.

The current case audit checks local case-file structure.

These audits do not browse the web and do not confirm live legal currency.

---

## Why AI Must Be Source-Grounded

CyberLex Sweden works with legal, compliance, privacy, and cybersecurity topics.

A normal language model may produce fluent answers that sound correct but are not supported by the project sources.

That is dangerous for this type of project because users may treat confident wording as legal, regulatory, or compliance truth.

Future AI answers must therefore follow one rule:

```text
No trusted source, no answer.
```

The AI should not answer legal or compliance questions from general memory.

It should only answer from retrieved CyberLex source chunks.

If case examples are used, they must be clearly labeled as educational examples and not treated as legal predictions.

---

## Future AI Goal

A future AI version should help CyberLex Sweden:

* understand more varied user wording
* summarize source material in clearer language
* combine multiple relevant source sections
* explain Swedish and EU cybersecurity-law concepts more naturally
* produce better bilingual answers
* preserve English, Swedish, and Auto language behavior
* support practical incident-response explanations
* improve SOC-style incident report wording
* explain related case examples more clearly
* preserve source traceability
* refuse unsupported questions
* refuse unsafe cyber misuse requests

The AI should improve readability, not weaken trust.

---

## Recommended Architecture: RAG

The recommended future architecture is Retrieval-Augmented Generation, or RAG.

RAG means the system retrieves trusted source material before generating an answer.

The future flow should be:

1. The user asks a question.
2. CyberLex checks whether the question is within scope.
3. CyberLex checks whether the request is unsafe.
4. CyberLex detects the answer language.
5. CyberLex searches trusted local source documents.
6. CyberLex retrieves the most relevant source sections.
7. CyberLex optionally retrieves clearly labeled related case examples.
8. The AI model receives the user question and retrieved source excerpts.
9. The AI writes an answer using only those excerpts.
10. CyberLex displays the answer, source details, official links, source metadata, case labels where relevant, and limitation notice.
11. If the retrieved sources are not strong enough, CyberLex refuses.

---

## Future RAG Flow

```text
User question
↓
Scope and safety check
↓
Language detection
↓
Source retrieval from data/
↓
Optional related case retrieval from cases/
↓
Best matching source chunks selected
↓
AI receives question + trusted source excerpts
↓
AI generates source-grounded answer
↓
CyberLex displays answer, citations, official links, metadata, related cases where relevant, and disclaimer
↓
CyberLex refuses if sources are insufficient
```

---

## What RAG Should Improve

RAG could improve:

* natural language answer quality
* explanations of difficult legal terms
* bilingual Swedish and English answers
* multi-source synthesis
* practical summaries
* SOC-style incident report wording
* user-friendly explanations of source material
* clearer explanation of related case examples
* smoother answers for questions phrased in unexpected ways

RAG should not be used to:

* invent legal obligations
* invent reporting deadlines
* invent fine amounts
* treat case examples as predictions
* replace official sources
* replace legal advice
* answer outside the CyberLex scope
* answer without citations
* provide harmful cyber instructions
* hide uncertainty
* pretend local sources are live-updated

---

## Required Retrieval Step Before RAG

Before AI-generated answers are added, CyberLex Sweden should first improve retrieval.

The recommended order is:

1. Keep the current rule-based retrieval working.
2. Add real vector search as a separate test mode.
3. Compare vector search against existing manual test cases.
4. Add minimum confidence or similarity thresholds.
5. Confirm that source metadata stays attached to every retrieved chunk.
6. Confirm that case examples remain separate from main legal source answers.
7. Only then test AI-generated answers in a separate experimental mode.

The detailed vector search implementation plan is stored in:

```text
docs/vector_search_plan.md
```

---

## Future RAG Prompt Rules

A future RAG prompt should include strict rules.

The AI should be instructed to:

* answer only from the provided source excerpts
* not use outside knowledge for legal claims
* not invent obligations, deadlines, authorities, fines, or legal consequences
* say when the sources are insufficient
* keep the answer educational
* state that the answer is not legal advice
* preserve uncertainty where needed
* cite the source chunks used
* clearly separate legal source material from case examples
* explain that case examples are not predictions
* preserve the selected or detected language
* refuse cybercrime, evasion, credential theft, exploitation, or unauthorized access instructions
* redirect unsafe cyber requests toward lawful defensive handling

---

## Safe Answer Pattern

A future AI-generated answer should follow this structure:

1. Short answer
2. Plain-language explanation
3. Relevant source basis
4. Citation details
5. Official source links
6. Source metadata
7. Related case examples where relevant
8. Important limitation
9. Optional practical checklist
10. Refusal if the source material is insufficient

This keeps the answer useful while preserving transparency.

For practical incident-response questions, the answer should focus on:

* containment
* evidence preservation
* documentation
* escalation
* recovery
* GDPR or NIS2 assessment reminders where relevant
* SOC-style report support where appropriate

For urgent practical incident-response triage, related historical case examples should normally be hidden so the answer does not distract from first steps.

---

## Source Citation Requirements

A future RAG answer should always preserve source traceability.

For each answer, CyberLex should be able to show:

* matched source file
* matched section
* retrieved source excerpt
* official source links
* source date
* version notes
* source quality label
* source freshness label
* source confidence or similarity explanation

This is important because the user should be able to inspect where the answer came from.

Legal and compliance answers should not feel like magic. Magic is just undocumented engineering with a superiority complex.

---

## Case Citation Requirements

If a future RAG answer uses related case examples, CyberLex should clearly show:

* case title
* local case file
* jurisdiction
* authority or source
* year
* short summary
* outcome or fine note where known
* official or reliable source links where available
* warning that case examples are educational context only

Case examples should not be treated as proof that a similar situation would produce the same legal result.

Case examples should support learning, not become a fake fine-prediction engine. Humanity has already invented enough misleading calculators.

---

## Refusal Behavior

CyberLex should refuse when no trusted source supports the answer.

Example refusal pattern:

```text
No trusted source was found for this question. CyberLex Sweden only covers selected Swedish and EU cybersecurity law, cybercrime, GDPR, NIS2, incident reporting, DORA, the Cyber Resilience Act, EU attacks against information systems, data protection, and related digital compliance topics.
```

The system should refuse:

* unrelated legal areas
* medical advice
* investment advice
* political trivia
* general homework questions outside scope
* cybercrime instructions
* unauthorized exploitation guidance
* credential theft
* log hiding
* detection bypassing
* unsupported legal claims

The system may explain cybercrime concepts in an educational and lawful context.

---

## Unsafe Cyber Requests

Future AI mode must preserve the current safety boundary.

CyberLex should refuse requests involving:

* stealing credentials
* breaking into accounts
* exploiting systems
* hiding traces
* deleting logs
* bypassing detection
* persistence after unauthorized access
* malware deployment
* phishing
* evasion or cover-up behavior

CyberLex may redirect toward:

* evidence preservation
* incident documentation
* responsible reporting
* system recovery
* defensive investigation
* lawful security education

---

## Legal and Safety Risks

Future AI or RAG features introduce risks.

| Risk                      | Explanation                                           | Mitigation                                               |
| ------------------------- | ----------------------------------------------------- | -------------------------------------------------------- |
| Hallucinated legal claims | AI may invent obligations or deadlines.               | Answer only from retrieved sources.                      |
| Outdated source material  | Local files may become stale.                         | Use source dates, source history, and review routines.   |
| Wrong source retrieval    | Similar topics may match incorrectly.                 | Compare retrieval modes and use thresholds.              |
| Case misuse               | Case examples may be treated as predictions.          | Label cases as educational examples only.                |
| Overconfidence            | Users may treat answers as legal advice.              | Keep limitation notices visible.                         |
| Cyber misuse              | Users may ask for harmful technical instructions.     | Refuse unsafe requests.                                  |
| Privacy issues            | Public deployment may process real questions.         | Add privacy policy and avoid unnecessary storage.        |
| Weak citations            | AI may summarize without traceability.                | Require source file, section, and metadata display.      |
| Language mismatch         | Auto mode may choose the wrong language.              | Preserve language detection tests and allow manual mode. |
| SOC report misuse         | Generated reports may be treated as official records. | Label reports as educational documentation aids.         |

---

## Minimum Requirements Before RAG

Before connecting a language model, CyberLex Sweden should have:

* stable source files
* clear source policy
* current source list
* source audit report
* case audit report
* tested retrieval quality
* reliable vector search or hybrid retrieval
* refusal behavior
* citation display
* visible legal disclaimer
* privacy and data-handling documentation
* Terms of Use
* manual test cases
* updated README
* updated technical design
* safe handling for unsafe cyber requests
* clear distinction between `data/` and `cases/`
* stable English, Swedish, and Auto language behavior

Most of these are already present in the current prototype.

The missing major step is reliable semantic retrieval.

---

## Recommended Implementation Order

The future implementation order should be:

1. Install Python 3.12 or Python 3.11.
2. Rebuild the virtual environment.
3. Install pinned AI dependencies.
4. Build a vector index from `data/`.
5. Keep case retrieval separate at first.
6. Create a command-line vector search test script.
7. Compare vector results against `docs/test_cases.md`.
8. Add vector search to the Streamlit sidebar as a separate test mode.
9. Add hybrid retrieval if needed.
10. Add a RAG prompt template.
11. Add AI-generated answers only in a separate experimental mode.
12. Keep the current rule-based answer system as a fallback.
13. Update test cases and documentation.
14. Only later consider public deployment.

---

## Current Decision

For the current final project phase, CyberLex Sweden should keep the stable rule-based prototype.

Vector search and RAG should be postponed until after final hand-in.

Reason:

* the current prototype works
* the project is close to final delivery
* real AI dependencies may introduce setup problems
* source-grounded behavior must not be broken
* testing and demo stability are more important right now
* breaking the working app would be an unusually ceremonial way to create suffering

Future AI work should resume only after the environment is prepared with Python 3.12 or Python 3.11.

---

## Relationship to Other Planning Documents

This document focuses on future AI and RAG behavior.

Related documents:

| Document                            | Purpose                                                          |
| ----------------------------------- | ---------------------------------------------------------------- |
| `docs/project_plan.md`              | Describes the school project journey and what was completed.     |
| `docs/product_roadmap.md`           | Describes the broader future product direction.                  |
| `docs/vector_search_plan.md`        | Describes the technical plan for semantic/vector search.         |
| `docs/technical_design.md`          | Describes how the current system is structured.                  |
| `docs/source_policy.md`             | Describes source rules and limitations.                          |
| `docs/privacy_and_data_handling.md` | Describes local data-handling and privacy limitations.           |
| `docs/terms_of_use.md`              | Describes intended use, prohibited use, and user responsibility. |

---

## Future External AI Provider Review

The current prototype does not require an external AI provider.

If a future version uses an external AI API or hosted model, CyberLex Sweden should document:

* what data is sent
* why it is sent
* where it is processed
* whether it is stored
* whether it can be used for model training
* how long it is retained
* who can access it
* whether sensitive data is allowed
* what user notice is required
* what security review is required

No real sensitive data should be sent to an external AI service unless legal, privacy, and security requirements are reviewed properly.

---

## Summary

CyberLex Sweden is ready for future AI and RAG development, but the current version remains a local source-grounded prototype.

The current system already demonstrates:

* trusted local source files
* local case-library examples
* source routing
* rule-based retrieval
* Swedish and English interface support
* Auto language behavior
* citation details
* source metadata
* official source links
* source audit
* case audit
* manual testing
* incident-response support
* SOC-style report export
* unsafe-request refusal

The next major AI step is real vector search.

After that, CyberLex Sweden can move toward RAG-style answer generation, but only if answers remain source-grounded, cautious, transparent, and limited to trusted source material.

Better retrieval first.

RAG later.

Better sources always.
