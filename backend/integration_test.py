#!/usr/bin/env python3
"""
Integration test that calls the running API and verifies it returns proper responses.
"""

import requests
import json
import time
import sys

def test_api_integration():
    """
    Test the API endpoint to verify it returns proper responses with sources.
    """
    url = "http://127.0.0.1:8000/api/v1/chat/query"

    # Test payload
    payload = {
        "query": "What is ROS2?",
        "top_k": 5
    }

    print("Testing API endpoint: POST /api/v1/chat/query")
    print(f"Payload: {json.dumps(payload)}")

    try:
        response = requests.post(url, json=payload, timeout=30)

        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")

        if response.status_code != 200:
            print("[FAILED] API returned non-200 status code")
            return False

        try:
            data = response.json()
            print(f"Parsed response: {data}")

            # Check if answer contains error (indicating failure)
            if "error processing your request" in data.get("answer", ""):
                print("[FAILED] Response contains error message")
                return False

            # Check if sources are present (requirement: sources length >= 1)
            sources = data.get("sources", [])
            if len(sources) == 0:
                print("[FAILED] No sources returned")
                return False

            # Check if at least one source URL includes "/docs/"
            docs_sources = [s for s in sources if "/docs/" in s.get("url", "")]
            if len(docs_sources) == 0:
                print("[FAILED] No sources contain '/docs/' in URL")
                print(f"Available sources: {[s.get('url') for s in sources]}")
                return False

            print(f"[SUCCESS] Got {len(sources)} sources, {len(docs_sources)} from /docs/")
            print(f"Answer preview: {data.get('answer', '')[:100]}...")
            return True

        except json.JSONDecodeError:
            print("[FAILED] Response is not valid JSON")
            return False

    except requests.exceptions.RequestException as e:
        print(f"[FAILED] Request error - {e}")
        return False

if __name__ == "__main__":
    print("Running API Integration Test...")
    success = test_api_integration()

    if not success:
        print("\nIntegration test FAILED")
        sys.exit(1)
    else:
        print("\nIntegration test PASSED")
        sys.exit(0)