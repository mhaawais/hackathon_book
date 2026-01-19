# Agent + Retrieval API Backend

This is the backend service for the Agent + Retrieval API, which provides an interface for querying documentation using an OpenAI agent with Qdrant-based retrieval capabilities.

## Features

- Query documentation with an AI agent
- Retrieve information from Qdrant vector database
- Selected-text-only mode for answering from provided text only
- Health and status monitoring
- Comprehensive error handling

## Prerequisites

- Python 3.11+
- OpenAI API key
- Cohere API key
- Qdrant Cloud account and API key

## Installation

1. Clone the repository
2. Navigate to the backend directory: `cd backend`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Create a `.env` file based on `.env.example` and add your API keys

## Usage

Start the development server:
```bash
python src/main.py
```

The API will be available at `http://localhost:8000`

## Endpoints

- `GET /` - Root endpoint
- `GET /api/v1/health` - Health check
- `POST /api/v1/chat/query` - Query the agent
- `GET /api/v1/chat/status` - Chat service status

## Environment Variables

- `OPENAI_API_KEY` - Your OpenAI API key
- `COHERE_API_KEY` - Your Cohere API key
- `QDRANT_URL` - URL for your Qdrant instance
- `QDRANT_API_KEY` - Your Qdrant API key
- `MODEL_NAME` - OpenAI model to use (default: gpt-4-turbo)

## Architecture

The service follows a clean architecture with the following layers:

- `src/api` - API endpoints and routing
- `src/services` - Business logic and external service integration
- `src/models` - Data models and schemas
- `src/config` - Configuration and settings
- `src/utils` - Utility functions
