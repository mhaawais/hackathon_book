from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn
import os
from .api.v1.router import api_router
from .config.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Starting up the application...")

    # Shutdown
    yield

    print("Shutting down the application...")


# Create FastAPI app with lifespan
app = FastAPI(
    title="Agent + Retrieval API",
    description="API for interacting with an OpenAI agent that can retrieve information from Docusaurus book content",
    version=settings.version,
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router, prefix="/api/v1")


@app.get("/")
def read_root():
    return {"message": "Agent + Retrieval API", "version": settings.version}


@app.get("/health")
def health_check():
    """Health check endpoint at root level."""
    from .services.qdrant_client import QdrantService
    from .config.settings import settings

    # Initialize services to check their status
    qdrant_service = QdrantService()

    # Check individual service statuses
    services_status = {
        "qdrant": False,
        "openrouter": False,
    }

    # Check Qdrant connection
    try:
        services_status["qdrant"] = qdrant_service.check_connection()
    except Exception:
        services_status["qdrant"] = False

    # Check OpenRouter connection by trying to make a simple request
    try:
        from openai import OpenAI
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=settings.openrouter_api_key
        )
        # Make a simple API call to check if the key works
        models = client.models.list()
        services_status["openrouter"] = True
    except Exception:
        services_status["openrouter"] = False

    # Determine overall status based on service statuses
    overall_status = "healthy"
    if not all(services_status.values()):
        if not services_status["qdrant"] or not services_status["openrouter"]:
            overall_status = "unhealthy"
        else:
            overall_status = "degraded"

    return {
        "status": overall_status,
        "services": services_status,
        "version": settings.version
    }


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("src.main:app", host="0.0.0.0", port=port, reload=True)