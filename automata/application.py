"""A module to define the main object of the application."""
from dataclasses import dataclass

from shceluder import set_tasks


@dataclass
class Automata:
    """The main object of the application."""

    schelude: callable = set_tasks
