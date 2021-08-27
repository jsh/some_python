#!/usr/bin/env python3.9
"""Custom logging."""

import logging
import sys
from datetime import date
from pathlib import Path


def configure_log(logfile: str = None, debug: bool = False) -> None:
    """Simple logging."""

    logdir = Path("/var/log") / Path(sys.argv[0]).stem

    if logfile:
        logpath = Path(logfile)
    else:
        logpath = logdir / str(date.today())

    logpath = logpath.with_suffix(".log")

    if debug:
        logging.basicConfig(level=logging.DEBUG)

    logging.basicConfig(filename=logpath, level=logging.INFO)

    logging.debug("logdir: %s, logfile: %s, logpath: %s", logdir, logfile, logpath)
