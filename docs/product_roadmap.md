# CyberLex Sweden Product Roadmap

## Purpose

This roadmap explains how CyberLex Sweden can develop from a school prototype into a more realistic legal-tech and cybersecurity compliance assistant.

CyberLex Sweden is currently an educational prototype. The roadmap is not a promise that every feature will be built, but it describes a realistic development path.

The goal is to make the project more structured, more trustworthy, easier to expand, and easier to explain.

---

## Current Status

CyberLex Sweden currently works as a local Streamlit application.

The current prototype includes:

- Local Markdown knowledge base in `data/`
- Source-based search and chunk ranking
- Source routing for clear topic questions
- Improved Swedish retrieval for supported topics
- Experimental retrieval module in `app/vector_search.py`
- Styled important limitation card
- Styled relevant source context cards
- Official source links with readable Markdown labels
- Source date and version notes
- Source metadata display
- Source quality labels
- Source freshness labels
- Source match confidence note
- Bilingual interface support for English and Swedish
- Styled other matching source section cards
- Auto language detection for user questions
- Styled assessment checklist card
- Rule-based short answers
- CyberLex attention level with styled status card
- Practical explanation section
- Topic-based assessment checklist
- Collapsible source context
- Styled official source links card
- Other matching source sections list
- Clickable example questions using Streamlit session state
- Sidebar prototype version label
- Sidebar future AI mode note
- Styled practical explanation card
- Styled source metadata card
- Legal limitation notice
- Refusal behavior for out-of-scope questions
- Source audit script in `scripts/source_audit.py`
- Metadata helper script in `scripts/add_missing_metadata.py`
- Weekly GitHub Actions source audit workflow
- Manual test cases in `docs/test_cases.md`
- Technical design documentation in `docs/technical_design.md`
- Source update history in `docs/source_update_history.md`

The current system does not yet use true vector search, semantic embeddings, ChromaDB, FAISS, a full language model, public deployment, or a production database.

These features make the current version a transparent, source-grounded educational prototype.

---

## Completed Milestone: Prototype Version 0.5

Prototype version **0.5** focused on improving the user experience, answer structure, and readability of CyberLex Sweden.

This version upgraded the app from a basic source-answer layout into a more structured interface with separate styled cards.

Completed improvements:

- Styled citation details card
- Styled official source links card
- Styled source metadata card
- Styled important limitation warning card
- Styled CyberLex attention level card
- Styled practical explanation card
- Styled assessment checklist card
- Styled relevant source context cards
- Styled other matching source section cards
- Improved readability of source-grounded answers
- Clearer separation between answer, source, limitation, and practical guidance sections
- Improved bilingual interface support
- Better presentation of source context and official references

This version keeps the app as a local, rule-based prototype. A full AI/RAG mode is still planned for a later version.

---

## Completed Milestone: Source and Retrieval Improvement Phase

### Status

Completed on 2026-06-03.

### Goal

Improve the trusted local source files and strengthen experimental retrieval so Swedish and English questions route to more accurate knowledge files.

### Completed Source Improvements

The following local source files were improved, cleaned, expanded, or tested:

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

Completed improvements included:

- Swedish summaries added or improved
- Swedish useful questions added
- Stronger practical explanations added
- Stronger assessment checklists added
- Official source links cleaned or added
- Source metadata standardized
- Duplicate metadata sections removed where needed
- DORA support expanded
- Cyber Resilience Act support expanded
- EU attacks against information systems support expanded
- GDPR personal data breach support improved
- GDPR core principles support improved
- IMY authority support improved
- NIS2 cybersecurity law support improved
- NIS2 incident reporting support improved
- Swedish dataintrång support improved

### Completed Retrieval Improvements

The experimental retrieval module in:

```text
app/vector_search.py
```

was improved so Swedish questions route more accurately.

Current expected routing examples:

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
| EU attacks against information systems | `Vad säger EU om attacker mot informationssystem?` | `eu_attacks_against_information_systems.md` |
| EU illegal access | `Vad är olaglig åtkomst enligt EU-regler?` | `eu_attacks_against_information_systems.md` |
| EU DDoS rules | `Vad säger EU om DDoS-attacker?` | `eu_attacks_against_information_systems.md` |

### Why This Phase Matters

This phase improved the quality of the project before adding real AI features.

The design principle is:

```text
Better sources first. Better AI second.
```

A future AI or RAG system will only be useful if the sources are structured, testable, and reliable.

---

## Phase 1: Prototype Foundation

### Status

Completed.

### Goal

Build a working local prototype that proves the core idea.

### Completed Features

- Streamlit web interface
- Local Markdown knowledge base
- Source-based search
- Chunk-based search
- Styled citation details card
- Source routing
- Styled assessment checklist card
- Simple answer generation
- Styled other matching source section cards
- Official source links
- Source metadata
- Citation details
- Practical explanations
- Styled relevant source context cards
- Assessment checklists
- Styled attention level card
- Clickable example questions
- Styled important limitation card
- Future AI mode sidebar note
- Prototype version label
- Source update history
- Manual test cases
- Final report draft
- Source policy
- Legal disclaimer draft
- Terms of Use draft
- Privacy Policy draft
- Source match confidence note
- Source audit system
- GitHub Actions audit workflow

### Purpose

This phase proves that CyberLex Sweden can answer selected cybersecurity-law questions using trusted local source material.

---

## Phase 2: Source Expansion and Source Quality

### Status

Core source improvement phase completed. Future expansion remains open.

### Goal

Keep expanding the trusted knowledge base with more Swedish and EU cybersecurity law sources while maintaining source quality.

### Completed Source Areas

CyberLex Sweden currently includes local source support for:

- GDPR core principles
- GDPR personal data breach notification
- IMY GDPR supervision
- NIS2 and Swedish cybersecurity law
- NIS2 incident reporting
- Swedish cybercrime and dataintrång
- DORA and digital operational resilience
- Cyber Resilience Act and product cybersecurity
- EU attacks against information systems

### Planned Future Source Areas

Possible future source areas include:

- Additional GDPR guidance
- More IMY guidance
- NIS2 sector-specific information
- Swedish Cybersecurity Act updates when official Swedish implementation details change
- DORA technical standards and guidance
- EU Cybersecurity Act and ENISA certification
- Protective Security Act, `säkerhetsskyddslagen`
- Electronic communications security rules
- AI Act cybersecurity and compliance connections
- EDPB guidance on security and data protection
- Cybersecurity procurement and supplier security guidance
- Swedish public-sector cybersecurity guidance

### Requirements for New Sources

Each new knowledge file should include:

- topic
- main authority or legal source
- key idea
- important points
- cybersecurity connection
- useful questions
- Swedish summary if relevant
- Swedish useful questions if relevant
- official source links
- source metadata
- source date
- version notes
- disclaimer

### Success Criteria

This phase is successful when CyberLex Sweden can answer more questions while still showing citation details and refusing unsupported topics.

---

## Phase 3: Better Source Management

### Status

Partly completed.

### Completed Improvements

- Source metadata standardization
- Source audit script
- Source audit report
- Metadata helper script
- Source update history document
- Weekly GitHub Actions source audit workflow
- Official source link cleanup
- Source review dates stored in Markdown files

### Goal

Make source handling more reliable and easier to maintain.

### Planned Improvements

- Add a source update checklist
- Add source categories
- Add source status values, such as active, needs review, outdated
- Add source version history per source file
- Add source owner or reviewer field
- Add link-checking process
- Add a clear method for retiring outdated sources
- Add a manual legal-currentness review process
- Add periodic review tasks for high-priority legal sources

### Why This Matters

Legal and cybersecurity information changes over time.

A real system must show when sources were checked and whether they are still reliable.

The current source audit checks structure, not live legal currency.

Without source management, the system may eventually give outdated answers.

---

## Phase 4: Real Vector Search

### Status

Next major technical phase.

### Goal

Improve retrieval quality beyond simple keyword matching and rule-based topic boosts.

### Planned Improvements

- Add `sentence-transformers`
- Generate embeddings for source chunks
- Store chunk embeddings locally
- Add vector search with ChromaDB or FAISS
- Keep source metadata connected to each chunk
- Compare vector search results with current keyword and routing logic
- Add retrieval mode comparison:
  - current main search
  - experimental keyword/rule-based search
  - vector search
- Add minimum confidence thresholds
- Improve refusal behavior for weak matches
- Preserve mandatory source grounding

### ChromaDB Option

ChromaDB could be used as a local vector database.

It would store document chunks and embeddings, making it possible to search by semantic similarity.

This may be easier to inspect and maintain during development.

### FAISS Option

FAISS could be used as a lightweight local vector search engine.

It may be useful if the project needs fast similarity search without a larger database system.

### Success Criteria

This phase is successful when CyberLex Sweden can find the correct source section even when the user does not use the exact same words as the source file.

The system should still display:

- matched source file
- matched section
- relevance or similarity score
- official source links
- source metadata
- source confidence explanation
- limitation notice

---

## Phase 5: Language Model Integration and RAG

### Status

Future phase.

### Goal

Connect a language model to generate better natural language answers.

### Important Rule

The language model should not answer freely from memory.

It should only answer using retrieved source chunks from the trusted CyberLex knowledge base.

### Planned Improvements

- Use retrieved source chunks as context
- Generate clearer answers from source material
- Include citation details in every answer
- Refuse unsupported questions
- Add prompt rules for legal safety
- Prevent unsupported legal claims
- Avoid cybercrime instructions
- Keep disclaimers visible
- Keep source links visible
- Add multi-source answer synthesis
- Add answer traceability to specific source chunks

### Safe Answer Pattern

A future language model answer should follow this pattern:

1. Short answer
2. Explanation
3. Source citation
4. Source context
5. Important limitation
6. Recommendation to check official sources for serious decisions

### Success Criteria

This phase is successful when answers become easier to read while still remaining source-grounded, cautious, and transparent.

---

## Phase 6: User Experience and Visual Design

### Status

Partly completed.

### Goal

Make CyberLex Sweden look more professional and easier to use.

### Completed UX Improvements

- Main page header
- Supported topic badges
- Styled source metadata card
- Sidebar project resources
- Prototype version label
- Future AI mode sidebar note
- Styled important limitation card
- Styled other matching source section cards
- Styled citation details card
- Styled assessment checklist card
- Styled relevant source context cards
- Styled official source links card
- Clickable example questions
- Styled practical explanation card
- Collapsible assessment checklist
- Collapsible source context
- Styled CyberLex attention level card
- Bilingual interface controls
- Experimental search sidebar

### Planned Improvements

- Better source cards
- Better citation cards
- Improved mobile layout
- More polished cybersecurity/legal-tech visual identity
- Better screenshot-ready interface for final presentation
- Better empty-state messages
- Better onboarding text
- Clearer explanation of prototype limitations
- Improved sidebar organization

### Possible UI Sections

- Ask CyberLex
- Supported topics
- Citation details
- Source context
- Assessment checklist
- Knowledge base status
- Legal disclaimer
- Source audit status
- Retrieval mode status

### Success Criteria

This phase is successful when a user can understand what the app does without needing personal guidance from the developer.

---

## Phase 7: Public Deployment Preparation

### Status

Future phase.

### Goal

Prepare CyberLex Sweden for possible public deployment.

### Required Work Before Deployment

- Review Terms of Use
- Review Privacy Policy
- Review Legal Disclaimer
- Decide whether user questions are stored
- Decide whether analytics are used
- Decide whether external AI APIs are used
- Add secure configuration handling
- Avoid exposing secrets or API keys
- Add deployment documentation
- Add basic logging policy
- Add security review checklist
- Add abuse-prevention rules
- Add rate limiting if public
- Add clear contact/support information if public

### Possible Deployment Options

- Streamlit Community Cloud
- Render
- Railway
- Azure App Service
- AWS
- Hetzner
- Docker-based deployment

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

- Keep copyright notices
- Avoid adding an open-source license unless intentionally chosen
- Create stronger Terms of Use
- Create stronger Privacy Policy
- Create stronger disclaimer
- Consider registering the CyberLex Sweden name as a trademark
- Consider logo and brand protection
- Check for name conflicts before trademark registration
- Review whether public use requires legal review from a qualified lawyer
- Review whether the project should include stronger non-advice wording

### Trademark Note

If CyberLex Sweden becomes a serious product, trademark protection may be useful for the name and brand identity.

This should be handled later, when the project has clearer long-term value.

### Success Criteria

This phase is successful when the project has a clear identity, ownership notice, and legal protection plan.

---

## Phase 9: Real Product Direction

### Status

Future decision phase.

### Goal

Decide whether CyberLex Sweden should remain a portfolio project or become a real product concept.

### Possible Product Directions

- Bilingual Swedish and English cybersecurity law assistant
- Student portfolio project
- Cybersecurity law learning tool
- Compliance assistant prototype
- Internal company knowledge assistant
- Swedish cyber law research assistant
- Legal-tech startup concept

### Questions to Answer

- Who is the target user?
- What problem does CyberLex solve better than existing sources?
- How should CyberLex Sweden support both Swedish and English as main languages?
- Should it answer only from official sources?
- Should it store user questions?
- Should it use a cloud language model?
- How should source updates be reviewed?
- What legal review is required before public use?
- Should CyberLex remain a local/offline assistant or become a hosted product?
- Which sectors should be prioritized first?

### Success Criteria

This phase is successful when the project has a clear direction and realistic next steps.

---

## Language Support Plan

### Goal

CyberLex Sweden should support both English and Swedish as main languages.

English is useful for project documentation, technical development, GitHub presentation, and international cybersecurity terminology.

Swedish is important because many legal sources, authority pages, laws, and real users in Sweden use Swedish.

### Current Language Support

CyberLex Sweden currently supports:

- English interface mode
- Swedish interface mode
- Auto language mode
- English user questions
- Swedish user questions
- English answer headings
- Swedish answer headings
- Swedish and English example questions
- Swedish source summaries in key knowledge files
- Swedish retrieval routing for supported topics
- Swedish useful questions in many source files

### Planned Language Support

CyberLex Sweden should eventually support:

- Better Swedish answer generation
- Better English explanations of Swedish legal terms
- Source citations in the original source language
- More bilingual source summaries
- More Swedish legal terminology support
- More consistent bilingual source metadata
- Better handling of mixed Swedish and English questions

### Example Questions

English examples:

```text
What is IMY?
What is NIS2 incident reporting?
What is DORA?
When must a personal data breach be reported?
Can an incident need to be reported under both NIS2 and GDPR?
What is the Cyber Resilience Act?
What does EU law say about attacks against information systems?
```

Swedish examples:

```text
Vad är IMY?
Vad är NIS2?
Vad är DORA?
När måste en personuppgiftsincident rapporteras?
Kan en incident behöva rapporteras enligt både NIS2 och GDPR?
Vad betyder cybersäkerhetskrav för digitala produkter?
Vad säger EU om attacker mot informationssystem?
```

---

## Risk Overview

| Risk | Explanation | Mitigation |
|---|---|---|
| Outdated legal sources | Laws and guidance can change | Add source review dates, source history, and manual review routines |
| Unsupported answers | The system may answer without enough evidence | Use scope checks, source routing, and refusal behavior |
| Wrong source match | Similar legal topics may confuse search | Use source routing, retrieval tests, and later vector search |
| Overreliance by users | Users may treat answers as legal advice | Keep disclaimers and Terms of Use clear |
| Privacy issues | Public deployment may process user input | Add Privacy Policy and avoid storing sensitive data |
| Cyber misuse | Users may ask harmful cybercrime questions | Refuse harmful or out-of-scope questions |
| Brand copying | Others may copy the name or concept | Keep copyright notice and consider trademark later |
| False legal currency | Users may assume sources are live-updated | Explain that audit checks local structure, not live legal changes |
| AI hallucination risk | Future AI mode may generate unsupported statements | Require source-grounded RAG and refusal rules |

---

## Near-Term Roadmap

The next practical steps are:

1. Review and commit updated roadmap documentation.
2. Update any remaining documentation that still describes DORA, CRA, or EU attacks as future work only.
3. Prepare a real vector search implementation plan.
4. Decide whether to use ChromaDB or FAISS for the first vector search prototype.
5. Add `sentence-transformers` as the likely embedding library.
6. Create a small embedding index for the existing Markdown chunks.
7. Add a retrieval mode comparison view:
   - current main search
   - experimental rule-based search
   - vector search
8. Test vector search against the Swedish retrieval test cases.
9. Keep the current rule-based system as a fallback while vector search is tested.
10. Only connect a language model after retrieval quality is reliable.
11. Continue improving Terms of Use, Privacy Policy, and Legal Disclaimer before any public deployment.

---

## Future AI Improvements

Future AI-related improvements may include:

- Vector search using ChromaDB or FAISS
- Local embeddings using `sentence-transformers`
- Retrieval-Augmented Generation, also called RAG
- AI-generated answers based only on trusted retrieved source sections
- Better multi-source answer synthesis
- Stronger citation handling
- Refusal when source material is insufficient
- Clear separation between legal information and practical guidance
- Retrieval comparison between keyword search and vector search
- Source-grounded answer evaluation tests

The future AI version should remain source-grounded and should not answer legal or compliance questions from general model memory alone.

---

## Possible Deployment Improvements

Possible deployment improvements include:

- Public deployment through Streamlit Community Cloud, Render, Azure, or AWS
- Environment-based configuration
- Better project branding
- Improved UI layout for mobile screens
- Public-facing README updates
- Clear user-facing legal disclaimer
- Privacy-conscious logging policy
- Basic monitoring and error handling
- Security review before public use

---

## Long-Term Vision

CyberLex Sweden could become a source-grounded assistant for Swedish and EU cybersecurity law.

A mature version should:

- rely on official sources
- show citations clearly
- explain legal concepts in plain language
- refuse unsupported questions
- keep source history
- protect user privacy
- avoid harmful cybersecurity guidance
- support future expansion into more compliance areas
- support both Swedish and English as first-class languages
- maintain a strict difference between educational information and legal advice

---

## Summary

CyberLex Sweden has moved beyond a basic prototype.

The project now has a working application, trusted knowledge files, citation details, metadata, source policy, test cases, legal disclaimer drafts, clickable examples, structured answer sections, styled attention levels, experimental retrieval, source audit automation, and a development roadmap.

The main source and Swedish retrieval improvement phase has been completed for the current nine source files.

The next major technical step is real vector search.

The project should continue improving source quality, documentation, safety, privacy, and user experience before becoming public or adding full AI-generated answers.
