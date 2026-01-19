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