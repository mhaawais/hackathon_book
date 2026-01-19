---
description: "Task list for Chat UI for Docusaurus Frontend"
---

# Tasks: Chat UI for Docusaurus Frontend

**Input**: Design documents from `/specs/004-chat-ui/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by functional requirements to ensure 100% coverage.

## Format: `[ID] [Title] [FR-XXX] [Dependencies] Description`

- **[ID]**: Sequential task identifier (T001, T002, etc.)
- **[Title]**: Brief descriptive title
- **[FR-XXX]**: Which functional requirement this task addresses (e.g., [FR-001], [FR-002], [FR-003])
- **[Dependencies]**: Task IDs that must be completed before this task
- Include exact file paths in descriptions

## Path Conventions

- **Repository root**: `physical-ai-book/`, `specs/`, `history/`
- **Docusaurus project**: `physical-ai-book/` directory
- **React components**: `physical-ai-book/src/components/`
- **Pages**: `physical-ai-book/src/pages/chat.jsx`
- **Utils**: `physical-ai-book/src/utils/chat-api.js`
- **Configuration**: `physical-ai-book/.env.example`, `physical-ai-book/docusaurus.config.ts`
- **Documentation**: `physical-ai-book/docs/`

## Phase 0: Research and Analysis (Blocking Prerequisites)

**Purpose**: Understand existing architecture and prepare for implementation

- [ ] T001 [Research Docusaurus Pattern] [FR-001] [] Research Docusaurus page creation pattern and confirm /chat route feasibility
- [ ] T002 [Verify Backend Endpoints] [FR-006] [] Verify backend API endpoints: POST /api/v1/chat/query and GET /health
- [ ] T003 [Examine API Response] [FR-006] [] Examine backend API response structure for {answer, sources, mode_used, retrieval_time_ms, total_time_ms, error?}
- [ ] T004 [Analyze CORS Options] [FR-010] [] Analyze CORS configuration options for Vercel production deployment
- [ ] T005 [Confirm Fetch Compatibility] [FR-006] [] Confirm native fetch API compatibility with Docusaurus environment

**Acceptance Criteria**:
- Docusaurus page creation pattern understood and documented
- Backend API endpoints confirmed working
- API response structure documented
- CORS configuration requirements identified
- Native fetch confirmed working with Docusaurus

**Files to Touch**:
- `physical-ai-book/docusaurus.config.ts`
- `backend/src/api/v1/chat.py`
- `backend/src/api/v1/health.py`

**Checkpoint**: Research complete - ready to implement architecture decisions

---

## Phase 1: Architecture and Environment Setup

**Purpose**: Establish foundational infrastructure for the chat UI

- [ ] T006 [Create Env Example] [FR-009] [T001] Create .env.example with CHAT_API_BASE_URL placeholder
- [ ] T007 [Env Variable Handling] [FR-009] [T006] Implement environment variable handling for API base URL
- [ ] T008 [Create API Service] [FR-006] [T002, T003, T005] Create chat-api.js utility with native fetch for POST /api/v1/chat/query
- [ ] T009 [Request Builder] [FR-006] [T008] Implement API request builder for query, top_k, and optional selected_text
- [ ] T010 [Response Handler] [FR-006] [T008] Create API response handler for {answer, sources, mode_used, retrieval_time_ms, total_time_ms, error?}
- [ ] T011 [Health Check Function] [FR-008] [T002] Create health check function using GET /health endpoint
- [ ] T012 [Create Chat Page] [FR-001] [T001] Create main chat page component at src/pages/chat.jsx

**Acceptance Criteria**:
- Environment variable properly configured and documented
- API service created with proper fetch implementation
- Request builder creates correct JSON bodies
- Response handler processes all expected fields
- Health check function works properly
- Chat page component created and renders

**Files to Touch**:
- `physical-ai-book/.env.example`
- `physical-ai-book/src/utils/chat-api.js`
- `physical-ai-book/src/pages/chat.jsx`

**Checkpoint**: Foundation ready - UI components can now be built

---

## Phase 2: Core UI Components (Docusaurus Chat Page)

**Purpose**: Implement the fundamental chat interface with messaging functionality

- [ ] T013 [Add Chat Route] [FR-001] [T012] Add /chat route to docusaurus.config.ts navigation
- [ ] T014 [Chat Window Component] [FR-002] [T012] Create ChatWindow component with container layout for message display
- [ ] T015 [Message List Component] [FR-002] [T014] Create MessageList component for displaying scrollable message history
- [ ] T016 [Message Styling] [FR-002] [T015] Implement user and assistant message bubble styling
- [ ] T017 [Message Input Component] [FR-003] [T012] Create MessageInput component with text area and send button
- [ ] T018 [Enter-to-Send] [FR-003] [T017] Implement Enter-key-to-send functionality
- [ ] T019 [Loading Indicator] [FR-003] [T017] Add loading indicator during API calls
- [ ] T020 [Non-regression Check] [FR-012] [] Verify no breaking changes to existing Docusaurus build

**Acceptance Criteria**:
- Chat route accessible at /chat
- Chat window renders properly with container layout
- Message list scrolls properly with message history
- User and assistant messages visually distinct
- Message input works with text area and send button
- Enter key submits message
- Loading indicator shows during API calls
- Existing Docusaurus functionality unchanged

**Files to Touch**:
- `physical-ai-book/docusaurus.config.ts`
- `physical-ai-book/src/components/Chat/ChatWindow.jsx`
- `physical-ai-book/src/components/Chat/MessageList.jsx`
- `physical-ai-book/src/components/Chat/MessageInput.jsx`

**Checkpoint**: Core chat interface functional with message display and input

---

## Phase 3: Control Components (Retrieval Parameters)

**Purpose**: Implement retrieval controls including top_k selector and mode toggles

- [ ] T021 [Controls Component] [FR-004] [T012] Create ChatControls component with top_k selector (default 5)
- [ ] T022 [Mode Toggle] [FR-004] [T021] Implement retrieval mode toggle functionality
- [ ] T023 [Selected Text Toggle] [FR-005] [T021] Create selected-text-only mode toggle
- [ ] T024 [Selected Text Input] [FR-005] [T023] Add conditional textarea for selected_text when mode enabled
- [ ] T025 [Request Integration] [FR-005] [T024] Ensure selected_text is included in requests when mode is enabled
- [ ] T026 [Control Integration] [FR-004, FR-005] [T021, T022, T025] Integrate controls with API request parameters

**Acceptance Criteria**:
- Top_k selector shows default value of 5 and allows changes
- Retrieval mode toggle switches between modes
- Selected-text-only mode toggle enables/disables textarea
- Textarea appears when selected-text mode is enabled
- selected_text included in requests when mode enabled
- All control values passed to API requests properly

**Files to Touch**:
- `physical-ai-book/src/components/Chat/ChatControls.jsx`
- `physical-ai-book/src/components/Chat/ModeToggle.jsx`
- `physical-ai-book/src/components/Chat/SelectedTextModal.jsx`

**Checkpoint**: All retrieval controls functional and integrated with API calls

---

## Phase 4: Sources and Citations UI

**Purpose**: Display sources returned by backend in a user-friendly, collapsible format

- [ ] T027 [Source Display Component] [FR-007] [T012] Create SourceDisplay component for citations
- [ ] T028 [Collapsible Sources] [FR-007] [T027] Implement collapsible "Sources" section per assistant message
- [ ] T029 [Clickable URLs] [FR-007] [T027] Create clickable URL links in sources that open in new tabs
- [ ] T030 [Content Display] [FR-007] [T027] Display content snippets and scores from source data
- [ ] T031 [Zero Sources Warning] [FR-007] [T027] Show warning message when retrieval mode returns 0 sources
- [ ] T032 [Source Formatting] [FR-007] [T027, T028, T029, T030] Format source display with URL, content snippet, and score

**Acceptance Criteria**:
- Sources display in collapsible sections per assistant message
- URLs are clickable and open in new tabs
- Content snippets and scores display properly
- Warning appears when 0 sources returned
- Source formatting includes URL, snippet, and score
- Sources UI responsive and user-friendly

**Files to Touch**:
- `physical-ai-book/src/components/Chat/SourceDisplay.jsx`
- `physical-ai-book/src/components/Chat/SourceItem.jsx`

**Checkpoint**: Sources display correctly with proper formatting and interactivity

---

## Phase 5: Health Monitoring

**Purpose**: Implement backend health indicator to show connection status

- [ ] T033 [Health Indicator Component] [FR-008] [T011] Create HealthIndicator component to check backend connectivity
- [ ] T034 [Health Check Integration] [FR-008] [T033] Integrate health check call to GET /health on page load
- [ ] T035 [Status Display] [FR-008] [T034] Display "Backend connected" or "Backend unreachable" status
- [ ] T036 [Periodic Checks] [FR-008] [T035] Implement periodic health checks with status updates

**Acceptance Criteria**:
- Health indicator component created and displays status
- Health check called on page load
- Correct status displayed (connected/unreachable)
- Periodic health checks update status appropriately
- Health status is visually clear to users

**Files to Touch**:
- `physical-ai-book/src/components/Chat/HealthIndicator.jsx`

**Checkpoint**: Health monitoring functional and informative

---

## Phase 6: Backend Integration and Error Handling

**Purpose**: Connect all UI components to backend API with comprehensive error handling

- [ ] T037 [Message Input Integration] [FR-006] [T008, T017] Integrate MessageInput with API service for POST /api/v1/chat/query calls
- [ ] T038 [JSON Request Body] [FR-006] [T009, T026] Implement proper JSON request body construction with query, top_k, and selected_text
- [ ] T039 [Answer Display] [FR-006] [T010, T015] Display assistant answers from API response in MessageList
- [ ] T040 [Response Error Handling] [FR-006] [T010] Handle error field in API response gracefully without UI crashes
- [ ] T041 [HTTP Error Handling] [FR-006] [T008] Handle HTTP errors from API calls with appropriate user feedback
- [ ] T042 [Security Verification] [FR-011] [T007] Verify no API keys or secrets are exposed in frontend code
- [ ] T043 [Regression Check] [FR-012] [T020] Verify existing Docusaurus functionality remains unaffected

**Acceptance Criteria**:
- Message input sends requests to backend API
- Request bodies include all required parameters
- Assistant answers display properly in message list
- Error responses handled gracefully without crashes
- HTTP errors caught and displayed appropriately
- No secrets exposed in frontend code
- Existing functionality remains intact

**Files to Touch**:
- `physical-ai-book/src/pages/chat.jsx`
- `physical-ai-book/src/utils/chat-api.js`
- `physical-ai-book/src/components/Chat/MessageInput.jsx`
- `physical-ai-book/src/components/Chat/MessageList.jsx`

**Checkpoint**: Full backend integration complete with proper error handling

---

## Phase 7: Production Deployment Preparation (Network Configuration)

**Purpose**: Prepare for production deployment on Vercel with proper network configuration

### Option A: CORS + Direct API Calls (Primary)

- [ ] T044 [Document CORS Config] [FR-010] [] Document CORS configuration for backend (allow Vercel domain + localhost)
- [ ] T045 [Vercel Env Setup] [FR-010] [T006] Document Vercel environment variable setup steps for CHAT_API_BASE_URL

### Option B: Proxy Approach (Fallback)

- [ ] T046 [Plan Proxy Approach] [FR-010] [] Plan fallback proxy approach if direct calls are blocked by CORS

- [ ] T047 [Env Config Test] [FR-009, FR-010] [T007, T045] Test environment variable configuration in production build
- [ ] T048 [Build Verification] [FR-012] [] Verify production build process doesn't break existing Docusaurus functionality

**Acceptance Criteria**:
- CORS configuration documented for production backend
- Vercel environment variable setup documented
- Fallback proxy approach planned if needed
- Environment variables work in production builds
- Production build succeeds without breaking existing functionality

**Files to Touch**:
- `backend/src/main.py` (for CORS configuration documentation)
- `physical-ai-book/.env.example`
- Documentation files

**Checkpoint**: Production deployment preparation complete with documented steps

---

## Phase 8: Verification and Testing

**Purpose**: Verify functionality in both local and production environments

- [ ] T049 [Local Verification] [FR-001, FR-002, FR-003, FR-004, FR-005, FR-006, FR-007, FR-008] [T043, T040, T041] Local verification: test chat functionality with running backend
- [ ] T050 [Production Verification] [FR-001, FR-002, FR-003, FR-004, FR-005, FR-006, FR-007, FR-008] [T049] Production verification: test deployed site calling deployed backend
- [ ] T051 [Request Builder Test] [FR-006, FR-007, FR-008] [T009, T010] Create minimal automated check for request builder functionality
- [ ] T052 [End-to-End Test] [FR-001, FR-002, FR-003, FR-004, FR-005, FR-006, FR-007, FR-008] [T049] End-to-end integration test with sample queries
- [ ] T053 [Proxy Fallback Test] [FR-010] [T046] Test fallback proxy approach if needed
- [ ] T054 [Final Regression] [FR-012] [T043, T048] Final verification that no existing Docusaurus functionality was broken

**Acceptance Criteria**:
- All features work locally with running backend
- All features work in production environment
- Request builder functions correctly
- End-to-end tests pass
- Fallback approach works if needed
- No regression in existing functionality

**Files to Touch**:
- Test scripts
- `physical-ai-book/src/test/chat-integration.test.js` (if created)

**Checkpoint**: All functionality verified in both local and production environments

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Final improvements that enhance the user experience

- [ ] T055 [Comprehensive Error Handling] [FR-002, FR-003, FR-006] [T040, T041] Add comprehensive error handling throughout the UI
- [ ] T056 [Input Validation] [FR-005] [T024] Implement proper input validation for selected_text when mode enabled
- [ ] T057 [Accessibility Features] [FR-002, FR-003] [T014, T017] Add accessibility features (ARIA labels, keyboard navigation)
- [ ] T058 [Mobile Responsiveness] [FR-002, FR-003, FR-007] [T014, T017, T027] Optimize for mobile responsiveness
- [ ] T059 [Enhanced UX] [FR-003] [T019] Add loading spinners and better UX feedback during API calls
- [ ] T060 [Documentation] [FR-001, FR-002, FR-003, FR-004, FR-005, FR-006, FR-007, FR-008] [T012, T014, T017, T021, T027, T033] Create README documentation for chat integration
- [ ] T061 [Event Cleanup] [FR-002, FR-003, FR-006, FR-007] [T015, T017, T027, T033] Implement proper cleanup of event listeners
- [ ] T062 [Final Integration Test] [FR-001, FR-002, FR-003, FR-004, FR-005, FR-006, FR-007, FR-008] [T052] Final integration test with comprehensive scenarios

**Acceptance Criteria**:
- Error handling covers all possible failure scenarios
- Input validation prevents invalid data submission
- Accessibility features meet standards
- UI responsive on all device sizes
- Enhanced UX feedback during operations
- Documentation complete and helpful
- Event listeners properly cleaned up
- All integration tests pass

**Files to Touch**:
- `physical-ai-book/src/components/Chat/*.jsx`
- `physical-ai-book/docs/chat-integration.md`
- `physical-ai-book/src/pages/chat.jsx`

## Traceability Matrix

| Functional Requirement | Tasks Addressing It |
|------------------------|-------------------|
| FR-001: Add new Docusaurus route/page | T013, T012 |
| FR-002: Message UI with bubbles and history | T014, T015, T016 |
| FR-003: Input features and loading state | T017, T018, T019 |
| FR-004: Retrieval controls (top_k, mode toggle) | T021, T022 |
| FR-005: Selected-text-only mode | T023, T024, T025 |
| FR-006: Backend API integration | T008, T009, T010, T037, T038, T039, T040, T041 |
| FR-007: Sources/citations display | T027, T028, T029, T030, T031, T032 |
| FR-008: Health indicator | T033, T034, T035, T036 |
| FR-009: Environment configuration | T006, T007, T047 |
| FR-010: CORS/proxy strategy | T044, T045, T046 |
| FR-011: Security measures | T042 |
| FR-012: Non-regression | T020, T043, T048, T054 |

## Verification Checklist

### Local Verification
- [ ] Backend running on http://127.0.0.1:8000
- [ ] Docusaurus running on http://localhost:3000
- [ ] Manual test: Navigate to /chat and verify UI loads
- [ ] Manual test: Submit query and verify response displays
- [ ] Manual test: Test top_k selector functionality
- [ ] Manual test: Test mode toggle functionality
- [ ] Manual test: Test selected-text-only mode
- [ ] Manual test: Verify sources display properly
- [ ] Manual test: Verify health indicator shows correct status
- [ ] Manual test: Verify error handling works (try bad query)
- [ ] Curl example: `curl -X POST http://127.0.0.1:8000/api/v1/chat/query -H "Content-Type: application/json" -d "{\"query\":\"test\",\"top_k\":5}"`
- [ ] Verify existing Docusaurus pages still work

### Production Verification
- [ ] Vercel environment variable CHAT_API_BASE_URL set to production backend URL
- [ ] Deployed backend URL accessible from Vercel frontend
- [ ] Chat functionality works on deployed Vercel site
- [ ] Health indicator shows correct status on production
- [ ] All controls function properly in production
- [ ] Sources display correctly in production
- [ ] Error handling works in production environment
- [ ] No performance issues in production

### Network Configuration Verification
- [ ] **Option A (Primary)**: CORS configured to allow Vercel domain and localhost
  - Backend accepts requests from Vercel deployment URL
  - Backend accepts requests from localhost:3000 during development
- [ ] **Option B (Fallback)**: Proxy approach implemented if CORS fails
  - Alternative proxy method documented and tested
  - Proxy configuration compatible with Docusaurus/Vercel

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 0 (Research)**: No dependencies - can start immediately
- **Phase 1 (Architecture)**: Depends on Phase 0 completion - BLOCKS all other phases
- **Phase 2-6**: All depend on Phase 1 completion
  - Phases 2-6 can proceed in parallel (if staffed)
  - Or sequentially as needed
- **Phase 7 (Production)**: Depends on core functionality being complete
- **Phase 8 (Verification)**: Depends on all functionality being complete
- **Phase 9 (Polish)**: Depends on all core functionality being complete

### Within Each Phase

- Core implementation before integration
- Each phase should be independently testable
- Tasks within phases follow dependency chains as specified

### Parallel Opportunities

- Tasks within phases can run in parallel when not dependent on each other
- Phases 2-6 can be worked on in parallel by different team members
- Multiple verification tasks can run in parallel

## Implementation Strategy

### Sequential Delivery

1. Complete Phase 0: Research → Ensure understanding of architecture
2. Complete Phase 1: Architecture → Foundation established
3. Complete Phase 2: Core UI → Basic chat functionality
4. Complete Phases 3-6: Feature implementation → All requirements met
5. Complete Phase 7: Production → Network configuration prepared
6. Complete Phase 8: Verification → Functionality validated
7. Complete Phase 9: Polish → Final enhancements

### Parallel Team Strategy

With multiple developers:

1. Team completes Phase 0-1 together (foundational work)
2. Once Phase 1 is done, parallel work on Phases 2-6:
   - Developer A: Phase 2 (Core UI)
   - Developer B: Phase 3 (Controls)
   - Developer C: Phase 4 (Sources)
   - Developer D: Phase 5 (Health)
   - Developer E: Phase 6 (Integration)
3. Consolidate and complete Phases 7-9 together

## Notes

- Each task has specific dependencies to ensure proper sequence
- FR mapping ensures 100% coverage of functional requirements
- Network configuration includes both primary and fallback approaches
- Verification includes both manual and automated testing
- Security measures prevent secret exposure in frontend
- Non-regression checks ensure existing functionality preserved