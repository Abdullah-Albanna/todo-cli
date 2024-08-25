import sys
from .help_screen import showHelp
from .db import getTasks


def printTasks(status, tasks, no_status: bool = False):
    if no_status:
        # don't show the paranthsis that shows the status of the task if we're specifing the listing, e.g(todo-cli list done)
        message_format = [f"  {task[0]}: {task[1]}" for task in tasks]

    else:
        message_format = [f"  {task[0]}: {task[1]} ({task[2]})" for task in tasks]

    _tasks = "\n".join(message_format)

    # if the tasks of the specified listing is empty
    if len(tasks) < 1:
        _tasks = "  N/A"

    formatted_tasks = f"\n{status.title()}:\n\n{_tasks}"

    return formatted_tasks


def listTasks(args: str, compiled_mode: bool):
    try:
        # if only list if passed with no filtering, e.g(todo-cli list)
        if len(args) <= 2 - compiled_mode:
            tasks = getTasks()

            print(printTasks(status="All", tasks=tasks))

            return

        # if a single filtering is passed, e.g(todo-cli list done)
        elif len(args) <= 3 - compiled_mode:
            status: str = args[2 - compiled_mode]

            if status in ["todo", "in-progress", "done"]:
                tasks = getTasks(status)

                print(printTasks(status=status, tasks=tasks, no_status=True))

            else:
                print("\nInvalid status", file=sys.stderr)
                showHelp()
        
        # if more args are passed
        else:
            print("\nonly one status is allowed", file=sys.stderr)
            showHelp()

    except IndexError:
        print(
            "invalid list command",
            file=sys.stderr,
        )

        showHelp()
