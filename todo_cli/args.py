import sys

from .help_screen import showHelp
from .add import add
from .delete import delete
from .update import update
from .mark_tasks import mark
from .list_tasks import listTasks

def performCommand(args: str, compiled_mode: bool):
    command = args[1 - compiled_mode]

    match command:
        case 'add':
            add(args, compiled_mode)
        case 'update':
            update(args, compiled_mode)
        case 'delete':
            delete(args, compiled_mode)
        case 'mark':
            mark(args, compiled_mode)
        case 'list':
            listTasks(args, compiled_mode)
        case 'help':
            showHelp()



def checkArgs():
    args = sys.argv

    # nuitka mode is for if you compiled the program with nuitka, 
    # hince running nuitka's compiled  programs is one less args (the .py file)
    compiled_mode = 1

    if args[0].endswith(".py"):
        compiled_mode = 0

    if len(args) <= 1:
        # prints the help text if no command is provided
        showHelp()

    if any(
        command in args[1 - compiled_mode]
        for command in ["add", "update", "delete", "mark", "list", "help"]
    ):
        performCommand(args, compiled_mode)

    else:
        # not a recognize command
        print("invalid command", file=sys.stderr)
        showHelp()
