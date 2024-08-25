import sys
from .help_screen import showHelp


def delete(args: str, compiled_mode: bool):
    try:
        task = args[2 - compiled_mode]

        print("deleting {}".format(task))

    except IndexError:
        print("invalid delete command, no id were provided", file=sys.stderr)
        showHelp()
