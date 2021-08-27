#!/usr/bin/env python3.9
"""Custom logging."""

import logging


def configure_log(logfile: str = None, debug: bool = False) -> None:
    """Simple logging."""

    if debug:
        logging.basicConfig(level=logging.DEBUG)

    if logfile:
        logging.basicConfig(filename=logfile, level=logging.DEBUG)
