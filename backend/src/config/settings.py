from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional


class Settings(BaseSettings):
    # API Keys
    openai_api_key: str = Field(alias="OPENAI_API_KEY")
    cohere_api_key: str = Field(alias="COHERE_API_KEY")
    qdrant_api_key: str = Field(alias="QDRANT_API_KEY")
    openrouter_api_key: str = Field(alias="OPENROUTER_API_KEY")
    gemini_api_key: str = Field(alias="GEMINI_API_KEY")

    # Service URLs
    qdrant_url: str = Field(alias="QDRANT_URL")

    # Additional environment variables that might be present
    deployed_vercel_url: Optional[str] = Field(default=None, alias="DEPLOYED_VERCEL_URL")

    # Model Configuration
    model_name: str = Field(default="openrouter/auto", alias="MODEL_NAME")
    gemini_model: str = Field(default="gemini-1.5-pro", alias="GEMINI_MODEL")

    # Qdrant Configuration
    qdrant_collection_name: str = Field(default="docusaurus_content")
    default_top_k: int = Field(default=5)

    # Application Configuration
    debug: bool = Field(default=False)
    version: str = Field(default="1.0.0")

    class Config:
        env_file = ".env"
        case_sensitive = False  # Allow case-insensitive matching
        # Allow extra fields to prevent validation errors for additional env vars
        extra = "ignore"


settings = Settings()