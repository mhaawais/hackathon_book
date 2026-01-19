---
description: "Task list for Agent + Retrieval API implementation"
---

# Tasks: Agent + Retrieval API (OpenAI Agents SDK + FastAPI)

**Input**: Design documents from `/specs/003-agent-retrieval/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Backend API**: `backend/src/`, `backend/tests/`
- **Paths shown below follow the structure from plan.md**

<!--
  ============================================================================
  IMPORTANT: The tasks below are based on the feature specification and implementation plan.

  Tasks are organized by user story so each story can be:
  - Implemented independently
  - Tested independently
  - Delivered as an MVP increment
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create backend directory structure per implementation plan
- [X] T002 Initialize Python project with FastAPI, OpenAI, Cohere, Qdrant dependencies in backend/
- [X] T003 [P] Create requirements.txt with all required dependencies
- [X] T004 [P] Create .env.example file with required environment variables
- [X] T005 [P] Create Dockerfile for containerization

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T006 Create configuration module to load environment variables in backend/src/config/settings.py
- [X] T007 [P] Create request/response models in backend/src/models/request.py
- [X] T008 [P] Create chunk model in backend/src/models/chunk.py
- [X] T009 Create Qdrant client wrapper in backend/src/services/qdrant_client.py
- [X] T010 Create basic FastAPI application in backend/src/main.py
- [X] T011 Create API router structure in backend/src/api/v1/router.py
- [X] T012 Set up error handling and logging infrastructure in backend/src/utils/

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Query Documentation with Agent (Priority: P1) 🎯 MVP

**Goal**: Enable users to ask questions about documentation and receive answers with source citations from Qdrant

**Independent Test**: Can be fully tested by sending a query to the chat/query endpoint and verifying that the agent returns a response with proper provenance information.

### Tests for User Story 1 (OPTIONAL - for verification) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T013 [P] [US1] Contract test for chat/query endpoint in backend/tests/contract/test_chat_api.py
- [ ] T014 [P] [US1] Integration test for full query flow in backend/tests/integration/test_query_flow.py

### Implementation for User Story 1

- [X] T015 [P] [US1] Create retrieval tool service in backend/src/services/retrieval_tool.py
- [X] T016 [US1] Create agent service in backend/src/services/agent_service.py
- [X] T017 [US1] Implement health endpoint in backend/src/api/v1/health.py
- [X] T018 [US1] Implement chat/query endpoint in backend/src/api/v1/chat.py
- [X] T019 [US1] Connect retrieval tool to agent service
- [X] T020 [US1] Add provenance information to responses
- [X] T021 [US1] Add timing measurements for retrieval and total processing

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Selected Text Only Mode (Priority: P2)

**Goal**: Allow users to provide specific text selections for the agent to answer from, bypassing Qdrant retrieval

**Independent Test**: Can be tested by submitting a query with selected text parameter and verifying the agent only uses that text for answers.

### Tests for User Story 2 (OPTIONAL - for verification) ⚠️

- [ ] T022 [P] [US2] Contract test for selected-text-only functionality in backend/tests/contract/test_selected_text.py
- [ ] T023 [P] [US2] Integration test for selected-text-only flow in backend/tests/integration/test_selected_text_flow.py

### Implementation for User Story 2

- [X] T024 [P] [US2] Enhance agent service to support selected-text-only mode in backend/src/services/agent_service.py
- [X] T025 [US2] Update chat endpoint to handle selected_text parameter in backend/src/api/v1/chat.py
- [X] T026 [US2] Modify response format to indicate mode used in backend/src/models/request.py
- [X] T027 [US2] Ensure Qdrant retrieval is bypassed when selected_text is provided

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Health and Status Monitoring (Priority: P3)

**Goal**: Provide monitoring capabilities for system administrators to check service health

**Independent Test**: Can be tested by calling the health/status endpoint and verifying it returns appropriate status information.

### Tests for User Story 3 (OPTIONAL - for verification) ⚠️

- [ ] T028 [P] [US3] Contract test for health endpoint in backend/tests/contract/test_health_api.py
- [ ] T029 [P] [US3] Integration test for health monitoring in backend/tests/integration/test_health_monitoring.py

### Implementation for User Story 3

- [X] T030 [P] [US3] Enhance health status model in backend/src/models/chunk.py (HealthStatus)
- [X] T031 [US3] Implement service connectivity checks in backend/src/api/v1/health.py
- [X] T032 [US3] Add version reporting to health endpoint

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Error Handling & Validation

**Purpose**: Robust error handling for empty queries, retrieval failures, and upstream API failures

- [X] T033 [P] Add input validation utilities in backend/src/utils/validation.py
- [X] T034 [P] Add comprehensive error handling for empty queries
- [X] T035 Add error handling for Qdrant retrieval failures
- [X] T036 Add error handling for upstream API (OpenAI, Cohere) failures
- [X] T037 Update response models to include error states in backend/src/models/request.py

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T038 [P] Documentation updates in backend/README.md
- [X] T039 Code cleanup and refactoring across all modules
- [ ] T040 Performance optimization for retrieval and agent processing
- [ ] T041 [P] Additional unit tests in backend/tests/unit/
- [ ] T042 Security hardening (API key validation, rate limiting)
- [ ] T043 Run quickstart.md validation and update if needed
- [X] T044 Create end-to-end test runner for verification
- [X] T045 Save test run reports to history/ directory

---
## Phase 8: Missing Requirements Coverage

**Purpose**: Address uncovered functional requirements from spec analysis

- [ ] T046 [FR-007] Add comprehensive error handling for empty query validation in backend/src/utils/validation.py
- [ ] T047 [FR-008] Enhance Qdrant retrieval error handling with graceful fallbacks in backend/src/services/qdrant_client.py
- [ ] T048 [FR-009] Implement upstream API failure handling (OpenAI/Cohere) with retry logic in backend/src/services/agent_service.py
- [ ] T049 [FR-012] Create artifact archival system to save run logs to history/ directory in backend/src/utils/logging.py

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Error Handling (Phase 6)**: Depends on foundational completion and can run in parallel with user stories
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Builds on US1 agent service
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Independent of other stories

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence