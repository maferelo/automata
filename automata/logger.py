"""A module to configure and create the logger."""
import functools
import logging
from logging.config import dictConfig
from typing import Callable

logging_schema = {
    "version": 1,
    "formatters": {
        "standard": {
            "format": "%(asctime)s\t%(name)s\t%(levelname)s\t%(filename)s\t%(message)s",
            "datefmt": "%d %b %y %H:%M:%S",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "level": "INFO",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "standard",
            "level": "INFO",
            "filename": f"logs/{__name__}.log",
            "maxBytes": 500000,
            "backupCount": 4,
        },
    },
    "loggers": {
        "__main__": {
            "handlers": ["file", "console"],
            "level": "INFO",
            "propagate": False,
        }
    },
    "root": {"level": "INFO", "handlers": ["file"]},
}


dictConfig(logging_schema)
logger = logging.getLogger("__main__")


def log_execution(function: Callable) -> Callable:
    """A decorator to log the function's execution."""

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        logger.info("Started %s", function.__name__)
        result = function(*args, **kwargs)
        logger.info("Finished %s", function.__name__)
        return result

    return wrapper
