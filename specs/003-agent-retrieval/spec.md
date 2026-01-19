# Feature Specification: Agent + Retrieval API (OpenAI Agents SDK + FastAPI)

**Feature Branch**: `003-agent-retrieval`
**Created**: 2026-01-13
**Status**: Draft
**Input**: User description: "Spec-3: Agent + Retrieval API (OpenAI Agents SDK + FastAPI)

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

optionally answer using only user-selected text when provided."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Query Documentation with Agent (Priority: P1)

As a developer working with a Docusaurus book, I want to ask questions about the documentation using an AI agent so that I can get accurate, contextual answers with source citations.

**Why this priority**: This is the core functionality that enables developers to interact with documentation in a natural way, providing immediate value by reducing search time and improving comprehension.

**Independent Test**: Can be fully tested by sending a query to the chat/query endpoint and verifying that the agent returns a response with proper provenance information.

**Acceptance Scenarios**:

1. **Given** a user has a question about the documentation, **When** they submit the query to the agent, **Then** the agent retrieves relevant content from Qdrant and responds with an answer citing the sources
2. **Given** the agent receives a query, **When** it processes the request, **Then** it returns a response within 10 seconds with at least 3 source citations

---

### User Story 2 - Selected Text Only Mode (Priority: P2)

As a developer, I want to provide specific text selections to the agent so that it only responds based on that content without querying the broader documentation.

**Why this priority**: This provides flexibility for users who want answers based on specific sections they've highlighted or selected, enabling more focused interactions.

**Independent Test**: Can be tested by submitting a query with selected text parameter and verifying the agent only uses that text for answers.

**Acceptance Scenarios**:

1. **Given** a user provides selected text with their query, **When** the agent processes the request, **Then** it responds using only the provided text without performing Qdrant retrieval
2. **Given** a user provides selected text, **When** they submit a query, **Then** the agent ignores the Qdrant retrieval tool and focuses only on the provided text

---

### User Story 3 - Health and Status Monitoring (Priority: P3)

As a system administrator, I want to monitor the health status of the agent API so that I can ensure the service is running properly.

**Why this priority**: Essential for operational reliability and monitoring the service in production environments.

**Independent Test**: Can be tested by calling the health/status endpoint and verifying it returns appropriate status information.

**Acceptance Scenarios**:

1. **Given** the service is running, **When** a GET request is made to the health endpoint, **Then** it returns a 200 status with system health information
2. **Given** the service is running, **When** the health is degraded, **Then** the endpoint returns appropriate error codes

---

### Edge Cases

- What happens when the query is empty or contains only whitespace?
- How does the system handle Qdrant retrieval failures gracefully?
- What occurs when upstream APIs (OpenAI, Cohere) are unavailable?
- How does the system behave when the selected text is extremely large?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST accept user questions via a chat/query endpoint
- **FR-002**: System MUST provide a health/status endpoint for monitoring
- **FR-003**: Agent MUST be able to call a retrieval tool that queries Qdrant using Cohere embeddings
- **FR-004**: Agent MUST answer using retrieved book chunks from the docusaurus_content collection
- **FR-005**: Agent MUST support selected-text-only mode when provided with user-selected text
- **FR-006**: Responses MUST include basic provenance information (top source URLs or chunk IDs)
- **FR-007**: System MUST handle empty query errors gracefully with appropriate error messages
- **FR-008**: System MUST handle retrieval failures gracefully with appropriate fallbacks
- **FR-009**: System MUST handle upstream API failures gracefully with appropriate error responses
- **FR-010**: System MUST default to retrieving top_k=5 results with prioritization of /docs/ content
- **FR-011**: System MUST reuse existing retrieval logic from Spec-2 without re-indexing
- **FR-012**: System MUST save key run artifacts/logs to the history directory

### Key Entities

- **Query Request**: Contains user question and optional selected text for the selected-text-only mode
- **Retrieved Chunks**: Document fragments retrieved from Qdrant with associated metadata (URLs, chunk IDs)
- **Agent Response**: Answer generated by the OpenAI agent with provenance information
- **Health Status**: System health information including service availability and performance metrics

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: FastAPI server starts successfully and exposes working endpoints within 30 seconds of startup
- **SC-002**: Chat/query endpoint returns agent responses with provenance information in under 15 seconds for 95% of requests
- **SC-003**: Agent successfully retrieves and answers from Qdrant with 90% accuracy in grounding responses to retrieved chunks
- **SC-004**: Selected-text-only mode functions correctly 95% of the time when selected text is provided
- **SC-005**: End-to-end test run generates a timestamped report in history/ with all required information (input query, retrieved chunks, final answer, mode used)
- **SC-006**: System handles retrieval failures gracefully with appropriate error responses 100% of the time
- **SC-007**: Health endpoint returns status information within 1 second 99% of the time