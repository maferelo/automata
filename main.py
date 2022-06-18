"""A module to run the application."""
import typer

from app import scheluder

app = typer.Typer(help="Utilities to automate project execution and learn clean code.")


@app.command()
def reset_jobs() -> None:
    """Reset recurrent bash jobs."""
    scheluder.reset_jobs()


@app.command()
def test() -> None:
    """Test command."""
    print("Test command.")


if __name__ == "__main__":
    app()
