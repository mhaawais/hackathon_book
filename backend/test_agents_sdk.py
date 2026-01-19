#!/usr/bin/env python3
"""
Test script to verify the OpenAI Agents SDK implementation works correctly.
"""

import sys
import os
import time
import json
from datetime import datetime
from pathlib import Path

# Add the src directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))

from src.services.agent_service import AgentService
from src.models.request import QueryRequest


def test_agents_sdk_implementation():
    """
    Test the OpenAI Agents SDK implementation with both modes.
    """
    print("[TESTING] OpenAI Agents SDK Implementation...")

    # Initialize the agent service
    agent_service = AgentService()

    # Create test report structure
    test_report = {
        "timestamp": datetime.now().isoformat(),
        "feature": "OpenAI Agents SDK Implementation",
        "test_results": {},
        "summary": {}
    }

    print("\n[TEST 1] Retrieval Mode (should call retrieval tool)")
    try:
        start_time = time.time()

        # Create a test query for retrieval mode
        query_request = QueryRequest(
            query="What is this system about?",
            top_k=3
        )

        # Process the query
        import asyncio
        response = asyncio.run(agent_service.process_query_with_full_response(query_request))

        test_duration = time.time() - start_time

        # Check if the response is valid - for retrieval mode, we need at least 1 source and the source URLs should contain "/docs/"
        has_sources = len(response.sources) > 0
        has_docs_urls = any("/docs/" in source.url for source in response.sources) if response.sources else False

        is_valid = (
            response.answer and
            response.mode_used == "retrieval" and
            has_sources and  # Must have at least 1 source
            has_docs_urls    # At least one source must be from /docs/ section
        )

        # Determine status based on strict requirements
        if response.error:
            status = "ERROR"
        elif not has_sources:
            status = "FAILED"  # Fail if no sources returned
        elif not has_docs_urls:
            status = "FAILED"  # Fail if no sources from /docs/ section
        elif is_valid:
            status = "PASSED"
        else:
            status = "FAILED"

        test_result = {
            "test_id": "T001",
            "test_name": "Retrieval Mode",
            "status": status,
            "duration_ms": test_duration * 1000,
            "mode_used": response.mode_used,
            "sources_count": len(response.sources),
            "has_answer": bool(response.answer),
            "has_docs_sources": has_docs_urls,
            "error_present": response.error is not None,
            "response_preview": response.answer[:100] + "..." if len(response.answer) > 100 else response.answer if response.answer else "No answer",
            "retrieval_time_ms": response.retrieval_time_ms,
            "total_time_ms": response.total_time_ms
        }

        print(f"  Status: {test_result['status']}")
        print(f"  Duration: {test_result['duration_ms']:.2f}ms")
        print(f"  Mode: {response.mode_used}")
        print(f"  Sources: {len(response.sources)}")
        print(f"  Has /docs/ sources: {has_docs_urls}")
        print(f"  Has answer: {bool(response.answer)}")

        if response.error:
            print(f"  Error: {response.error.message}")
        elif len(response.sources) == 0:
            print(f"  Issue: No sources returned - retrieval failed")
        elif not has_docs_urls:
            print(f"  Issue: No sources from /docs/ section found")

        test_report["test_results"]["retrieval_mode"] = test_result

    except Exception as e:
        test_result = {
            "test_id": "T001",
            "test_name": "Retrieval Mode",
            "status": "ERROR",
            "error": str(e),
            "duration_ms": 0
        }
        test_report["test_results"]["retrieval_mode"] = test_result
        print(f"  Status: ERROR - {str(e)}")

    print("\n[TEST 2] Selected-text-only Mode (should NOT call retrieval tool)")
    try:
        start_time = time.time()

        # Create a test query with selected text for selected-text-only mode
        query_request = QueryRequest(
            query="What does this text say about testing?",
            selected_text="Testing is an important part of software development. It helps ensure quality and reliability. Automated tests can catch bugs early in the development cycle.",
            top_k=3
        )

        # Process the query
        import asyncio
        response = asyncio.run(agent_service.process_query_with_full_response(query_request))

        test_duration = time.time() - start_time

        # Check if the response is valid for selected-text-only mode
        is_valid = (
            response.answer and
            response.mode_used == "selected-text-only" and
            len(response.sources) == 0  # Should have no sources in selected-text-only mode
        )

        test_result = {
            "test_id": "T002",
            "test_name": "Selected-text-only Mode",
            "status": "PASSED" if is_valid else "FAILED",
            "duration_ms": test_duration * 1000,
            "mode_used": response.mode_used,
            "sources_count": len(response.sources),
            "has_answer": bool(response.answer),
            "error_present": response.error is not None,
            "response_preview": response.answer[:100] + "..." if len(response.answer) > 100 else response.answer if response.answer else "No answer",
            "retrieval_time_ms": response.retrieval_time_ms,
            "total_time_ms": response.total_time_ms
        }

        print(f"  Status: {test_result['status']}")
        print(f"  Duration: {test_result['duration_ms']:.2f}ms")
        print(f"  Mode: {response.mode_used}")
        print(f"  Sources: {len(response.sources)} (should be 0 in selected-text-only mode)")
        print(f"  Has answer: {bool(response.answer)}")

        if response.error:
            print(f"  Error: {response.error.message}")

        test_report["test_results"]["selected_text_only_mode"] = test_result

    except Exception as e:
        test_result = {
            "test_id": "T002",
            "test_name": "Selected-text-only Mode",
            "status": "ERROR",
            "error": str(e),
            "duration_ms": 0
        }
        test_report["test_results"]["selected_text_only_mode"] = test_result
        print(f"  Status: ERROR - {str(e)}")

    # Generate summary
    results = test_report["test_results"]
    passed_tests = 0
    total_tests = len(results)

    for result in results.values():
        if result["status"] == "PASSED" or result.get("status") == "WARNING":  # Count WARNING as partial success
            passed_tests += 1

    test_report["summary"] = {
        "total_tests": total_tests,
        "passed": passed_tests,
        "failed": total_tests - passed_tests,
        "success_rate": (passed_tests / total_tests * 100) if total_tests > 0 else 0
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
    report_filename = output_dir / f"agents_sdk_test_report_{timestamp_str}.json"

    with open(report_filename, 'w', encoding='utf-8') as f:
        json.dump(test_report, f, indent=2, default=str)

    print(f"\n[SAVED] Test report saved to: {report_filename}")

    # Also save to history directory
    history_dir = Path("../history/003-agent-retrieval")
    history_dir.mkdir(parents=True, exist_ok=True)

    history_filename = history_dir / f"agents_sdk_test_report_{timestamp_str}.json"

    with open(history_filename, 'w', encoding='utf-8') as f:
        json.dump(test_report, f, indent=2, default=str)

    print(f"[SAVED] Test report also saved to: {history_filename}")

    # Clean up the assistant
    try:
        agent_service.cleanup_assistant()
        print("🧹 Cleaned up assistant resources")
    except Exception as e:
        print(f"[WARNING] Could not clean up assistant: {str(e)}")

    return test_report


if __name__ == "__main__":
    print("Running OpenAI Agents SDK tests...")
    report = test_agents_sdk_implementation()

    print(f"\n[SUCCESS] OpenAI Agents SDK tests completed!")

    if report["summary"]["failed"] > 0:
        print("[WARNING] Some tests failed or encountered errors. Please check the report for details.")
        exit(1)
    else:
        print("[INFO] Tests completed! Note: Some tests may show 'WARNING' if no sources were found due to lack of proper API keys, which is expected in test environments.")
        exit(0)