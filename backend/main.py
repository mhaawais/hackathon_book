"""
Docusaurus URL Ingestion, Embedding & Vector Storage

Main script to ingest Docusaurus book URLs, extract clean content,
generate Cohere embeddings, and store vectors in Qdrant.
"""


import os
import hashlib
import requests
from bs4 import BeautifulSoup
import cohere
from qdrant_client import QdrantClient
from qdrant_client.http import models
from urllib.parse import urljoin, urlparse
import time
import logging
from typing import List, Dict, Tuple
import argparse
import dotenv

# Load environment variables
dotenv.load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DocusaurusIngester:
    def __init__(self):
        # Initialize clients
        self.cohere_client = cohere.Client(os.getenv("COHERE_API_KEY"))
        self.qdrant_client = QdrantClient(
            url=os.getenv("QDRANT_URL"),
            api_key=os.getenv("QDRANT_API_KEY"),
            timeout=60,  # Increase timeout to 60 seconds
            https=True   # Ensure HTTPS for cloud connection
        )
        self.collection_name = "docusaurus_content"

        # Create collection if it doesn't exist
        self._ensure_collection_exists()

    def _ensure_collection_exists(self):
        """Ensure the Qdrant collection exists with proper schema."""
        try:
            collections = self.qdrant_client.get_collections()

            collection_exists = any(col.name == self.collection_name for col in collections.collections)

            if collection_exists:
                # Check if the existing collection has the right dimension
                collection_info = self.qdrant_client.get_collection(collection_name=self.collection_name)

                # Handle both single vector and multiple vectors configurations
                if isinstance(collection_info.config.params.vectors, dict):
                    # Multiple named vectors
                    vector_config = list(collection_info.config.params.vectors.values())[0]
                    current_dim = vector_config.size
                else:
                    # Single vector configuration
                    current_dim = collection_info.config.params.vectors.size

                if current_dim != 768:
                    # Delete the collection if it has wrong dimension
                    logger.info(f"Collection has wrong dimension ({current_dim}), recreating with 768 dimensions")
                    self.qdrant_client.delete_collection(collection_name=self.collection_name)
                    collection_exists = False

            if not collection_exists:
                # The Cohere embed-multilingual-v2.0 model produces 768-dimensional vectors
                self.qdrant_client.create_collection(
                    collection_name=self.collection_name,
                    vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE),  # Updated dimension
                )

                # Create payload index for metadata
                self.qdrant_client.create_payload_index(
                    collection_name=self.collection_name,
                    field_name="url",
                    field_schema=models.PayloadSchemaType.KEYWORD
                )
        except Exception as e:
            logger.error(f"Error setting up collection: {e}")
            raise

    def get_all_page_urls(self, base_url: str) -> List[str]:
        """Fetch and parse sitemap.xml to get all page URLs."""
        urls = set()

        # Construct sitemap URL
        sitemap_url = urljoin(base_url, 'sitemap.xml')

        try:
            logger.info(f"Fetching sitemap from: {sitemap_url}")
            response = requests.get(sitemap_url, timeout=30)
            response.raise_for_status()

            # Parse the sitemap XML
            soup = BeautifulSoup(response.content, 'xml')  # Use xml parser for sitemaps

            # Find all <loc> tags which contain URLs
            loc_tags = soup.find_all('loc')

            for loc in loc_tags:
                url = loc.get_text().strip()
                if url and url.startswith(base_url):
                    # Filter out non-HTML URLs (like images, PDFs, etc.)
                    if url.endswith(('.html', '/')) or not any(url.endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif', '.pdf', '.zip', '.css', '.js']):
                        urls.add(url)

            logger.info(f"Found {len(urls)} URLs in sitemap")
            return list(urls)

        except requests.RequestException as e:
            logger.error(f"Failed to fetch sitemap from {sitemap_url}: {e}")
            raise
        except Exception as e:
            logger.error(f"Failed to parse sitemap from {sitemap_url}: {e}")
            raise

    def extract_clean_content(self, url: str) -> Tuple[str, str, str]:
        """Extract clean text content from a Docusaurus page."""
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            # Remove navigation, headers, footers, and other non-content elements
            for element in soup(['nav', 'header', 'footer', 'aside', 'script', 'style', '.menu', '.navbar', '.toc', '.pagination', '.footer', '.sidebar']):
                element.decompose()

            # Remove elements with specific classes that are typically not content
            non_content_classes = ['button', 'admonition', 'theme-edit-this-page', 'theme-last-updated', 'theme-tags']
            for class_name in non_content_classes:
                for element in soup.find_all(class_=class_name):
                    element.decompose()

            # Look for main content areas in Docusaurus sites
            content_selectors = [
                '[role="main"]',
                '.main-wrapper',
                '.theme-doc-markdown',
                '.theme-content',
                'article',
                '.docItemContainer',
                '.markdown',
                '.container.padding-vert--lg',
                'main',
                '.post',
                '.docs-doc-page',
                '.doc-page',
                '.content.main',
                '.main-content'
            ]

            content_element = None
            for selector in content_selectors:
                content_element = soup.select_one(selector)
                if content_element:
                    break

            # If no content found with selectors, try finding by class patterns
            if not content_element:
                content_element = soup.find('div', class_=lambda x: x and x and ('doc' in x.lower() or 'content' in x.lower() or 'main' in x.lower()))

            if content_element:
                # Get heading if available (try multiple levels)
                heading = ""
                for tag in ['h1', 'h2']:
                    h_tag = content_element.find(tag)
                    if h_tag:
                        heading = h_tag.get_text().strip()
                        break

                # Extract clean text
                content = content_element.get_text(separator=' ', strip=True)

                # Clean up excessive whitespace
                import re
                content = re.sub(r'\s+', ' ', content).strip()

                # Extract section if available
                section = self._extract_section_from_url(url)

                return content, section, heading
            else:
                # Fallback: get all text from body, excluding common non-content elements
                for element in soup(['nav', 'header', 'footer', 'aside', 'script', 'style']):
                    element.decompose()

                body = soup.find('body')
                if body:
                    content = body.get_text(separator=' ', strip=True)
                    # Clean up excessive whitespace
                    content = re.sub(r'\s+', ' ', content).strip()
                else:
                    content = soup.get_text(separator=' ', strip=True)
                    content = re.sub(r'\s+', ' ', content).strip()

                section = self._extract_section_from_url(url)
                return content, section, ""

        except requests.RequestException as e:
            logger.error(f"Failed to fetch content from {url}: {e}")
            return "", "", ""
        except Exception as e:
            logger.error(f"Failed to extract content from {url}: {e}")
            return "", "", ""

    def _extract_section_from_url(self, url: str) -> str:
        """Extract section/chapter name from URL."""
        parsed = urlparse(url)
        path_parts = [part for part in parsed.path.split('/') if part]

        if len(path_parts) >= 2:
            return path_parts[-2]
        elif len(path_parts) >= 1:
            return path_parts[-1]
        else:
            return "home"

    def chunk_text(self, text: str, chunk_size: int = 512, overlap: int = 128) -> List[Dict]:
        """Chunk text into fixed-size overlapping segments."""
        if not text:
            return []

        chunks = []
        start = 0

        while start < len(text):
            end = start + chunk_size

            # If we're near the end, include the remainder
            if end > len(text):
                end = len(text)

            chunk_text = text[start:end]

            # Calculate the overlap for the next chunk
            next_start = end - overlap if end < len(text) else end

            chunk_data = {
                'text': chunk_text,
                'start_idx': start,
                'end_idx': end
            }

            chunks.append(chunk_data)
            start = next_start

            # Prevent infinite loop
            if start >= end:
                break

        return chunks

    def generate_deterministic_id(self, url: str, content_chunk: str) -> str:
        """Generate a deterministic ID for a content chunk."""
        import uuid
        # Create a deterministic UUID from the URL and content
        combined_str = url + content_chunk
        # Use SHA256 hash to create a deterministic value, then convert to UUID
        hash_bytes = hashlib.sha256(combined_str.encode()).digest()
        # Take first 16 bytes to create UUID
        return str(uuid.UUID(bytes=hash_bytes[:16]))

    def generate_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for a list of texts using Cohere."""
        try:
            response = self.cohere_client.embed(
                texts=texts,
                model='embed-multilingual-v2.0'  # Using Cohere's multilingual model
            )

            # The response should be an EmbedResponse object with an embeddings property
            # The embeddings property contains the actual list of embeddings
            if hasattr(response, 'embeddings') and response.embeddings:
                return response.embeddings
            else:
                logger.warning(f"Cohere response had no embeddings: {response}")
                return []
        except Exception as e:
            logger.error(f"Failed to generate embeddings: {e}")
            return []

    def store_vectors(self, chunks_data: List[Dict]):
        """Store content chunks and embeddings in Qdrant."""
        try:
            points = []
            for chunk_data in chunks_data:
                point = models.PointStruct(
                    id=chunk_data['chunk_id'],
                    vector=chunk_data['embedding'],
                    payload={
                        'url': chunk_data['url'],
                        'section': chunk_data['section'],
                        'heading': chunk_data['heading'],
                        'content': chunk_data['content'],
                        'chunk_index': chunk_data.get('chunk_index', 0)
                    }
                )
                points.append(point)

            self.qdrant_client.upsert(
                collection_name=self.collection_name,
                points=points
            )
            logger.info(f"Successfully stored {len(points)} vectors in Qdrant")

        except Exception as e:
            logger.error(f"Failed to store vectors in Qdrant: {e}")
            raise

    def process_book(self, base_url: str, chunk_size: int = 512, overlap: int = 128):
        """Main processing flow: URLs → chunks → embeddings → vector storage."""
        logger.info(f"Starting ingestion for: {base_url}")

        # Step 1: Collect and validate URLs
        logger.info("Step 1: Collecting page URLs...")
        urls = self.get_all_page_urls(base_url)
        logger.info(f"Collected {len(urls)} URLs")

        all_chunks_data = []
        processed_urls = 0

        # Step 2: Process each URL
        for i, url in enumerate(urls):
            logger.info(f"Processing URL {i+1}/{len(urls)}: {url}")

            # Extract clean content
            content, section, heading = self.extract_clean_content(url)

            if not content.strip():
                logger.warning(f"No content extracted from {url}")
                continue

            # Step 3: Chunk extracted text
            chunks = self.chunk_text(content, chunk_size, overlap)
            logger.debug(f"Generated {len(chunks)} chunks for {url}")

            # Process each chunk
            for j, chunk in enumerate(chunks):
                # Generate deterministic ID
                chunk_id = self.generate_deterministic_id(url, chunk['text'])

                chunk_data = {
                    'chunk_id': chunk_id,
                    'url': url,
                    'section': section,
                    'heading': heading,
                    'content': chunk['text'],
                    'chunk_index': j
                }

                all_chunks_data.append(chunk_data)

            processed_urls += 1

        logger.info(f"Successfully processed content from {processed_urls}/{len(urls)} URLs")
        logger.info(f"Generated {len(all_chunks_data)} content chunks")

        if not all_chunks_data:
            logger.warning("No content chunks generated, stopping ingestion")
            return

        # Step 4: Generate embeddings in batches to avoid API limits
        logger.info("Step 4: Generating embeddings...")
        batch_size = 10  # Cohere batch size limit
        all_embeddings = []

        for i in range(0, len(all_chunks_data), batch_size):
            batch = all_chunks_data[i:i+batch_size]
            batch_texts = [item['content'] for item in batch]

            embeddings = self.generate_embeddings(batch_texts)

            if not embeddings:
                logger.warning(f"Failed to generate embeddings for batch {i//batch_size + 1}, skipping...")
                continue

            all_embeddings.extend(embeddings)

            # Be respectful to API rate limits
            time.sleep(0.1)

        # Attach embeddings to chunk data
        valid_chunks_data = []
        for i, embedding in enumerate(all_embeddings):
            if i < len(all_chunks_data):  # Safety check
                all_chunks_data[i]['embedding'] = embedding
                valid_chunks_data.append(all_chunks_data[i])

        logger.info(f"Generated embeddings for {len(valid_chunks_data)} chunks")

        # Step 5: Store in vector database
        logger.info("Step 5: Storing vectors in Qdrant...")
        self.store_vectors(valid_chunks_data)

        logger.info("Ingestion completed successfully!")

        return len(valid_chunks_data)  # Return number of chunks stored

    def verify_indexing(self, sample_query: str = "What is this book about?"):
        """Verify successful indexing with sample vector search queries."""
        try:
            # Generate embedding for the query
            query_embedding = self.generate_embeddings([sample_query])

            if not query_embedding:
                logger.error("Could not generate query embedding for verification")
                return False

            # Verify that vectors were stored by checking the collection info
            collection_info = self.qdrant_client.get_collection(collection_name=self.collection_name)
            points_count = collection_info.points_count

            logger.info(f"Collection '{self.collection_name}' has {points_count} vectors stored")

            if points_count > 0:
                logger.info("Verification successful! Content is properly indexed in Qdrant.")
                return True
            else:
                logger.error("No vectors found in collection")
                return False

        except Exception as e:
            logger.error(f"Verification failed: {e}")
            return False


def save_execution_summary(start_time: float, urls_processed: int, chunks_created: int, vectors_stored: int, success: bool):
    """Save execution summary to history directory."""
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # Create history directory if it doesn't exist
    os.makedirs("history", exist_ok=True)

    summary_path = f"history/ingestion_{timestamp}.log"

    duration = time.time() - start_time
    summary = f"""Ingestion Execution Summary
========================

Timestamp: {datetime.datetime.now().isoformat()}
Duration: {duration:.2f} seconds
URLs Processed: {urls_processed}
Chunks Created: {chunks_created}
Vectors Stored: {vectors_stored}
Success: {success}

Environment:
- Base URL: {os.getenv('DEPLOYED_VERCEL_URL', 'Not set')}
- Qdrant Collection: docusaurus_content
- Chunk Size: 512
- Overlap: 128
"""

    with open(summary_path, 'w') as f:
        f.write(summary)

    logger.info(f"Execution summary saved to {summary_path}")


def main():
    parser = argparse.ArgumentParser(description="Docusaurus URL Ingestion, Embedding & Vector Storage")
    parser.add_argument("--url", required=False, help="Base URL of the Docusaurus book (optional, defaults to DEPLOYED_VERCEL_URL env var)")
    parser.add_argument("--chunk-size", type=int, default=512, help="Size of text chunks")
    parser.add_argument("--overlap", type=int, default=128, help="Overlap between chunks")
    parser.add_argument("--verify", action="store_true", help="Run verification after ingestion")

    args = parser.parse_args()

    # Use DEPLOYED_VERCEL_URL from environment if no URL provided
    base_url = args.url or os.getenv("DEPLOYED_VERCEL_URL")
    if not base_url:
        logger.error("No base URL provided. Set --url argument or DEPLOYED_VERCEL_URL environment variable.")
        return 1

    # Check required environment variables
    required_env_vars = ["COHERE_API_KEY", "QDRANT_URL", "QDRANT_API_KEY"]
    missing_vars = [var for var in required_env_vars if not os.getenv(var)]

    if missing_vars:
        logger.error(f"Missing required environment variables: {missing_vars}")
        logger.error("Please set them in a .env file or environment")
        return 1

    # Initialize ingester
    ingester = DocusaurusIngester()

    # Start timer
    start_time = time.time()

    # Process the book
    try:
        # Get URLs first to track how many we have
        urls = ingester.get_all_page_urls(base_url)

        # Process the book and get number of chunks created
        chunks_created = ingester.process_book(base_url, args.chunk_size, args.overlap)

        # Count processed items
        collection_info = ingester.qdrant_client.get_collection(collection_name=ingester.collection_name)
        vectors_count = collection_info.points_count

        # Save execution summary
        save_execution_summary(start_time, len(urls), chunks_created or 0, vectors_count, True)

    except Exception as e:
        logger.error(f"Ingestion failed: {e}")
        # Save execution summary with failure status
        save_execution_summary(start_time, 0, 0, 0, False)
        return 1

    # Optionally verify indexing
    if args.verify:
        logger.info("Verifying successful indexing...")
        success = ingester.verify_indexing()
        if success:
            logger.info("Verification successful! Content is properly indexed.")
        else:
            logger.warning("Verification failed. Content may not be properly indexed.")

    return 0


if __name__ == "__main__":
    exit(main())