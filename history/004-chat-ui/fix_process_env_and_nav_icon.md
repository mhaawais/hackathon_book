# Fix process.env and add navbar chat icon

## Changes Made

### 1. Fixed "process is not defined" error
- Updated `docusaurus.config.ts` to use `customFields` to pass `CHAT_API_BASE_URL` to the browser
- Changed default port from 8000 to 8001 for local development
- Refactored `src/utils/chat-api.js` to accept base URL as a parameter instead of using `process.env`
- Updated `src/components/Chat/ChatWindow.jsx` to use `useDocusaurusContext()` to access the API base URL

### 2. Added navbar chat icon
- Created `static/img/chat.svg` with a simple chat bubble icon
- Updated navbar item in `docusaurus.config.ts` to include `className: 'navbar__link--chat'`
- Added CSS rules in `src/css/custom.css` to display the chat icon using CSS masking technique
- Icon inherits the current text color and works in both light/dark modes

### 3. Improved API error handling
- Enhanced error messages in the API client
- Better JSON response parsing with proper error handling

## Verification Steps

1. **Environment Configuration**:
   - Backend runs on http://127.0.0.1:8001 (default for local dev)
   - Frontend accesses the URL via Docusaurus customFields
   - No more "process is not defined" error in browser

2. **Navbar Icon**:
   - Chat icon appears next to "Chat" text in navbar
   - Icon is visible in both light and dark modes
   - Icon color follows the current text color

3. **API Integration**:
   - Chat page successfully connects to backend
   - Health indicator updates correctly
   - Query responses and sources display properly

4. **Local Development**:
   - Backend: `uv run python -m uvicorn src.main:app --host 127.0.0.1 --port 8001`
   - Frontend: `$env:CHAT_API_BASE_URL="http://127.0.0.1:8001"; npm run start`
   - Chat UI accessible at http://localhost:3000/chat

## Files Modified
- `physical-ai-book/docusaurus.config.ts` - Added customFields and navbar class
- `physical-ai-book/src/utils/chat-api.js` - Removed process.env, added createChatApi function
- `physical-ai-book/src/components/Chat/ChatWindow.jsx` - Use Docusaurus context for API URL
- `physical-ai-book/src/css/custom.css` - Added chat icon styling
- `physical-ai-book/static/img/chat.svg` - Added chat icon SVG
- `physical-ai-book/LOCAL_DEV.md` - Added local development instructions