import logging


def main(args):
    logging.debug(f"This is a debug log message: {args.verbose}")
    logging.info(f"This is an info log message: {args.verbose}")
