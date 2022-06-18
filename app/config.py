"""A module setup environment and app variables."""
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Tuple

from dotenv import load_dotenv

import app

load_dotenv()


@dataclass
class Paths:
    """A dataclass to define global variables."""

    project_dir: Path = Path(app.__file__).parent.parent
    log_file_path: Path = project_dir / "logs" / "app.log"
    scripts_path: Path = project_dir / "scripts"
    scheluder_scripts: Tuple[str] = tuple(os.environ["SCHELUDER_SCRIPTS"].split(","))


paths = Paths()
