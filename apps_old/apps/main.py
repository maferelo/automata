"""A module to run the application."""
import typer

from apps.applications import App
from apps.logger import logger


def main(name: str) -> None:
    """The main function of the application."""
    app = App()
    if name == "shceluder":
        app.schelude()
    logger.info("%s is running", name)


if __name__ == "__main__":
    typer.run(main)
