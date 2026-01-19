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