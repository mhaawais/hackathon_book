---
id: 4
title: "plan-agent-retrieval-api"
stage: plan
date_iso: "2026-01-13"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "003-agent-retrieval"
branch: "003-agent-retrieval"
user: "stech"
command: "/sp.plan -- Spec-3: Agent + Retrieval API (OpenAI Agents SDK + FastAPI)"
labels: ["plan", "agent", "api", "retrieval", "fastapi"]
links:
  spec: "specs/003-agent-retrieval/spec.md"
  plan: "specs/003-agent-retrieval/plan.md"
  ticket: null
  adr: null
  pr: null
files_yaml:
  - "specs/003-agent-retrieval/plan.md"
  - "specs/003-agent-retrieval/research.md"
  - "specs/003-agent-retrieval/data-model.md"
  - "specs/003-agent-retrieval/contracts/openapi.yaml"
  - "specs/003-agent-retrieval/quickstart.md"
tests_yaml: []
---

# PHR: plan-agent-retrieval-api

## Summary

Created comprehensive implementation plan for Agent + Retrieval API (OpenAI Agents SDK + FastAPI). This plan details the technical architecture, data models, API contracts, and setup instructions for implementing a FastAPI backend that integrates an OpenAI agent with Qdrant-based document retrieval.

## Outcome

Successfully created all required planning artifacts:
- Implementation plan (plan.md) with technical context and architecture
- Research document (research.md) with technology decisions and rationale
- Data models (data-model.md) with request/response structures
- API contracts (contracts/openapi.yaml) in OpenAPI format
- Quickstart guide (quickstart.md) with setup and usage instructions

All artifacts align with the feature specification and constitutional principles, ensuring proper separation of concerns, secure key handling, and source-grounded accuracy.

## Prompt Text

```
Spec-3: Agent + Retrieval API (OpenAI Agents SDK + FastAPI)

Setup & Governance:
Create/update specs/003-agent-retrieval/ and ensure all runs write timestamped outputs to history/; load env from .env (no secrets in code)

Backend API Foundation:
Initialize a FastAPI service with /health + /chat endpoints and structured request/response models

Agent + Tools Wiring:
Instantiate an OpenAI Agents SDK agent and register a retrieval tool that reuses Spec-2 logic (Cohere embed → Qdrant search docusaurus_content, top_k=5, prioritize /docs/)

Selected-Text-Only Mode:
Implement a strict bypass path: if selected_text is provided, answer only from that text and do not call Qdrant retrieval

Verification & Evidence:
Run end-to-end tests (normal query + selected_text query), print sources (URLs/chunk_ids), and save a complete run report to history/ showing mode, retrieved chunks, and final answer
```

## Response Text

Created comprehensive implementation plan with all required artifacts:

1. Implementation plan (plan.md) detailing the technical architecture using FastAPI, OpenAI Agents SDK, Cohere, and Qdrant
2. Research document (research.md) with decisions on technology stack and implementation approaches
3. Data models (data-model.md) defining request/response structures and internal models
4. API contracts (contracts/openapi.yaml) specifying the endpoints and data schemas in OpenAPI format
5. Quickstart guide (quickstart.md) with setup instructions, API usage examples, and troubleshooting

The plan follows constitutional principles with proper separation of concerns, secure handling of API keys through environment variables, and grounding responses in the existing docusaurus_content collection in Qdrant. The architecture supports both normal retrieval mode and selected-text-only mode as specified in the requirements.