#!/usr/bin/env python

"""Automates loading of Fixtures."""

__author__ = "seyLu"
__github__ = "github.com/seyLu"

__licence__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "seyLu"
__status__ = "Prototype"

import logging
import os
import subprocess
from logging.config import fileConfig

FIXTURE_PATH = "fixtures/"

LOADDATA_COMMAND = [
    "python",
    "manage.py",
    "loaddata",
]


def main():
    loaddata(["region", "province", "city", "district"])


def loaddata(fixtures: str) -> None:
    """Loads all fixtures in order."""

    for fixture in fixtures:
        fixture = f"{fixture}.json"
        logging.info(f"Loading fixture {fixture}.")

        subprocess.call([*LOADDATA_COMMAND, os.path.join(FIXTURE_PATH, fixture)])


if __name__ == "__main__":
    fileConfig("logging.ini")
    main()
