"""A module to run the application."""
import typer

from shceluder import reset_jobs

commands = (reset_jobs,)


def main(command_name: str) -> None:
    """The main function of the application."""
    for command in commands:
        if command_name == command.__name__:
            command()


if __name__ == "__main__":
    typer.run(main)
