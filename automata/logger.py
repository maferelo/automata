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
            "filename": "logs/automata.log",
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


def log_execution(func: Callable) -> Callable:
    """A decorator to log the function's execution."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info("Started %s", func.__name__)
        func(*args, **kwargs)
        logger.info("Finished %s", func.__name__)
        return func(*args, **kwargs)

    return wrapper
