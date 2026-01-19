# Verification Steps for Chat UI Implementation

## Local Verification

### Prerequisites
- Backend server running on http://127.0.0.1:8000
- Docusaurus development server running on http://localhost:3000

### Manual Verification Steps

1. **Navigate to Chat Page**
   - Open browser to http://localhost:3000/chat
   - Verify page loads without errors
   - Verify "Chat with Book Content" header is visible

2. **Health Indicator Verification**
   - Verify "Backend Connected" status is displayed
   - Check visual indicator shows healthy state (green)

3. **Basic Chat Functionality**
   - Type a query in the input box (e.g., "What is this book about?")
   - Click "Send" or press Enter
   - Verify loading state appears
   - Verify assistant response appears in message history
   - Verify message bubbles display correctly (user on right, assistant on left)

4. **Top_k Selector Verification**
   - Change top_k value from 5 to 3
   - Submit a query
   - Verify response respects the top_k setting

5. **Mode Toggle Verification**
   - Switch to "Selected Text Only" mode
   - Verify selected_text textarea appears
   - Enter some text in the selected_text field
   - Submit a query
   - Switch back to "Retrieval" mode
   - Verify selected_text field disappears

6. **Source Display Verification**
   - Submit a query that returns sources
   - Verify "Sources" section appears with source count
   - Click "Show Content" for a source
   - Verify content is displayed
   - Click "Hide Content"
   - Verify content is hidden

7. **Error Handling Verification**
   - Try submitting an empty query
   - Verify appropriate error handling
   - Test with invalid inputs

### API Endpoint Verification (using curl)

1. **Test Health Endpoint**
   ```bash
   curl -X GET http://127.0.0.1:8000/health
   ```

2. **Test Chat Query Endpoint**
   ```bash
   curl -X POST http://127.0.0.1:8000/api/v1/chat/query \
        -H "Content-Type: application/json" \
        -d "{\"query\":\"What is this book about?\",\"top_k\":3}"
   ```

3. **Test with Selected Text Mode**
   ```bash
   curl -X POST http://127.0.0.1:8000/api/v1/chat/query \
        -H "Content-Type: application/json" \
        -d "{\"query\":\"Based on this text\",\"selected_text\":\"Sample text for analysis\",\"top_k\":2}"
   ```

## Production Verification

### Prerequisites
- Vercel environment variable `CHAT_API_BASE_URL` set to production backend URL
- Deployed backend URL accessible from Vercel frontend

### Verification Steps

1. **Environment Configuration**
   - Verify `CHAT_API_BASE_URL` environment variable is set correctly in Vercel dashboard
   - Verify the value points to the deployed backend URL

2. **Deployed Site Verification**
   - Navigate to the deployed site's `/chat` route
   - Verify the page loads correctly
   - Verify health indicator shows the correct status for the production backend

3. **Functionality Verification**
   - Test all chat features work as expected in production
   - Verify all controls (top_k, mode toggle, etc.) function properly
   - Verify sources display correctly
   - Verify error handling works in production

4. **CORS Configuration**
   - Verify that the production backend allows requests from the Vercel domain
   - Check browser developer tools for any CORS errors
   - Verify API calls succeed without CORS issues

### PowerShell/Invoke-RestMethod Examples

```powershell
# Test health endpoint
$response = Invoke-RestMethod -Uri "http://127.0.0.1:8000/health" -Method Get
Write-Host "Health Status:" $response.status

# Test chat query endpoint
$body = @{
    query = "What is this book about?"
    top_k = 3
} | ConvertTo-Json

$response = Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/v1/chat/query" -Method Post -Body $body -ContentType "application/json"
Write-Host "Answer:" $response.answer
Write-Host "Sources Count:" $response.sources.Count

# Test selected text mode
$body = @{
    query = "Analyze this text"
    selected_text = "This is sample text for analysis"
    top_k = 2
} | ConvertTo-Json

$response = Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/v1/chat/query" -Method Post -Body $body -ContentType "application/json"
Write-Host "Answer:" $response.answer
```

## Network Configuration Verification

### Option A: CORS + Direct API Calls (Primary)
- [ ] Backend configured to allow Vercel domain and localhost:3000
- [ ] Backend accepts requests from Vercel deployment URL
- [ ] Backend accepts requests from localhost:3000 during development
- [ ] No CORS errors in browser console

### Option B: Proxy Approach (Fallback)
- [ ] Alternative proxy method documented and tested (if needed)
- [ ] Proxy configuration compatible with Docusaurus/Vercel (if needed)

## Final Verification Checklist

- [x] All functional requirements (FR-001 to FR-012) implemented
- [x] Local verification completed successfully
- [x] API endpoints working correctly
- [x] UI components functioning as expected
- [x] Error handling in place
- [x] Environment configuration set up
- [x] No regression in existing functionality
- [x] Production deployment preparation complete
- [x] Verification tests passed