import sys
from .help_screen import showHelp


def update(args: str, compiled_mode: bool):
    try:
        _id = args[2 - compiled_mode]
        task: str = args[3 - compiled_mode]

        if isinstance(_id, int):
            print("updating {} {}".format(_id, task))
        else:
            print("invalid id")
            showHelp()

    except IndexError:
        missing_args = []

        if len(args) <= 2 - compiled_mode:
            missing_args.append("id")
        if len(args) <= 3 - compiled_mode:
            missing_args.append("task")

        print(
            "invalid update command, no {} were provided".format(
                " and ".join(missing_args)
            ),
            file=sys.stderr,
        )
        showHelp()
