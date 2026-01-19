#!/usr/bin/env python3
"""
Debug script to test AgentService directly without FastAPI.
This helps isolate issues between the service layer and API layer.
"""

import asyncio
import sys
import os

# Add the src directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))

from src.services.agent_service import AgentService
from src.models.request import QueryRequest


async def debug_agent_service():
    """
    Test the AgentService directly to verify retrieval works properly.
    """
    print("=== Debug AgentService Direct Call ===")

    # Initialize the agent service
    agent_service = AgentService()

    # Create a test query for retrieval mode
    query_request = QueryRequest(
        query="ROS2",
        top_k=5
    )

    print(f"Query: {query_request.query}")
    print(f"Top K: {query_request.top_k}")

    try:
        # Process the query directly using the agent service
        print("\nCalling agent_service.process_query_with_full_response()...")
        response = await agent_service.process_query_with_full_response(query_request)

        print(f"\nResponse received:")
        print(f"  Answer: {response.answer[:200]}..." if response.answer and len(response.answer) > 200 else f"  Answer: {response.answer}")
        print(f"  Mode used: {response.mode_used}")
        print(f"  Retrieval time: {response.retrieval_time_ms}ms")
        print(f"  Total time: {response.total_time_ms}ms")
        print(f"  Number of sources: {len(response.sources)}")

        if response.sources:
            print(f"\nFirst few sources:")
            for i, source in enumerate(response.sources[:3]):  # Show first 3 sources
                print(f"    [{i+1}] URL: {source.url}")
                print(f"        Score: {source.score}")
                print(f"        Content preview: {source.content[:100]}...")

        if response.error:
            print(f"\nError: {response.error.message}")

        print(f"\nSuccess: Direct AgentService call completed!")
        return response

    except Exception as e:
        print(f"Error in debug_agent_service: {str(e)}")
        import traceback
        traceback.print_exc()
        return None


if __name__ == "__main__":
    print("Starting AgentService debug test...")
    result = asyncio.run(debug_agent_service())

    if result:
        print("\n✅ Debug test completed successfully!")
        print(f"   - Answer length: {len(result.answer) if result.answer else 0}")
        print(f"   - Sources returned: {len(result.sources)}")
        print(f"   - Mode: {result.mode_used}")
        print(f"   - Total time: {result.total_time_ms}ms")
    else:
        print("\n❌ Debug test failed!")
        sys.exit(1)