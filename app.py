#!/usr/bin/env python3
"""
Control IntellJ IDEA with voice commands

Usage:
./app.py -h

Run with -v for verbose logging
./app.py -vv
"""

from argparse import ArgumentParser, RawDescriptionHelpFormatter

from koder import sr_wrapper
from koder.common_utils import setup_logging


def parse_args():
    parser = ArgumentParser(description=__doc__, formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        dest="verbose",
        help="Increase verbosity of logging output",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    setup_logging(args.verbose)
    sr_wrapper.main(args)
