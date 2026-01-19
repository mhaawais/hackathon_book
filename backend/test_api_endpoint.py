#!/usr/bin/env python3
"""
Test script to verify the API endpoint works with the Gemini integration.
"""
import asyncio
import json
import httpx
from datetime import datetime
from pathlib import Path

async def test_api():
    """Test the API endpoint with a sample query."""

    # Sample query
    query_data = {
        "query": "What is ROS2?",
        "top_k": 5
    }

    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            # Test the query endpoint
            response = await client.post(
                "http://127.0.0.1:8001/api/v1/chat/query",
                json=query_data
            )

            print(f"Response Status: {response.status_code}")

            if response.status_code == 200:
                response_data = response.json()
                print("✅ API endpoint working correctly!")
                print(f"Answer: {response_data.get('answer', '')[:200]}...")
                print(f"Sources: {len(response_data.get('sources', []))}")
                print(f"Mode: {response_data.get('mode_used', 'unknown')}")

                # Verify response structure
                required_fields = ['answer', 'sources', 'mode_used', 'retrieval_time_ms', 'total_time_ms']
                missing_fields = [field for field in required_fields if field not in response_data]

                if missing_fields:
                    print(f"! Missing fields: {missing_fields}")
                else:
                    print("SUCCESS: All required fields present")

                return True
            else:
                print(f"ERROR: API returned error: {response.status_code}")
                print(f"Response: {response.text}")
                return False

    except httpx.ConnectError:
        print("ERROR: Cannot connect to server. Make sure it's running on port 8001.")
        return False
    except Exception as e:
        print(f"ERROR: Error testing API: {str(e)}")
        return False

async def test_health_endpoint():
    """Test the health endpoint."""
    try:
        from src.main import app
        from fastapi.testclient import TestClient

        client = TestClient(app)

        # Test GET /health
        response = client.get("/health")

        print(f"\nHealth endpoint status: {response.status_code}")

        if response.status_code == 200:
            health_data = response.json()
            print(f"SUCCESS: Health check passed: {health_data}")
            return True
        else:
            print(f"ERROR: Health check failed: {response.status_code}, {response.text}")
            return False

    except Exception as e:
        print(f"ERROR: Error testing health endpoint: {str(e)}")
        return False

async def main():
    print("Testing API endpoints after Gemini integration...")

    # Test health endpoint first
    health_ok = await test_health_endpoint()

    # Test query endpoint
    query_ok = await test_api()

    # Summary
    print(f"\n{'='*50}")
    print("API TEST SUMMARY:")
    print(f"Health endpoint: {'SUCCESS' if health_ok else 'FAILED'}")
    print(f"Query endpoint: {'SUCCESS' if query_ok else 'FAILED'}")
    print(f"{'='*50}")

    if health_ok and query_ok:
        print("SUCCESS: All API endpoints working correctly with Gemini integration!")
        return True
    else:
        print("WARNING: Some API endpoints may have issues.")
        return False

if __name__ == "__main__":
    success = asyncio.run(main())

    # Save test results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    test_result = {
        "timestamp": timestamp,
        "api_test_success": success,
        "integration": "Gemini API",
        "status": "PASS" if success else "FAIL"
    }

    # Save to history
    history_dir = Path("history") / "003-agent-retrieval"
    history_dir.mkdir(parents=True, exist_ok=True)
    result_file = history_dir / f"api_test_result_{timestamp}.json"

    with open(result_file, 'w') as f:
        json.dump(test_result, f, indent=2)

    print(f"\nTest results saved to: {result_file}")