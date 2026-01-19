# Quickstart: Docusaurus URL Ingestion, Embedding & Vector Storage

## Overview
Quickstart guide to set up and run the Docusaurus ingestion pipeline.

## Prerequisites
- Python 3.11+
- UV package manager
- Cohere API key
- Qdrant Cloud account and API key
- Access to target Docusaurus book URLs

## Setup

### 1. Clone the repository
```bash
git clone <repository-url>
cd <repository-root>
```

### 2. Create backend directory
```bash
mkdir backend
cd backend
```

### 3. Install dependencies using UV
```bash
uv init
uv pip install requests beautifulsoup4 cohere qdrant-client python-dotenv
```

### 4. Create environment file
Create a `.env` file with the following variables:
```env
COHERE_API_KEY=your_cohere_api_key_here
QDRANT_URL=your_qdrant_cloud_url_here
QDRANT_API_KEY=your_qdrant_api_key_here
```

### 5. Create main.py
Create a `main.py` file with the ingestion pipeline implementation following the specification.

## Running the Ingestion Pipeline

### 1. Basic Usage
```bash
cd backend
python main.py --url "https://your-docusaurus-book.com"
```

### 2. With custom parameters
```bash
python main.py --url "https://your-docusaurus-book.com" --chunk-size 512 --overlap 128
```

### 3. Environment Variables
Ensure the following environment variables are set:
- `COHERE_API_KEY`: Your Cohere API key for embeddings
- `QDRANT_URL`: Qdrant Cloud cluster URL
- `QDRANT_API_KEY`: Qdrant Cloud API key

## Expected Output
- All pages from the Docusaurus book are crawled and clean content extracted
- Content is chunked with semantic overlap
- Embeddings are generated using Cohere
- Vectors are stored in Qdrant Cloud with metadata
- Sample search queries verify successful indexing

## Troubleshooting
- If pages fail to load, verify the base URL is accessible
- If embeddings fail, check the Cohere API key and rate limits
- If storage fails, verify Qdrant credentials and collection schema
- Enable debug logging with `--verbose` flag for detailed output