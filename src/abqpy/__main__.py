import fire

from .cli import AbqpyCLI


def main():
    """The abqpy command line interface"""
    fire.Fire(AbqpyCLI)


if __name__ == "__main__":
    main()
