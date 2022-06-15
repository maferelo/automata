"""Tests for logger module."""
from apps.app import App


def test_logger(app: App) -> None:
    """Test the logger."""
    assert app.logger.LEVEL == "INFO"
