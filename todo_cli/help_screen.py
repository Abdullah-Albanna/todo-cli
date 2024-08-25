from textwrap import dedent
import sys

def showHelp():
    # dedent helps removing the spacing if triple quotation is used
    print(
        dedent("""
    Usage:
               
      todo-cli add <task>                           - Adds a new task
      todo-cli update <id> <task>                   - Updates an existing task
      todo-cli delete <id>                          - Deletes a task with the provided id
      todo-cli mark <id> <status>                   - Marks a task as (in-progress, done) with the provided id
      todo-cli list                                 - Lists all tasks
      todo-cli list <status>                        - Lists specified tasks (todo, in-progress, done)
      todo-cli help                                 - Shows this help screen
""")
    )

    sys.exit(0)