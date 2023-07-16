#!/usr/bin/env python

"""Automates loading of Fixtures."""

__author__ = "seyLu"
__github__ = "github.com/seyLu"

__licence__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "seyLu"
__status__ = "Prototype"

import os
import subprocess

FIXTURE_PATH = "fixtures/"

LOADDATA_COMMAND = [
    "python",
    "manage.py",
    "loaddata",
]


def main():
    loaddata("region")
    loaddata("province")
    loaddata("city")
    loaddata("district")


def loaddata(fixture: str) -> None:
    """Loads fixture."""

    subprocess.call([*LOADDATA_COMMAND, os.path.join(FIXTURE_PATH, f"{fixture}.json")])


if __name__ == "__main__":
    main()
