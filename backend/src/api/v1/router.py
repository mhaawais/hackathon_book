from fastapi import APIRouter
from . import health, chat


# Create main API router
api_router = APIRouter()

# Include health endpoints
api_router.include_router(
    health.router,
    tags=["health"]
)

# Include chat endpoints
api_router.include_router(
    chat.router,
    prefix="/chat",
    tags=["chat"]
)