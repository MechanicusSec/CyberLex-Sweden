# CyberLex Sweden AI and RAG Plan

## Purpose

CyberLex Sweden is currently a source-based educational prototype that searches local Markdown knowledge files and generates rule-based answers.

A future version could use AI to produce more natural, complete, and flexible answers. However, because the project deals with cybersecurity law, GDPR, NIS2, incident reporting, DORA, cybercrime, Cyber Resilience Act, and digital compliance, the AI must remain source-grounded.

CyberLex Sweden should not provide legal advice and should not answer legal or compliance questions without trusted source material.

This document explains the planned path from the current rule-based prototype toward future vector search and Retrieval-Augmented Generation, also called RAG.

---

## Current system

The current CyberLex Sweden prototype uses:

- local Markdown files in `data/`
- keyword-based search
- source routing
- chunk ranking
- topic keyword expansion
- rule-based answer generation
- official source links
- source metadata
- source quality labels
- source freshness labels
- source match confidence explanations
- detected topic labels
- practical explanation cards
- topic-based assessment checklists
- relevant source context
- out-of-scope refusal
- an experimental AI search sidebar

This makes the current system simple, transparent, and suitable for an educational prototype.

The current app does not use:

- a full language model
- true semantic vector search
- ChromaDB
- FAISS
- RAG answer generation
- live web browsing for legal answers

---

## Current source-grounded design

CyberLex Sweden answers are currently based on selected local source files.

Current source files include:

```text
data/cybercrime_dataintrang.md
data/eu_attacks_against_information_systems.md
data/eu_cyber_resilience_act.md
data/eu_dora_digital_operational_resilience.md
data/gdpr_core_principles.md
data/gdpr_personal_data_breach.md
data/imy_gdpr_supervision.md
data/nis2_cybersecurity_law.md
data/nis2_incident_reporting.md
```

The prototype uses these files as a controlled educational knowledge base.

Each source file should include:

- topic
- main authority or legal source
- key idea
- important points
- official source links
- source metadata
- disclaimer

The source audit target is:

```text
Files marked OK: 9
Files needing review: 0
```

---

## Experimental AI search sidebar

CyberLex Sweden includes an experimental AI search sidebar.

Despite the name, this feature is not real AI search yet.

It is currently a rule-based retrieval test area using:

- Markdown source chunks
- keyword scoring
- section boosts
- weak-section penalties
- topic-specific routing rules
- source-specific boosts and penalties

The purpose is to test retrieval behavior before adding real vector search.

The experimental retrieval module is:

```text
app/vector_search.py
```

The module has been improved so Swedish questions route to more accurate source files.

Examples:

| Swedish question | Expected source |
|---|---|
| `Vad är NIS2?` | `nis2_cybersecurity_law.md` |
| `Vad ska ett företag göra efter en ransomwareattack?` | `nis2_incident_reporting.md` |
| `Vad ska ett företag göra efter en personuppgiftsincident?` | `gdpr_personal_data_breach.md` |
| `Vad är IMY?` | `imy_gdpr_supervision.md` |
| `Vilka är GDPR-principerna?` | `gdpr_core_principles.md` |
| `Vad är dataintrång?` | `cybercrime_dataintrang.md` |
| `Vad är DORA?` | `eu_dora_digital_operational_resilience.md` |
| `Vad betyder cybersäkerhetskrav för digitala produkter?` | `eu_cyber_resilience_act.md` |
| `Vad säger EU om attacker mot informationssystem?` | `eu_attacks_against_information_systems.md` |

---

## Current vector search status

Real vector search is planned but not currently active.

A first attempt was started by adding vector-search dependencies and creating a draft vector index builder. That attempt was paused.

Reason:

- the local environment used Python 3.14
- some AI package dependencies were not yet smooth with that Python version
- `tokenizers` attempted to build from source
- the build required compiler tools such as Microsoft C++ build tools
- this was too much risk for the current project phase

Decision:

Vector search will be resumed later with Python 3.12 or Python 3.11.

This keeps the current working prototype stable.

Tiny mercy from the machine spirit, for once.

---

## Future AI goal

The future goal is to make CyberLex Sweden answer more naturally while still using trusted sources.

A future AI version should be able to:

- read the user question
- check whether the question is in scope
- search the CyberLex knowledge base
- retrieve relevant source sections
- summarize legal and compliance information in plain language
- combine information from multiple trusted source sections
- include citation details
- show official source links
- show source date and version notes
- show an important limitation
- refuse to answer if no trusted source is found
- clearly state that the answer is not legal advice

The AI should not answer legal or compliance questions from general memory alone.

---

## Recommended architecture: RAG

The recommended future architecture is Retrieval-Augmented Generation, also called RAG.

RAG means that the system retrieves relevant trusted source material before generating an answer.

The future flow should be:

1. The user asks a question.
2. CyberLex checks whether the question is within scope.
3. CyberLex searches trusted source documents.
4. CyberLex retrieves the most relevant source sections.
5. An AI model receives the user question and retrieved source text.
6. The AI writes an answer based only on those sources.
7. CyberLex displays the answer, citations, official links, source metadata, and disclaimer.

The AI should not answer from general memory alone.

---

## Future answer flow

```text
User question
↓
Scope check
↓
Source retrieval
↓
Best matching chunks selected
↓
AI receives question + trusted source excerpts
↓
AI generates source-grounded answer
↓
CyberLex displays answer, citations, official links, source metadata, and disclaimer
```

---

## Planned vector search phase

Before using an AI model for answers, CyberLex should first add real semantic retrieval.

Planned steps:

1. Install Python 3.12 or Python 3.11.
2. Recreate the virtual environment with the stable Python version.
3. Add controlled AI package dependencies.
4. Use `sentence-transformers` to create embeddings.
5. Split Markdown source files into chunks.
6. Store chunk text, source file, section title, and metadata.
7. Save embeddings locally.
8. Create a vector search test script.
9. Compare vector search results with current rule-based retrieval.
10. Keep the current search working until vector search is reliable.

Possible package choices:

```text
sentence-transformers
numpy
scikit-learn
ChromaDB
FAISS
```

The first version can use `sentence-transformers`, `numpy`, and cosine similarity before adding ChromaDB or FAISS.

---

## Vector index design

A future vector index should store both embeddings and metadata.

Each chunk should keep:

- source file name
- section title
- source text
- official source links if available
- source date
- version notes
- source quality type
- source freshness label

Example metadata:

```json
{
  "filename": "nis2_incident_reporting.md",
  "section": "Incident assessment checklist",
  "source_date": "Last checked: 2026-06-03",
  "version_notes": "Source reviewed for CyberLex Sweden educational prototype."
}
```

This is important because future AI answers must still show which source sections were used.

---

## Retrieval comparison plan

Vector search should not immediately replace the current system.

The first version should compare:

- current rule-based retrieval
- experimental keyword retrieval
- vector retrieval

Example comparison questions:

```text
Vad är NIS2?
Vad ska ett företag göra efter en ransomwareattack?
Vad ska ett företag göra efter en personuppgiftsincident?
Vad är IMY?
Vad är DORA?
Vad betyder cybersäkerhetskrav för digitala produkter?
Vad säger EU om attacker mot informationssystem?
```

The vector search should only be connected to the main app after it performs at least as well as the current rule-based routing for supported topics.

---

## Future RAG prompt rules

A future RAG prompt should include strict rules.

The AI should be told:

- Answer only from the provided source excerpts.
- Do not use outside knowledge for legal claims.
- Do not invent obligations, deadlines, authorities, or legal consequences.
- If the sources are insufficient, say that no trusted source is available.
- Keep the answer educational.
- Do not provide legal advice.
- Do not provide instructions for cybercrime or unauthorized activity.
- Mention relevant uncertainty.
- Preserve citation details.
- Encourage checking official sources for serious decisions.

---

## Safe answer pattern

A future AI-generated answer should follow this structure:

1. Short answer
2. Plain-language explanation
3. Relevant source context
4. Citation details
5. Official source links
6. Source metadata
7. Important limitation
8. Optional practical checklist
9. Refusal if the source material is insufficient

This keeps the answer useful while preserving transparency.

---

## Refusal behavior

If no trusted source is found, CyberLex should refuse.

Example:

```text
No trusted source was found for this question. CyberLex Sweden only covers selected Swedish and EU cybersecurity law, cybercrime, GDPR, NIS2, incident reporting, DORA, Cyber Resilience Act, EU attacks against information systems, data protection, and related digital compliance topics.
```

The system should refuse:

- unrelated legal areas
- medical advice
- investment advice
- political trivia
- cybercrime instructions
- unauthorized exploitation guidance
- credential theft
- evasion or hiding activity
- unsupported legal claims

The system may explain cybercrime concepts in an educational and lawful context.

---

## Legal and safety risks

Future AI or RAG features introduce risks.

Main risks:

| Risk | Explanation | Mitigation |
|---|---|---|
| Hallucinated legal claims | AI may invent legal obligations | Use retrieved sources only |
| Outdated source material | Local files may become stale | Use source dates and source audit |
| Wrong source retrieval | Similar topics may match incorrectly | Compare retrieval modes and add thresholds |
| Overconfidence | Users may treat answers as legal advice | Keep disclaimers and limitation cards |
| Cyber misuse | Users may ask for harmful technical instructions | Refuse harmful requests |
| Privacy issues | Public deployment may process real questions | Add privacy policy and avoid unnecessary storage |

---

## Minimum requirements before RAG

Before connecting a language model, CyberLex Sweden should have:

- stable source files
- clear source policy
- source audit report
- tested retrieval quality
- reliable vector search or hybrid retrieval
- refusal behavior
- citation display
- visible legal disclaimer
- manual test cases
- updated README and technical design
- privacy and Terms of Use drafts

Most of these are already present in the current prototype, but vector search and RAG are not ready yet.

---

## Recommended implementation order

The future implementation order should be:

1. Install Python 3.12 or 3.11.
2. Rebuild `.venv`.
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
13. Only later consider production deployment.

---

## Current decision

For the current project phase, CyberLex Sweden should keep the stable rule-based prototype.

The vector search and RAG implementation should be postponed until the Python environment is prepared with Python 3.12 or Python 3.11.

This avoids breaking the working prototype close to final delivery.

---

## Summary

CyberLex Sweden is ready for future AI and RAG development, but the current version remains a local source-grounded prototype.

The current system already demonstrates:

- local trusted source files
- source routing
- rule-based retrieval
- Swedish and English interface support
- citation details
- source metadata
- official source links
- source audit
- source update history
- experimental retrieval testing

The next major AI step is real vector search.

After that, CyberLex can move toward RAG-style answer generation, but only if answers remain source-grounded, cautious, and transparent.
