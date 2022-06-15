"""A module to define the main object of the application."""
import logging
from dataclasses import dataclass

from .logger import create_logger
from .shceluder import set_tasks


@dataclass
class App:
    """The main object of the application."""

    logger: logging.Logger = create_logger()
    set_tasks: callable = set_tasks
