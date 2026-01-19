# Local Development Setup

## Running the Application Locally

### Backend Setup (Port 8001)

```powershell
# Navigate to backend directory
cd backend

# Run the backend server on port 8001 (default for local development)
uv run python -m uvicorn src.main:app --host 127.0.0.1 --port 8001 --reload
```

### Frontend Setup (Docusaurus)

```powershell
# Navigate to the Docusaurus directory
cd physical-ai-book

# Install dependencies (if not already done)
npm install

# Install clsx dependency if not already installed
npm install clsx

# Set environment variable and run the development server
$env:CHAT_API_BASE_URL="http://127.0.0.1:8001"
npm run start
```

Alternatively, you can create a `.env` file in the `physical-ai-book` directory with:

```
CHAT_API_BASE_URL=http://127.0.0.1:8001
```

## API Endpoints Verification

### Check Backend Health
```powershell
Invoke-RestMethod http://127.0.0.1:8001/health
```

### Test Chat Query
```powershell
$body = @{
    query = "What is ROS2?"
    top_k = 5
} | ConvertTo-Json

Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8001/api/v1/chat/query -ContentType "application/json" -Body $body
```

## Troubleshooting

### Common Issues

1. **"process is not defined" error**: This has been fixed by using Docusaurus customFields to pass the API URL to the browser.

2. **Module not found errors**: Fixed import statement in ChatWindow.jsx to use correct Docusaurus v3 pattern `{ useDocusaurusContext } from '@docusaurus/core'`.

3. **CORS errors**: The backend is configured to allow all origins, but if you encounter CORS issues, ensure your backend is running and accessible.

4. **Port conflicts**: If port 8000 is busy, the default configuration uses port 8001 for local development.

### Environment Variables

The frontend now uses Docusaurus best practices:
- Environment variables are read in `docusaurus.config.ts` (Node.js context)
- Passed to the browser via `customFields`
- Accessed in React components using `useDocusaurusContext()`

### Floating Chat Icon

The chat feature is now accessed via a floating chat icon that appears on all pages:
- Look for the circular chat icon in the bottom-right corner of any page
- Clicking the icon will take you to the /chat page
- The icon has a subtle pulsing animation to draw attention
- It's visible on all pages except the /chat page itself to avoid duplication

## Verification Steps

1. Start both backend and frontend servers
2. Visit any page on http://localhost:3000 (e.g., homepage, docs, blog)
3. Verify the floating chat icon appears in the bottom-right corner
4. Click the floating chat icon to navigate to the chat page
5. Send a test query like "What is ROS2?"
6. Verify responses and sources appear correctly
7. Check that the health indicator updates based on backend availability