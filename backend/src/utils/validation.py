from typing import Optional
from ..models.request import QueryRequest
import re


def validate_query_request(request: QueryRequest) -> tuple[bool, Optional[str]]:
    """
    Validate a QueryRequest object.

    Args:
        request: The QueryRequest to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Check if query is empty or just whitespace
    if not request.query or not request.query.strip():
        return False, "Query cannot be empty or contain only whitespace"

    # Check query length
    if len(request.query.strip()) < 3:
        return False, "Query must be at least 3 characters long"

    # Check selected_text length if provided
    if request.selected_text and len(request.selected_text) > 10000:
        return False, "Selected text exceeds maximum length of 10,000 characters"

    # Check top_k bounds
    if request.top_k < 1 or request.top_k > 10:
        return False, "top_k must be between 1 and 10"

    return True, None


def sanitize_input(text: str) -> str:
    """
    Sanitize input text by removing potentially harmful content.

    Args:
        text: Input text to sanitize

    Returns:
        Sanitized text
    """
    if not text:
        return text

    # Remove potentially dangerous patterns (SQL injection, script tags, etc.)
    sanitized = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.IGNORECASE)
    sanitized = re.sub(r'javascript:', '', sanitized, flags=re.IGNORECASE)
    sanitized = re.sub(r'vbscript:', '', sanitized, flags=re.IGNORECASE)
    sanitized = re.sub(r'on\w+\s*=', '', sanitized, flags=re.IGNORECASE)

    return sanitized.strip()


def validate_url(url: str) -> bool:
    """
    Validate if a string is a properly formatted URL.

    Args:
        url: URL string to validate

    Returns:
        True if valid URL, False otherwise
    """
    if not url:
        return False

    # Basic URL regex pattern
    pattern = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}'  # domain
        r'(?:/[^\s]*)?$'  # optional path
    )

    return bool(pattern.match(url))