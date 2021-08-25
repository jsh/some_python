#!/usr/bin/env python3
"""Test parse_args module."""

from parse_args import parse_args


def test_no_args() -> None:
    """No args."""
    params = parse_args([])
    assert params.greetee == "world"
    assert params.logfile is None


def test_greetee_short() -> None:
    """Test greetee parsing."""
    params = parse_args(["-gPaul"])  # short form
    assert params.greetee == "Paul"


def test_greetee_long() -> None:
    """Test greetee parsing."""
    params = parse_args(["--greetee=Jeff"])  # long form
    assert params.greetee == "Jeff"


def test_logfile_short() -> None:
    """Test logfile parsing."""
    params = parse_args(["-lshortname.log"])  # short form
    assert params.logfile == "shortname.log"


def test_longfile_long() -> None:
    """Test logfile parsing."""
    params = parse_args(["--logfile=longname.log"])  # long form
    assert params.logfile == "longname.log"


def test_badarg() -> None:
    """Test handling bad arg."""
    # TODO: pass a bad arg and handle it.


def test_help() -> None:
    """Test handling help."""
    # TODO: handle "--help".
