import time
from typing import List, Dict, Any
from ..models.chunk import Chunk
from .qdrant_client import QdrantService
from ..config.settings import settings


class RetrievalTool:
    """
    A tool that retrieves relevant chunks from Qdrant based on a query.
    This tool is designed to be used with the OpenAI Agent system.
    """

    def __init__(self):
        self.qdrant_service = QdrantService()

    def retrieve(self, query: str, top_k: int = None, filters: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        """
        Retrieve relevant chunks from Qdrant based on the query.

        Args:
            query: The search query
            top_k: Number of chunks to retrieve (defaults to settings.default_top_k)
            filters: Optional filters for the search

        Returns:
            List of dictionaries containing chunk information
        """
        start_time = time.time()

        if top_k is None:
            top_k = settings.default_top_k

        # Search for relevant chunks in Qdrant
        retrieved_chunks = self.qdrant_service.search_chunks(
            query=query,
            top_k=top_k,
            filters=filters
        )

        # Convert chunks to the required format for the agent
        result = []
        for chunk in retrieved_chunks:
            result.append({
                "id": chunk.id,
                "content": chunk.content,
                "url": chunk.url,
                "score": chunk.score,
                "metadata": chunk.metadata
            })

        retrieval_time = (time.time() - start_time) * 1000  # Convert to milliseconds

        # Handle potential encoding issues when printing
        # Suppress print during automated tests to avoid duplicate output
        import os
        if os.environ.get('SUPPRESS_RETRIEVAL_LOGS', 'false').lower() != 'true':
            try:
                print(f"Retrieval took {retrieval_time:.2f}ms for {len(result)} chunks")
            except UnicodeEncodeError:
                # Fallback to encoded string if there are encoding issues
                print(f"Retrieval took {retrieval_time:.2f}ms for {len(result)} chunks".encode('utf-8', errors='ignore').decode('utf-8'))

        return result

    def get_total_points(self) -> int:
        """
        Get the total number of points in the Qdrant collection.

        Returns:
            Total number of points in the collection
        """
        return self.qdrant_service.get_total_points()

    def check_availability(self) -> bool:
        """
        Check if the retrieval tool is available (can connect to Qdrant).

        Returns:
            True if the tool is available, False otherwise
        """
        return self.qdrant_service.check_connection()