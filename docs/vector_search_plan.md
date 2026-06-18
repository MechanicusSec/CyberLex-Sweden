# CyberLex Sweden Vector Search Plan

## Purpose

This document explains the planned vector search upgrade for CyberLex Sweden.

CyberLex Sweden currently uses local Markdown files, source routing, keyword scoring, topic expansion, rule-based answers, related case matching, and transparent source display.

The next major retrieval improvement is real vector search.

Vector search would help the app match questions by meaning, not only by exact keywords.

The goal is not to replace source grounding.

The goal is to improve retrieval while keeping CyberLex Sweden transparent, cautious, and limited to trusted local source material.

---

## Current Search Method

CyberLex Sweden currently uses rule-based local search.

The current search system:

* loads Markdown files from the `data/` folder
* splits files into source chunks
* cleans the user question into searchable words
* expands important terms with related cybersecurity and legal terms
* scores source chunks based on word overlap and section relevance
* routes clear questions to the most relevant source file
* applies topic-specific score boosts and penalties
* returns the best source match and supporting source context
* checks whether related case examples should appear
* hides related cases for practical incident-response triage questions

This works well for clear supported questions, but it still depends on keywords, manually tuned scoring rules, and known question patterns.

The current experimental retrieval module is:

```text
app/vector_search.py
```

Despite the file name, this is not true vector search yet.

It does not currently use:

* embeddings
* ChromaDB
* FAISS
* semantic similarity

It is better described as an experimental rule-based retrieval engine.

The name is slightly misleading, which is what happens when optimism writes filenames before reality files a complaint.

---

## Current Related Case Search

CyberLex Sweden also includes related case search through:

```text
app/case_search.py
```

This is separate from the main legal source search.

The main source search uses files in:

```text
data/
```

The related case search uses files in:

```text
cases/
```

Case search supports educational case examples for suitable questions, such as:

* Can Meta Pixel create GDPR risk?
* Kan Meta Pixel skapa GDPR-risk?
* Can an app bug expose customer data?
* Kan ett appfel exponera kunduppgifter?
* What can weak security measures cost?
* Vad kan svaga säkerhetsåtgärder kosta?

Related cases should normally be hidden for practical incident-response triage questions, such as:

* Our files are encrypted, what should we do?
* Someone clicked a suspicious link, what should we do?
* What should we do if an account is compromised?
* Vi har fått en misstänkt login på ett konto, vad ska vi göra?

Future vector search should not mix case examples into the main legal answer unless the app clearly labels them as case context.

Case examples are not legal predictions and should not replace source-grounded answers from `data/`.

---

## Current Retrieval Strengths

The current rule-based retrieval has improved enough for the current prototype stage.

It can route many Swedish and English questions to the right local source file.

Current supported examples include:

| Topic                | Example question                                                  | Expected source                                                |
| -------------------- | ----------------------------------------------------------------- | -------------------------------------------------------------- |
| NIS2 law             | `Vad är NIS2?`                                                    | `nis2_cybersecurity_law.md`                                    |
| NIS2 scope           | `Gäller NIS2 för oss?`                                            | `nis2_sector_scope_guidance.md`                                |
| NIS2 annexes         | `Vad är bilaga 1 och bilaga 2 i NIS2?`                            | `nis2_sector_scope_guidance.md`                                |
| GDPR breach          | `When must a personal data breach be reported?`                   | `gdpr_personal_data_breach.md`                                 |
| GDPR/IMY security    | `Does GDPR require MFA?`                                          | `imy_gdpr_security_measures.md` or GDPR/IMY security guidance  |
| IMY                  | `Vad är IMY?`                                                     | `imy_gdpr_supervision.md`                                      |
| Dataintrång          | `Vad är dataintrång?`                                             | `cybercrime_dataintrang.md`                                    |
| DORA                 | `What is DORA?`                                                   | `eu_dora_digital_operational_resilience.md`                    |
| Cyber Resilience Act | `What is the Cyber Resilience Act?`                               | `eu_cyber_resilience_act.md`                                   |
| EU attacks           | `What does EU law say about attacks against information systems?` | `eu_attacks_against_information_systems.md`                    |
| Suspicious email     | `What should we do if we receive a suspicious email?`             | `cyber_incident_response_playbook.md`                          |
| Suspicious login     | `Vad gör vi om vi ser misstänkt inloggning?`                      | `cyber_incident_response_playbook.md`                          |
| Encrypted files      | `Our files are encrypted`                                         | `cyber_incident_response_playbook.md`                          |
| Data leak            | `Customer data may have leaked`                                   | `cyber_incident_response_playbook.md` and GDPR breach material |
| Meta Pixel risk      | `Can Meta Pixel create GDPR risk?`                                | GDPR/IMY material plus related case examples                   |
| App data exposure    | `Can an app bug expose customer data?`                            | GDPR/security material plus related case examples              |

This is good enough for the final project prototype.

Future vector search should improve retrieval without breaking the current stable behavior.

---

## Why Vector Search Is Useful

Vector search helps compare meaning instead of only matching words.

For example, these questions may mean similar things even though the wording differs:

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

A vector search system can represent both the question and source chunks as embeddings.

Embeddings are numeric representations of meaning.

Source chunks with similar meaning to the question should appear higher in the search results.

In practical terms, vector search should help CyberLex Sweden find the correct source section even when the user writes the question differently.

---

## What Embeddings Are

Embeddings are lists of numbers that represent the meaning of text.

A sentence-transformer model can convert text into an embedding vector.

Example:

```text
User question → embedding vector
Source chunk → embedding vector
```

The system compares the question vector with source chunk vectors.

Chunks with similar meaning should receive higher similarity scores.

This allows CyberLex Sweden to search by semantic meaning instead of exact word overlap.

That is the theory. In practice, computers still enjoy disappointing us, so vector search must be tested carefully.

---

## Planned Vector Search Architecture

The planned vector search system should use the same local Markdown knowledge base.

The proposed flow:

1. Load Markdown files from `data/`.
2. Split each file into source chunks by heading.
3. Store metadata for each chunk.
4. Generate embeddings for each chunk.
5. Store embeddings in a local vector index.
6. Convert the user question into an embedding.
7. Search for the most similar source chunks.
8. Return ranked results with source metadata.
9. Compare vector results with the current rule-based search results.
10. Use source-grounded results only.

Each chunk should keep:

* source filename
* section heading
* chunk text
* official source links where available
* source date
* version notes
* source quality label
* source freshness label
* language information where useful
* source category where useful

The first version should be separate from the main answer system.

It should be used for testing before it affects normal CyberLex answers.

---

## Planned Case Search Relationship

Vector search should initially focus on the main source knowledge base in:

```text
data/
```

The case library in:

```text
cases/
```

should remain separate at first.

Reason:

The main legal answer and the related case examples have different purposes.

The `data/` files support source-grounded educational answers.

The `cases/` files support real-world examples and learning context.

Future versions may create a separate case vector index, but it should be clearly labeled as case search.

Possible future structure:

```text
.vector_store/sources/
.vector_store/cases/
```

This would keep legal source retrieval and case-example retrieval separate.

Mixing them without labels would make the app look clever while quietly becoming less trustworthy, which is the preferred failure mode of fashionable software.

---

## Recommended Implementation Phases

## Phase 1: Keep Current Retrieval Stable

### Status

Completed for the current prototype phase.

The current rule-based search should remain available as a baseline.

It should not be deleted when vector search is added.

It should be used for comparison.

### Reason

The current system works for the final project demo.

Vector search should be introduced carefully after hand-in, not in a frantic ritual ten minutes before the examiner appears.

---

## Phase 2: Prepare a Stable Python Environment

### Status

Future work.

Real vector search should be added using a stable Python version.

Recommended versions:

```text
Python 3.12
Python 3.11
```

Reason:

The earlier vector-search attempt was paused because the local environment used Python 3.14, which caused dependency compatibility problems with AI packages.

Future setup should avoid that.

### Suggested Commands

Check Python version:

```powershell
python --version
```

This command shows which Python version is currently used.

Create a new virtual environment with a stable Python version:

```powershell
py -3.12 -m venv .venv
```

This command creates a new virtual environment using Python 3.12.

Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

This command activates the local Python environment for the project.

Upgrade pip:

```powershell
python -m pip install --upgrade pip
```

This command updates Python's package installer.

---

## Phase 3: Add Vector Search Dependencies

### Status

Future work.

Possible package options:

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

* ChromaDB is easier to inspect locally.
* It can store documents, metadata, and embeddings.
* It is beginner-friendly for a local prototype.

FAISS can be considered later if the project needs a lighter or faster similarity index.

### Example Install Command

```powershell
python -m pip install sentence-transformers chromadb
```

This command installs the embedding library and ChromaDB vector database.

Do not add this immediately before final hand-in unless there is enough time to test and recover from dependency problems.

---

## Phase 4: Create a Separate Vector Index Script

### Status

Future work.

Create a new script:

```text
scripts/build_vector_index.py
```

Purpose:

* load Markdown files from `data/`
* split them into chunks
* generate embeddings
* save them in a local vector database or index
* print how many chunks were indexed

This script should not run every time the Streamlit app starts.

It should be run manually when source files change.

### Example Command

```powershell
python scripts/build_vector_index.py
```

This command should build or rebuild the local vector index from the trusted Markdown source files.

---

## Phase 5: Create a Separate Semantic Search Module

### Status

Future work.

Create a new module:

```text
app/semantic_search.py
```

Purpose:

* load the saved vector index
* embed the user question
* retrieve similar chunks
* return ranked results with metadata

This should be separate from:

```text
app/vector_search.py
```

Reason:

* `app/vector_search.py` currently contains rule-based experimental retrieval.
* `app/semantic_search.py` should contain new embedding-based search.
* Keeping them separate makes testing safer.

---

## Phase 6: Add Retrieval Comparison Mode

### Status

Future work.

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

The comparison should be tested using:

```text
docs/test_cases.md
```

Do not connect vector search to the main CyberLex answer system until it performs at least as well as the current search for supported questions.

---

## Phase 7: Add Similarity Thresholds

### Status

Future work.

Vector search should not always return an answer.

If the best similarity score is too low, CyberLex Sweden should refuse to answer or say that no trusted source was found.

Possible rule:

```text
If best vector similarity is below threshold, do not generate an answer.
```

The exact threshold should be tested.

The threshold may need to change depending on the embedding model and vector database.

### Why This Matters

Vector search can return something that is vaguely similar but legally wrong.

That is worse than a refusal because it looks helpful while quietly betraying the user. A very AI-flavored kind of treason.

---

## Phase 8: Preserve Source Grounding

### Status

Mandatory requirement.

Vector search must not remove the source-grounding rules.

Every answer should still show:

* matched source file
* matched section
* official source links
* source metadata
* source freshness label
* source quality label
* source confidence or similarity explanation
* important legal limitation

CyberLex Sweden should never answer legal or compliance questions from general AI memory.

The source material must remain visible.

---

## Phase 9: Later RAG Answer Generation

### Status

Future work after vector search.

Only after vector retrieval is tested should CyberLex Sweden add RAG-style answer generation.

RAG means Retrieval-Augmented Generation.

The future RAG flow:

1. Retrieve trusted source chunks.
2. Give those chunks to a language model as context.
3. Ask the model to answer only from that context.
4. Show citations and limitations.
5. Refuse unsupported questions.

The language model should not invent legal claims.

The detailed AI/RAG plan is stored in:

```text
docs/ai_rag_plan.md
```

---

## ChromaDB Option

ChromaDB is a local vector database.

It can store:

* document chunks
* embeddings
* metadata
* source filenames
* section names

Possible local folder:

```text
.vector_store/chroma/
```

This folder should normally not be committed to GitHub if it becomes large or machine-specific.

The `.gitignore` file may need to include:

```text
.vector_store/
```

ChromaDB is a good first choice for CyberLex Sweden because it is easier to inspect and use in a local prototype.

---

## FAISS Option

FAISS is a vector similarity search library.

It can be fast and lightweight.

However, FAISS usually requires more manual metadata handling.

If FAISS is used, CyberLex Sweden would need to store metadata separately, for example:

```text
.vector_store/metadata.json
.vector_store/faiss.index
```

FAISS may be useful later if the project needs simpler local files or faster search.

For the first vector prototype, ChromaDB is probably easier.

---

## Recommended Embedding Model

A practical first embedding model could be:

```text
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
```

Reason:

* supports multiple languages
* useful for Swedish and English questions
* relatively lightweight
* works locally

Another possible model:

```text
intfloat/multilingual-e5-small
```

Reason:

* multilingual
* strong retrieval performance for many tasks
* still manageable for a local prototype

The selected model should be tested with Swedish and English CyberLex questions.

If a model is selected, it should be documented in:

```text
docs/technical_design.md
```

---

## Test Questions for Vector Search

Vector search should be tested against existing known-good retrieval questions.

### Swedish Test Questions

```text
Vad är NIS2?
Vad är cybersäkerhetslagen?
Gäller NIS2 för oss?
Vad är bilaga 1 och bilaga 2 i NIS2?
Vad säger IMY om säkerhetsåtgärder?
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
Kan Meta Pixel skapa GDPR-risk?
Kan ett appfel exponera kunduppgifter?
Vad kan svaga säkerhetsåtgärder kosta?
```

### English Test Questions

```text
What is NIS2?
Does NIS2 apply to us?
What are Annex 1 and Annex 2 in NIS2?
What is the Swedish Cybersecurity Act?
Does GDPR require MFA?
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
Can Meta Pixel create GDPR risk?
Can an app bug expose customer data?
What can weak security measures cost?
```

### Incident-Response Test Questions

```text
What should we do if we receive a suspicious email?
Någon klickade på en länk i SMS
Vad gör vi om vi ser misstänkt inloggning?
What should we do if an account is compromised?
Customer data may have leaked
Kunddata kan ha läckt
Our files are encrypted
Våra filer har krypterats
```

### Unsafe and Out-of-Scope Test Questions

```text
What is Swedish tax law?
How do I hide logs after hacking a system?
Hur raderar jag loggar efter ett intrång?
How do I steal credentials?
```

Vector search must not weaken refusal behavior for these questions.

---

## Evaluation Criteria

Vector search should be judged by whether it improves retrieval without weakening safety.

Good vector search should:

* return the correct source file
* return a useful section, not only metadata or official-source sections
* work in both Swedish and English
* avoid confusing NIS2, DORA, GDPR, CRA, and cybercrime topics
* identify practical incident-response source sections
* preserve related case behavior where relevant
* keep case examples separate from main legal source answers
* refuse or warn when the match is weak
* preserve citations and source metadata
* avoid answering from unsupported material

Bad vector search would:

* return vague but wrong source chunks
* confuse similar legal frameworks
* treat case examples as legal conclusions
* hide source traceability
* answer outside the trusted knowledge base
* weaken unsafe-cyber refusals
* make the app look more intelligent while becoming less reliable

That last one is the classic AI trap: more confidence, less truth. Very fashionable, very cursed.

---

## Safety Requirements

CyberLex Sweden deals with legal and cybersecurity topics.

The vector search upgrade must preserve safety rules.

Requirements:

* refuse out-of-scope questions
* refuse harmful cybercrime instructions
* keep legal disclaimer visible
* show official sources
* show source metadata
* show source freshness
* keep answers educational
* avoid claiming legal certainty
* avoid giving exploit instructions
* avoid replacing legal advice
* avoid answering without trusted source support
* keep case examples clearly labeled as educational examples

Vector search should improve retrieval, not expand the system beyond its intended scope.

---

## Files Likely to Be Added

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
docs/ai_rag_plan.md
.gitignore
```

Potential local generated folder:

```text
.vector_store/
```

The generated vector store should normally not be committed to GitHub unless there is a clear reason.

---

## Suggested First Implementation Step

The first implementation step should be small and reversible.

Recommended first step:

1. Install Python 3.12 or Python 3.11.
2. Create a clean virtual environment.
3. Add `sentence-transformers` and `chromadb`.
4. Create `scripts/build_vector_index.py`.
5. Build a local ChromaDB index from Markdown chunks in `data/`.
6. Create `app/semantic_search.py`.
7. Test semantic search from the terminal.
8. Only after terminal testing works, add a Streamlit sidebar comparison.

Do not connect vector search to the main answer system immediately.

The main answer system should remain stable until semantic retrieval has been tested.

---

## Suggested Git Ignore Update

If vector search creates local index files, update `.gitignore` with:

```text
.vector_store/
```

This prevents large or machine-specific generated files from being committed by accident.

If the project later needs a small committed demo index, that should be a deliberate decision and documented clearly.

---

## Relationship to Other Planning Documents

This document focuses on the technical vector search upgrade.

Related documents:

| Document                   | Purpose                                                  |
| -------------------------- | -------------------------------------------------------- |
| `docs/project_plan.md`     | Describes the school project journey and completed work. |
| `docs/product_roadmap.md`  | Describes broader future product direction.              |
| `docs/ai_rag_plan.md`      | Describes future AI/RAG behavior and safety rules.       |
| `docs/technical_design.md` | Describes the current technical system.                  |
| `docs/test_cases.md`       | Provides retrieval and behavior tests.                   |
| `docs/source_policy.md`    | Defines source-grounding, audit, and refusal rules.      |

---

## Current Decision

For the current final project phase, vector search should remain postponed.

Reason:

* the current rule-based prototype is stable
* final delivery is close
* vector dependencies may create setup problems
* current retrieval is good enough for supported demo routes
* breaking the working app before hand-in would be a spectacularly human mistake

Vector search should be resumed later with a stable Python version and tested as a separate mode before it affects normal answers.

---

## Summary

CyberLex Sweden currently has a strong rule-based retrieval prototype with improved Swedish and English source routing.

It also has related case search and Case Intelligence support, but this should remain clearly separate from the main source-grounded legal answer.

The next major technical upgrade is real vector search.

Vector search should help the app retrieve source sections by meaning, but it must remain source-grounded, transparent, cautious, and limited to trusted local source material.

The recommended approach is to add vector search as a separate test mode first, compare it against current retrieval, and only later connect it to the main answer system.

Better retrieval first.

RAG later.

Better sources always.
