"""Pytest test configuration."""
import pytest
from apps.app import App


@pytest.fixture
def app() -> App:
    """Create an instance of the application."""
    return App()
