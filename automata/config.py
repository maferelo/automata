"""A module setup environment and app variables."""
import os
import sys
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

import automata

load_dotenv()


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

    token: str = os.environ["TELEGRAM_TOKEN"]
    chat_id: str = os.environ["TELEGRAM_CHAT_ID"]


scheluder_scripts = tuple(os.environ["SCHELUDER_SCRIPTS"].split(","))
paths = Paths()
telegram_config = TelegramConfig()
