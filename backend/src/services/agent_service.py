import time
from datetime import datetime
from typing import Dict, Any, List, Optional
from ..models.request import QueryRequest, AgentResponse, RetrievedChunk, ErrorDetails
from .retrieval_tool import RetrievalTool
from .qdrant_client import QdrantService
from ..config.settings import settings
from ..utils.validation import validate_query_request, sanitize_input
from ..utils.logging import get_logger
from .gemini_service import GeminiService


class AgentService:
    """
    Service that orchestrates the Gemini API with retrieval capabilities for RAG.
    """

    def __init__(self):
        self.retrieval_tool = RetrievalTool()
        self.qdrant_service = QdrantService()
        self.logger = get_logger("agent_service")
        self.gemini_service = GeminiService()

    async def process_query(self, request: QueryRequest) -> AgentResponse:
        """
        Process a query request using either retrieval mode or selected-text-only mode.

        Args:
            request: The query request containing the user's question

        Returns:
            AgentResponse with the answer and provenance information
        """
        start_time = time.time()
        error_details = None

        try:
            # Validate the request
            is_valid, error_msg = validate_query_request(request)
            if not is_valid:
                raise ValueError(error_msg)

            # Sanitize inputs
            sanitized_query = sanitize_input(request.query)

            # Determine which mode to use
            mode_used = "selected-text-only" if request.selected_text else "retrieval"

            sources: List[RetrievedChunk] = []
            answer = ""
            tool_call_count = 0

            # Calculate total time - measure the entire request processing
            if mode_used == "retrieval":
                # For retrieval mode, retrieve relevant chunks and generate answer with Gemini
                answer, sources, tool_call_count = await self._answer_with_retrieval(sanitized_query, request)

                # Measure retrieval time separately for metrics
                retrieval_start = time.time()
                retrieved_chunks = self.retrieval_tool.retrieve(
                    query=sanitized_query,
                    top_k=request.top_k
                )
                retrieval_time = (time.time() - retrieval_start) * 1000

                # Add debug logs for retrieval
                self.logger.info(f"retrieved_n_chunks: {len(retrieved_chunks)}")
                if retrieved_chunks:
                    first_chunk = retrieved_chunks[0] if isinstance(retrieved_chunks[0], dict) else retrieved_chunks[0].__dict__ if hasattr(retrieved_chunks[0], '__dict__') else str(retrieved_chunks[0])
                    if isinstance(first_chunk, dict):
                        first_url = first_chunk.get('url', 'no-url-found')
                        top_score = first_chunk.get('score', 'no-score-found')
                        # Handle potential encoding issues in content
                        first_content = first_chunk.get('content', '')[:100] if first_chunk.get('content') else ''
                    else:
                        first_url = getattr(retrieved_chunks[0], 'url', 'no-url-found')
                        top_score = getattr(retrieved_chunks[0], 'score', 'no-score-found')
                        # Handle potential encoding issues in content
                        first_content = getattr(retrieved_chunks[0], 'content', '')[:100] if hasattr(retrieved_chunks[0], 'content') else ''

                    # Safely log with encoding handling
                    try:
                        self.logger.info(f"first_chunk_url: {first_url}")
                        self.logger.info(f"top_score: {top_score}")
                    except UnicodeEncodeError:
                        self.logger.info(f"first_chunk_url: {str(first_url).encode('utf-8', errors='ignore').decode('utf-8')}")
                        self.logger.info(f"top_score: {str(top_score)}")
            else:
                # For selected-text-only mode, generate answer from selected text only
                retrieval_time = 0
                answer, tool_call_count = await self._answer_from_selected_text(sanitized_query, request.selected_text)

            # Calculate total time - must be from start to finish of entire request
            total_time = (time.time() - start_time) * 1000

            # Ensure retrieval_time does not exceed total_time (it's part of the total processing)
            # The retrieval happens during the agent processing, so retrieval time should be part of total time
            if retrieval_time > total_time:
                retrieval_time = total_time

        except Exception as e:
            # Handle errors and create error details
            error_details = ErrorDetails(
                type=type(e).__name__,
                message=str(e),
                timestamp=datetime.utcnow()
            )
            # Set default values for response in case of error
            answer = f"I encountered an error processing your request: {str(e)}"
            sources = []
            mode_used = "retrieval"  # Default mode
            retrieval_time = 0
            total_time = (time.time() - start_time) * 1000

        response = AgentResponse(
            answer=answer,
            sources=sources,
            mode_used=mode_used,
            retrieval_time_ms=retrieval_time,
            total_time_ms=total_time,
            session_id=request.session_id,
            error=error_details
        )

        if error_details:
            try:
                self.logger.error(f"Error processing query after {total_time:.2f}ms: {error_details.message}")
            except UnicodeEncodeError:
                self.logger.error(f"Error processing query after {total_time:.2f}ms: {str(error_details.message).encode('utf-8', errors='ignore').decode('utf-8')}")
        else:
            try:
                self.logger.info(f"Processed query in {total_time:.2f}ms using {mode_used} mode. Tool calls made: {tool_call_count}, Sources: {len(sources)}, Retrieval time: {retrieval_time:.2f}ms")
            except UnicodeEncodeError:
                self.logger.info(f"Processed query in {total_time:.2f}ms using {mode_used} mode. Tool calls made: {tool_call_count}, Sources: {len(sources)}, Retrieval time: {retrieval_time:.2f}ms")

        return response

    async def _answer_with_retrieval(self, query: str, request: QueryRequest) -> tuple[str, List[RetrievedChunk], int]:
        """
        Generate an answer using Gemini with retrieved context chunks.

        Args:
            query: The user's question
            request: The original request object

        Returns:
            Tuple of (answer, sources, tool_call_count)
        """
        try:
            # Retrieve relevant chunks from Qdrant
            retrieved_chunks = self.retrieval_tool.retrieve(
                query=query,
                top_k=request.top_k
            )

            # Build the prompt with retrieved context
            context_parts = []
            sources = []

            for idx, chunk in enumerate(retrieved_chunks):
                # Clean the content to remove problematic characters
                clean_content = chunk['content'].encode('utf-8', errors='ignore').decode('utf-8')
                clean_url = chunk['url'].encode('utf-8', errors='ignore').decode('utf-8')

                # Add context with source numbering
                context_parts.append(f"[SOURCE {idx + 1}]\nContent: {clean_content}\nURL: {clean_url}\n")

                # Create RetrievedChunk object with cleaned content
                sources.append(RetrievedChunk(
                    chunk_id=chunk["id"],
                    content=clean_content,
                    url=clean_url,
                    score=chunk["score"],
                    metadata=chunk["metadata"]
                ))

            # Build the complete prompt
            context_str = "\n".join(context_parts)
            prompt = f"""You are a helpful assistant that answers based on provided documentation.
Answer the user's question using ONLY the information provided in the context below.
If the answer is not in the context, say so.

Context:
{context_str}

Question: {query}

Provide a comprehensive answer based on the context and cite your sources like [1], [2], etc. matching the SOURCE numbers above."""

            # Generate answer using Gemini
            answer = await self.gemini_service.generate_text(prompt)

            # Estimate tool call count (1 for the retrieval operation)
            tool_call_count = 1 if retrieved_chunks else 0

            return answer, sources, tool_call_count

        except Exception as e:
            self.logger.error(f"Error retrieving and generating answer with Gemini: {str(e)}")
            return f"I encountered an error processing your request: {str(e)}", [], 0

    async def _answer_from_selected_text(self, query: str, selected_text: str) -> tuple[str, int]:
        """
        Generate an answer using Gemini from selected text only.

        Args:
            query: The user's question
            selected_text: The text to base the answer on

        Returns:
            The generated answer and tool call count (always 0)
        """
        try:
            if not selected_text:
                return "No selected text provided for this mode.", 0

            # Build the prompt with selected text
            prompt = f"""You are a helpful assistant. Answer the user's question based ONLY on the provided text.
Do not use any other knowledge. If the answer is not in the provided text, say so.
Do not call any tools or functions.

Text: {selected_text}

Question: {query}

Provide a clear and concise answer based only on the provided text."""

            # Generate answer using Gemini
            answer = await self.gemini_service.generate_text(prompt)

            # Tool call count is 0 for selected-text-only mode
            tool_call_count = 0

            return answer, tool_call_count

        except Exception as e:
            self.logger.error(f"Error generating answer from selected text with Gemini: {str(e)}")
            return f"I encountered an error processing your request: {str(e)}", 0