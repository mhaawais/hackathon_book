#!/usr/bin/env python3
"""
Debug script to test OpenRouter integration directly.
This script verifies that the OpenRouter client is properly configured and working.
"""

import asyncio
import os
import sys
from pathlib import Path

# Add the backend directory to the path so we can import our modules
sys.path.insert(0, str(Path(__file__).parent))

from src.config.settings import settings
from src.services.agent_service import AgentService


async def test_openrouter_connection():
    """
    Test the OpenRouter client connection and basic functionality.
    """
    print("=== OpenRouter Connection Test ===")
    print(f"Using model: {settings.model_name}")
    print(f"API Key configured: {'Yes' if settings.openrouter_api_key else 'No'}")

    if not settings.openrouter_api_key:
        print("ERROR: OPENROUTER_API_KEY not found in environment!")
        print("Please set OPENROUTER_API_KEY in your .env file")
        return False

    try:
        print("\nInitializing AgentService...")
        agent_service = AgentService()

        print(f"Model being used: {agent_service.model_name}")
        print("OpenRouter client initialized successfully!")

        # Perform a quick test by attempting to process a simple query
        from src.models.request import QueryRequest

        print("\nTesting with a simple query...")
        query_request = QueryRequest(
            query="What is Python programming?",
            top_k=1
        )

        # Process the query using the agent service
        response = await agent_service.process_query_with_full_response(query_request)

        print(f"Response mode: {response.mode_used}")
        print(f"Sources returned: {len(response.sources)}")
        print(f"Answer preview: {response.answer[:100] if response.answer else 'No answer'}...")

        if response.error:
            print(f"Error occurred: {response.error.message}")
        else:
            print("SUCCESS: OpenRouter call completed!")

        return True

    except Exception as e:
        print(f"ERROR during OpenRouter test: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    print("Starting OpenRouter verification test...")

    success = asyncio.run(test_openrouter_connection())

    if success:
        print("\nSUCCESS: OpenRouter verification completed successfully!")
        print("The OpenRouter client is properly configured and working.")
    else:
        print("\nFAILURE: OpenRouter verification failed!")
        sys.exit(1)