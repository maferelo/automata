"""A module setup environment and app variables."""
import sys
from dataclasses import dataclass
from pathlib import Path

from decouple import config

import automata


@dataclass(frozen=True)
class Paths:
    """A dataclass to define global variables."""

    project: Path = Path(automata.__file__).parent.parent
    log_file: Path = project / "logs" / "app.log"
    main: Path = project / "main.py"
    python_executable: Path = Path(sys.executable)
    scripts: Path = project / "scripts"


@dataclass(frozen=True)
class TelegramConfig:
    """A dataclass to define the behaviour of the telegram bot."""

    token: str = config("TELEGRAM_TOKEN")
    chat_id: str = config("TELEGRAM_CHAT_ID")


scheluder_scripts = tuple(config("SCHELUDER_SCRIPTS").split(","))
paths = Paths()
telegram_config = TelegramConfig()
