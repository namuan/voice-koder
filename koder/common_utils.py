import logging
import random
import string
import subprocess
import uuid
from functools import wraps
from time import time

from rich.logging import RichHandler


def setup_logging(verbosity):
    logging_level = logging.WARNING
    if verbosity == 1:
        logging_level = logging.INFO
    elif verbosity >= 2:
        logging_level = logging.DEBUG

    logging.basicConfig(
        handlers=[
            RichHandler(rich_tracebacks=True),
        ],
        format="%(asctime)s - %(filename)s:%(lineno)d - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging_level,
    )
    logging.captureWarnings(capture=True)


def random_string(length):
    return "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


def run_command(command: str) -> str:
    logging.info("⚡ %s", command)
    return subprocess.check_output(command, shell=True).decode("utf-8")  # nosemgrep


def uuid_gen():
    return uuid.uuid4()


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        time_taken_seconds = te - ts
        alert_level = "✅"
        if time_taken_seconds > 3:
            alert_level = "🚨"
        logging.debug(f"{alert_level} - Time spent in {f.__name__}: {te - ts:.2f} seconds")
        return result

    return wrap
