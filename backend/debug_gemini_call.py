#!/usr/bin/env python3
"""
Debug script to verify Gemini API integration works properly.
This script tests:
1) GEMINI_API_KEY is set and accessible
2) Retrieval functionality works
3) Gemini returns a real answer
"""

import asyncio
import os
from pathlib import Path
from datetime import datetime

# Add the src directory to the path so we can import our modules
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))

from src.config.settings import settings
from src.services.agent_service import AgentService
from src.models.request import QueryRequest


async def main():
    print("=" * 60)
    print("Gemini API Integration Debug Script")
    print("=" * 60)

    # Check if GEMINI_API_KEY is set
    print(f"GEMINI_API_KEY set: {'Yes' if settings.gemini_api_key else 'No'}")
    print(f"GEMINI_MODEL: {settings.gemini_model}")

    if not settings.gemini_api_key:
        print("ERROR: GEMINI_API_KEY is not set in environment!")
        return False

    # Initialize the agent service
    print("\nInitializing AgentService...")
    agent_service = AgentService()

    # Test retrieval functionality
    print("\nTesting retrieval functionality...")
    try:
        # Perform a test retrieval
        test_query = "What is ROS2?"
        retrieved_chunks = agent_service.retrieval_tool.retrieve(
            query=test_query,
            top_k=3
        )

        print(f"Retrieved {len(retrieved_chunks)} chunks for query '{test_query}'")

        if retrieved_chunks:
            first_chunk = retrieved_chunks[0]

            # Safely print the chunk information handling encoding issues
            try:
                print(f"First chunk URL: {first_chunk['url']}")
                print(f"First chunk score: {first_chunk['score']}")
                print(f"First chunk preview: {first_chunk['content'][:100]}...")
            except UnicodeEncodeError:
                print(f"First chunk URL: {first_chunk['url'].encode('utf-8', errors='ignore').decode('utf-8')}")
                print(f"First chunk score: {first_chunk['score']}")
                print(f"First chunk preview: {first_chunk['content'][:100].encode('utf-8', errors='ignore').decode('utf-8')}...")
        else:
            print("WARNING: No chunks retrieved - Qdrant connection might be failing")

    except Exception as e:
        print(f"ERROR in retrieval: {str(e)}")
        return False

    # Test Gemini answer generation with retrieval
    print("\nTesting Gemini answer generation with retrieval...")
    try:
        query_request = QueryRequest(
            query="What is ROS2 and what are its main features?",
            top_k=3
        )

        response = await agent_service.process_query(query_request)

        print(f"Response mode: {response.mode_used}")
        print(f"Answer length: {len(response.answer)} characters")
        print(f"Number of sources: {len(response.sources)}")
        print(f"Retrieval time: {response.retrieval_time_ms:.2f}ms")
        print(f"Total time: {response.total_time_ms:.2f}ms")

        if response.error:
            print(f"ERROR in response: {str(response.error.message).encode('utf-8', errors='ignore').decode('utf-8')}")
            return False

        if not response.answer or len(response.answer.strip()) == 0:
            print("ERROR: Empty answer returned from Gemini")
            return False

        if response.mode_used != "retrieval":
            print(f"ERROR: Expected retrieval mode, got {response.mode_used}")
            return False

        if len(response.sources) == 0:
            print("ERROR: No sources returned in retrieval mode")
            return False

        # Check if at least one source URL contains "/docs/"
        has_docs_url = any("/docs/" in source.url for source in response.sources)
        if not has_docs_url:
            print("WARNING: No source URLs contain '/docs/' - this may indicate incorrect provenance")

        # Safely print the answer preview
        try:
            print(f"Answer preview: {response.answer[:200]}...")
        except UnicodeEncodeError:
            print(f"Answer preview: {response.answer[:200].encode('utf-8', errors='ignore').decode('utf-8')}...")

    except Exception as e:
        print(f"ERROR in Gemini answer generation: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

    # Test Gemini answer generation with selected text only
    print("\nTesting Gemini answer generation with selected text only...")
    try:
        query_request = QueryRequest(
            query="What does this text say about testing?",
            selected_text="Testing is a crucial part of software development. It helps ensure quality and reliability.",
            top_k=3
        )

        response = await agent_service.process_query(query_request)

        print(f"Response mode: {response.mode_used}")
        print(f"Answer length: {len(response.answer)} characters")
        print(f"Number of sources: {len(response.sources)}")

        if response.error:
            print(f"ERROR in response: {response.error.message}")
            return False

        if not response.answer or len(response.answer.strip()) == 0:
            print("ERROR: Empty answer returned from Gemini in selected-text mode")
            return False

        if response.mode_used != "selected-text-only":
            print(f"ERROR: Expected selected-text-only mode, got {response.mode_used}")
            return False

        if len(response.sources) != 0:
            print(f"ERROR: Expected 0 sources in selected-text mode, got {len(response.sources)}")
            return False

        print(f"Answer preview: {response.answer[:200]}...")

    except Exception as e:
        print(f"ERROR in Gemini selected-text answer generation: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

    print("\n" + "=" * 60)
    print("SUCCESS: All Gemini integration tests passed!")
    print("- GEMINI_API_KEY is properly set")
    print("- Retrieval functionality works")
    print("- Gemini returns real answers in both modes")
    print("- Response format is correct")
    print("=" * 60)

    # Save verification results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Save to backend history
    backend_history_dir = Path("history") / "003-agent-retrieval"
    backend_history_dir.mkdir(parents=True, exist_ok=True)
    backend_log_path = backend_history_dir / f"gemini_verification_{timestamp}.log"

    with open(backend_log_path, 'w') as f:
        f.write(f"Model: {settings.gemini_model}\n")
        f.write(f"Timestamp: {datetime.now()}\n")
        f.write(f"Status: SUCCESS\n")
        f.write(f"Verification: All Gemini integration tests passed\n")

    # Save to main history
    main_history_dir = Path("..") / "history" / "003-agent-retrieval"
    main_history_dir.mkdir(parents=True, exist_ok=True)
    main_log_path = main_history_dir / f"gemini_verification_{timestamp}.log"

    with open(main_log_path, 'w') as f:
        f.write(f"Model: {settings.gemini_model}\n")
        f.write(f"Timestamp: {datetime.now()}\n")
        f.write(f"Status: SUCCESS\n")
        f.write(f"Verification: All Gemini integration tests passed\n")

    print(f"Verification log saved to: {backend_log_path}")
    print(f"Verification log also saved to: {main_log_path}")

    return True


if __name__ == "__main__":
    success = asyncio.run(main())
    if success:
        print("\nSUCCESS: Gemini integration verification completed successfully!")
        exit(0)
    else:
        print("\nERROR: Gemini integration verification failed!")
        exit(1)