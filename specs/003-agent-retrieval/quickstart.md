# Quickstart: Agent + Retrieval API

## Prerequisites

- Python 3.11+
- Access to OpenAI API (API key)
- Access to Cohere API (API key)
- Access to Qdrant Cloud (URL and API key)
- Existing docusaurus_content collection in Qdrant with 435 vectors

## Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Set Up Environment

Copy the example environment file and add your API keys:

```bash
cp .env.example .env
```

Edit `.env` and add your API keys:

```bash
OPENAI_API_KEY=your_openai_api_key_here
COHERE_API_KEY=your_cohere_api_key_here
QDRANT_URL=your_qdrant_url_here
QDRANT_API_KEY=your_qdrant_api_key_here
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Service

### Start the Development Server

```bash
cd backend
python src/main.py
```

The API will be available at `http://localhost:8000`

## API Usage

### Health Check

Verify the service is running:

```bash
curl http://localhost:8000/health
```

Expected response:
```json
{
  "status": "healthy",
  "timestamp": "2026-01-13T10:00:00Z",
  "services": {
    "qdrant": true,
    "openai": true,
    "cohere": true
  },
  "version": "1.0.0"
}
```

### Query the Agent

#### Normal Retrieval Mode

Submit a query to retrieve information from the documentation:

```bash
curl -X POST http://localhost:8000/chat/query \
  -H "Content-Type: application/json" \
  -d '{
    "query": "How do I configure authentication?",
    "top_k": 5
  }'
```

#### Selected-Text-Only Mode

Provide specific text for the agent to answer from (bypassing Qdrant retrieval):

```bash
curl -X POST http://localhost:8000/chat/query \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What does this text say about security?",
    "selected_text": "Security is configured through environment variables. The main settings are SECURITY_ENABLED=true and SECURITY_LEVEL=high.",
    "top_k": 5
  }'
```

### Expected Response Format

Both query types return a response in this format:

```json
{
  "answer": "To configure authentication, you need to set the AUTH_TOKEN environment variable...",
  "sources": [
    {
      "chunk_id": "chunk_abc123",
      "content": "Authentication is configured through environment variables...",
      "url": "https://example.com/docs/authentication",
      "score": 0.85,
      "metadata": {}
    }
  ],
  "mode_used": "retrieval",
  "retrieval_time_ms": 125.5,
  "total_time_ms": 2450.2,
  "session_id": "session_12345"
}
```

## Testing

Run the unit tests:

```bash
cd backend
pytest tests/unit/
```

Run the integration tests:

```bash
cd backend
pytest tests/integration/
```

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| OPENAI_API_KEY | OpenAI API key for agent functionality | Yes |
| COHERE_API_KEY | Cohere API key for embeddings | Yes |
| QDRANT_URL | URL for Qdrant vector database | Yes |
| QDRANT_API_KEY | API key for Qdrant access | Yes |
| MODEL_NAME | OpenAI model to use (default: gpt-4-turbo) | No |

## Troubleshooting

### Common Issues

1. **API Keys Not Working**: Verify all API keys are correctly set in the environment
2. **Qdrant Connection Issues**: Check QDRANT_URL and QDRANT_API_KEY
3. **Empty Responses**: Verify the docusaurus_content collection exists and has data
4. **Rate Limits**: Check if you've exceeded API limits for OpenAI or Cohere

### Debug Mode

Start the server with debug logging:

```bash
DEBUG=true python src/main.py
```