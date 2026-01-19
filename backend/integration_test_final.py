#!/usr/bin/env python3
"""
Final integration test that calls the running API and verifies it works properly.
"""

import requests
import json
import time
import sys
import subprocess
import threading
import signal
import os

def start_server():
    """Start the uvicorn server in a subprocess."""
    cmd = ["python", "-m", "uvicorn", "src.main:app", "--host", "127.0.0.1", "--port", "8000", "--reload"]
    process = subprocess.Popen(cmd, cwd=".", stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Give the server time to start
    time.sleep(5)
    return process

def test_api_integration():
    """
    Test the API endpoint to verify it returns proper responses with sources.
    """
    url = "http://127.0.0.1:8000/api/v1/chat/query"

    # Test payload for retrieval mode
    payload = {
        "query": "What is ROS2?",
        "top_k": 5
    }

    print("Testing API endpoint: POST /api/v1/chat/query")
    print(f"Payload: {json.dumps(payload)}")

    try:
        response = requests.post(url, json=payload, timeout=30)

        print(f"Status Code: {response.status_code}")

        if response.status_code != 200:
            print(f"❌ FAILED: API returned non-200 status code: {response.status_code}")
            print(f"Response: {response.text}")
            return False

        try:
            data = response.json()
            print(f"Response: {json.dumps(data, indent=2)}")

            # Check if answer contains error (indicating failure)
            answer = data.get("answer", "")
            if "error processing your request" in answer:
                print("❌ FAILED: Response contains error message")
                print(f"Error: {answer}")
                return False

            # Check if sources are present (requirement: sources length >= 1 for retrieval mode)
            sources = data.get("sources", [])
            if len(sources) == 0:
                print("❌ FAILED: No sources returned (expected >= 1 for retrieval mode)")
                return False

            # Check if at least one source URL includes "/docs/"
            docs_sources = [s for s in sources if "/docs/" in s.get("url", "")]
            if len(docs_sources) == 0:
                print("❌ FAILED: No sources contain '/docs/' in URL")
                print(f"Available sources: {[s.get('url') for s in sources]}")
                return False

            print(f"✅ SUCCESS: Got {len(sources)} sources, {len(docs_sources)} from /docs/")
            print(f"Answer preview: {answer[:100]}...")

            # Test selected-text-only mode as well
            print("\nTesting selected-text-only mode...")
            selected_text_payload = {
                "query": "What does this text say about testing?",
                "selected_text": "Testing is an important part of software development. It helps ensure quality and reliability.",
                "top_k": 5
            }

            response2 = requests.post(url, json=selected_text_payload, timeout=30)
            data2 = response2.json()
            sources2 = data2.get("sources", [])

            if len(sources2) != 0:
                print(f"❌ FAILED: Selected-text mode should return 0 sources, got {len(sources2)}")
                return False

            print("✅ SUCCESS: Selected-text mode correctly returned 0 sources")
            return True

        except json.JSONDecodeError:
            print("❌ FAILED: Response is not valid JSON")
            print(f"Raw response: {response.text}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"❌ FAILED: Request error - {e}")
        return False

def main():
    """Main function to start server and run tests."""
    print("Starting server and running integration test...")

    # Start the server
    server_process = start_server()

    try:
        # Run the test
        success = test_api_integration()

        if success:
            print("\n🎉 Integration test PASSED - API is working correctly!")
            return 0
        else:
            print("\n💥 Integration test FAILED")
            return 1

    finally:
        # Terminate the server
        server_process.terminate()
        try:
            server_process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            server_process.kill()

if __name__ == "__main__":
    result = main()
    sys.exit(result)