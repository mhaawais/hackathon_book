# Quickstart Guide for Chatbot UI

## Prerequisites
- Node.js (v16 or higher)
- Python 3.9+
- uv package manager
- Access to backend API keys (configured in backend/.env)

## Setup Instructions

### 1. Backend Setup
```bash
# Navigate to backend directory
cd backend/

# Install dependencies with uv
uv sync

# Or if using pip
pip install -r requirements.txt

# Ensure backend/.env has required keys:
# - GEMINI_API_KEY
# - QDRANT_API_KEY
# - QDRANT_URL
# - COHERE_API_KEY
```

### 2. Start Backend Server
```bash
# From backend directory
uv run python -m uvicorn src.main:app --reload --host 127.0.0.1 --port 8000
```

### 3. Frontend Setup
```bash
# Navigate to frontend directory
cd frontend/

# Install dependencies
npm install

# Create .env file with backend URL
echo "NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:8000" > .env

# Start development server
npm run dev
```

### 4. Access the Application
- Backend API: http://127.0.0.1:8000
- Frontend UI: http://localhost:3000
- Health check: http://127.0.0.1:8000/health

## Environment Variables

### Frontend (.env)
```env
NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:8000
```

### Backend (.env) - Already configured
- Contains API keys (kept secure on backend only)

## Available Scripts

### Backend
```bash
# Start development server
uv run python -m uvicorn src.main:app --reload

# Run tests
uv run python test_e2e.py

# Check API endpoint
curl -X POST "http://127.0.0.1:8000/api/v1/chat/query" \
  -H "Content-Type: application/json" \
  -d '{"query":"Hello", "top_k":5}'
```

### Frontend
```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Run linting
npm run lint
```

## Troubleshooting

### Common Issues
1. **CORS errors**: Ensure backend is running and CORS is configured
2. **API connection errors**: Verify NEXT_PUBLIC_API_BASE_URL is correct
3. **Port conflicts**: Change ports if 8000 or 3000 are in use

### Verification Steps
```bash
# Check backend health
curl http://127.0.0.1:8000/health

# Test API endpoint
curl -X POST "http://127.0.0.1:8000/api/v1/chat/query" \
  -H "Content-Type: application/json" \
  -d '{"query":"What is ROS2?", "top_k":5}'
```