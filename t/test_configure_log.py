#!/usr/bin/env python3
"""Test configure_log module."""

import logging

from configure_log import configure_log


def test_info_logging(caplog) -> None:
    """logging.INFO emits logging.info()."""
    configure_log(logfile="wherever")
    caplog.set_level(logging.INFO)
    logging.debug("This is another debug message.")
    logging.info("this is another info message.")
    assert "This is another debug message." not in caplog.text
    assert "this is another info message." in caplog.text
    # pytest doesn't actually write this to the named file,
    # but does recognize the coverage increase.
    # TODO: Is there a way to test the 'write it to a file' piece?


def test_debug_logging(caplog) -> None:
    """logging.DEBUG emits logging.debug() and logging.info()."""
    configure_log(debug=True)
    caplog.set_level(logging.DEBUG)
    logging.debug("This is a debug message.")
    assert "This is a debug message." in caplog.text
    logging.info("this is an info message.")
    assert "this is an info message." in caplog.text
