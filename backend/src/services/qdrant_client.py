import asyncio
from typing import List, Optional
from qdrant_client import QdrantClient
from qdrant_client.http.models import (
    PointStruct,
    VectorParams,
    Distance,
    SearchRequest,
    SearchParams,
    Filter
)
from qdrant_client.http import models
import cohere
import numpy as np
from ..config.settings import settings
from ..models.chunk import Chunk


class QdrantService:
    def __init__(self):
        self.client = QdrantClient(
            url=settings.qdrant_url,
            api_key=settings.qdrant_api_key,
            timeout=30
        )
        self.cohere_client = cohere.Client(settings.cohere_api_key)
        self.collection_name = settings.qdrant_collection_name

    def _embed_text(self, text: str) -> List[float]:
        """Generate embeddings for text using Cohere."""
        response = self.cohere_client.embed(
            texts=[text],
            model="multilingual-22-12"
        )
        return response.embeddings[0]

    def search_chunks(self, query: str, top_k: int = 5, filters: Optional[dict] = None) -> List[Chunk]:
        """
        Search for relevant chunks in Qdrant based on the query.

        Args:
            query: The search query
            top_k: Number of chunks to retrieve
            filters: Optional filters for the search

        Returns:
            List of Chunk objects with the most relevant content
        """
        try:
            # Generate embedding for the query using Cohere
            query_embedding = self._embed_text(query)

            # Prepare search filters if provided
            qdrant_filters = None
            if filters:
                filter_conditions = []
                for key, value in filters.items():
                    filter_conditions.append(
                        models.FieldCondition(
                            key=key,
                            match=models.MatchValue(value=value)
                        )
                    )

                if filter_conditions:
                    qdrant_filters = models.Filter(
                        must=filter_conditions
                    )

            # Try different search methods based on the Qdrant client version
            search_results = None

            # First, try the newer query_points method
            try:
                search_results = self.client.query_points(
                    collection_name=self.collection_name,
                    query=query_embedding,
                    limit=top_k,
                    with_payload=True,
                    query_filter=qdrant_filters
                )

                # Handle the new QueryResponse structure
                if hasattr(search_results, 'points'):
                    search_points = search_results.points
                else:
                    search_points = search_results

                # Convert search results to Chunk objects
                chunks = []
                for result in search_points:
                    # Handle different result formats depending on the method used
                    if hasattr(result, 'score'):  # New format from query_points (ScoredPoint)
                        score = result.score
                        payload = result.payload if hasattr(result, 'payload') else {}
                    else:
                        # Assume it's an older format
                        score = getattr(result, 'score', 0.0)
                        payload = getattr(result, 'payload', {})

                    # Ensure payload is a dictionary
                    if not isinstance(payload, dict):
                        payload = {}

                    chunk = Chunk(
                        id=result.id if hasattr(result, 'id') else 'unknown',
                        content=payload.get('content', payload.get('text', '')),
                        url=payload.get('url', ''),
                        metadata=payload.get('metadata', {}),
                        score=score
                    )
                    chunks.append(chunk)

                return chunks

            except (AttributeError, Exception) as e:
                print(f"query_points method failed: {e}")

                # Fallback to the older search method
                try:
                    search_results = self.client.search(
                        collection_name=self.collection_name,
                        query_vector=query_embedding,
                        limit=top_k,
                        query_filter=qdrant_filters,
                        with_payload=True,
                        with_vectors=False
                    )

                    # Convert search results to Chunk objects
                    chunks = []
                    for result in search_results:
                        payload = result.payload
                        chunk = Chunk(
                            id=result.id,
                            content=payload.get('content', payload.get('text', '')),
                            url=payload.get('url', ''),
                            metadata=payload.get('metadata', {}),
                            score=result.score
                        )
                        chunks.append(chunk)

                    return chunks

                except Exception as e2:
                    print(f"Both search methods failed: {e}, {e2}")
                    return []

        except Exception as e:
            print(f"Error searching Qdrant: {str(e)}")
            return []

    def check_connection(self) -> bool:
        """
        Check if the Qdrant connection is working.

        Returns:
            True if connection is successful, False otherwise
        """
        try:
            # Try to get collection info to verify connection
            collections = self.client.get_collections()
            return True
        except Exception as e:
            print(f"Qdrant connection check failed: {str(e)}")
            return False

    def get_total_points(self) -> int:
        """
        Get the total number of points in the collection.

        Returns:
            Total number of points in the collection
        """
        try:
            collection_info = self.client.get_collection(self.collection_name)
            return collection_info.points_count
        except Exception as e:
            print(f"Error getting collection info: {str(e)}")
            return 0