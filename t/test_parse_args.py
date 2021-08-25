#!/usr/bin/env python3
"""Test parse_args module."""

from parse_args import parse_args


def test_no_args(capsys) -> None:
    """No args."""
    params = parse_args([])
    assert params.greetee == "world"
    captured = capsys.readouterr()
    assert captured.out == "hello, world\n"
    assert captured.err == "My favorite integer is 69\n"


def test_greetee_short(capsys) -> None:
    """Test argument parsing."""
    params = parse_args(["-gPaul"])  # short form
    assert params.greetee == "Paul"
    captured = capsys.readouterr()
    assert captured.out == "hello, Paul\n"
    assert captured.err == "My favorite integer is 69\n"


def test_greetee_long(capsys) -> None:
    """Test argument parsing."""
    params = parse_args(["--greetee=Jeff"])  # long form
    assert params.greetee == "Jeff"
    captured = capsys.readouterr()
    assert captured.out == "hello, Jeff\n"
    assert captured.err == "My favorite integer is 69\n"


def test_badarg() -> None:
    """Test handling bad arg."""
    # TODO: pass a bad arg and handle it.


def test_help() -> None:
    """Test handling help."""
    # TODO: handle "--help".
