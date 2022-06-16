"""A module to run the application."""
import typer

from application import Automata
from logger import logger


def main(name: str) -> None:
    """The main function of the application."""
    app = Automata()
    if name == "shceluder":
        app.schelude()
    logger.info("%s is running", name)


if __name__ == "__main__":
    typer.run(main)
