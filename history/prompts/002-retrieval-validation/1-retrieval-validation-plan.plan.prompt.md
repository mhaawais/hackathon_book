---
id: 1
title: Retrieval Validation Plan
stage: plan
date: 2026-01-13
surface: agent
model: claude-sonnet-4-5-20250929
feature: 002-retrieval-validation
branch: 001-docusaurus-ingestion
user: stech
command: -- Spec-2: Retrieval Pipeline Validation (Strong Plan)

Initial Setup & Governance

Create/update feature artifacts in specs/002-retrieval-validation/ and always write execution outputs to history/ (timestamped retrieval reports)

Core Retrieval Pipeline (Read-Only)

Implement a strict read-only retrieval workflow against Qdrant collection docusaurus_content (no ingestion, no embedding storage updates)

Retrieval flow must follow: user query → Cohere embed(query) → Qdrant vector search (top_k) → return ranked chunks

Result Quality & Metadata Integrity

Ensure each retrieved result includes: score, url, heading/section (if available), chunk_index, and chunk_text preview

Validate metadata integrity (URL matches content source and chunk text is not empty/garbage)

Filtering & Book-Only Validation

Add payload/URL-based filtering to validate correct scope:

Prefer book content: /docs/

Exclude non-book pages: /blog/, /404, tags, archive

Filtering must be applied at retrieval time (do not re-index)

Testing & Reporting

Run a test suite covering:

Normal queries (book topics)

Short queries (keywords)

Long queries (multi-sentence)

Empty/nonsense queries (edge cases)

Save test outcomes and top results into history/ as a structured summary to prove retrieval correctness and readiness for Spec-3/4 integration
labels: [spec-2,retrieval,validation,plan]
links:
  spec: ./spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/002-retrieval-validation/plan.md
  - specs/002-retrieval-validation/research.md
  - specs/002-retrieval-validation/data-model.md
  - specs/002-retrieval-validation/quickstart.md
  - specs/002-retrieval-validation/contracts/validation-interface.md
tests:
  - null
---

## Prompt

-- Spec-2: Retrieval Pipeline Validation (Strong Plan)

Initial Setup & Governance

Create/update feature artifacts in specs/002-retrieval-validation/ and always write execution outputs to history/ (timestamped retrieval reports)

Core Retrieval Pipeline (Read-Only)

Implement a strict read-only retrieval workflow against Qdrant collection docusaurus_content (no ingestion, no embedding storage updates)

Retrieval flow must follow: user query → Cohere embed(query) → Qdrant vector search (top_k) → return ranked chunks

Result Quality & Metadata Integrity

Ensure each retrieved result includes: score, url, heading/section (if available), chunk_index, and chunk_text preview

Validate metadata integrity (URL matches content source and chunk text is not empty/garbage)

Filtering & Book-Only Validation

Add payload/URL-based filtering to validate correct scope:

Prefer book content: /docs/

Exclude non-book pages: /blog/, /404, tags, archive

Filtering must be applied at retrieval time (do not re-index)

Testing & Reporting

Run a test suite covering:

Normal queries (book topics)

Short queries (keywords)

Long queries (multi-sentence)

Empty/nonsense queries (edge cases)

Save test outcomes and top results into history/ as a structured summary to prove retrieval correctness and readiness for Spec-3/4 integration

## Response snapshot

# Implementation Plan: Retrieval Pipeline Validation

**Branch**: `002-retrieval-validation` | **Date**: 2026-01-13 | **Spec**: [link to spec.md](./spec.md)
**Input**: Feature specification from `/specs/002-retrieval-validation/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Backend validation pipeline to test retrieval accuracy from Qdrant collection `docusaurus_content`. The solution follows a read-only approach that validates query → embedding → vector search → result quality workflow against existing indexed book content. The implementation includes query validation, metadata verification, and test reporting capabilities.

## Technical Context

**Language/Version**: Python 3.11
**Primary Dependencies**: requests, cohere, qdrant-client, python-dotenv, pytest
**Storage**: Qdrant Cloud (read-only access to `docusaurus_content` collection)
**Testing**: pytest with validation test suite
**Target Platform**: Linux server (backend validation)
**Project Type**: Single backend validation script
**Performance Goals**: Complete validation suite within 10 minutes (SC-006)
**Constraints**: Read-only access to Qdrant, reuse existing Cohere embeddings schema, environment variable configuration
**Scale/Scope**: Handle up to 50 queries in validation suite, validate metadata integrity across all retrieved chunks

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- ✅ Spec-first execution: Following the spec from `/specs/002-retrieval-validation/spec.md`
- ✅ Source-grounded accuracy: Using established libraries for vector search and validation
- ✅ Clear separation of concerns: Backend-only validation implementation with clear data flow (query → embed → search → validate)
- ✅ Reader-first technical clarity: Implementation will include clear documentation and validation reports
- ✅ Deterministic, reproducible outputs: Using environment-based configuration and consistent validation methodology
- ✅ Secure key handling: Using environment variables for API keys (cohere, qdrant)

## Project Structure

### Documentation (this feature)
```text
specs/002-retrieval-validation/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)
```text
backend/
├── retrieval_validator.py    # Single file containing all validation logic
├── requirements.txt          # Python dependencies managed by uv
├── .env.example             # Example environment variables file
├── .env                     # Local environment variables (gitignored)
├── docs/
│   └── README.md            # Documentation for the validation process
└── tests/
    ├── test_retrieval.py    # Tests for retrieval validation logic
    └── test_metadata.py     # Tests for metadata validation
```

**Structure Decision**: Backend-only implementation as a single Python validation script following the user's requirement to create a validation pipeline that reuses existing Spec-1 artifacts.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| N/A | N/A | N/A |

# Research: Retrieval Pipeline Validation

## Decision: Retrieval Pipeline Architecture
**Rationale**: The retrieval pipeline needs to validate query → embedding → search → result quality workflow against existing Qdrant collection without modifying stored data. Using Cohere for query embeddings to match the existing content embeddings ensures compatibility.

**Alternatives considered**:
- Using OpenAI embeddings for queries: Would require additional API costs and might not match existing 768-dim Cohere embeddings
- Using Sentence Transformers: Would add complexity but could be more cost-effective for query embeddings
- Using existing embeddings only: Would limit validation to exact matches

## Decision: Filtering Strategy
**Rationale**: Apply URL-based filtering at retrieval time to ensure book-only content (/docs/) is prioritized while excluding non-book pages (/blog/, /404, tags, archive). This maintains data integrity without requiring re-indexing.

**Alternatives considered**:
- Pre-filtering at index time: Would require re-indexing which violates read-only constraint
- No filtering: Would return irrelevant content like blog posts and 404 pages
- Post-filtering with re-query: Would be less efficient than filtering during search

## Decision: Validation Metrics
**Rationale**: Implement comprehensive validation metrics including relevance scoring, metadata accuracy, and query type coverage to ensure retrieval quality across different scenarios.

**Alternatives considered**:
- Simple accuracy metrics only: Would miss important metadata validation requirements
- Manual validation: Would not be reproducible or scalable
- No validation reporting: Would not meet observability requirements

## Decision: Test Query Types
**Rationale**: Implement tests for normal queries (book topics), short queries (keywords), long queries (multi-sentence), and edge cases (empty/nonsense) to ensure robust retrieval across all usage scenarios.

**Alternatives considered**:
- Only normal queries: Would not validate edge case handling
- Random queries: Would not provide consistent validation results
- No query categorization: Would miss specific validation requirements for different query types

# Data Model: Retrieval Pipeline Validation

## Core Entities

### RetrievalValidationResult
Represents the outcome of validating a query against the retrieval pipeline

**Fields**:
- `query` (str): The original query text
- `retrieved_chunks` (list): List of retrieved content chunks
- `validation_score` (float): Overall validation score (0-1)
- `metadata_accuracy` (float): Score for metadata accuracy (0-1)
- `content_relevance` (float): Score for content relevance (0-1)
- `query_type` (str): Type of query (normal, short, long, edge_case)
- `timestamp` (datetime): When validation was performed
- `execution_time` (float): Time taken for validation in seconds

**Relationships**:
- Contains multiple `RetrievedChunk` entities

### RetrievedChunk
Represents a single content chunk returned from Qdrant

**Fields**:
- `score` (float): Similarity score from vector search
- `url` (str): Original URL of the content source
- `heading` (str): Heading/section title from the content
- `chunk_index` (int): Index of the chunk in the original document
- `chunk_text` (str): Preview text of the content chunk
- `section` (str): Section name from the content
- `validation_passed` (bool): Whether this chunk passed validation

### QueryValidationTest
Represents a specific test case for validating retrieval quality

**Fields**:
- `test_id` (str): Unique identifier for the test
- `query_text` (str): The query to test
- `expected_results` (list): Expected URLs or content snippets
- `test_type` (str): Type of test (accuracy, metadata, query_type)
- `validation_rules` (dict): Specific rules for this test

### MetadataVerification
Represents the validation of metadata fields for retrieved content

**Fields**:
- `url_valid` (bool): Whether URL matches expected source
- `heading_present` (bool): Whether heading is present and meaningful
- `section_correct` (bool): Whether section matches content
- `chunk_index_valid` (bool): Whether chunk index is sequential and correct
- `text_quality` (bool): Whether chunk text is not empty or garbage
- `overall_score` (float): Combined metadata validation score

## Validation Rules

### Content Relevance Validation
- Chunk text must contain terms related to the query
- Similarity score must be above threshold (0.3)
- Content must match expected book sections

### Metadata Integrity Validation
- URL must start with expected book base URL
- Heading and section must not be empty
- Chunk text must not be empty or contain only whitespace
- URL must map to actual content in the book

### Filtering Validation
- Results with URLs containing `/docs/` should be prioritized
- Results with URLs containing `/blog/`, `/404`, `/tags`, `/archive` should be filtered out or de-prioritized
- At least 80% of results should be from book content sections

## State Transitions

### Validation Process Flow
1. `QUEUED` → Query submitted for validation
2. `PROCESSING` → Query embedded and search executed
3. `VALIDATING` → Results checked against validation rules
4. `COMPLETED` → Final validation score calculated
5. `REPORTED` → Results saved to history with timestamp

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

# Quickstart: Retrieval Pipeline Validation

## Setup

1. **Install dependencies**:
   ```bash
   cd backend
   uv pip install -r requirements.txt
   ```

2. **Configure environment variables**:
   Copy `.env.example` to `.env` and set:
   - `QDRANT_URL`: Your Qdrant Cloud cluster URL
   - `QDRANT_API_KEY`: Your Qdrant API key
   - `COHERE_API_KEY`: Your Cohere API key

3. **Verify Qdrant connection**:
   Ensure the `docusaurus_content` collection exists with indexed book content from Spec-1.

## Running Validation

### Single Query Validation
```bash
cd backend
uv run python retrieval_validator.py --query "What is the main concept of this book?"
```

### Full Validation Suite
```bash
cd backend
uv run python retrieval_validator.py --validate-all
```

### Specific Test Types
```bash
# Test normal queries
uv run python retrieval_validator.py --test-type normal

# Test short queries
uv run python retrieval_validator.py --test-type short

# Test long queries
uv run python retrieval_validator.py --test-type long

# Test edge cases
uv run python retrieval_validator.py --test-type edge
```

## Expected Output

The validation will produce:
- Console output with validation scores
- Detailed report in `history/retrieval_validation_YYYYMMDD_HHMMSS.log`
- Individual chunk validation results with metadata verification

## Sample Output
```
Validation Results:
- Query: "What is the main concept of this book?"
- Retrieved: 5 chunks
- Content Relevance: 92%
- Metadata Accuracy: 98%
- Book Content Ratio: 100%
- Execution Time: 2.34 seconds
```

## Troubleshooting

- **No results returned**: Verify Qdrant connection and collection name
- **Low relevance scores**: Check that content was properly indexed in Spec-1
- **Missing metadata**: Validate that Spec-1 ingestion preserved metadata fields
- **API errors**: Verify API keys in `.env` file

## Outcome

- ✅ Impact: Created comprehensive implementation plan for retrieval validation pipeline that follows read-only approach and validates query retrieval accuracy
- 🧪 Tests: null
- 📁 Files: specs/002-retrieval-validation/plan.md, specs/002-retrieval-validation/research.md, specs/002-retrieval-validation/data-model.md, specs/002-retrieval-validation/quickstart.md, specs/002-retrieval-validation/contracts/validation-interface.md
- 🔁 Next prompts: Ready to generate tasks with /sp.tasks command
- 🧠 Reflection: The plan provides a solid foundation for implementing the retrieval validation pipeline with proper architecture, data models, and validation criteria.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Generate tasks with /sp.tasks command to implement the validation pipeline