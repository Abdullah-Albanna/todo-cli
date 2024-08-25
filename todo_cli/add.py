import sys
from .help_screen import showHelp
from .db import addTask

def add(args: str, compiled_mode: bool):
    try:
        task = args[2 - compiled_mode]
    
        adding_result = addTask(task)

        if adding_result:
            print("added {}".format(task))
            return
        
        elif adding_result == "duplicated":
            print("can't add duplicated tasks", file=sys.stderr)
            

    except IndexError:
        print("invalid add command, no task were provided", file=sys.stderr)
        showHelp()
        
