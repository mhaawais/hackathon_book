---
id: 3
title: "spec-agent-retrieval-api"
stage: spec
date_iso: "2026-01-13"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "003-agent-retrieval"
branch: "003-agent-retrieval"
user: "stech"
command: "/sp.specify -- Spec-3: Agent + Retrieval API (OpenAI Agents SDK + FastAPI)"
labels: ["spec", "agent", "api", "retrieval", "fastapi"]
links:
  spec: "specs/003-agent-retrieval/spec.md"
  ticket: null
  adr: null
  pr: null
files_yaml:
  - "specs/003-agent-retrieval/spec.md"
  - "specs/003-agent-retrieval/checklists/requirements.md"
tests_yaml: []
---

# PHR: spec-agent-retrieval-api

## Summary

Created feature specification for Agent + Retrieval API (OpenAI Agents SDK + FastAPI). This feature implements a FastAPI backend that exposes retrieval functionality to an OpenAI agent, allowing it to answer questions based on a Docusaurus book's content stored in Qdrant.

## Outcome

Successfully created comprehensive specification document at specs/003-agent-retrieval/spec.md with:
- User scenarios and testing requirements
- Functional requirements (FR-001 to FR-012)
- Success criteria (SC-001 to SC-007)
- Key entities definition
- Edge cases identification

Quality checklist created at specs/003-agent-retrieval/checklists/requirements.md confirming all validation items passed.

## Prompt Text

```
Spec-3: Agent + Retrieval API (OpenAI Agents SDK + FastAPI)

Instructions

Create and maintain specs/003-agent-retrieval/ and write execution/test outputs to history/ (timestamped).

Reuse the working Spec-1/Spec-2 pipeline as-is: Qdrant collection docusaurus_content (435 vectors) + Cohere embeddings + proven retrieval script.

Build only what is needed to expose retrieval to an Agent via FastAPI and validate end-to-end behavior.

Keep the system deterministic, testable, and secure (no secrets in code; env-only).

Target Audience
Developers building a RAG chatbot for a published Docusaurus book who need an agentic interface with retrieval.

Focus
Build an Agent using the OpenAI Agents SDK and a FastAPI backend that can:

accept user questions,

call a retrieval tool that queries Qdrant (via Cohere query embeddings),

answer using retrieved book chunks,

optionally answer using only user-selected text when provided.

Success Criteria

FastAPI server starts successfully and exposes working endpoints:

health/status

chat/query endpoint returning agent responses

Agent can call retrieval tool and return answers grounded in retrieved chunks from docusaurus_content

Responses include basic provenance (at minimum: top source URLs or chunk IDs)

"Selected-text-only mode" works: if selected text is provided, the agent answers only from that text and does not retrieve from Qdrant

End-to-end test run generates a timestamped report in history/ showing:

input query

retrieved top_k chunks (URLs + previews)

final agent answer

mode used (retrieval vs selected-text-only)

Constraints

Use existing environment variables (root/backend .env):
COHERE_API_KEY, QDRANT_URL, QDRANT_API_KEY, plus required OpenAI Agents config

Use the existing retrieval logic from Spec-2 (do not re-index; read-only Qdrant access)

Default retrieval: top_k=5, prioritize /docs/ content

Backend-only (no Docusaurus UI integration yet; that's Spec-4)

Robust error handling for:

empty query

retrieval failures

upstream API failures

Save key run artifacts/logs to history/

Not Building

No frontend widget / Docusaurus embedding

No auth/user accounts

No reranking/feedback loops (unless already present)

No re-ingestion/re-embedding

No streaming UI polish (optional, not required)

Deliverables

specs/003-agent-retrieval/spec.md + supporting checklist

FastAPI app that wires:

Agent (OpenAI Agents SDK)

Retrieval tool (Qdrant + Cohere)

Selected-text-only path

A minimal test runner or curl examples + a saved run report in history/
```

## Response Text

Created comprehensive feature specification document following the template structure with user scenarios, functional requirements, success criteria, and key entities. The specification covers all required aspects including the agent functionality, retrieval tool integration, selected-text-only mode, health endpoints, and error handling requirements.