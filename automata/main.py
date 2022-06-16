"""A module to run the application."""
import typer

from shceluder import set_tasks


def main(name: str) -> None:
    """The main function of the application."""
    if name == "scheluder":
        set_tasks()


if __name__ == "__main__":
    typer.run(main)
