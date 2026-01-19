# Data Model: Agent + Retrieval API

## Overview
This document defines the data structures and models for the Agent + Retrieval API feature based on the requirements in `specs/003-agent-retrieval/spec.md`.

## Request Models

### QueryRequest
Represents the input to the chat/query endpoint.

**Fields:**
- `query`: str (required) - The user's question/query
- `selected_text`: Optional[str] (optional) - User-selected text for selected-text-only mode
- `top_k`: int (optional, default: 5) - Number of chunks to retrieve from Qdrant
- `session_id`: Optional[str] (optional) - Session identifier for tracking conversations

**Validation Rules:**
- `query` must not be empty or whitespace only
- `top_k` must be between 1 and 10
- If `selected_text` is provided, it should not exceed 10000 characters

## Response Models

### RetrievedChunk
Represents a single chunk retrieved from Qdrant.

**Fields:**
- `chunk_id`: str - Unique identifier for the chunk
- `content`: str - The text content of the chunk
- `url`: str - Source URL where the content originated
- `score`: float - Similarity score from the retrieval
- `metadata`: Dict[str, Any] - Additional metadata from Qdrant

**Validation Rules:**
- `chunk_id` must be unique within a retrieval result
- `content` must not be empty
- `url` must be a valid URL format

### AgentResponse
Represents the final response from the agent.

**Fields:**
- `answer`: str - The agent's answer to the query
- `sources`: List[RetrievedChunk] - List of source chunks used in the response
- `mode_used`: Literal["retrieval", "selected-text-only"] - Which mode was used
- `retrieval_time_ms`: float - Time taken for retrieval process
- `total_time_ms`: float - Total processing time
- `session_id`: Optional[str] - Session identifier if provided in request

**Validation Rules:**
- `answer` must not be empty
- `sources` list must contain at least 1 item when mode_used is "retrieval"
- `retrieval_time_ms` and `total_time_ms` must be positive values

## Internal Models

### AgentConfig
Configuration parameters for the OpenAI Agent.

**Fields:**
- `openai_api_key`: str - OpenAI API key
- `model`: str - Model identifier (e.g., "gpt-4-turbo")
- `temperature`: float - Temperature setting for generation

### RetrievalConfig
Configuration parameters for the retrieval functionality.

**Fields:**
- `cohere_api_key`: str - Cohere API key
- `qdrant_url`: str - Qdrant server URL
- `qdrant_api_key`: str - Qdrant API key
- `collection_name`: str - Name of the Qdrant collection ("docusaurus_content")
- `top_k_default`: int - Default number of chunks to retrieve (5)

## Health Status Model

### HealthStatus
Represents the health status of the service.

**Fields:**
- `status`: Literal["healthy", "degraded", "unhealthy"] - Overall service status
- `timestamp`: datetime - Time when status was checked
- `services`: Dict[str, bool] - Status of individual services (qdrant, openai, cohere)
- `version`: str - Current version of the service

**Validation Rules:**
- `timestamp` must be current (within 1 minute of request time)
- `status` is determined by the lowest status among services

## State Transitions

### Query Processing Workflow
1. **Received**: QueryRequest validated and accepted
2. **Processing**: Agent initialized, retrieval performed if needed
3. **Responding**: Agent generating final response with provenance
4. **Completed**: AgentResponse generated and returned to client

### Error States
- **ValidationError**: QueryRequest fails validation
- **RetrievalError**: Qdrant or Cohere services unavailable
- **UpstreamError**: OpenAI services unavailable
- **ServiceError**: Internal service error during processing

## Relationships

```
QueryRequest --[triggers]--> AgentService
AgentService --[uses]--> RetrievalTool
RetrievalTool --[queries]--> QdrantCollection[docusaurus_content]
QdrantCollection --[returns]--> RetrievedChunk[]
RetrievedChunk[] --[used_by]--> AgentResponse
QueryRequest[selected_text] --[bypasses]--> RetrievalTool
```

## Constraints

- All API keys must be loaded from environment variables (no hardcoding)
- Retrieved chunks must maintain their original content integrity
- Provenance information (URLs/chunk IDs) must be preserved in responses
- Selected-text-only mode must not trigger Qdrant retrieval
- All timestamps must be in UTC timezone