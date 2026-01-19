import logging
from typing import Any
import json
from datetime import datetime
from ..config.settings import settings


def setup_logging():
    """Configure logging for the application."""
    log_level = logging.DEBUG if settings.debug else logging.INFO

    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
        ]
    )


def get_logger(name: str) -> logging.Logger:
    """Get a logger instance with the specified name."""
    logger = logging.getLogger(name)

    if settings.debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    return logger


def log_api_call(
    endpoint: str,
    method: str,
    user_id: str = None,
    params: dict = None,
    response_size: int = None,
    execution_time: float = None
):
    """Log an API call with relevant information."""
    logger = get_logger("api")

    log_data = {
        "timestamp": datetime.utcnow().isoformat(),
        "endpoint": endpoint,
        "method": method,
        "user_id": user_id,
        "params": params,
        "response_size": response_size,
        "execution_time_ms": execution_time
    }

    logger.info(json.dumps(log_data))


def log_error(error: Exception, context: str = ""):
    """Log an error with context."""
    logger = get_logger("error")

    log_data = {
        "timestamp": datetime.utcnow().isoformat(),
        "context": context,
        "error_type": type(error).__name__,
        "error_message": str(error),
        "traceback": str(error.__traceback__) if hasattr(error, '__traceback__') else None
    }

    logger.error(json.dumps(log_data))