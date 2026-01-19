# Docusaurus Ingestion Pipeline

## Overview
This backend application ingests Docusaurus book URLs, extracts clean content, generates Cohere embeddings, and stores vectors in Qdrant Cloud for semantic search and retrieval.

## Features
- Crawls all pages from a Docusaurus book
- Extracts clean text content excluding navigation and boilerplate
- Chunks content with semantic overlap
- Generates embeddings using Cohere
- Stores vectors in Qdrant Cloud with metadata
- Uses deterministic IDs to prevent duplication
- Verifies successful indexing with sample queries

## Requirements
- Python 3.11+
- UV package manager
- Cohere API key
- Qdrant Cloud account and API key

## Installation
1. Install dependencies using UV:
   ```bash
   uv pip install -r requirements.txt
   ```

2. Copy the environment example:
   ```bash
   cp .env.example .env
   ```

3. Update `.env` with your API keys

## Usage
```bash
python main.py --url "https://your-docusaurus-book.com" --verify
```

### Options
- `--url`: Base URL of the Docusaurus book (required)
- `--chunk-size`: Size of text chunks (default: 512)
- `--overlap`: Overlap between chunks (default: 128)
- `--verify`: Run verification after ingestion (optional)

## Environment Variables
- `COHERE_API_KEY`: Your Cohere API key for embeddings
- `QDRANT_URL`: Qdrant Cloud cluster URL
- `QDRANT_API_KEY`: Qdrant Cloud API key

## Architecture
The pipeline follows this processing order:
1. URLs → collect all pages from the Docusaurus book
2. Chunks → split content into fixed-size overlapping segments
3. Embeddings → generate vector representations using Cohere
4. Vector storage → store in Qdrant Cloud with metadata

## Verification
After ingestion, the system verifies successful indexing by performing sample vector search queries to ensure content is properly retrievable.