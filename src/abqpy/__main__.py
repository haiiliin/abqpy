import os
import sys

import fire

from .cli import AbqpyCLI


def main():
    """The abqpy command line interface."""
    # Print to stdout, a workaround from https://github.com/google/python-fire/issues/188#issuecomment-1528976874
    fire.core.Display = lambda lines, out: out.write("\n".join(lines) + "\n")
    sys.tracebacklimit = int(os.environ.get("ABQPY_CLI_TRACEBACK_LIMIT", 0))
    fire.Fire(AbqpyCLI())


if __name__ == "__main__":
    main()
