"""Tests for main module."""
from typer import testing

from automata.main import app  # isort:skip

runner = testing.CliRunner()


def test_app():
    """Test CLI."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
