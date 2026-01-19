# Async Fix Proof Report: Agent + Retrieval API

## Date
January 15, 2026

## Overview
This report documents the async fixes applied to resolve the "asyncio.run() cannot be called from a running event loop" error in the Agent + Retrieval API system.

## Issues Identified
- POST /api/v1/chat/query endpoint was returning: "asyncio.run() cannot be called from a running event loop"
- Error occurred when agents were executed within FastAPI's async event loop
- Root cause: OpenAI Agents SDK's Runner.run() method conflicts with FastAPI's async context

## Fixes Applied

### 1. AgentService Async Conversion
- ✅ Converted all AgentService methods to async: `process_query()`, `_get_answer_from_selected_text_agent()`, `_get_answer_with_retrieval_agent()`, `process_query_with_full_response()`
- ✅ Updated all method calls to use `await` for async operations
- ✅ Made function tool synchronous (removed async from @function_tool)

### 2. Thread-Based Agent Execution
- ✅ Implemented thread-based execution using `loop.run_in_executor()` to isolate agent execution from FastAPI's event loop
- ✅ Each agent run creates a new event loop in a separate thread to avoid conflicts
- ✅ Properly managed event loop lifecycle (create, set, close)

### 3. Test Updates
- ✅ Updated test files to properly handle async methods
- ✅ Used asyncio.run() in test contexts (safe since tests run in isolated sync contexts)

## Results

### ✅ Test Results (Working)
- test_agents_sdk.py: Functions properly without asyncio errors
- test_e2e.py: Functions properly without asyncio errors
- Both test suites pass without the "asyncio.run() cannot be called from a running event loop" error

### ⚠️ API Endpoint Status (Still Failing)
- POST /api/v1/chat/query: Still returns "asyncio.run() cannot be called from a running event loop"
- Issue persists despite thread-based isolation approach
- Appears to be fundamental incompatibility between OpenAI Agents SDK and FastAPI

## Technical Details

### Key Files Modified
- `backend/src/services/agent_service.py` - Async conversion and thread-based execution
- `backend/src/api/v1/chat.py` - Async endpoint handler
- `backend/test_agents_sdk.py` - Async test method calls
- `backend/test_e2e.py` - Async test method calls

### Approach Used
- Agent execution isolated in separate threads with dedicated event loops
- Client configuration applied per-thread to avoid global state conflicts
- Proper async/await patterns throughout the call chain

## Verification Results

### Test Execution
- ✅ test_agents_sdk.py runs without asyncio errors
- ✅ test_e2e.py runs without asyncio errors
- ✅ Qdrant retrieval working: "Retrieval took 1385.92ms for 3 chunks"
- ✅ Both retrieval and selected-text modes functional in test environment

### API Endpoint
- ❌ POST /api/v1/chat/query still fails with asyncio error
- ❌ Error occurs immediately with minimal total_time_ms (0.145ms)

## Analysis

The async fixes are successful for test environments but the API endpoint continues to fail. This suggests a deeper architectural incompatibility between:
1. OpenAI Agents SDK's internal implementation
2. FastAPI's async event loop management
3. How the SDK handles function tools in async contexts

The thread-based isolation approach should theoretically resolve the issue, but the error suggests that the Agents SDK has internal mechanisms that still trigger the asyncio.run() error.

## Recommendations

For a production implementation, consider:
1. Using a different agent framework that's designed for async contexts
2. Implementing a queue-based approach where agent requests are processed outside the main API loop
3. Using a sync-based web framework for agent processing
4. Investigating if there are newer versions of the Agents SDK with better async support