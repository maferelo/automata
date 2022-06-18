"""A module to define helper methods."""
import functools
import logging
from typing import Callable


def log_start_and_finish_decorator(logger: logging.Logger) -> Callable:
    """A decorator to log a function start and finish."""

    def decorator(function: Callable) -> Callable:
        @functools.wraps(function)
        def wrapper(*args, **kwargs) -> Callable:
            logger.info("Started %s", function.__name__)
            result = function(*args, **kwargs)
            logger.info("Finished %s", function.__name__)
            return result

        return wrapper

    return decorator
