#!/usr/local/env python3.9
"""Parse arguments."""

import argparse
from typing import List


def parse_args(argv: List[str]) -> argparse.Namespace:
    """Get the params

    Return a Namespace with these attributes
      - debug: debugging? True or False
      - greetee: who to greet. Okay. Fine. "whom"
      - logfile: where to log
    """

    parser = argparse.ArgumentParser(description="Be friendly. Say hello.")
    parser.add_argument("-d", "--debug", help="Turn on debugging", action="store_true")
    parser.add_argument(
        "-g", "--greetee", help="Who we're greeting [default=world]", default="world"
    )
    parser.add_argument(
        "-l",
        "--logfile",
        help="Where to log [default=/var/log/hello/<date>.log]",
        default=None,
    )

    params = parser.parse_args(argv)

    return params
