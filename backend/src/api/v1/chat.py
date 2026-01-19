from fastapi import APIRouter, HTTPException
from typing import Dict, Any
from ...models.request import QueryRequest, AgentResponse
from ...services.agent_service import AgentService
from ...utils.logging import log_api_call, log_error, get_logger
from ...utils.validation import validate_query_request
import time


router = APIRouter()
logger = get_logger("chat_api")


@router.post("/query", response_model=AgentResponse)
async def query_endpoint(request: QueryRequest):
    """
    Query the agent and receive a response with provenance information.

    Args:
        request: QueryRequest containing the user's question

    Returns:
        AgentResponse with answer and source information
    """
    from datetime import datetime

    # Record start time for total execution time
    request_start_time = time.time()

    try:
        # Log the API call
        log_api_call(
            endpoint="/chat/query",
            method="POST",
            params={"query_length": len(request.query), "has_selected_text": request.selected_text is not None},
            execution_time=None  # Will add after processing
        )

        # Validate the request
        is_valid, error_msg = validate_query_request(request)
        if not is_valid:
            # Return error in response instead of raising exception
            from ...models.request import AgentResponse, ErrorDetails
            return AgentResponse(
                answer=f"Invalid request: {error_msg}",
                sources=[],
                mode_used="retrieval",  # Default mode
                retrieval_time_ms=0,
                total_time_ms=(time.time() - request_start_time) * 1000,
                session_id=request.session_id,
                error=ErrorDetails(
                    type="ValidationError",
                    message=error_msg,
                    timestamp=datetime.utcnow()
                )
            )

        # Process the query using the agent service
        agent_service = AgentService()
        response = await agent_service.process_query(request)

        # Ensure total_time_ms is calculated from request start to end
        actual_total_time = (time.time() - request_start_time) * 1000

        # Update the response with correct total time to ensure total_time >= retrieval_time
        response.total_time_ms = actual_total_time

        # Log successful completion
        log_api_call(
            endpoint="/chat/query",
            method="POST",
            params={"query_length": len(request.query), "has_selected_text": request.selected_text is not None},
            response_size=len(response.answer) if response.answer else 0,
            execution_time=actual_total_time
        )

        return response

    except Exception as e:
        # Handle unexpected errors by returning them in the response instead of raising HTTPException
        execution_time = (time.time() - request_start_time) * 1000
        log_error(e, "query_endpoint")
        logger.error(f"Unexpected error in query endpoint: {str(e)} after {execution_time:.2f}ms")

        from ...models.request import AgentResponse, ErrorDetails
        return AgentResponse(
            answer=f"An unexpected error occurred while processing your request: {str(e)}",
            sources=[],
            mode_used="retrieval",  # Default mode
            retrieval_time_ms=0,
            total_time_ms=execution_time,
            session_id=request.session_id,
            error=ErrorDetails(
                type=type(e).__name__,
                message=str(e),
                timestamp=datetime.utcnow()
            )
        )


@router.get("/status")
async def chat_status():
    """
    Get the status of the chat service.

    Returns:
        Dictionary with service status information
    """
    try:
        agent_service = AgentService()

        # Check if the agent service is available
        retrieval_available = agent_service.retrieval_tool.check_availability()

        return {
            "status": "operational" if retrieval_available else "degraded",
            "retrieval_tool_available": retrieval_available,
            "timestamp": time.time()
        }
    except Exception as e:
        log_error(e, "chat_status")
        return {
            "status": "unavailable",
            "retrieval_tool_available": False,
            "timestamp": time.time(),
            "error": str(e)
        }