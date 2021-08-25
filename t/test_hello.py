#!/usr/bin/env python3
"""Test hello executable."""

from hello import add_one, greet, main


def test_main(capsys) -> None:
    """Output of main()."""
    main(["--greetee=everybody"])
    captured = capsys.readouterr()
    assert captured.out == "hello, everybody\n"
    assert captured.err == "My favorite integer is 69\n"


def test_greet() -> None:
    """Output of greet()."""
    assert greet("there") == "hello, there"


def test_add_one() -> None:
    """Output of add_one()."""
    assert add_one(1) == 2
