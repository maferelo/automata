"""A module to run the application."""
import typer

from automata import scheluder
from automata.logger import logger

app = typer.Typer(help="Utilities to automate project execution and learn clean code.")


@app.command()
def reset_jobs() -> None:
    """Reset recurrent bash jobs."""
    scheluder.reset_jobs()


@app.command()
def log_message(message: str) -> None:
    """Log message to file and telegram."""
    logger.info(message)


if __name__ == "__main__":
    app()
