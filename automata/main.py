"""A module to run the application."""
import typer

from automata.scheluder import reset_jobs

app = typer.Typer()

commands = (reset_jobs,)


@app.command()
def main(command_name: str) -> None:
    """The main function of the application."""
    for command in commands:
        if command_name == command.__name__:
            command()


if __name__ == "__main__":
    app()
