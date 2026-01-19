#!/usr/bin/env python3
"""
End-to-end test runner for the Agent + Retrieval API.
"""

import sys
import os
import time
import json
from datetime import datetime
from pathlib import Path

# Add the src directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))

# Import the necessary modules from our backend
from src.services.agent_service import AgentService
from src.models.request import QueryRequest


def run_e2e_tests():
    """
    Run end-to-end tests for the Agent + Retrieval API.
    """
    print("[START] Starting End-to-End Tests for Agent + Retrieval API...")

    # Create test report structure
    test_report = {
        "timestamp": datetime.now().isoformat(),
        "feature": "Agent + Retrieval API",
        "tests_run": [],
        "summary": {}
    }

    # Initialize the agent service
    agent_service = AgentService()

    # Test 1: Normal retrieval mode
    print("\n[TEST 1] Normal retrieval mode")
    try:
        start_time = time.time()

        # Create a test query (this would normally retrieve from Qdrant)
        query_request = QueryRequest(
            query="What is the main purpose of this system?",
            top_k=3
        )

        # Process the query
        import asyncio
        response = asyncio.run(agent_service.process_query(query_request))

        test_duration = time.time() - start_time

        # Check if the response is valid for retrieval mode
        # Must have answer and sources in retrieval mode
        # At least one source URL should contain "/docs/"
        has_docs_url = any("/docs/" in source.url for source in response.sources) if response.sources else False

        is_valid = (
            response.answer and
            len(response.answer.strip()) > 0 and  # Non-empty answer
            not response.error and
            response.mode_used == "retrieval" and
            len(response.sources) >= 1 and  # At least 1 source in retrieval mode
            has_docs_url  # At least one source URL contains "/docs/"
        )

        test_result = {
            "test_id": "T001",
            "test_name": "Normal retrieval mode",
            "status": "PASSED" if is_valid else "FAILED",
            "duration_ms": test_duration * 1000,
            "mode_used": response.mode_used,
            "sources_count": len(response.sources),
            "response_preview": response.answer[:100] + "..." if len(response.answer) > 100 else response.answer,
            "retrieval_time_ms": response.retrieval_time_ms,
            "total_time_ms": response.total_time_ms
        }

        print(f"  Status: {test_result['status']}")
        print(f"  Duration: {test_result['duration_ms']:.2f}ms")
        print(f"  Mode: {response.mode_used}")
        print(f"  Sources: {len(response.sources)}")

        test_report["tests_run"].append(test_result)

    except Exception as e:
        test_result = {
            "test_id": "T001",
            "test_name": "Normal retrieval mode",
            "status": "ERROR",
            "error": str(e),
            "duration_ms": 0
        }
        test_report["tests_run"].append(test_result)
        print(f"  Status: ERROR - {str(e)}")

    # Test 2: Selected-text-only mode
    print("\n[TEST 2] Selected-text-only mode")
    try:
        start_time = time.time()

        # Create a test query with selected text
        query_request = QueryRequest(
            query="What does this text say about testing?",
            selected_text="Testing is an important part of software development. It helps ensure quality and reliability.",
            top_k=3
        )

        # Process the query
        import asyncio
        response = asyncio.run(agent_service.process_query(query_request))

        test_duration = time.time() - start_time

        test_result = {
            "test_id": "T002",
            "test_name": "Selected-text-only mode",
            "status": "PASSED" if response.answer and len(response.answer.strip()) > 0 and not response.error and len(response.sources) == 0 else "FAILED",
            "duration_ms": test_duration * 1000,
            "mode_used": response.mode_used,
            "sources_count": len(response.sources),
            "response_preview": response.answer[:100] + "..." if len(response.answer) > 100 else response.answer,
            "retrieval_time_ms": response.retrieval_time_ms,
            "total_time_ms": response.total_time_ms
        }

        print(f"  Status: {test_result['status']}")
        print(f"  Duration: {test_result['duration_ms']:.2f}ms")
        print(f"  Mode: {response.mode_used}")
        print(f"  Sources: {len(response.sources)} (should be 0 in selected-text-only mode)")

        test_report["tests_run"].append(test_result)

    except Exception as e:
        test_result = {
            "test_id": "T002",
            "test_name": "Selected-text-only mode",
            "status": "ERROR",
            "error": str(e),
            "duration_ms": 0
        }
        test_report["tests_run"].append(test_result)
        print(f"  Status: ERROR - {str(e)}")

    # Test 3: Health check simulation
    print("\n[TEST 3] Service availability check")
    try:
        start_time = time.time()

        # Check if services are available
        retrieval_available = agent_service.retrieval_tool.check_availability()

        test_duration = time.time() - start_time

        test_result = {
            "test_id": "T003",
            "test_name": "Service availability check",
            "status": "PASSED" if retrieval_available else "WARNING",
            "duration_ms": test_duration * 1000,
            "retrieval_tool_available": retrieval_available
        }

        print(f"  Status: {test_result['status']}")
        print(f"  Retrieval tool available: {retrieval_available}")

        test_report["tests_run"].append(test_result)

    except Exception as e:
        test_result = {
            "test_id": "T003",
            "test_name": "Service availability check",
            "status": "ERROR",
            "error": str(e),
            "duration_ms": 0
        }
        test_report["tests_run"].append(test_result)
        print(f"  Status: ERROR - {str(e)}")

    # Generate summary
    passed_tests = [t for t in test_report["tests_run"] if t["status"] == "PASSED"]
    failed_tests = [t for t in test_report["tests_run"] if t["status"] in ["FAILED", "ERROR"]]

    test_report["summary"] = {
        "total_tests": len(test_report["tests_run"]),
        "passed": len(passed_tests),
        "failed": len(failed_tests),
        "success_rate": len(passed_tests) / len(test_report["tests_run"]) * 100 if test_report["tests_run"] else 0
    }

    print(f"\n[SUMMARY] Test Summary:")
    print(f"  Total tests: {test_report['summary']['total_tests']}")
    print(f"  Passed: {test_report['summary']['passed']}")
    print(f"  Failed: {test_report['summary']['failed']}")
    print(f"  Success rate: {test_report['summary']['success_rate']:.1f}%")

    # Save test report
    output_dir = Path("test_results")
    output_dir.mkdir(exist_ok=True)

    timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_filename = output_dir / f"e2e_test_report_{timestamp_str}.json"

    with open(report_filename, 'w', encoding='utf-8') as f:
        json.dump(test_report, f, indent=2, default=str)

    print(f"\n[SAVED] Test report saved to: {report_filename}")

    # Also save to history directory as requested in the spec
    history_dir = Path("../history")
    history_dir.mkdir(exist_ok=True)

    history_subdir = history_dir / "003-agent-retrieval"
    history_subdir.mkdir(exist_ok=True)

    history_filename = history_subdir / f"e2e_test_report_{timestamp_str}.json"

    with open(history_filename, 'w', encoding='utf-8') as f:
        json.dump(test_report, f, indent=2, default=str)

    print(f"[SAVED] Test report also saved to: {history_filename}")

    return test_report


if __name__ == "__main__":
    print("Running end-to-end tests for Agent + Retrieval API...")
    report = run_e2e_tests()

    print(f"\n[SUCCESS] End-to-end tests completed!")

    if report["summary"]["failed"] > 0:
        print("[WARNING] Some tests failed or encountered errors. Please check the report for details.")
        exit(1)
    else:
        print("[INFO] All tests passed successfully!")
        exit(0)