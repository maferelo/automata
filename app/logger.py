"""A module to configure and create the logger."""
import logging
from logging.config import dictConfig

from app.config import paths

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
            "filename": paths.log_file_path,
            "maxBytes": 500_000,  # 0.5 MB
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
