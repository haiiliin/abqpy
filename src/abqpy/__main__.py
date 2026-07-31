import sys

import fire

from .cli import AbqpyCLI
from .config import config


def main():
    """The abqpy command line interface."""
    sys.tracebacklimit = config.cli_traceback_limit
    fire.Fire(AbqpyCLI())


if __name__ == "__main__":
    main()
