"""A module setup environment and app variables."""
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Tuple

from dotenv import load_dotenv

import automata

load_dotenv()


@dataclass(frozen=True)
class Paths:
    """A dataclass to define global variables."""

    project: Path = Path(automata.__file__).parent.parent
    log_file: Path = project / "logs" / "app.log"
    scripts: Path = project / "scripts"


scheluder_scripts: tuple(os.environ["SCHELUDER_SCRIPTS"].split(","))
paths = Paths()
