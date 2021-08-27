#!/usr/bin/env python3.9
"""The canonical program."""

import logging
import sys
from typing import List

from configure_log import configure_log
from parse_args import parse_args


def add_one(num: int) -> int:
    """Increment arg by one."""
    return num + 1


def greet(greetee: str) -> str:
    """A generic greeting."""
    return f"hello, {greetee}"


def main(argv: List[str]) -> None:
    """A function to provide scoping."""
    args = parse_args(argv)
    configure_log(args.logfile, args.debug)
    logging.debug(args)

    print(greet(args.greetee))
    sys.stderr.write(f"My favorite integer is {add_one(68)}\n")


if __name__ == "__main__":
    main(sys.argv[1:])
