"""A module to run the application."""
import typer

from apps.app import App


def main(name: str) -> None:
    """The main function of the application."""
    app = App()
    if name == "shceluder":
        app.set_tasks()
    app.logger.info("%s is running", name)


if __name__ == "__main__":
    typer.run(main)
