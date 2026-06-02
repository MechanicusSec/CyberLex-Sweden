# CyberLex Sweden Product Roadmap

## Purpose

This roadmap explains how CyberLex Sweden could develop from a school prototype into a more realistic legal-tech and cybersecurity compliance assistant.

CyberLex Sweden is currently an educational prototype. The roadmap is not a promise that every feature will be built, but it describes a realistic development path.

The goal is to make the project more structured, more trustworthy, and easier to expand.

---

## Current Status

CyberLex Sweden currently works as a local Streamlit application.

The current prototype includes:

- Local Markdown knowledge base in `data/`
- Source-based search and chunk ranking
- Source routing for clear topic questions
- Official source links with readable Markdown labels
- Source date and version notes
- Bilingual interface support for English and Swedish
- Auto language detection for user questions
- Rule-based short answers
- CyberLex attention level with styled status card
- Practical explanation section
- Topic-based assessment checklist
- Collapsible source context
- Other matching source sections list
- Clickable example questions using Streamlit session state
- Sidebar prototype version label
- Sidebar future AI mode note
- Legal limitation notice
- Refusal behavior for out-of-scope questions

The current system does not yet use vector search, a full language model, public deployment, or a production database.

These features make the current version a transparent, source-grounded educational prototype.

---

## Phase 1: Prototype Foundation

### Status

Mostly completed.

### Goal

Build a working local prototype that proves the core idea.

### Completed Features

- Streamlit web interface
- Local Markdown knowledge base
- Source-based search
- Chunk-based search
- Source routing
- Simple answer generation
- Official source links
- Source metadata
- Citation details
- Practical explanations
- Assessment checklists
- Styled attention level card
- Clickable example questions
- Future AI mode sidebar note
- Prototype version label
- Source update history
- Manual test cases
- Final report draft
- Source policy
- Legal disclaimer draft
- Terms of Use draft
- Privacy Policy draft

### Purpose

This phase proves that CyberLex Sweden can answer selected cybersecurity-law questions using trusted local source material.

---

## Phase 2: Source Expansion

### Goal

Expand the trusted knowledge base with more Swedish and EU cybersecurity law sources.

### Planned Source Areas

- Additional GDPR guidance
- More IMY guidance
- NIS2 sector-specific information
- Swedish Cybersecurity Act updates
- DORA technical standards and guidance
- EU Cybersecurity Act and ENISA certification
- Protective Security Act, säkerhetsskyddslagen
- Electronic communications security rules
- AI Act cybersecurity and compliance connections
- EDPB guidance on security and data protection

### Requirements for New Sources

Each new knowledge file should include:

- topic
- main authority or legal source
- key idea
- important points
- cybersecurity connection
- useful questions
- official source links
- source date
- version notes
- disclaimer

### Success Criteria

This phase is successful when CyberLex Sweden can answer more questions while still showing citation details and refusing unsupported topics.

---

## Phase 3: Better Source Management

### Goal

Make source handling more reliable and easier to maintain.

### Planned Improvements

- Add a source update checklist
- Add source categories
- Add source status values, such as active, needs review, outdated
- Add source version history
- Add date reviewed
- Add source owner or reviewer field
- Add link-checking process
- Add a clear method for retiring outdated sources

### Why This Matters

Legal and cybersecurity information changes over time.

A real system must show when sources were checked and whether they are still reliable.

Without source management, the system may eventually give outdated answers.

---

## Phase 4: Improved Search

### Goal

Improve retrieval quality beyond simple keyword matching and source routing.

### Planned Improvements

- Add vector search with ChromaDB or FAISS
- Store chunks as embeddings
- Match user questions by semantic meaning instead of only keywords
- Keep source metadata connected to each chunk
- Compare vector search results with current keyword routing
- Add minimum confidence thresholds
- Improve refusal behavior for weak matches

### ChromaDB Option

ChromaDB could be used as a local vector database.

It would store document chunks and embeddings, making it possible to search by semantic similarity.

### FAISS Option

FAISS could be used as a lightweight local vector search engine.

It may be useful if the project needs fast similarity search without a larger database system.

### Success Criteria

This phase is successful when CyberLex Sweden can find the correct source section even when the user does not use the exact same words as the source file.

---

## Phase 5: Language Model Integration

### Goal

Connect a language model to generate better natural language answers.

### Important Rule

The language model should not answer freely from memory.

It should only answer using retrieved source chunks.

### Planned Improvements

- Use retrieved source chunks as context
- Generate clearer answers from source material
- Include citation details in every answer
- Refuse unsupported questions
- Add prompt rules for legal safety
- Prevent unsupported legal claims
- Avoid cybercrime instructions
- Keep disclaimers visible

### Safe Answer Pattern

A future language model answer should follow this pattern:

1. Short answer
2. Explanation
3. Source citation
4. Important limitation
5. Recommendation to check official sources for serious decisions

### Success Criteria

This phase is successful when answers become easier to read while still remaining source-grounded and cautious.

---

## Phase 6: User Experience and Visual Design

### Goal

Make CyberLex Sweden look more professional and easier to use.

### Completed UX Improvements

- Main page header
- Supported topic badges
- Sidebar project resources
- Prototype version label
- Future AI mode sidebar note
- Clickable example questions
- Collapsible assessment checklist
- Collapsible source context
- Styled CyberLex attention level card

### Planned Improvements

- Better source cards
- Better citation cards
- Improved mobile layout
- More polished cybersecurity/legal-tech visual identity
- Better screenshot-ready interface for final presentation

### Possible UI Sections

- Ask CyberLex
- Supported topics
- Citation details
- Source context
- Assessment checklist
- Knowledge base status
- Legal disclaimer

### Success Criteria

This phase is successful when a user can understand what the app does without needing personal guidance.

---

## Phase 7: Public Deployment Preparation

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

### Trademark Note

If CyberLex Sweden becomes a serious product, trademark protection may be useful for the name and brand identity.

This should be handled later, when the project has clearer long-term value.

### Success Criteria

This phase is successful when the project has a clear identity, ownership notice, and legal protection plan.

---

## Phase 9: Real Product Direction

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

### Planned Language Support

CyberLex Sweden should eventually support:

- Better Swedish answer generation
- Better English explanations of Swedish legal terms
- Source citations in the original source language
- More bilingual source summaries
- More Swedish legal terminology support

### Example Questions

English examples:

```text
What is IMY?
What is NIS2 incident reporting?
What is DORA?
When must a personal data breach be reported?
Can an incident need to be reported under both NIS2 and GDPR?

```

Swedish examples:

```text
Vad är IMY?
Vad är NIS2?
Vad är DORA?
När måste en personuppgiftsincident rapporteras?
Kan en incident behöva rapporteras enligt både NIS2 och GDPR?
```

---

## Risk Overview

| Risk | Explanation | Mitigation |
|---|---|---|
| Outdated legal sources | Laws and guidance can change | Add source review dates and update history |
| Unsupported answers | The system may answer without enough evidence | Use scope checks, source routing, and refusal behavior |
| Wrong source match | Similar legal topics may confuse search | Use source routing and later vector search |
| Overreliance by users | Users may treat answers as legal advice | Keep disclaimers and Terms of Use clear |
| Privacy issues | Public deployment may process user input | Add Privacy Policy and avoid storing sensitive data |
| Cyber misuse | Users may ask harmful cybercrime questions | Refuse harmful or out-of-scope questions |
| Brand copying | Others may copy the name or concept | Keep copyright notice and consider trademark later |

---

## Near-Term Roadmap

The next practical steps are:

1. Add more Swedish and EU sources
2. Add source update history improvements
3. Prepare for ChromaDB vector search
4. Test vector search against current keyword search
5. Connect a language model only after retrieval is reliable
6. Prepare deployment documentation
7. Improve source cards and citation cards
8. Review Terms of Use, Privacy Policy, and Legal Disclaimer

---

## Future AI Improvements

Future AI-related improvements may include:

- Vector search using ChromaDB or FAISS
- Retrieval-Augmented Generation, also called RAG
- AI-generated answers based only on trusted retrieved source sections
- Better multi-source answer synthesis
- Stronger citation handling
- Refusal when source material is insufficient
- Clear separation between legal information and practical guidance

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

---

## Summary

CyberLex Sweden has moved beyond a basic prototype.

The project now has a working application, trusted knowledge files, citation details, metadata, source policy, test cases, legal disclaimer drafts, clickable examples, structured answer sections, styled attention levels, and a development roadmap.

The next major technical step is vector search, but the project should continue improving source quality, documentation, safety, and user experience before becoming public.