#!/usr/bin/env python

"""Automates loading of all fixtures."""

__author__ = "seyLu"
__github__ = "github.com/seyLu"

__licence__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "seyLu"
__status__ = "Prototype"

import os
import subprocess

SCRIPTS_PATH: str = "scripts"
MODELS_IN_ORDER: list = [
    "regions",
    "users",
]


def main():
    for model in MODELS_IN_ORDER:
        subprocess.call(
            [
                "python",
                os.path.join("scripts", f"loaddata_{model}.py"),
            ]
        )


if __name__ == "__main__":
    main()
