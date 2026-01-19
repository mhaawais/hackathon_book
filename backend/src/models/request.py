from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from datetime import datetime
import time


class QueryRequest(BaseModel):
    """
    Represents the input to the chat/query endpoint.
    """
    query: str = Field(..., description="The user's question/query", min_length=1)
    selected_text: Optional[str] = Field(
        None,
        description="User-selected text for selected-text-only mode",
        max_length=10000
    )
    top_k: int = Field(5, ge=1, le=10, description="Number of chunks to retrieve from Qdrant")
    session_id: Optional[str] = Field(None, description="Session identifier for tracking conversations")


class RetrievedChunk(BaseModel):
    """
    Represents a single chunk retrieved from Qdrant.
    """
    chunk_id: str = Field(..., description="Unique identifier for the chunk")
    content: str = Field(..., description="The text content of the chunk")
    url: str = Field(..., description="Source URL where the content originated")
    score: float = Field(..., description="Similarity score from the retrieval")
    metadata: dict = Field(default_factory=dict, description="Additional metadata from Qdrant")


class ErrorDetails(BaseModel):
    """
    Details about an error that occurred.
    """
    type: str = Field(..., description="Type of error that occurred")
    message: str = Field(..., description="Human-readable error message")
    code: Optional[str] = Field(None, description="Error code if applicable")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="When the error occurred")


class AgentResponse(BaseModel):
    """
    Represents the final response from the agent.
    """
    answer: str = Field(..., description="The agent's answer to the query")
    sources: List[RetrievedChunk] = Field(
        default_factory=list,
        description="List of source chunks used in the response"
    )
    mode_used: Literal["retrieval", "selected-text-only"] = Field(
        ...,
        description="Which mode was used"
    )
    retrieval_time_ms: float = Field(..., description="Time taken for retrieval process")
    total_time_ms: float = Field(..., description="Total processing time")
    session_id: Optional[str] = Field(None, description="Session identifier if provided in request")
    error: Optional[ErrorDetails] = Field(None, description="Error details if an error occurred")


class HealthStatus(BaseModel):
    """
    Represents the health status of the service.
    """
    status: Literal["healthy", "degraded", "unhealthy"] = Field(
        ...,
        description="Overall service status"
    )
    timestamp: datetime = Field(..., description="Time when status was checked")
    services: dict = Field(
        ...,
        description="Status of individual services (qdrant, openai, cohere)"
    )
    version: str = Field(..., description="Current version of the service")