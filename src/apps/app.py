"""Define the main object of the application."""
import logging
from dataclasses import dataclass

from .logger import create_logger


@dataclass
class App:
    """The main object of the application."""

    logger: logging.Logger = create_logger()
