from pydantic import BaseModel, Field
from typing import Dict, Any, Optional
from datetime import datetime
from .request import HealthStatus  # Import HealthStatus from the same directory


class Chunk(BaseModel):
    """
    Represents a document chunk for retrieval purposes.
    """
    id: str = Field(..., description="Unique identifier for the chunk")
    content: str = Field(..., description="The text content of the chunk")
    url: str = Field(..., description="Source URL where the content originated")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")
    score: Optional[float] = Field(None, description="Similarity score if from retrieval")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Creation timestamp")
    updated_at: datetime = Field(default_factory=datetime.utcnow, description="Last update timestamp")

    class Config:
        arbitrary_types_allowed = True


# Export HealthStatus for use in other modules
__all__ = ["Chunk", "HealthStatus"]