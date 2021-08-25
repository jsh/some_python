#!/usr/local/env python3.9
"""Module docstring."""  # TODO: Remove boilerplate.

import argparse
from typing import List


def parse_args(argv: List[str]) -> argparse.Namespace:
    """Get the params

    Return a Namespace with these attributes
      - greetee: who to greet. Okay. Fine. "whom"
    """
    # TODO: add more argument parsing

    parser = argparse.ArgumentParser(description="Be friendly. Say hello.")
    parser.add_argument(
        "-g", "--greetee", help="Who we're greeting [default=world]", default="world"
    )
    parser.add_argument(
        "-l", "--logfile", help="Where to log [default=world]", default=None
    )

    params = parser.parse_args(argv)

    return params