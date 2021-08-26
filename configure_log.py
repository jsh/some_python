#!/usr/bin/env python3.9
"""Custom logging."""

import logging


def configure_log(logfile: str = None) -> None:
    """Simple logging."""

    if logfile:
        logging.basicConfig(filename=logfile, level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.DEBUG)
