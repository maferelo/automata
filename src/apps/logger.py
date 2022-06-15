"""Define the logger."""
import logging
from logging.config import dictConfig

logging_schema = {
    # Always 1. Schema versioning may be added in a future release of logging
    "version": 1,
    # "Name of formatter" : {Formatter Config Dict}
    "formatters": {
        # Formatter Name
        "standard": {
            # class is always "logging.Formatter"
            "class": "logging.Formatter",
            # Optional: logging output format
            "format": "%(asctime)s\t%(name)s\t%(levelname)s\t%(filename)s\t%(message)s",
            # Optional: asctime format
            "datefmt": "%d %b %y %H:%M:%S",
        }
    },
    # Handlers use the formatter names declared above
    "handlers": {
        # Name of handler
        "console": {
            # The class of logger. A mixture of logging.config.dictConfig() and
            # logger class-specific keyword arguments (kwargs) are passed in here.
            "class": "logging.StreamHandler",
            # This is the formatter name declared above
            "formatter": "standard",
            "level": "INFO",
            # The default is stderr
            "stream": "ext://sys.stdout",
        },
        # Same as the StreamHandler example above, but with different
        # handler-specific kwargs.
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "standard",
            "level": "INFO",
            "filename": "logs/.log",
            "mode": "a",
            "encoding": "utf-8",
            "maxBytes": 500000,
            "backupCount": 4,
        },
    },
    # Loggers use the handler names declared above
    "loggers": {
        "__main__": {  # if __name__ == "__main__"
            # Use a list even if one handler is used
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": False,
        }
    },
    # Just a standalone kwarg for the root logger
    "root": {"level": "INFO", "handlers": ["file"]},
}


def create_logger() -> logging.Logger:
    """Configure and return the logger."""
    dictConfig(logging_schema)
    return logging.getLogger(__name__)
