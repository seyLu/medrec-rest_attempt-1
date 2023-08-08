#!/usr/bin/env python

"""Automates loading of users fixture."""

__author__ = "seyLu"
__github__ = "github.com/seyLu"

__licence__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "seyLu"
__status__ = "Prototype"

from lib.loaddata import loaddata


def main():
    loaddata(["User"])


if __name__ == "__main__":
    main()
