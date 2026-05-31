# CyberLex Sweden Product Roadmap

## Purpose

This roadmap explains how CyberLex Sweden could develop from a school prototype into a more realistic legal-tech and cybersecurity compliance assistant.

CyberLex Sweden is currently an educational prototype. The roadmap is not a promise that every feature will be built, but it describes a realistic development path.

The goal is to make the project more structured, more trustworthy, and easier to expand.

---

## Current Status

CyberLex Sweden currently works as a local Streamlit application.

The prototype can:

- Load local Markdown knowledge base files
- Split source documents into searchable chunks
- Route questions to specific source files
- Match questions to relevant source sections
- Generate simple source-based answers
- Display citation details
- Display official source links
- Display source metadata
- Show matched source excerpts
- Refuse out-of-scope questions

The current system does not yet use vector search, a full language model, public deployment, or a production database.

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
- Source update history
- Manual test cases
- Final report
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

Without source management, the system may eventually give outdated answers, which is exactly the kind of nonsense we are trying to avoid.

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

### Planned Improvements

- Cleaner app layout
- Better page header
- Better sidebar organization
- Search examples
- Topic buttons
- Source cards
- Citation cards
- Better warning and disclaimer design
- Better color scheme
- Cybersecurity/legal-tech visual identity
- Better screenshot-ready interface for the final presentation

### Possible UI Sections

- Ask CyberLex
- Supported topics
- Citation details
- Source excerpt
- Knowledge base status
- Legal disclaimer

### Success Criteria

This phase is successful when a user can understand what the app does without needing personal guidance from the Omnissiah’s least rested assistant.

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

- Student portfolio project
- Cybersecurity law learning tool
- Compliance assistant prototype
- Internal company knowledge assistant
- Swedish cyber law research assistant
- Legal-tech startup concept

### Questions to Answer

- Who is the target user?
- What problem does CyberLex solve better than existing sources?
- Should it support Swedish only, English only, or both?
- Should it answer only from official sources?
- Should it store user questions?
- Should it use a cloud language model?
- How should source updates be reviewed?
- What legal review is required before public use?

### Success Criteria

This phase is successful when the project has a clear direction and realistic next steps.

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

1. Finish Terms of Use, Privacy Policy, and Legal Disclaimer
2. Improve visual design
3. Add more Swedish and EU sources
4. Add source update history improvements
5. Prepare for ChromaDB vector search
6. Test vector search against current keyword search
7. Connect a language model only after retrieval is reliable
8. Prepare deployment documentation

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

The project now has a working application, trusted knowledge files, citation details, metadata, source policy, test cases, legal disclaimer drafts, and a development roadmap.

The next major technical step is vector search, but the project should continue improving source quality, documentation, safety, and user experience before becoming public.