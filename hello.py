#!/usr/bin/env python3.9
"""The canonical program."""

import sys


def add_one(num: int) -> int:
    """Increment arg by one."""
    return num + 1


def greet(greetee: str) -> str:
    """A generic greeting."""
    return f"hello, {greetee}"


def main() -> None:
    """A function to provide scoping."""
    world = "world"
    print(greet(world))
    sys.stderr.write(f"My favorite integer is {add_one(68)}\n")


if __name__ == "__main__":
    main()
