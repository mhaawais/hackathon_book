# Implementation Plan: Agent + Retrieval API (OpenAI Agents SDK + FastAPI)

**Branch**: `003-agent-retrieval` | **Date**: 2026-01-13 | **Spec**: [specs/003-agent-retrieval/spec.md](./spec.md)

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implement a FastAPI backend that integrates an OpenAI Agent with a retrieval tool for Qdrant-based document search. The system will allow users to ask questions about Docusaurus book content, with support for both retrieval-based answers and selected-text-only mode. The agent will leverage Cohere embeddings to query the docusaurus_content collection in Qdrant and provide responses with provenance information.

## Technical Context

**Language/Version**: Python 3.11
**Primary Dependencies**: FastAPI, OpenAI Agents SDK, Cohere, Qdrant, Pydantic
**Storage**: Qdrant Cloud (vector database), environment variables for API keys
**Testing**: pytest for unit and integration tests
**Target Platform**: Linux server (backend API service)
**Project Type**: web (backend API)
**Performance Goals**: 95% of queries return within 15 seconds, support 100 concurrent users
**Constraints**: <200ms p95 for health checks, secure handling of API keys, proper error handling for empty queries and upstream failures
**Scale/Scope**: 10K+ document chunks in Qdrant, 1M+ possible queries

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Spec-first execution**: ✅ Confirmed - following spec from `specs/003-agent-retrieval/spec.md`
- **Source-grounded accuracy**: ✅ Confirmed - using established retrieval logic from Spec-2
- **Clear separation of concerns**: ✅ Confirmed - separating API layer, agent logic, and retrieval tools
- **Reader-first technical clarity**: ✅ Confirmed - API responses will include clear provenance
- **Deterministic, reproducible outputs**: ✅ Confirmed - using versioned dependencies and environment config
- **Secure key handling**: ✅ Confirmed - using environment variables for API keys
- **RAG Chatbot Constraints**: ✅ Confirmed - responses will be grounded in retrieved content with citations

## Project Structure

### Documentation (this feature)

```text
specs/003-agent-retrieval/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── main.py              # FastAPI application entry point
│   ├── config/
│   │   └── settings.py      # Configuration and environment loading
│   ├── models/
│   │   ├── request.py       # Request/response models (QueryRequest, AgentResponse)
│   │   └── chunk.py         # Chunk/data models
│   ├── services/
│   │   ├── agent_service.py # OpenAI Agent orchestration
│   │   ├── retrieval_tool.py # Qdrant/Cohere retrieval functionality
│   │   └── qdrant_client.py # Qdrant client wrapper
│   ├── api/
│   │   └── v1/
│   │       ├── router.py    # Main API router
│   │       ├── health.py    # Health check endpoints
│   │       └── chat.py      # Chat/query endpoints
│   └── utils/
│       ├── validation.py    # Input validation utilities
│       └── logging.py       # Logging utilities
├── tests/
│   ├── unit/
│   │   ├── test_models.py   # Model validation tests
│   │   ├── test_retrieval.py # Retrieval logic tests
│   │   └── test_agent.py    # Agent service tests
│   ├── integration/
│   │   └── test_api.py      # API integration tests
│   └── fixtures/
│       └── mock_data.py     # Test data fixtures
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
└── Dockerfile              # Containerization
```

**Structure Decision**: Backend API structure selected to house the FastAPI service with clear separation between models, services, API routes, and utilities. This follows the constitution's principle of clear separation of concerns.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| N/A | N/A | N/A |