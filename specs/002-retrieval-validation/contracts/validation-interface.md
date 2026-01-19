# Validation Interface Specification

## Overview
The retrieval validation system provides programmatic validation of query retrieval accuracy against the Qdrant `docusaurus_content` collection. The system operates in read-only mode, validating that queries return relevant content chunks with proper metadata.

## Core Validation Functions

### validate_query_retrieval(query: str, top_k: int = 5) -> RetrievalValidationResult
Validates that a given query retrieves relevant content from Qdrant.

**Parameters**:
- `query` (str): The query text to validate
- `top_k` (int): Number of results to retrieve (default: 5)

**Returns**: `RetrievalValidationResult` object with validation metrics

**Validation Steps**:
1. Generate embedding for query using Cohere
2. Execute vector search against `docusaurus_content` collection
3. Apply URL-based filtering to prioritize `/docs/` content
4. Validate metadata integrity for each result
5. Calculate relevance scores
6. Return comprehensive validation result

### validate_metadata_integrity(retrieved_chunks: list) -> MetadataVerification
Validates that all retrieved chunks have proper metadata.

**Parameters**:
- `retrieved_chunks` (list): List of retrieved chunk objects

**Returns**: `MetadataVerification` object with validation scores

### run_validation_suite(test_queries: list) -> dict
Executes a comprehensive validation suite against multiple query types.

**Parameters**:
- `test_queries` (list): List of test queries to validate

**Returns**: Dictionary with aggregated validation results

## Validation Criteria

### Content Relevance
- At least 80% of returned chunks should be from `/docs/` sections
- Similarity scores should be above 0.3 threshold
- Content should match query intent

### Metadata Integrity
- All chunks must have non-empty URL, heading, and text
- URLs must map to valid book content
- Section and chunk_index fields must be present

### Query Type Handling
- Normal queries: Should return relevant book sections
- Short queries: Should return precise content matches
- Long queries: Should return comprehensive content
- Edge case queries: Should handle gracefully with appropriate messages