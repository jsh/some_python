#!/usr/bin/env python3
"""Test configure_log module."""

import logging

from configure_log import configure_log


def test_no_args(caplog) -> None:
    """Output of main()."""
    configure_log()
    caplog.set_level(logging.DEBUG)
    logging.debug("This is a debug message.")
    assert "This is a debug message." in caplog.text


def test_with_args(caplog) -> None:
    """Output of main()."""
    configure_log("wherever")
    caplog.set_level(logging.DEBUG)
    logging.debug("This is another debug message.")
    assert "This is another debug message." in caplog.text
    # pytest doesn't actually write this to a file,
    # but does recognize the coverage increase.
    # TODO: Is there a way to test the 'write it to a file' piece?
