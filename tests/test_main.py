"""Tests for main module."""
from typer import testing

from main import app  # isort:skip

runner = testing.CliRunner()


def test_app() -> None:
    """Test CLI."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
