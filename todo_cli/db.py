import sqlite3
import os
from typing import Optional, Literal
import sys


from .get_app_dir import getAppDirectory

sqllite_file = os.path.join(getAppDirectory(), "data.db")


def executeSQL(
    command: str,
    *args: Optional[str | int],
    fetchall: bool = False,
    fetchone: bool = False,
) -> Optional[list | tuple | None]:
    """
    Used to execute sqlite3 commands, I think this is better
    """
    try:
        with sqlite3.connect(sqllite_file) as conn:
            cursor = conn.cursor()

            cursor.execute(command, args)
            conn.commit()

            # so it won't get confused
            if fetchone and fetchall:
                return None

            elif fetchall:
                return cursor.fetchall()
            elif fetchone:
                return cursor.fetchone()

    except sqlite3.Error:
        # raised so I can catch it from outside
        raise


# This should run as soon as the program runs
executeSQL("""CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT UNIQUE,
        status TEXT
)""")


def addTask(
    task: str, status: Optional[str] = "todo"
) -> bool | Literal["duplicate"]:
    try:
        executeSQL(
            """
            INSERT INTO todos (task, status) VALUES (?, ?)
            """,
            task,
            status,
        )
        return True

    except sqlite3.IntegrityError:
        return "duplicate"

    except sqlite3.Error as e:
        print(f"An error occurred in sqlite3, error: {e}", file=sys.stderr)

def updateTask(task_id: int, task: str) -> bool | Literal["task_id not found"]:
    try:
        query = executeSQL(
            """
            SELECT * FROM todos WHERE id = ?
            """,
            task_id,
            fetchone=True,
        )

        if not query:
            return "task_id not found"

        executeSQL(
            """
                UPDATE todos SET task = ? WHERE id = ?
                """,
            task,
            task_id,
        )

        return True

    except sqlite3.Error as e:
        print(f"An error occurred in sqlite3, error: {e}", file=sys.stderr)

def getTasks(status: Optional[str] = None) -> list:
    try:
        if status:
            # get the specified task status if user provided one
            query = executeSQL(
                """
                SELECT * FROM todos WHERE status = ?
                """,
                status,
                fetchall=True,
            )
        else:
            query = executeSQL(
                """
                SELECT * FROM todos
                """,
                fetchall=True,
            )

        list_of_tasks = []

        for task_id, task_name, task_status in query:
            list_of_tasks.append([task_id, task_name, task_status])

        return list_of_tasks

    except sqlite3.Error as e:
        print(f"An error occurred in sqlite3, error: {e}", file=sys.stderr)

def deleteTask(task_id: int) -> bool | Literal["task_id is not found"]:
    try:
        query = executeSQL(
            """
            SELECT id FROM todos WHERE id = ?
            """,
            task_id,
            fetchone=True,
        )

        if not query:
            return "task_id is not found"

        executeSQL(
            """
            DELETE FROM todos WHERE id = ?
            """,
            task_id,
        )

        return True

    except sqlite3.Error as e:
        print(f"An error occurred in sqlite3, error: {e}", file=sys.stderr)

def markTask(
    task_id: int, status: Literal["todo", "in-progress", "done"]
) -> bool | Literal["task_id is not found"]:
    try:
        query = executeSQL(
            """
                SELECT id FROM todos WHERE id = ?
                """,
            task_id,
            fetchone=True,
        )

        if not query:
            return "task_id is not found"

        executeSQL(
            """
        UPDATE todos SET status = ? WHERE id = ?
        """,
            status,
            task_id,
        )

        return True

    except sqlite3.Error as e:
        print(f"An error occurred in sqlite3, error: {e}", file=sys.stderr)