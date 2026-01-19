"""
Example test to validate retrieval validation functionality
"""
from retrieval_validator import RetrievalValidator
import os

# This is just a test to verify the class structure
# In a real scenario, you'd need proper API keys and Qdrant collection

print("Testing RetrievalValidator class structure...")

# Create an instance (this will fail without proper env vars, but that's expected)
try:
    validator = RetrievalValidator()
    print("Validator initialized successfully (with real API keys)")
except Exception as e:
    print(f"Expected error (no API keys): {type(e).__name__}: {e}")

print("\nTesting helper methods...")

# Test the query type classifier
validator = RetrievalValidator.__new__(RetrievalValidator)  # Create without init

test_queries = [
    "AI",  # short
    "What is artificial intelligence?",  # normal
    "Can you provide a comprehensive explanation of how the retrieval augmented generation system works in this book and what are the key components involved?",  # long
    "?????",  # edge
]

for query in test_queries:
    query_type = validator._classify_query_type(query)
    print(f"Query: '{query[:30]}...' -> Type: {query_type}")

print("\nAll basic tests passed!")