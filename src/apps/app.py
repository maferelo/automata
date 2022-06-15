"""Define the main object of the application."""
import os

from logger import create_logger


class App:
    """The app class handles the excecution of each module"""

    def __init__(self):
        """The constructor"""

        # Then name of the application. The import name
        self.name = os.path.splitext(os.path.basename("__main__"))[0]

        # A standard Python :class:`~logging.Logger` for the app
        self.logger = create_logger()
