# Feature Specification: Chat UI for Docusaurus Frontend

**Feature Branch**: `004-chat-ui`
**Created**: 2026-01-17
**Status**: Draft
**Input**: User description: "Add a fully functional chatbot UI to the Docusaurus frontend (physical-ai-book) and connect it to the backend API so it works locally and in production."

Instructions

Treat this spec as the authoritative definition for the chat UI feature.
Do not introduce features outside this scope
Prefer simple, deterministic, and maintainable logic
Assume downstream features may depend on this UI
Optimize for user experience and seamless backend integration
Follow Spec-Driven Development strictly; no speculative design

Target Audience

Docusaurus users who want to interact with the AI-powered chatbot to get information about the book content.

Focus

Create a clean, functional chat UI integrated into the Docusaurus frontend that connects to the backend API for querying book content. The UI should work both locally and in production deployment on Vercel.

Success Criteria

- New Docusaurus route/page `/chat` with clean chat UI
- Message bubbles with user and assistant responses
- Input with text area, send button, and Enter-to-send functionality
- Retrieval controls: top_k selector and retrieval mode toggle
- Selected-text-only mode with toggle and required input field
- Proper API integration with error handling
- Sources/citations display with collapsible sections
- Health indicator showing backend connectivity
- Environment configuration for local and production
- CORS/proxy strategy documented for production deployment
- No breaking changes to existing Docusaurus functionality

Constraints

- Must integrate seamlessly with Docusaurus framework
- No AI keys in frontend; only call backend
- Responsive design for desktop and mobile
- Minimal dependencies; use native Docusaurus/React where possible
- Proper environment configuration for local vs production
- Maintain existing Docusaurus build and routes

Not Building

- Authentication/login
- Streaming responses (unless trivial)
- Persistent chat history across reloads
- Advanced conversation features beyond single queries
- Backend API changes (only consume existing API)

always create specs and history of complete work

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Access Chat Interface (Priority: P1)

A visitor wants to access the chat interface to ask questions about the book content. The user navigates to the /chat route and sees a clean, functional chat interface with input controls.

**Why this priority**: This is the foundational functionality - without access to the chat UI, no other functionality can be used. This delivers the core value of making book content queryable through AI.

**Independent Test**: The /chat route loads successfully with a functional chat interface including input area, send button, and message display area.

**Acceptance Scenarios**:

1. **Given** a user visits the /chat route, **When** the page loads, **Then** they see a clean chat interface with input controls
2. **Given** a user is on any other page of the site, **When** they access the chat feature, **Then** they can navigate to the /chat route and see the interface

---

### User Story 2 - Send Queries and Receive Responses (Priority: P1)

A user wants to ask questions about the book content and receive AI-generated responses. The user types a query, sends it, and receives a response with sources.

**Why this priority**: This is the core functionality that provides value to users by enabling them to interact with the AI and get answers to their questions.

**Independent Test**: The user can submit queries to the backend API and receive properly formatted responses with answer and sources.

**Acceptance Scenarios**:

1. **Given** a user types a query in the input box, **When** they press send or Enter, **Then** the query is sent to the backend and the response is displayed
2. **Given** a user submits a query, **When** the response comes back, **Then** it shows the answer and sources in a clear format
3. **Given** the backend returns an error, **When** the response is received, **Then** the error is displayed to the user without crashing the UI

---

### User Story 3 - Configure Retrieval Parameters (Priority: P2)

A user wants to control how the retrieval works by adjusting parameters like top_k and retrieval mode. The user can toggle between different modes and adjust settings.

**Why this priority**: This enhances the user experience by allowing customization of the retrieval behavior to suit their needs.

**Independent Test**: The user can adjust retrieval parameters (top_k, mode) and these settings are sent to the backend API.

**Acceptance Scenarios**:

1. **Given** a user wants to change the number of sources, **When** they adjust the top_k selector, **Then** this value is sent to the backend API
2. **Given** a user wants to use selected-text-only mode, **When** they toggle the mode and provide selected text, **Then** both query and selected_text are sent to the backend

---

### User Story 4 - View Sources and Citations (Priority: P2)

A user wants to see the sources used to generate the AI response to verify information and explore further. The sources are displayed in an organized way.

**Why this priority**: This provides transparency and allows users to validate the AI's responses and discover related content.

**Independent Test**: The sources returned by the backend are displayed in a collapsible section with clickable URLs and content snippets.

**Acceptance Scenarios**:

1. **Given** a response includes sources, **When** it's displayed, **Then** sources are shown in a collapsible section
2. **Given** a source has a URL, **When** the user clicks it, **Then** it opens in a new tab
3. **Given** a source has content, **When** it's displayed, **Then** it shows a readable snippet

---

### User Story 5 - Monitor Backend Health (Priority: P3)

A user wants to know if the backend is available and functioning properly. The UI shows the connection status to the backend service.

**Why this priority**: This provides transparency about system status and helps users understand when there are connectivity issues.

**Independent Test**: On page load, the UI checks backend health and displays the connection status.

**Acceptance Scenarios**:

1. **Given** the chat page loads, **When** a health check is performed, **Then** the UI shows either "Backend connected" or "Backend unreachable"
2. **Given** the backend is unreachable, **When** the status is displayed, **Then** the user is informed of the issue

---

### Edge Cases

- What happens when the backend API is temporarily unavailable during a query?
- How does the UI handle very long responses or sources?
- What occurs when the user submits an empty query?
- How does the UI behave when the selected-text-only mode is enabled but no text is provided?
- What happens when retrieval returns 0 sources?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST add new Docusaurus route/page: /chat (or /chatbot) with a clean chat UI
- **FR-002**: System MUST implement message UI with user and assistant bubbles, scrollable history, optional clear timestamps
- **FR-003**: System MUST provide input features: text input, send button, Enter-to-send functionality, and loading state
- **FR-004**: System MUST include retrieval controls: top_k selector (default 5) and "Retrieval mode" toggle
- **FR-005**: System MUST implement selected-text-only mode:
  - toggle ON/OFF functionality
  - when ON, show required textarea for selected_text
  - request must include selected_text and still include query
- **FR-006**: System MUST integrate with backend API:
  - frontend must call backend POST /api/v1/chat/query and display answer
  - show error messages from backend in UI (do not crash)
- **FR-007**: System MUST display sources/citations:
  - Collapsible "Sources" section per assistant message
  - each source shows clickable URL + snippet + score if present
  - show warning if retrieval mode returns 0 sources
- **FR-008**: System MUST include health indicator:
  - on page load call GET /health and show "Backend connected" or "Backend unreachable"
- **FR-009**: System MUST handle environment configuration:
  - frontend must read API base URL from env (e.g. CHAT_API_BASE_URL)
  - local default: http://127.0.0.1:8000
  - production: use env value (no hardcoding)
- **FR-010**: System MUST implement CORS/proxy strategy for production:
  - enable backend CORS for Vercel domain + localhost and call backend directly, OR
  - implement a proxy strategy that works with Docusaurus on Vercel
  - document exact steps for production deployment
- **FR-011**: System MUST implement security measures:
  - no Gemini/OpenAI/OpenRouter keys in frontend
  - frontend only calls backend; backend keeps secrets
- **FR-012**: System MUST ensure non-regression:
  - existing Docusaurus build must still succeed
  - no breaking changes to existing routes

### Key Entities

- **ChatMessage**: Represents a single message in the conversation, containing sender type (user/assistant), content, timestamp, and optional sources
- **QueryRequest**: Represents the data sent to the backend API, including query, selected_text, top_k, and session_id
- **AgentResponse**: Represents the data received from the backend API, including answer, sources, mode_used, timing information, and optional error
- **ChatConfig**: Represents user-configurable settings like top_k value and retrieval mode

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Chat UI loads successfully on both local and production environments (100% success rate)
- **SC-002**: Messages are displayed in clear user/assistant bubbles with proper formatting (100% of messages correctly formatted)
- **SC-003**: API integration works reliably with 95%+ success rate for query requests
- **SC-004**: Sources are displayed properly with clickable URLs and content snippets (100% of sources correctly displayed)
- **SC-005**: Health check indicates backend status accurately (100% accuracy in status reporting)
- **SC-006**: Retrieval controls function correctly and parameters are sent to backend (100% of parameter changes applied)
- **SC-007**: Selected-text-only mode works as specified with proper validation (100% of mode toggles work correctly)
- **SC-008**: Existing Docusaurus functionality remains unaffected (0% regression in existing features)
- **SC-009**: UI is responsive and works on both desktop and mobile devices (100% responsive design compliance)
- **SC-010**: Error handling prevents UI crashes and displays meaningful messages (100% of errors handled gracefully)