# CyberLex Sweden Vector Search Plan

## Purpose

This document explains the planned vector search upgrade for CyberLex Sweden.

CyberLex Sweden currently uses local Markdown files, source routing, keyword scoring, topic expansion, rule-based answers, and transparent source display.

The next AI improvement is to add real vector search so the app can match questions by meaning, not only by exact keywords.

The goal is not to replace source grounding. The goal is to improve retrieval while keeping CyberLex Sweden transparent, cautious, and limited to trusted local source material.

---

## Current search method

CyberLex Sweden currently uses rule-based local search.

The current search system:

- loads Markdown files from the `data/` folder
- splits the files into source chunks
- cleans the user question into searchable words
- expands important terms with related cybersecurity and legal words
- scores source chunks based on word overlap and section relevance
- routes clear questions to the most relevant source file
- applies topic-specific score boosts and penalties
- returns the best source match and supporting source context

This works well for clear questions, but it still depends heavily on keywords, manually tuned scoring rules, and known question patterns.

The current experimental retrieval module is:

```text
app/vector_search.py
```

Despite the file name, it is not true vector search yet. It does not currently use embeddings, ChromaDB, FAISS, or semantic similarity.

It is better described as an experimental rule-based retrieval engine.

---

## Current retrieval strengths

The current rule-based retrieval has been improved significantly.

It can now correctly route many Swedish and English questions to the right local source file.

Current Swedish examples:

| Topic | Example question | Expected source |
|---|---|---|
| NIS2 law | `Vad är NIS2?` | `nis2_cybersecurity_law.md` |
| Swedish Cybersecurity Act | `Vad är cybersäkerhetslagen?` | `nis2_cybersecurity_law.md` |
| NIS2 risk management | `Vad betyder riskhantering enligt NIS2?` | `nis2_cybersecurity_law.md` |
| Ransomware incident | `Vad ska ett företag göra efter en ransomwareattack?` | `nis2_incident_reporting.md` |
| GDPR breach | `Vad ska ett företag göra efter en personuppgiftsincident?` | `gdpr_personal_data_breach.md` |
| IMY | `Vad är IMY?` | `imy_gdpr_supervision.md` |
| GDPR principles | `Vilka är GDPR-principerna?` | `gdpr_core_principles.md` |
| Dataintrång | `Vad är dataintrång?` | `cybercrime_dataintrang.md` |
| DORA | `Vad är DORA?` | `eu_dora_digital_operational_resilience.md` |
| Cyber Resilience Act | `Vad betyder cybersäkerhetskrav för digitala produkter?` | `eu_cyber_resilience_act.md` |
| EU attacks | `Vad säger EU om attacker mot informationssystem?` | `eu_attacks_against_information_systems.md` |
| EU illegal access | `Vad är olaglig åtkomst enligt EU-regler?` | `eu_attacks_against_information_systems.md` |
| EU DDoS rules | `Vad säger EU om DDoS-attacker?` | `eu_attacks_against_information_systems.md` |

This is good enough for the current prototype stage.

However, this accuracy depends on many hand-written rules. A future system should rely less on manual keyword patches and more on semantic retrieval.

---

## Why vector search is useful

Vector search helps CyberLex Sweden compare meaning instead of only words.

For example, these questions may mean similar things even though they use different wording:

```text
What should a company do after a ransomware attack?
```

```text
What should an organization check after its systems are encrypted by malware?
```

```text
Vad ska ett företag kontrollera efter att skadlig kod låst viktiga system?
```

A keyword system may fail if the exact words do not appear in the source file.

A vector search system can represent both the question and source chunks as embeddings. Embeddings are numeric representations of meaning. Similar meanings should end up close to each other in vector space.

In practical terms, vector search should help CyberLex find the correct source section even when the user writes the question in a different way.

---

## What embeddings are

Embeddings are lists of numbers that represent the meaning of text.

A sentence-transformer model can convert a question or source chunk into a vector.

Example:

```text
Question → embedding vector
Source chunk → embedding vector
```

Then the system compares the question vector with the source chunk vectors.

Chunks with similar meaning should receive higher similarity scores.

This allows CyberLex Sweden to search by semantic meaning instead of exact word matching.

That is the theory. In practice, computers still enjoy disappointing us, so vector search must be tested carefully.

---

## Planned vector search architecture

The planned vector search architecture should use the same local Markdown knowledge base.

The proposed flow:

1. Load Markdown files from `data/`.
2. Split each file into source chunks by heading.
3. Store metadata for each chunk:
   - source filename
   - section heading
   - chunk text
   - official source links
   - source date
   - version notes
4. Generate embeddings for each chunk.
5. Store embeddings in a local vector index.
6. Convert the user question into an embedding.
7. Search for the most similar source chunks.
8. Return ranked results with citations and metadata.
9. Compare vector results with the current rule-based search results.
10. Use source-grounded results only.

The first version should be separate from the main answer system.

It should be used for testing before it affects normal CyberLex answers.

---

## Recommended implementation phases

### Phase 1: Keep current rule-based retrieval stable

Status: Completed for the current prototype phase.

The current retrieval system should remain available as a baseline.

It already supports source routing for:

- NIS2
- GDPR breach
- IMY
- GDPR principles
- dataintrång
- DORA
- Cyber Resilience Act
- EU attacks against information systems
- ransomware and cyber incidents

This system should not be deleted when vector search is added.

It should be used for comparison.

---

### Phase 2: Add vector search dependencies

Add dependencies carefully.

Possible packages:

```text
sentence-transformers
chromadb
```

or:

```text
sentence-transformers
faiss-cpu
```

Recommended first option:

```text
sentence-transformers + ChromaDB
```

Reason:

- ChromaDB is easier to inspect and use locally.
- It can store documents, metadata, and embeddings.
- It is beginner-friendly for a local prototype.

FAISS can be considered later if the project needs a lighter or faster similarity index.

---

### Phase 3: Create a separate vector index script

Create a new script:

```text
scripts/build_vector_index.py
```

Purpose:

- load Markdown files from `data/`
- split them into chunks
- generate embeddings
- save them in a local vector database or index

This script should not run every time the Streamlit app starts.

It should be run manually when the source files change.

Example command:

```powershell
python scripts/build_vector_index.py
```

What the command should do:

- read all trusted Markdown files
- create source chunks
- generate embeddings
- store the index locally
- print how many chunks were indexed

---

### Phase 4: Create a separate vector search module

Create a new module:

```text
app/semantic_search.py
```

Purpose:

- load the saved vector index
- embed the user question
- retrieve similar chunks
- return ranked results with metadata

This should be separate from:

```text
app/vector_search.py
```

Reason:

- `app/vector_search.py` currently contains the rule-based experimental search.
- `app/semantic_search.py` should contain the new embedding-based search.
- Keeping them separate makes testing safer.

The current file name `vector_search.py` is a bit misleading, because it does not yet use vectors. That is tragic, but fixable.

---

### Phase 5: Add retrieval comparison mode

The Streamlit sidebar should eventually include a comparison mode.

Possible display:

```text
Experimental retrieval comparison

Rule-based result:
- source file
- section
- score

Vector result:
- source file
- section
- similarity score
```

This helps compare whether vector search improves retrieval.

The comparison should be tested using the existing manual test cases in:

```text
docs/test_cases.md
```

Important test topics:

- Swedish NIS2 questions
- Swedish ransomware questions
- Swedish GDPR breach questions
- Swedish IMY questions
- Swedish GDPR principle questions
- Swedish dataintrång questions
- Swedish DORA questions
- Swedish CRA questions
- Swedish EU attacks questions

---

### Phase 6: Add minimum similarity thresholds

Vector search should not always return an answer.

If the best similarity score is too low, CyberLex Sweden should refuse to answer or say that no trusted source was found.

This is important because vector search can return something that is vaguely similar but legally wrong.

Possible rule:

```text
If best vector similarity is below threshold, do not generate an answer.
```

The exact threshold should be tested.

The threshold may need to be different depending on the embedding model and vector database.

---

### Phase 7: Keep source grounding mandatory

Vector search must not remove the source-grounding rules.

Every answer must still show:

- matched source file
- matched section
- official source links
- source metadata
- source freshness
- source quality label
- source confidence or similarity explanation
- important legal limitation

CyberLex Sweden should never answer legal or compliance questions from general model memory.

The source material must remain visible.

---

### Phase 8: Later RAG answer generation

Only after vector retrieval is tested should CyberLex Sweden add RAG-style answer generation.

RAG means Retrieval-Augmented Generation.

The idea:

1. Retrieve trusted source chunks.
2. Give those chunks to a language model as context.
3. Ask the model to answer only from that context.
4. Show citations and limitations.
5. Refuse unsupported questions.

The language model should not be allowed to invent legal claims.

A future RAG answer should follow this pattern:

1. Short answer
2. Practical explanation
3. Matched source citation
4. Important limitation
5. Official source links
6. Optional checklist

---

## ChromaDB option

ChromaDB is a local vector database.

It can store:

- document chunks
- embeddings
- metadata
- source filenames
- section names

Possible local folder:

```text
.vector_store/chroma/
```

This folder should probably not be committed to GitHub if it becomes large or machine-specific.

The `.gitignore` file may need to include:

```text
.vector_store/
```

ChromaDB is a good first choice for CyberLex Sweden because it is easier to inspect and use in a local prototype.

---

## FAISS option

FAISS is a vector similarity search library.

It can be fast and lightweight.

However, FAISS usually requires a little more manual metadata handling.

If FAISS is used, CyberLex Sweden would need to store metadata separately, such as in:

```text
.vector_store/metadata.json
.vector_store/faiss.index
```

FAISS may be useful later if the project needs simpler local files or faster search.

For the first prototype, ChromaDB is probably easier.

---

## Recommended embedding model

A practical first embedding model could be:

```text
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
```

Reason:

- supports multiple languages
- useful for Swedish and English questions
- relatively lightweight
- works locally

Another possible model:

```text
intfloat/multilingual-e5-small
```

Reason:

- multilingual
- strong retrieval performance for many tasks
- still manageable for a local prototype

The model should be tested with Swedish and English CyberLex questions.

The selected model should be documented in this file and in the technical design document if used.

---

## Test questions for vector search

Vector search should be tested against the existing known-good retrieval questions.

### Swedish test questions

```text
Vad är NIS2?
Vad är cybersäkerhetslagen?
Vad betyder riskhantering enligt NIS2?
Vad ska ett företag göra efter en ransomwareattack?
Vad ska ett företag göra efter en personuppgiftsincident?
Vad är IMY?
Vilka är GDPR-principerna?
Vad betyder uppgiftsminimering?
Vad är dataintrång?
Är obehörig åtkomst olagligt i Sverige?
Vad är DORA?
Vad betyder digital operativ motståndskraft?
Vad betyder tredjepartsrisk enligt DORA?
Vad är Cyber Resilience Act?
Vad betyder cybersäkerhetskrav för digitala produkter?
Vad säger CRA om säkerhetsuppdateringar?
Vad säger EU om attacker mot informationssystem?
Vad är olaglig åtkomst enligt EU-regler?
Vad säger EU om DDoS-attacker?
```

### English test questions

```text
What is NIS2?
What is the Swedish Cybersecurity Act?
What should a company do after a ransomware attack?
When must a personal data breach be reported?
What is IMY?
What are the GDPR principles?
Is unauthorized access illegal in Sweden?
What is DORA?
What is third-party ICT risk under DORA?
What is the Cyber Resilience Act?
What does the Cyber Resilience Act say about security updates?
What does EU law say about attacks against information systems?
What is illegal access under EU cybercrime rules?
What does EU law say about DDoS attacks?
```

---

## Evaluation criteria

Vector search should be judged by whether it improves retrieval without weakening safety.

Good vector search should:

- return the correct source file
- return a useful section, not only an official source or metadata section
- work in both Swedish and English
- avoid confusing NIS2, DORA, GDPR, CRA, and cybercrime topics
- refuse or warn when the match is weak
- preserve citations and source metadata
- not answer from unsupported material

Bad vector search would:

- return vague but wrong source chunks
- confuse similar legal frameworks
- hide source traceability
- answer outside the trusted knowledge base
- make the app look more intelligent while becoming less reliable

That last one is the classic AI trap: more confidence, less truth. Very fashionable, very cursed.

---

## Safety requirements

CyberLex Sweden deals with legal and cybersecurity topics.

The vector search upgrade must preserve safety rules.

Requirements:

- refuse out-of-scope questions
- refuse harmful cybercrime instructions
- keep legal disclaimer visible
- show official sources
- show source metadata
- show source freshness
- keep answers educational
- avoid claiming legal certainty
- avoid giving exploit instructions
- avoid replacing legal advice
- avoid answering without trusted source support

Vector search should improve retrieval, not expand the system beyond its intended scope.

---

## Files likely to be added

Potential new files:

```text
scripts/build_vector_index.py
app/semantic_search.py
```

Potential updated files:

```text
requirements.txt
app/main.py
app/vector_search.py
docs/technical_design.md
docs/test_cases.md
docs/product_roadmap.md
.gitignore
```

Potential local generated folder:

```text
.vector_store/
```

The generated vector store should normally not be committed to GitHub unless there is a clear reason.

---

## Suggested first implementation step

The first implementation step should be small and reversible.

Recommended first step:

1. Add `sentence-transformers` and `chromadb` to `requirements.txt`.
2. Create `scripts/build_vector_index.py`.
3. Build a local ChromaDB index from the Markdown chunks.
4. Create `app/semantic_search.py`.
5. Test semantic search from the terminal.
6. Only after terminal testing works, add a Streamlit sidebar comparison.

Do not connect vector search to the main answer system immediately.

The main answer system should remain stable until semantic retrieval has been tested.

---

## Summary

CyberLex Sweden currently has a strong rule-based retrieval prototype with improved Swedish and English source routing.

The next major technical upgrade is real vector search.

Vector search should help the app retrieve source sections by meaning, but it must remain source-grounded, transparent, and cautious.

The recommended approach is to add vector search as a separate test mode first, compare it against the current rule-based retrieval, and only later connect it to the main answer system.

Better retrieval first. RAG later.

Better sources always.
