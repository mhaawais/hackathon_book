<!-- SYNC IMPACT REPORT
Version change: N/A → 1.0.0
Modified principles: N/A (new constitution)
Added sections: Core Principles, Authoring Standards, RAG Chatbot Constraints, Technical Stack, Quality Rules
Removed sections: N/A
Templates requiring updates:
- .specify/templates/plan-template.md ✅ updated
- .specify/templates/spec-template.md ✅ updated
- .specify/templates/tasks-template.md ✅ updated
- .specify/templates/commands/*.md ⚠ pending
Follow-up TODOs: None
-->

# Technical Book Constitution

## Core Principles

### I. Spec-first execution
Every feature and change must be documented in specifications before implementation; No undocumented decisions allowed; Specifications serve as the single source of truth for project requirements and architecture.

### II. Source-grounded accuracy
All content must be factually accurate and grounded in verified sources; No hallucinations or speculative information; All claims must be supported by authoritative references or working code examples.

### III. Clear separation of concerns
Strict separation between content (documentation), infrastructure (deployment), and AI logic (RAG/chatbot); Each layer must be independently maintainable and testable; Clear interfaces between components.

### IV. Reader-first technical clarity
All content must prioritize reader comprehension; Complex topics should be broken down into digestible sections; Examples must be practical and immediately applicable; Navigation and search must be intuitive.

### V. Deterministic, reproducible outputs
Build processes must be deterministic and reproducible across environments; Version-controlled dependencies; Automated testing ensures consistent output quality; Deployment pipeline must be reliable and repeatable.

## Authoring Standards

### Docusaurus + MDX best practices
All documentation follows Docusaurus and MDX standards; Proper heading hierarchy and semantic markup; Responsive design considerations; Accessibility compliance (WCAG guidelines).

### Incremental writing via Spec-Kit Plus tasks
Content creation follows structured task breakdowns; Each task represents a measurable, reviewable unit of work; Progress tracked through Spec-Kit Plus workflow; Quality gates enforced at each stage.

### Runnable, versioned code only
All code examples must be tested and functional; Version control for all code snippets; Clear distinction between conceptual examples and production-ready implementations; Regular verification of code accuracy.

### Clear distinction between concepts and implementation
Theoretical concepts clearly separated from practical implementation; Each concept explained before showing code; Implementation details appropriately contextualized; Clear mapping between theory and practice.

## RAG Chatbot Constraints

### Answers ONLY from retrieved book content
Chatbot responses must be grounded solely in the book's content; No external knowledge or speculation allowed; Strict adherence to content boundaries; Clear indication when information is not available.

### Support user-selected text grounding
Chatbot must cite specific sections of the book in every response; Source attribution for all claims made; Ability to reference specific paragraphs or sections; Transparent connection between content and answers.

### Cite source section/chunk in every answer
Every response must include specific citations to book sections; Page numbers or section headers where available; Direct links to referenced content when possible; Clear provenance trail for all information.

### Explicit fallback when content is missing
Clear communication when requested information is not in the book; Suggest alternative resources or sections; Acknowledge limitations of the knowledge base; Guide users to appropriate next steps.

## Technical Stack

### Frontend: Docusaurus (GitHub Pages)
Docusaurus serves as the primary documentation platform; GitHub Pages for hosting and deployment; Static site generation for performance; Search functionality integrated; Mobile-responsive design.

### Backend: FastAPI
FastAPI provides the backend services; RESTful API design principles; Async support for performance; Built-in documentation and validation; Type hints for reliability.

### Vector DB: Qdrant Cloud (Free Tier)
Qdrant Cloud manages vector embeddings for RAG functionality; Semantic search capabilities; Scalable retrieval mechanism; Proper indexing for book content; Efficient similarity matching.

### Relational DB: Neon Serverless Postgres
Neon Serverless Postgres for structured data storage; Connection pooling and scaling; ACID compliance for data integrity; Backup and recovery mechanisms; Proper schema management.

### AI: OpenAI Agents / ChatKit SDKs
OpenAI Agents for advanced AI capabilities; ChatKit SDKs for chat interface; Proper rate limiting and cost management; Secure API key handling; Response quality monitoring.

## Quality Rules

### No speculative APIs
Only implement APIs that are actually needed and validated; No anticipatory or speculative API design; Follow YAGNI principles; Validate API designs with actual usage patterns.

### Secure key handling
Proper environment variable management; No hardcoded credentials; Secure storage and transmission of sensitive data; Regular rotation of API keys; Access control enforcement.

## Governance

All contributions must comply with these constitutional principles; Changes to this constitution require explicit approval and documentation; Quality gates must be passed before merging; Regular reviews ensure continued adherence to principles; Version control tracks all changes with clear justification.

**Version**: 1.0.0 | **Ratified**: 2025-12-16 | **Last Amended**: 2025-12-16
