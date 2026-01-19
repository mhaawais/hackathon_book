# Research: Agent + Retrieval API Implementation

## Overview
This research document covers the technical decisions and investigations required for implementing the Agent + Retrieval API feature, based on the specification in `specs/003-agent-retrieval/spec.md`.

## Decision: OpenAI Agents SDK Integration
**Rationale**: The specification requires using the OpenAI Agents SDK to create an agent that can call retrieval tools. This approach provides a managed way to handle complex agent interactions, tool calling, and response generation.
**Alternatives considered**:
- OpenAI Function Calling API (lower-level, more manual management)
- LangChain agents (would add additional complexity and dependencies)
- Custom agent implementation (too complex for the scope)

## Decision: FastAPI for Backend Framework
**Rationale**: FastAPI provides async support, automatic API documentation, built-in validation, and excellent performance for API services. It aligns with the technical stack specified in the constitution.
**Alternatives considered**:
- Flask (simpler but less performant and fewer built-in features)
- Django (overkill for API-only service)
- Express.js (would change language to JavaScript/Node.js)

## Decision: Cohere Embeddings for Query Processing
**Rationale**: The specification requires reusing the existing Spec-2 pipeline which uses Cohere embeddings. This ensures consistency with the existing docusaurus_content collection in Qdrant.
**Alternatives considered**:
- OpenAI embeddings (would require re-indexing the content)
- Sentence Transformers (local option but less consistent with existing setup)

## Decision: Qdrant for Vector Storage and Retrieval
**Rationale**: The existing docusaurus_content collection (435 vectors) is already in Qdrant from previous specs. Reusing this aligns with the constraint to use existing retrieval logic.
**Alternatives considered**:
- Pinecone (would require data migration)
- Weaviate (would require data migration)
- Elasticsearch (not optimized for vector similarity search)

## Decision: Selected-Text-Only Mode Implementation
**Rationale**: The specification requires a bypass mode where the agent answers only from provided selected text without calling Qdrant. This requires implementing a conditional execution path in the agent service.
**Implementation approach**: Check for selected_text parameter in request and bypass the retrieval tool if present.

## Decision: Provenance Information in Responses
**Rationale**: The specification requires responses to include basic provenance (top source URLs or chunk IDs). This will be implemented by capturing the retrieved chunks metadata and including it in the final response.
**Format**: JSON response will include both the answer and a list of source URLs/chunk IDs.

## Decision: Error Handling Strategy
**Rationale**: The specification requires robust error handling for empty queries, retrieval failures, and upstream API failures. This will be implemented using FastAPI exception handlers and proper HTTP status codes.
**Approach**:
- 400 Bad Request for empty queries
- 503 Service Unavailable for upstream failures
- 200 OK with error details in response body for retrieval-specific issues

## Decision: Environment Configuration
**Rationale**: The specification requires using existing environment variables (COHERE_API_KEY, QDRANT_URL, QDRANT_API_KEY, plus OpenAI Agents config) with no secrets in code.
**Implementation**: Using Pydantic's BaseSettings to load configuration from environment variables with proper validation.