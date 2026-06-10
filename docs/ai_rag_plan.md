# CyberLex Sweden AI and RAG Plan

## Purpose

This document explains how CyberLex Sweden could later use AI and Retrieval-Augmented Generation, also called RAG.

CyberLex Sweden is currently a local source-grounded educational prototype. It searches trusted Markdown source files and generates rule-based answers.

A future AI version could make answers more natural, flexible, and easier to read. However, because CyberLex Sweden deals with cybersecurity law, GDPR, NIS2, DORA, cybercrime, incident reporting, the Cyber Resilience Act, and digital compliance, AI answers must remain source-grounded.

CyberLex Sweden should not provide legal advice and should not answer legal or compliance questions without trusted source material.

---

## Current System

The current CyberLex Sweden prototype uses:

* local Markdown files in `data/`
* keyword-based search
* source routing
* chunk ranking
* topic keyword expansion
* rule-based answer generation
* official source links
* source metadata
* source quality labels
* source freshness labels
* source confidence explanations
* detected topic labels
* practical explanation cards
* topic-based assessment checklists
* relevant source context
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

---

## Current Source-Grounded Design

CyberLex Sweden answers are based on selected local source files.

The local knowledge base is stored in:

```text
data/
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

The current source audit checks local file structure and metadata.

It does not browse the web and does not confirm live legal currency.

---

## Why AI Must Be Source-Grounded

CyberLex Sweden works with legal, compliance, and cybersecurity topics.

A normal language model may produce fluent answers that sound correct but are not supported by the project sources.

That is dangerous for this type of project because users may treat confident wording as legal or compliance truth.

Future AI answers must therefore follow one rule:

```text
No trusted source, no answer.
```

The AI should not answer legal or compliance questions from general memory.

It should only answer from retrieved CyberLex source chunks.

---

## Future AI Goal

A future AI version should help CyberLex Sweden:

* understand more varied user wording
* summarize source material in clearer language
* combine multiple relevant source sections
* explain Swedish and EU cybersecurity-law concepts more naturally
* produce better bilingual answers
* support practical incident-response explanations
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
3. CyberLex searches trusted local source documents.
4. CyberLex retrieves the most relevant source sections.
5. The AI model receives the user question and retrieved source excerpts.
6. The AI writes an answer using only those excerpts.
7. CyberLex displays the answer, source details, official links, source metadata, and limitation notice.
8. If the retrieved sources are not strong enough, CyberLex refuses.

---

## Future RAG Flow

```text
User question
↓
Scope and safety check
↓
Source retrieval
↓
Best matching source chunks selected
↓
AI receives question + trusted source excerpts
↓
AI generates source-grounded answer
↓
CyberLex displays answer, citations, official links, metadata, and disclaimer
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
* incident-response report wording
* user-friendly explanations of source material

RAG should not be used to:

* invent legal obligations
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
6. Only then test AI-generated answers in a separate experimental mode.

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
* not invent obligations, deadlines, authorities, or legal consequences
* say when the sources are insufficient
* keep the answer educational
* state that the answer is not legal advice
* preserve uncertainty where needed
* cite the source chunks used
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
7. Important limitation
8. Optional practical checklist
9. Refusal if the source material is insufficient

This keeps the answer useful while preserving transparency.

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

This is important because the user should be able to inspect where the answer came from.

Legal and compliance answers should not feel like magic. Magic is just undocumented engineering with a superiority complex.

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

| Risk                      | Explanation                                      | Mitigation                                            |
| ------------------------- | ------------------------------------------------ | ----------------------------------------------------- |
| Hallucinated legal claims | AI may invent obligations or deadlines           | Answer only from retrieved sources                    |
| Outdated source material  | Local files may become stale                     | Use source dates, source history, and review routines |
| Wrong source retrieval    | Similar topics may match incorrectly             | Compare retrieval modes and use thresholds            |
| Overconfidence            | Users may treat answers as legal advice          | Keep limitation notices visible                       |
| Cyber misuse              | Users may ask for harmful technical instructions | Refuse unsafe requests                                |
| Privacy issues            | Public deployment may process real questions     | Add privacy policy and avoid unnecessary storage      |
| Weak citations            | AI may summarize without traceability            | Require source file, section, and metadata display    |

---

## Minimum Requirements Before RAG

Before connecting a language model, CyberLex Sweden should have:

* stable source files
* clear source policy
* current source list
* source audit report
* tested retrieval quality
* reliable vector search or hybrid retrieval
* refusal behavior
* citation display
* visible legal disclaimer
* manual test cases
* updated README
* updated technical design
* privacy and Terms of Use drafts
* safe handling for unsafe cyber requests

Most of these are already present in the current prototype.

The missing major step is reliable semantic retrieval.

---

## Recommended Implementation Order

The future implementation order should be:

1. Install Python 3.12 or Python 3.11.
2. Rebuild the virtual environment.
3. Install pinned AI dependencies.
4. Build a vector index from `data/`.
5. Create a command-line vector search test script.
6. Compare vector results against `docs/test_cases.md`.
7. Add vector search to the Streamlit sidebar as a separate test mode.
8. Add hybrid retrieval if needed.
9. Add a RAG prompt template.
10. Add AI-generated answers only in a separate experimental mode.
11. Keep the current rule-based answer system as a fallback.
12. Update test cases and documentation.
13. Only later consider public deployment.

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

Future AI work should resume only after the environment is prepared with Python 3.12 or Python 3.11.

---

## Relationship to Other Planning Documents

This document focuses on future AI and RAG behavior.

Related documents:

| Document                     | Purpose                                                      |
| ---------------------------- | ------------------------------------------------------------ |
| `docs/project_plan.md`       | Describes the school project journey and what was completed. |
| `docs/product_roadmap.md`    | Describes the broader future product direction.              |
| `docs/vector_search_plan.md` | Describes the technical plan for semantic/vector search.     |
| `docs/technical_design.md`   | Describes how the current system is structured.              |
| `docs/source_policy.md`      | Describes source rules and limitations.                      |

---

## Summary

CyberLex Sweden is ready for future AI and RAG development, but the current version remains a local source-grounded prototype.

The current system already demonstrates:

* trusted local source files
* source routing
* rule-based retrieval
* Swedish and English interface support
* citation details
* source metadata
* official source links
* source audit
* manual testing
* unsafe-request refusal

The next major AI step is real vector search.

After that, CyberLex can move toward RAG-style answer generation, but only if answers remain source-grounded, cautious, transparent, and limited to trusted source material.
