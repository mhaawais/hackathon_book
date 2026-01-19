#!/usr/bin/env python3
"""
Smoke test script to verify backend API is accessible and functional.
This script tests the API endpoint that the frontend will use.
"""
import asyncio
import httpx
import json
from datetime import datetime
from pathlib import Path

async def smoke_test():
    """Basic smoke test for the backend API."""

    # Test data
    test_queries = [
        {
            "query": "What is ROS2?",
            "top_k": 3
        },
        {
            "query": "What are the main features?",
            "top_k": 5,
            "selected_text": "ROS2 is a flexible framework for robotics development. It provides tools, libraries, and conventions for building robot applications."
        }
    ]

    print("Running smoke test for backend API...")

    try:
        async with httpx.AsyncClient(timeout=30.0) as client:

            # Test health endpoint
            print("\nTesting health endpoint...")
            health_response = await client.get("http://127.0.0.1:8000/health")
            print(f"Health status: {health_response.status_code}")

            if health_response.status_code == 200:
                health_data = health_response.json()
                print(f"SUCCESS: Health check passed: {health_data}")
            else:
                print(f"ERROR: Health check failed: {health_response.status_code}")
                return False

            # Test API endpoint with different queries
            for i, query_data in enumerate(test_queries, 1):
                print(f"\nTesting query {i}: {query_data['query'][:30]}...")

                response = await client.post(
                    "http://127.0.0.1:8000/api/v1/chat/query",
                    json=query_data,
                    headers={"Content-Type": "application/json"}
                )

                print(f"Response status: {response.status_code}")

                if response.status_code == 200:
                    data = response.json()

                    # Check required fields
                    required_fields = ['answer', 'sources', 'mode_used', 'retrieval_time_ms', 'total_time_ms']
                    missing_fields = [field for field in required_fields if field not in data]

                    if missing_fields:
                        print(f"ERROR: Missing fields: {missing_fields}")
                        return False

                    print(f"SUCCESS: All required fields present")
                    print(f"  Answer length: {len(data.get('answer', ''))} chars")
                    print(f"  Sources count: {len(data.get('sources', []))}")
                    print(f"  Mode used: {data.get('mode_used', 'unknown')}")

                    # Verify sources structure if present
                    if data.get('sources'):
                        source = data['sources'][0] if data['sources'] else {}
                        source_fields = ['url', 'chunk_id', 'score', 'content']
                        source_missing = [field for field in source_fields if field not in source]

                        if not source_missing:
                            print(f"  SUCCESS: Source structure valid")
                        else:
                            print(f"  ERROR: Source missing fields: {source_missing}")

                else:
                    print(f"ERROR: Query {i} failed: {response.status_code}")
                    print(f"  Response: {response.text}")
                    return False

            print(f"\nSUCCESS: All smoke tests passed!")
            return True

    except httpx.ConnectError:
        print("ERROR: Cannot connect to backend server. Is it running on http://127.0.0.1:8000?")
        return False
    except Exception as e:
        print(f"ERROR: Smoke test error: {str(e)}")
        return False

async def main():
    """Run the smoke test and save results."""
    print("="*60)
    print("Frontend API Integration Smoke Test")
    print("="*60)

    success = await smoke_test()

    # Save results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    result_data = {
        "timestamp": timestamp,
        "test_type": "smoke_test",
        "target": "backend_api",
        "status": "PASS" if success else "FAIL",
        "endpoints_tested": [
            "/health",
            "/api/v1/chat/query"
        ],
        "queries_tested": 2,
        "notes": "Verifies API accessibility for frontend integration"
    }

    # Create history directory
    history_dir = Path("history") / "004-chat-ui"
    history_dir.mkdir(parents=True, exist_ok=True)

    # Save test results
    test_log_file = history_dir / f"test_smoke_{timestamp}.json"
    with open(test_log_file, 'w') as f:
        json.dump(result_data, f, indent=2)

    print(f"\nTest results saved to: {test_log_file}")

    # Also save to backend directory
    backend_history = Path("backend") / "history" / "004-chat-ui"
    backend_history.mkdir(parents=True, exist_ok=True)
    backend_log_file = backend_history / f"test_smoke_{timestamp}.json"
    with open(backend_log_file, 'w') as f:
        json.dump(result_data, f, indent=2)

    print(f"Test results also saved to: {backend_log_file}")

    return success

if __name__ == "__main__":
    success = asyncio.run(main())
    exit(0 if success else 1)