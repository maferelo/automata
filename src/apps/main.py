"""A module to run the application."""
import typer

from app import App


def main(name: str):
    """The main function of the application."""
    app = App()
    typer.echo(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
