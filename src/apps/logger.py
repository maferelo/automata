"""Define the logger."""
import logging.config


def create_logger() -> logging.Logger:
    """Create and configure the logger."""
    print("create_logger() was just executed")
    logging.config.fileConfig("logging.conf")
    return logging.getLogger(__name__)
