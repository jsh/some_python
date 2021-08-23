#!/usr/bin/env python3
"""Test hello executable."""

from hello import main


def test_main(capsys):
    """Test output of main()."""
    main()
    captured = capsys.readouterr()
    assert captured.out == "hello, world\n"
