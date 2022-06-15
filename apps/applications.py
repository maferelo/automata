"""A module to define the main object of the application."""
from dataclasses import dataclass

from apps.shceluder import set_tasks


@dataclass
class App:
    """The main object of the application."""

    schelude: callable = set_tasks
