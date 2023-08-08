import logging
import os
import subprocess
from logging.config import fileConfig

LOADDATA_COMMAND: list = [
    "python",
    "manage.py",
    "loaddata",
]
FIXTURE_PATH: str = "fixtures"

fileConfig("logging.ini")


def loaddata(fixtures: list[str], ext: str = "yaml") -> None:
    """Loads all fixtures in order."""

    for fixture in fixtures:
        fixture = f"{fixture}.{ext}"
        logging.info(f"Loading fixture {fixture}.")

        subprocess.call([*LOADDATA_COMMAND, os.path.join(FIXTURE_PATH, fixture)])
