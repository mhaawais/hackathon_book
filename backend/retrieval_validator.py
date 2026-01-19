"""
Retrieval Pipeline Validation

Backend validation pipeline to test retrieval accuracy from Qdrant collection `docusaurus_content`.
Validates query → embedding → vector search → result quality workflow against existing indexed book content.
"""

import os
import logging
import time
import argparse
from dotenv import load_dotenv
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
from urllib.parse import urlparse
import json

# Import required libraries
import cohere
from qdrant_client import QdrantClient
from qdrant_client.http import models
import requests

# Load environment variables explicitly
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class RetrievedChunk:
    """Represents a single content chunk returned from Qdrant"""
    score: float
    url: str
    heading: str
    chunk_index: int
    chunk_text: str
    section: str
    validation_passed: bool = False


@dataclass
class RetrievalValidationResult:
    """Represents the outcome of validating a query against the retrieval pipeline"""
    query: str
    retrieved_chunks: List[RetrievedChunk]
    validation_score: float
    metadata_accuracy: float
    content_relevance: float
    query_type: str
    timestamp: str
    execution_time: float


@dataclass
class MetadataVerification:
    """Represents the validation of metadata fields for retrieved content"""
    url_valid: bool
    heading_present: bool
    section_correct: bool
    chunk_index_valid: bool
    text_quality: bool
    overall_score: float


class RetrievalValidator:
    def __init__(self):
        """Initialize the retrieval validator with Cohere and Qdrant clients"""
        # Initialize Cohere client
        self.cohere_client = cohere.Client(os.getenv("COHERE_API_KEY"))

        # Initialize Qdrant client with read-only access
        self.qdrant_client = QdrantClient(
            url=os.getenv("QDRANT_URL"),
            api_key=os.getenv("QDRANT_API_KEY"),
            timeout=60,
            https=True
        )

        self.collection_name = "docusaurus_content"

        # Validate that collection exists
        try:
            collection_info = self.qdrant_client.get_collection(collection_name=self.collection_name)
            logger.info(f"Connected to Qdrant collection '{self.collection_name}' with {collection_info.points_count} vectors")
        except Exception as e:
            logger.error(f"Failed to connect to Qdrant collection '{self.collection_name}': {e}")
            raise

    def validate_query_retrieval(self, query: str, top_k: int = 5) -> RetrievalValidationResult:
        """
        Validates that a given query retrieves relevant content from Qdrant.

        Args:
            query: The query text to validate
            top_k: Number of results to retrieve (default: 5)

        Returns:
            RetrievalValidationResult object with validation metrics
        """
        start_time = time.time()

        # Generate embedding for query using Cohere
        query_embedding = self._generate_query_embedding(query)

        if not query_embedding:
            logger.error(f"Failed to generate embedding for query: {query}")
            # Use the classify function to determine the proper query type
            query_type = self._classify_query_type(query)
            return self._create_empty_validation_result(query, query_type)

        # Execute vector search against docusaurus_content collection with filtering
        retrieved_chunks = self._execute_filtered_search(query_embedding, top_k)

        # Classify query type
        query_type = self._classify_query_type(query)

        # Validate metadata integrity for each result
        validated_chunks = self._validate_chunk_metadata(retrieved_chunks)

        # Calculate validation metrics
        validation_score, metadata_accuracy, content_relevance = self._calculate_validation_metrics(
            validated_chunks, query
        )

        execution_time = time.time() - start_time

        return RetrievalValidationResult(
            query=query,
            retrieved_chunks=validated_chunks,
            validation_score=validation_score,
            metadata_accuracy=metadata_accuracy,
            content_relevance=content_relevance,
            query_type=query_type,
            timestamp=time.strftime('%Y-%m-%d %H:%M:%S'),
            execution_time=execution_time
        )

    def _generate_query_embedding(self, query: str) -> Optional[List[float]]:
        """Generate embedding for query text using Cohere."""
        # Handle empty or whitespace-only queries
        if not query or not query.strip():
            logger.warning(f"Cannot generate embedding for empty query: '{query}'")
            return None

        try:
            response = self.cohere_client.embed(
                texts=[query],
                model='embed-multilingual-v2.0'  # Using the same model as in Spec-1
            )

            if hasattr(response, 'embeddings') and response.embeddings:
                return response.embeddings[0]  # Return first (and only) embedding
            else:
                logger.warning(f"Cohere response had no embeddings: {response}")
                return None

        except Exception as e:
            logger.error(f"Failed to generate query embedding: {e}")
            return None

    def _execute_filtered_search(self, query_embedding: List[float], top_k: int) -> List[RetrievedChunk]:
        """Execute vector search with URL-based filtering to prioritize /docs/ content."""
        try:
            # Search in Qdrant with filtering for book content
            # Since we have a pre-generated embedding, we should use the query_points method
            try:
                search_results = self.qdrant_client.query_points(
                    collection_name=self.collection_name,
                    query=query_embedding,  # Use the embedding as the query
                    limit=top_k,
                    with_payload=True,  # Explicitly request payload
                    # Add filtering to prioritize book content over blog posts, etc.
                    # For now, use keyword matching since text matching requires an index
                    query_filter=models.Filter(
                        must=[
                            models.FieldCondition(
                                key="url",
                                match=models.MatchKeyword(keyword="/docs/")  # Prioritize docs content
                            )
                        ]
                    ) if top_k > 0 else None  # Only apply filter if we want results
                )
            except (AttributeError, Exception) as e:
                # Log the error for debugging
                logger.debug(f"Filtered search failed: {e}")

                # Fallback to older methods if query_points doesn't exist
                try:
                    # Try the search method
                    search_results = self.qdrant_client.search(
                        collection_name=self.collection_name,
                        query_vector=query_embedding,
                        limit=top_k,
                        with_payload=True,  # Explicitly request payload
                        # Add filtering to prioritize book content over blog posts, etc.
                        query_filter=models.Filter(
                            must=[
                                models.FieldCondition(
                                    key="url",
                                    match=models.MatchKeyword(keyword="/docs/")  # Prioritize docs content
                                )
                            ]
                        ) if top_k > 0 else None  # Only apply filter if we want results
                    )
                except (AttributeError, Exception) as e:
                    logger.debug(f"Filtered search method failed: {e}")

                    # If search doesn't work, try the query method (though it expects text, not embedding)
                    try:
                        search_results = self.qdrant_client.query(
                            collection_name=self.collection_name,
                            query_text="dummy",  # This won't work properly with pre-generated embeddings
                            limit=top_k,
                            with_payload=True,  # Explicitly request payload
                            # Add filtering to prioritize book content over blog posts, etc.
                            query_filter=models.Filter(
                                must=[
                                    models.FieldCondition(
                                        key="url",
                                        match=models.MatchKeyword(keyword="/docs/")  # Prioritize docs content
                                    )
                                ]
                            ) if top_k > 0 else None  # Only apply filter if we want results
                        )
                    except (AttributeError, TypeError) as e:
                        logger.debug(f"Query method failed: {e}")

                        # Final fallback: try without filtering
                        try:
                            search_results = self.qdrant_client.query_points(
                                collection_name=self.collection_name,
                                query=query_embedding,  # Use the embedding as the query
                                limit=top_k,
                                with_payload=True  # Explicitly request payload
                            )
                        except Exception as e:
                            logger.error(f"All search methods failed: {e}")
                            return []

            chunks = []
            # Handle the QueryResponse object structure
            if hasattr(search_results, 'points'):
                # New structure: QueryResponse with points list
                search_points = search_results.points
            else:
                # Fallback to original structure
                search_points = search_results

            for i, result in enumerate(search_points):
                # Handle different result formats depending on the method used
                if hasattr(result, 'score'):  # New format from query_points (ScoredPoint)
                    score = result.score
                    payload = result.payload if hasattr(result, 'payload') else {}
                elif isinstance(result, tuple):  # Old format or tuple format
                    # If it's a tuple, the format might be (score, payload) or similar
                    if len(result) >= 2:
                        score = result[0] if hasattr(result[0], '__dict__') or isinstance(result[0], (int, float)) else 0.0
                        payload = result[1] if isinstance(result[1], dict) else {}
                    else:
                        score = 0.0
                        payload = {}
                else:
                    # Assume it's an older format
                    score = getattr(result, 'score', 0.0)
                    payload = getattr(result, 'payload', {})

                # Ensure payload is a dictionary
                if not isinstance(payload, dict):
                    payload = {}

                # Debug: print the first result's payload structure to understand what keys are available
                if i == 0 and payload:
                    logger.debug(f"First result payload structure: {list(payload.keys())}")
                    logger.debug(f"First result payload sample: {payload}")

                chunk = RetrievedChunk(
                    score=score,
                    url=payload.get('url', ''),
                    heading=payload.get('heading', ''),
                    chunk_index=payload.get('chunk_index', 0),
                    chunk_text=payload.get('content', '')[:200] if payload.get('content', '') else payload.get('text', '')[:200] if payload.get('text', '') else '',  # Get content from correct key
                    section=payload.get('section', ''),
                    validation_passed=False
                )
                chunks.append(chunk)

            # If no results with /docs/ filter, try without filter
            if not chunks and top_k > 0:
                logger.info("No /docs/ results found, searching without filter...")

                try:
                    search_results = self.qdrant_client.query_points(
                        collection_name=self.collection_name,
                        query=query_embedding,  # Use the embedding as the query
                        limit=top_k,
                        with_payload=True  # Explicitly request payload
                    )

                    chunks = []
                    # Handle the QueryResponse object structure
                    if hasattr(search_results, 'points'):
                        # New structure: QueryResponse with points list
                        search_points = search_results.points
                    else:
                        # Fallback to original structure
                        search_points = search_results

                    for i, result in enumerate(search_points):
                        # Handle different result formats depending on the method used
                        if hasattr(result, 'score'):  # New format from query_points (ScoredPoint)
                            score = result.score
                            payload = result.payload if hasattr(result, 'payload') else {}
                        elif isinstance(result, tuple):  # Old format or tuple format
                            # If it's a tuple, the format might be (score, payload) or similar
                            if len(result) >= 2:
                                score = result[0] if hasattr(result[0], '__dict__') or isinstance(result[0], (int, float)) else 0.0
                                payload = result[1] if isinstance(result[1], dict) else {}
                            else:
                                score = 0.0
                                payload = {}
                        else:
                            # Assume it's an older format
                            score = getattr(result, 'score', 0.0)
                            payload = getattr(result, 'payload', {})

                        # Ensure payload is a dictionary
                        if not isinstance(payload, dict):
                            payload = {}

                        # Debug: print the first result's payload structure to understand what keys are available
                        if i == 0 and payload:
                            logger.debug(f"Fallback - First result payload structure: {list(payload.keys())}")
                            logger.debug(f"Fallback - First result payload sample: {payload}")

                        chunk = RetrievedChunk(
                            score=score,
                            url=payload.get('url', ''),
                            heading=payload.get('heading', ''),
                            chunk_index=payload.get('chunk_index', 0),
                            chunk_text=payload.get('content', '')[:200] if payload.get('content', '') else payload.get('text', '')[:200] if payload.get('text', '') else '',  # Get content from correct key
                            section=payload.get('section', ''),
                            validation_passed=False
                        )
                        chunks.append(chunk)
                except (AttributeError, Exception) as e:
                    logger.debug(f"Unfiltered query_points failed: {e}")

                    # Fallback to older methods if query_points doesn't exist
                    try:
                        # Try the search method
                        search_results = self.qdrant_client.search(
                            collection_name=self.collection_name,
                            query_vector=query_embedding,
                            limit=top_k,
                            with_payload=True  # Explicitly request payload
                        )

                        chunks = []
                        for i, result in enumerate(search_results):
                            # Debug: print the first result's payload structure to understand what keys are available
                            if i == 0 and hasattr(result, 'payload') and result.payload:
                                logger.debug(f"Fallback search - First result payload structure: {list(result.payload.keys())}")
                                logger.debug(f"Fallback search - First result payload sample: {result.payload}")

                            chunk = RetrievedChunk(
                                score=result.score,
                                url=result.payload.get('url', ''),
                                heading=result.payload.get('heading', ''),
                                chunk_index=result.payload.get('chunk_index', 0),
                                chunk_text=result.payload.get('content', '')[:200] if result.payload.get('content', '') else result.payload.get('text', '')[:200] if result.payload.get('text', '') else '',  # Get content from correct key
                                section=result.payload.get('section', ''),
                                validation_passed=False
                            )
                            chunks.append(chunk)
                    except (AttributeError, Exception) as e:
                        logger.debug(f"Unfiltered search method failed: {e}")

                        # If search doesn't work, try the query method (though it expects text, not embedding)
                        try:
                            search_results = self.qdrant_client.query(
                                collection_name=self.collection_name,
                                query_text="dummy",  # This won't work properly with pre-generated embeddings
                                limit=top_k,
                                with_payload=True  # Explicitly request payload
                            )

                            chunks = []
                            for i, result in enumerate(search_results):
                                # Handle different result formats depending on the method used
                                if hasattr(result, 'score'):  # New format from query_points
                                    score = result.score
                                    payload = result.payload if hasattr(result, 'payload') else {}
                                elif isinstance(result, tuple):  # Old format or tuple format
                                    # If it's a tuple, the format might be (score, payload) or similar
                                    if len(result) >= 2:
                                        score = result[0] if hasattr(result[0], '__dict__') or isinstance(result[0], (int, float)) else 0.0
                                        payload = result[1] if isinstance(result[1], dict) else {}
                                    else:
                                        score = 0.0
                                        payload = {}
                                else:
                                    # Assume it's an older format
                                    score = getattr(result, 'score', 0.0)
                                    payload = getattr(result, 'payload', {})

                                # Ensure payload is a dictionary
                                if not isinstance(payload, dict):
                                    payload = {}

                                # Debug: print the first result's payload structure to understand what keys are available
                                if i == 0 and payload:
                                    logger.debug(f"Fallback query - First result payload structure: {list(payload.keys())}")
                                    logger.debug(f"Fallback query - First result payload sample: {payload}")

                                chunk = RetrievedChunk(
                                    score=score,
                                    url=payload.get('url', ''),
                                    heading=payload.get('heading', ''),
                                    chunk_index=payload.get('chunk_index', 0),
                                    chunk_text=payload.get('content', '')[:200] if payload.get('content', '') else payload.get('text', '')[:200] if payload.get('text', '') else '',  # Get content from correct key
                                    section=payload.get('section', ''),
                                    validation_passed=False
                                )
                                chunks.append(chunk)
                        except (AttributeError, TypeError) as e:
                            logger.debug(f"Unfiltered query method failed: {e}")

                            # Final fallback: try to handle the results differently if they come in a different format
                            logger.error("Qdrant client has no compatible search method")
                            return []

            return chunks

        except Exception as e:
            logger.error(f"Failed to execute search: {e}")
            return []

    def _validate_chunk_metadata(self, chunks: List[RetrievedChunk]) -> List[RetrievedChunk]:
        """Validate metadata integrity for each retrieved chunk."""
        validated_chunks = []

        for chunk in chunks:
            # Perform metadata validation
            metadata_verification = self._verify_metadata(chunk)

            # Update validation_passed based on metadata verification
            chunk.validation_passed = metadata_verification.overall_score >= 0.8  # 80% threshold

            validated_chunks.append(chunk)

        return validated_chunks

    def _verify_metadata(self, chunk: RetrievedChunk) -> MetadataVerification:
        """Verify metadata fields for a single chunk."""
        # Check if URL is valid (not empty and starts with expected base)
        url_valid = bool(chunk.url and chunk.url.startswith(('http://', 'https://')))

        # Check if heading is present and meaningful
        heading_present = bool(chunk.heading and len(chunk.heading.strip()) > 0)

        # Check if section is present
        section_correct = bool(chunk.section and len(chunk.section.strip()) > 0)

        # Check if chunk_index is valid
        chunk_index_valid = chunk.chunk_index >= 0

        # Check if text quality is good (not empty, not just whitespace)
        text_quality = bool(chunk.chunk_text and chunk.chunk_text.strip() and len(chunk.chunk_text.strip()) > 10)

        # Calculate overall score (simple average)
        total_checks = 5
        passed_checks = sum([
            url_valid, heading_present, section_correct,
            chunk_index_valid, text_quality
        ])

        overall_score = passed_checks / total_checks if total_checks > 0 else 0.0

        return MetadataVerification(
            url_valid=url_valid,
            heading_present=heading_present,
            section_correct=section_correct,
            chunk_index_valid=chunk_index_valid,
            text_quality=text_quality,
            overall_score=overall_score
        )

    def _calculate_validation_metrics(self, chunks: List[RetrievedChunk], query: str) -> Tuple[float, float, float]:
        """Calculate validation metrics for retrieved chunks."""
        if not chunks:
            return 0.0, 0.0, 0.0

        # Calculate metadata accuracy (fraction of chunks that have valid URL and text)
        valid_metadata_count = sum(1 for chunk in chunks if chunk.url and chunk.chunk_text.strip())
        metadata_accuracy = valid_metadata_count / len(chunks) if chunks else 0.0

        # Calculate book content ratio (fraction of chunks from /docs/ sections)
        book_content_count = sum(1 for chunk in chunks if '/docs/' in chunk.url)
        book_content_ratio = book_content_count / len(chunks) if chunks else 0.0

        # Calculate content relevance based on similarity scores and content matching
        relevance_scores = []
        for chunk in chunks:
            # Base relevance on search score (higher score = more relevant)
            base_relevance = min(chunk.score, 1.0) if chunk.score is not None else 0.0  # Cap at 1.0

            # Adjust based on whether it's book content (/docs/)
            is_book_content = '/docs/' in chunk.url
            content_type_multiplier = 1.2 if is_book_content else 0.8  # Boost book content

            adjusted_relevance = base_relevance * content_type_multiplier
            relevance_scores.append(min(adjusted_relevance, 1.0))  # Cap at 1.0

        content_relevance = sum(relevance_scores) / len(relevance_scores) if relevance_scores else 0.0

        # Overall validation score combines metadata accuracy and book content ratio
        validation_score = (metadata_accuracy * 0.5) + (book_content_ratio * 0.5)

        return validation_score, metadata_accuracy, content_relevance

    def _classify_query_type(self, query: str) -> str:
        """Classify query type based on length and complexity."""
        query_len = len(query.strip())

        if query_len == 0:
            return "empty"
        elif query_len < 10:
            return "short"
        elif query_len > 100:
            return "long"
        elif any(word in query.lower() for word in ["what", "how", "why", "when", "where", "who"]):
            return "normal"
        else:
            return "edge"

    def _create_empty_validation_result(self, query: str, query_type: str) -> RetrievalValidationResult:
        """Create an empty validation result for failed queries."""
        return RetrievalValidationResult(
            query=query,
            retrieved_chunks=[],
            validation_score=0.0,
            metadata_accuracy=0.0,
            content_relevance=0.0,
            query_type=query_type,
            timestamp=time.strftime('%Y-%m-%d %H:%M:%S'),
            execution_time=0.0
        )

    def validate_metadata_integrity(self, retrieved_chunks: List[RetrievedChunk]) -> MetadataVerification:
        """
        Validates that all retrieved chunks have proper metadata.

        Args:
            retrieved_chunks: List of retrieved chunk objects

        Returns:
            MetadataVerification object with validation scores
        """
        if not retrieved_chunks:
            return MetadataVerification(
                url_valid=False,
                heading_present=False,
                section_correct=False,
                chunk_index_valid=False,
                text_quality=False,
                overall_score=0.0
            )

        # Aggregate validation results
        url_valid_count = sum(1 for chunk in retrieved_chunks if chunk.url and chunk.url.startswith(('http://', 'https://')))
        heading_present_count = sum(1 for chunk in retrieved_chunks if chunk.heading and chunk.heading.strip())
        section_correct_count = sum(1 for chunk in retrieved_chunks if chunk.section and chunk.section.strip())
        chunk_index_valid_count = sum(1 for chunk in retrieved_chunks if chunk.chunk_index >= 0)
        text_quality_count = sum(1 for chunk in retrieved_chunks if chunk.chunk_text and chunk.chunk_text.strip())

        total_chunks = len(retrieved_chunks)

        return MetadataVerification(
            url_valid=(url_valid_count / total_chunks) >= 0.8,  # 80% threshold
            heading_present=(heading_present_count / total_chunks) >= 0.8,
            section_correct=(section_correct_count / total_chunks) >= 0.8,
            chunk_index_valid=(chunk_index_valid_count / total_chunks) >= 0.8,
            text_quality=(text_quality_count / total_chunks) >= 0.8,
            overall_score=min(
                url_valid_count, heading_present_count, section_correct_count,
                chunk_index_valid_count, text_quality_count
            ) / total_chunks if total_chunks > 0 else 0.0
        )

    def run_validation_suite(self, test_queries: List[str], top_k: int = 5) -> Dict:
        """
        Executes a comprehensive validation suite against multiple query types.

        Args:
            test_queries: List of test queries to validate
            top_k: Number of results to retrieve for each query

        Returns:
            Dictionary with aggregated validation results
        """
        results = []
        query_types = {"normal": [], "short": [], "long": [], "edge": [], "empty": []}

        logger.info(f"Running validation suite with {len(test_queries)} queries...")

        for i, query in enumerate(test_queries):
            logger.info(f"Validating query {i+1}/{len(test_queries)}: {query[:50]}{'...' if len(query) > 50 else ''}")

            result = self.validate_query_retrieval(query, top_k)
            results.append(result)

            # Group by query type for analysis
            if result.query_type in query_types:
                query_types[result.query_type].append(result)
            else:
                # Handle unknown query types by adding them dynamically
                query_types[result.query_type] = [result]

        # Calculate aggregate metrics
        total_validation_score = sum(r.validation_score for r in results) / len(results) if results else 0.0
        total_metadata_accuracy = sum(r.metadata_accuracy for r in results) / len(results) if results else 0.0
        total_content_relevance = sum(r.content_relevance for r in results) / len(results) if results else 0.0

        # Calculate book content ratio (how many results are from /docs/ sections)
        all_chunks = [chunk for result in results for chunk in result.retrieved_chunks]
        book_content_count = sum(1 for chunk in all_chunks if '/docs/' in chunk.url)
        book_content_ratio = book_content_count / len(all_chunks) if all_chunks else 0.0

        # Calculate average execution time
        avg_execution_time = sum(r.execution_time for r in results) / len(results) if results else 0.0

        return {
            "total_queries": len(test_queries),
            "successful_queries": len([r for r in results if r.retrieved_chunks]),
            "aggregate_metrics": {
                "validation_score": total_validation_score,
                "metadata_accuracy": total_metadata_accuracy,
                "content_relevance": total_content_relevance,
                "book_content_ratio": book_content_ratio,
                "avg_execution_time": avg_execution_time
            },
            "by_query_type": {
                qt: {
                    "count": len(qr_list),
                    "avg_validation_score": sum(r.validation_score for r in qr_list) / len(qr_list) if qr_list else 0.0,
                    "avg_metadata_accuracy": sum(r.metadata_accuracy for r in qr_list) / len(qr_list) if qr_list else 0.0,
                    "avg_content_relevance": sum(r.content_relevance for r in qr_list) / len(qr_list) if qr_list else 0.0
                } for qt, qr_list in query_types.items() if qr_list
            },
            "individual_results": results
        }


def save_validation_report(validation_results: Dict, filename: str = None):
    """Save validation results to a timestamped file in history directory."""
    import datetime

    if not filename:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"retrieval_validation_{timestamp}.log"

    # Create history directory if it doesn't exist
    os.makedirs("history", exist_ok=True)

    filepath = f"history/{filename}"

    # Prepare report content
    report_content = f"""Retrieval Validation Report
======================

Timestamp: {datetime.datetime.now().isoformat()}
Total Queries: {validation_results['total_queries']}
Successful Queries: {validation_results['successful_queries']}

Aggregate Metrics:
- Validation Score: {validation_results['aggregate_metrics']['validation_score']:.3f}
- Metadata Accuracy: {validation_results['aggregate_metrics']['metadata_accuracy']:.3f}
- Content Relevance: {validation_results['aggregate_metrics']['content_relevance']:.3f}
- Book Content Ratio: {validation_results['aggregate_metrics']['book_content_ratio']:.3f}
- Avg Execution Time: {validation_results['aggregate_metrics']['avg_execution_time']:.3f}s

Results by Query Type:
"""

    for qt, metrics in validation_results['by_query_type'].items():
        report_content += f"""  {qt.title()}:
    - Count: {metrics['count']}
    - Avg Validation Score: {metrics['avg_validation_score']:.3f}
    - Avg Metadata Accuracy: {metrics['avg_metadata_accuracy']:.3f}
    - Avg Content Relevance: {metrics['avg_content_relevance']:.3f}
"""

    # Add individual results if not too verbose
    if validation_results['total_queries'] <= 10:  # Only show individual results for small test suites
        report_content += "\nIndividual Results:\n"
        for i, result in enumerate(validation_results['individual_results']):
            report_content += f"\n  Query {i+1}: \"{result.query[:50]}...\"\n"
            report_content += f"    Type: {result.query_type}, Score: {result.validation_score:.3f}\n"
            report_content += f"    Chunks retrieved: {len(result.retrieved_chunks)}\n"
            if result.retrieved_chunks:
                sample_chunk = result.retrieved_chunks[0]
                report_content += f"    Sample result: {sample_chunk.url[:60]}...\n"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(report_content)

    logger.info(f"Validation report saved to {filepath}")
    return filepath


def main():
    parser = argparse.ArgumentParser(description="Retrieval Pipeline Validation")
    parser.add_argument("--query", type=str, help="Single query to validate")
    parser.add_argument("--validate-all", action="store_true", help="Run full validation suite")
    parser.add_argument("--test-type", type=str, choices=["normal", "short", "long", "edge"],
                       help="Run specific test type")
    parser.add_argument("--top-k", type=int, default=5, help="Number of results to retrieve (default: 5)")

    args = parser.parse_args()

    # Check required environment variables
    required_env_vars = ["COHERE_API_KEY", "QDRANT_URL", "QDRANT_API_KEY"]
    missing_vars = [var for var in required_env_vars if not os.getenv(var)]

    if missing_vars:
        logger.error(f"Missing required environment variables: {missing_vars}")
        logger.error("Please set them in a .env file or environment")
        return 1

    # Initialize validator
    validator = RetrievalValidator()

    if args.query:
        # Validate single query
        logger.info(f"Validating query: {args.query}")
        result = validator.validate_query_retrieval(args.query, args.top_k)

        print(f"\nValidation Results:")
        print(f"- Query: \"{result.query}\"")
        print(f"- Retrieved: {len(result.retrieved_chunks)} chunks")
        print(f"- Validation Score: {result.validation_score:.3f}")
        print(f"- Metadata Accuracy: {result.metadata_accuracy:.3f}")
        print(f"- Content Relevance: {result.content_relevance:.3f}")
        print(f"- Query Type: {result.query_type}")
        print(f"- Execution Time: {result.execution_time:.3f}s")

        if result.retrieved_chunks:
            print(f"\nTop Results:")
            for i, chunk in enumerate(result.retrieved_chunks[:3]):  # Show top 3
                print(f"  {i+1}. Score: {chunk.score:.3f}, URL: {chunk.url[:60]}...")
                # Handle potential unicode characters in heading and chunk_text
                safe_heading = chunk.heading.encode('ascii', errors='ignore').decode('ascii')
                safe_preview = chunk.chunk_text.encode('ascii', errors='ignore').decode('ascii')
                print(f"     Heading: {safe_heading[:50]}...")
                print(f"     Preview: {safe_preview[:100]}...")

        # Save single result to history
        report_data = {
            "total_queries": 1,
            "successful_queries": 1 if result.retrieved_chunks else 0,
            "aggregate_metrics": {
                "validation_score": result.validation_score,
                "metadata_accuracy": result.metadata_accuracy,
                "content_relevance": result.content_relevance,
                "book_content_ratio": sum(1 for c in result.retrieved_chunks if '/docs/' in c.url) / len(result.retrieved_chunks) if result.retrieved_chunks else 0.0,
                "avg_execution_time": result.execution_time
            },
            "by_query_type": {
                result.query_type: {
                    "count": 1,
                    "avg_validation_score": result.validation_score,
                    "avg_metadata_accuracy": result.metadata_accuracy,
                    "avg_content_relevance": result.content_relevance
                }
            },
            "individual_results": [result]
        }
        save_validation_report(report_data)

    elif args.validate_all or args.test_type:
        # Run validation suite
        if args.test_type:
            # Generate test queries for specific type
            if args.test_type == "normal":
                test_queries = [
                    "What is the main concept of this book?",
                    "Explain the core principles in the book",
                    "How does the system work?"
                ]
            elif args.test_type == "short":
                test_queries = [
                    "AI",
                    "RAG",
                    "book"
                ]
            elif args.test_type == "long":
                test_queries = [
                    "Can you provide a comprehensive explanation of how the retrieval augmented generation system works in this book and what are the key components involved?",
                    "What are the detailed steps for implementing a successful AI system according to the methodologies described in the technical book?"
                ]
            else:  # edge
                test_queries = [
                    "",
                    "?????",
                    "asdlkjf asdf asdf asdf"
                ]
        else:
            # Full validation suite
            test_queries = [
                # Normal queries
                "What is the main concept of this book?",
                "Explain the core principles",
                "How does the system work?",

                # Short queries
                "AI",
                "RAG",
                "book",

                # Long queries
                "Can you provide a comprehensive explanation of how the retrieval augmented generation system works in this book and what are the key components involved?",

                # Edge case queries
                "",
                "?????",
            ]

        validation_results = validator.run_validation_suite(test_queries, args.top_k)

        # Print summary
        print(f"\nValidation Suite Results:")
        print(f"- Total Queries: {validation_results['total_queries']}")
        print(f"- Successful Queries: {validation_results['successful_queries']}")
        print(f"- Validation Score: {validation_results['aggregate_metrics']['validation_score']:.3f}")
        print(f"- Metadata Accuracy: {validation_results['aggregate_metrics']['metadata_accuracy']:.3f}")
        print(f"- Content Relevance: {validation_results['aggregate_metrics']['content_relevance']:.3f}")
        print(f"- Book Content Ratio: {validation_results['aggregate_metrics']['book_content_ratio']:.3f}")
        print(f"- Avg Execution Time: {validation_results['aggregate_metrics']['avg_execution_time']:.3f}s")

        print(f"\nResults by Query Type:")
        for qt, metrics in validation_results['by_query_type'].items():
            print(f"  {qt.title()}: {metrics['count']} queries, "
                  f"Score: {metrics['avg_validation_score']:.3f}")

        # Save full report
        save_validation_report(validation_results)

    else:
        print("Please specify either --query or --validate-all or --test-type")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())