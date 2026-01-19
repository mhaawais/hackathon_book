from fastapi import APIRouter, HTTPException
from typing import Dict
from datetime import datetime
from ...models.request import HealthStatus
from ...services.qdrant_client import QdrantService
from ...config.settings import settings
from openai import OpenAI
import cohere


router = APIRouter()


@router.get("/health", response_model=HealthStatus)
async def health_check():
    """
    Health check endpoint that returns the health status of the service.
    """
    # Initialize services to check their status
    qdrant_service = QdrantService()

    # Check individual service statuses
    services_status = {
        "qdrant": False,
        "openai": False,
        "cohere": False
    }

    # Check Qdrant connection
    try:
        services_status["qdrant"] = qdrant_service.check_connection()
    except Exception:
        services_status["qdrant"] = False

    # Check OpenAI connection
    try:
        client = OpenAI(api_key=settings.openai_api_key)
        # Make a simple API call to check if the key works
        models = client.models.list()
        services_status["openai"] = True
    except Exception:
        services_status["openai"] = False

    # Check Cohere connection
    try:
        cohere_client = cohere.Client(settings.cohere_api_key)
        # Make a simple API call to check if the key works
        response = cohere_client.tokenize(text="test")
        services_status["cohere"] = True
    except Exception:
        services_status["cohere"] = False

    # Determine overall status based on service statuses
    overall_status = "healthy"
    if not all(services_status.values()):
        # If not all services are healthy, check which ones are critical
        if not services_status["qdrant"] or not services_status["openai"]:
            overall_status = "unhealthy"
        elif not services_status["cohere"]:
            overall_status = "degraded"
        else:
            overall_status = "degraded"

    health_status = HealthStatus(
        status=overall_status,
        timestamp=datetime.now(),
        services=services_status,
        version=settings.version
    )

    return health_status