# How to Run the Retrieval Validation Suite

## Prerequisites
- Ensure backend/.env contains:
  - `COHERE_API_KEY`
  - `QDRANT_URL`
  - `QDRANT_API_KEY`

## Commands

### 1. Run the complete validation suite:
```bash
cd backend
uv run python run_validation_test.py
```

### 2. Run a single query validation:
```bash
cd backend
uv run python -c "
from retrieval_validator import RetrievalValidator
validator = RetrievalValidator()
result = validator.validate_query_retrieval('What is this book about?', top_k=3)
print(f'Query: {result.query}')
print(f'Retrieved: {len(result.retrieved_chunks)} chunks')
print(f'Score: {result.validation_score:.3f}')
"
```

### 3. Run the validation from command line:
```bash
cd backend
uv run python retrieval_validator.py --query "What is this book about?" --top-k 3
```

## Features Verified
- ✅ Environment variable loading with python-dotenv
- ✅ Cohere query embedding generation
- ✅ Qdrant vector search in `docusaurus_content` collection
- ✅ Filtering for `/docs/` content over other page types
- ✅ Metadata preservation (URL, heading, section, chunk_index)
- ✅ Multiple query type handling (normal, short, long, edge cases)
- ✅ Validation report generation in `backend/history/`
- ✅ Proper error handling for empty queries

## Output Files
- Validation reports saved as `backend/history/retrieval_validation_YYYYMMDD_HHMMSS.log`
- Each report contains query results, scores, and performance metrics