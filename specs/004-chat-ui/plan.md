# Implementation Plan: Chat UI for Docusaurus Frontend

**Branch**: `004-chat-ui` | **Date**: 2026-01-17 | **Spec**: [link to spec.md](./spec.md)
**Input**: Feature specification from `/specs/004-chat-ui/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Integration of a chatbot UI into the Docusaurus frontend that connects to the existing FastAPI backend. The solution follows a Docusaurus page-based approach with a dedicated /chat route that implements a React-based chat interface with message history, input controls, retrieval configuration, and source citation display. The implementation includes proper API integration, error handling, and environment configuration for both local and production deployment.

## Technical Context

**Framework**: Docusaurus 3.x with React
**Frontend Language**: TypeScript/JavaScript
**Primary Dependencies**: React hooks, native fetch for API calls, Docusaurus framework
**Backend Integration**: FastAPI endpoints at POST /api/v1/chat/query and GET /health
**Target Platform**: Web browsers (desktop and mobile)
**Project Type**: Docusaurus page extension
**Performance Goals**: Responsive UI with loading states, <3s average response time
**Constraints**: No AI keys in frontend, responsive design, environment-based configuration
**Scale/Scope**: Single page chat interface serving concurrent users

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- ✅ Spec-first execution: Following the spec from `/specs/004-chat-ui/spec.md`
- ✅ Source-grounded accuracy: Using established Docusaurus and React patterns
- ✅ Clear separation of concerns: Frontend UI clearly separated from backend API
- ✅ Reader-first technical clarity: Implementation will include clear documentation and error handling
- ✅ Deterministic, reproducible outputs: Using environment variables for configuration
- ✅ Secure key handling: No secrets in frontend; backend keeps all API keys

## Phase 0: Research and Analysis

**Goal**: Understand existing Docusaurus structure, backend API capabilities, and CORS configuration options.

**Files Touched**:
- `physical-ai-book/docusaurus.config.ts`
- `backend/src/main.py`
- `backend/src/api/v1/chat.py`
- `backend/src/api/v1/health.py`

**Key Decisions**:
- Confirm Docusaurus page creation pattern for /chat route
- Verify backend API response structure matches {answer, sources, mode_used, retrieval_time_ms, total_time_ms, error?}
- Evaluate CORS configuration options for Vercel production deployment

**Risks + Mitigations**:
- Risk: CORS blocking requests from Vercel domain
  - Mitigation: Plan both direct call and proxy fallback approaches
- Risk: Docusaurus page routing conflicts
  - Mitigation: Follow Docusaurus conventions for page creation

**Acceptance Checks**:
- [ ] Backend API endpoints confirmed working with test requests
- [ ] Docusaurus page creation pattern understood
- [ ] CORS configuration requirements identified

## Phase 1: Architecture and Environment Setup

**Goal**: Establish the foundation for the chat UI with proper environment configuration and API integration patterns.

**Files Touched**:
- `physical-ai-book/.env.example`
- `physical-ai-book/src/pages/chat.jsx`
- `physical-ai-book/src/utils/chat-api.js`

**Key Decisions**:
- Use native fetch API for minimal dependencies
- Implement CHAT_API_BASE_URL environment variable for configuration
- Create centralized API service module for backend communication
- Plan CORS strategy: Backend allows Vercel domain + localhost for direct calls

**Risks + Mitigations**:
- Risk: Environment variables not working in Docusaurus
  - Mitigation: Use proper Docusaurus environment handling
- Risk: API base URL not configurable
  - Mitigation: Verify Docusaurus supports environment variable access

**Acceptance Checks**:
- [ ] Environment variable configuration documented in .env.example
- [ ] API service module created with proper request/response handling
- [ ] CORS strategy documented for production deployment

## Phase 2: Core UI Components

**Goal**: Build the fundamental chat interface components with message display and user interaction.

**Files Touched**:
- `physical-ai-book/src/components/Chat/ChatWindow.jsx`
- `physical-ai-book/src/components/Chat/MessageList.jsx`
- `physical-ai-book/src/components/Chat/MessageInput.jsx`

**Key Decisions**:
- Implement message bubbles with user/assistant differentiation
- Create scrollable message history container
- Add loading indicators during API calls
- Support Enter-to-send and send button functionality

**Risks + Mitigations**:
- Risk: Poor performance with large message histories
  - Mitigation: Implement virtual scrolling if needed
- Risk: Layout issues on mobile devices
  - Mitigation: Test responsive design throughout development

**Acceptance Checks**:
- [ ] Message bubbles display correctly for user and assistant
- [ ] Scrollable message history works properly
- [ ] Enter-to-send and send button functionality works
- [ ] Loading indicators appear during API calls

## Phase 3: Control Components

**Goal**: Implement retrieval controls including top_k selector and mode toggles.

**Files Touched**:
- `physical-ai-book/src/components/Chat/ChatControls.jsx`
- `physical-ai-book/src/components/Chat/ModeToggle.jsx`
- `physical-ai-book/src/components/Chat/SelectedTextModal.jsx`

**Key Decisions**:
- Create top_k selector with default value of 5
- Implement retrieval mode toggle
- Create selected-text-only mode with conditional textarea
- Ensure selected_text is included in requests when mode is enabled

**Risks + Mitigations**:
- Risk: Complex state management for multiple controls
  - Mitigation: Use React hooks for centralized state management
- Risk: Validation issues with selected-text-only mode
  - Mitigation: Implement proper validation before sending requests

**Acceptance Checks**:
- [ ] Top_k selector works with default value of 5
- [ ] Retrieval mode toggle functions correctly
- [ ] Selected-text-only mode shows textarea when enabled
- [ ] Requests include selected_text when mode is enabled

## Phase 4: Sources and Citations UI

**Goal**: Display sources returned by the backend in a collapsible, user-friendly format.

**Files Touched**:
- `physical-ai-book/src/components/Chat/SourceDisplay.jsx`
- `physical-ai-book/src/components/Chat/SourceItem.jsx`

**Key Decisions**:
- Create collapsible "Sources" section per assistant message
- Display clickable URLs, content snippets, and scores
- Show warning when retrieval mode returns 0 sources
- Ensure proper formatting of source information

**Risks + Mitigations**:
- Risk: Malformed source data from backend
  - Mitigation: Implement defensive programming with null checks
- Risk: Long source content breaking UI
  - Mitigation: Implement content truncation with expand option

**Acceptance Checks**:
- [ ] Sources display in collapsible sections per assistant message
- [ ] URLs are clickable and open in new tabs
- [ ] Content snippets and scores display properly
- [ ] Warning shows when retrieval returns 0 sources

## Phase 5: Health Monitoring

**Goal**: Implement backend health indicator to show connection status.

**Files Touched**:
- `physical-ai-book/src/components/Chat/HealthIndicator.jsx`

**Key Decisions**:
- Call GET /health on page load
- Display connected/unreachable status
- Potentially implement periodic health checks

**Risks + Mitigations**:
- Risk: Health checks impacting performance
  - Mitigation: Limit frequency of health checks
- Risk: False positive/negative health status
  - Mitigation: Implement appropriate timeout and retry logic

**Acceptance Checks**:
- [ ] Health check called on page load
- [ ] Connected/unreachable status displayed correctly
- [ ] Status updates appropriately when backend state changes

## Phase 6: Backend Integration and Error Handling

**Goal**: Connect all UI components to backend API with proper error handling.

**Files Touched**:
- `physical-ai-book/src/utils/chat-api.js`
- `physical-ai-book/src/pages/chat.jsx`
- `physical-ai-book/src/components/Chat/*`

**Key Decisions**:
- Implement comprehensive error handling for API failures
- Display error messages gracefully without UI crashes
- Handle both error field in response and HTTP errors
- Ensure proper request body construction (query, top_k, selected_text)

**Risks + Mitigations**:
- Risk: Unhandled API errors crashing UI
  - Mitigation: Comprehensive error boundary and try/catch implementation
- Risk: Invalid request bodies causing backend errors
  - Mitigation: Input validation before sending requests

**Acceptance Checks**:
- [ ] API requests sent with proper JSON body format
- [ ] Error responses handled gracefully
- [ ] HTTP errors caught and displayed appropriately
- [ ] All control values (top_k, selected_text) included in requests when appropriate

## Phase 7: Production Deployment Preparation

**Goal**: Prepare for production deployment on Vercel with proper environment configuration.

**Files Touched**:
- `physical-ai-book/.env.example`
- Documentation files
- Vercel configuration files

**Key Decisions**:
- Document CORS configuration for backend (allow Vercel domain + localhost)
- Document Vercel environment variable setup steps
- Plan fallback proxy approach if direct calls are blocked
- Ensure zero breaking changes to existing Docusaurus build

**Risks + Mitigations**:
- Risk: Production CORS configuration not working
  - Mitigation: Have proxy fallback plan ready
- Risk: Breaking changes to existing Docusaurus functionality
  - Mitigation: Thorough testing of existing pages during development

**Acceptance Checks**:
- [ ] CORS configuration documented for production backend
- [ ] Vercel environment variable setup documented
- [ ] Fallback proxy approach documented if needed
- [ ] Existing Docusaurus functionality remains intact

## Phase 8: Verification and Testing

**Goal**: Verify functionality in both local and production environments.

**Files Touched**:
- Test scripts and documentation
- `physical-ai-book/src/test/chat-integration.test.js` (optional)

**Key Decisions**:
- Create local verification steps with backend running
- Create production verification steps for deployed site
- Implement minimal automated checks where feasible
- Document both manual and automated verification procedures

**Risks + Mitigations**:
- Risk: Issues only appearing in production environment
  - Mitigation: Thorough local testing with realistic data
- Risk: Difficult-to-test production scenarios
  - Mitigation: Comprehensive test coverage and monitoring

**Acceptance Checks**:
- [ ] Local verification steps documented and tested
- [ ] Production verification steps documented
- [ ] Basic automated tests implemented if feasible
- [ ] End-to-end functionality verified

## Traceability

| Functional Requirement | Planned Tasks |
|------------------------|---------------|
| FR-001: Add new Docusaurus route/page | Phase 1: Create /chat page component |
| FR-002: Message UI with bubbles and history | Phase 2: Core UI components |
| FR-003: Input features and loading state | Phase 2: MessageInput component |
| FR-004: Retrieval controls (top_k, mode toggle) | Phase 3: Control components |
| FR-005: Selected-text-only mode | Phase 3: Mode toggle with textarea |
| FR-006: Backend API integration | Phase 6: Backend integration |
| FR-007: Sources/citations display | Phase 4: Sources and citations UI |
| FR-008: Health indicator | Phase 5: Health monitoring |
| FR-009: Environment configuration | Phase 1: Environment setup |
| FR-010: CORS/proxy strategy | Phase 7: Production deployment |
| FR-011: Security measures | Throughout: No secrets in frontend |
| FR-012: Non-regression | Phase 7: Zero breaking changes |

## Project Structure

### Documentation (this feature)

```text
specs/004-chat-ui/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
physical-ai-book/
├── src/
│   └── pages/
│       └── chat.jsx          # Main chat interface page component
├── src/
│   └── components/
│       └── Chat/
│           ├── ChatWindow.jsx        # Main chat window container
│           ├── MessageList.jsx       # Component for displaying message history
│           ├── MessageInput.jsx      # Component for user input
│           ├── ChatControls.jsx      # Component for retrieval controls
│           ├── ModeToggle.jsx        # Component for mode toggles
│           ├── SelectedTextModal.jsx # Component for selected text input
│           ├── SourceDisplay.jsx     # Component for showing citations
│           ├── SourceItem.jsx        # Component for individual sources
│           └── HealthIndicator.jsx   # Component for backend health status
├── src/
│   └── utils/
│       └── chat-api.js              # API service for backend communication
├── .env.example                     # Example environment variables file
└── docs/
    └── chat-integration.md          # Documentation for the chat integration
```

**Structure Decision**: Docusaurus-based implementation using React components following Docusaurus conventions for page creation and component organization.

## Complexity Tracking

> Constitution Check has violations Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| N/A | N/A | N/A |