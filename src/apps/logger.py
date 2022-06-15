"""A module to define the logger."""
import logging
from logging.config import dictConfig

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
            "filename": "logs/.log",
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


def create_logger() -> logging.Logger:
    """Configure and create the logger."""
    dictConfig(logging_schema)
    return logging.getLogger(__name__)
