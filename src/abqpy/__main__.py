import sys

import fire

from .cli import abaqus
from .config import config


def main():
    """The abqpy command line interface."""
    sys.tracebacklimit = config.cli_traceback_limit
    fire.Fire(abaqus)


if __name__ == "__main__":
    main()
