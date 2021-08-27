#!/usr/bin/env python3
"""
A stub to illustrate logging.
"""

import sys

import pytest


def test_success() -> None:
    """Succeed."""
    assert True


def test_failure() -> None:
    """Fail."""
    assert not False


def test_except() -> None:
    """Catch an exception."""
    with pytest.raises(AssertionError):
        assert False


def test_myoutput(capsys):  # or use "capfd" for fd-level
    """Illustrate capsys."""
    print("hello")
    sys.stderr.write("world\n")
    captured = capsys.readouterr()
    assert captured.out == "hello\n"
    assert captured.err == "world\n"
    print("next")
    print("second line")
    captured = capsys.readouterr()
    assert captured.out == "next\nsecond line\n"
