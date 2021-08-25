#!/usr/bin/env python3.9
"""Custom logging."""

import logging


def setup_logging(logfile: str) -> None:
    """Simple logging."""

    if logfile:
        logging.basicConfig(filename=logfile, level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.DEBUG)
