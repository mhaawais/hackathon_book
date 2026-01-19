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
- `text_quality` (bool): Whether chunk text is not empty/garbage
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