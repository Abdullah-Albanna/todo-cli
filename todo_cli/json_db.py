import json
import os

from .get_app_dir import getAppDirectory

# Path to the JSON file
JSON_FILE_PATH = os.path.join(getAppDirectory(), "data.json")


def loadJSON():
    """Load the JSON file and return the data."""
    if os.path.exists(JSON_FILE_PATH):
        with open(JSON_FILE_PATH, "r") as file:
            return json.load(file)
    return {}


def saveJSON(data):
    """Save the data to the JSON file."""
    with open(JSON_FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)


def addTask(task_id, task_info):
    """Add a new task to the JSON file."""
    data = loadJSON()
    if "tasks" not in data:
        data["tasks"] = {}

    data["tasks"][task_id] = task_info
    saveJSON(data)


def updateTask(task_id, task_info):
    """Update an existing task in the JSON file."""
    data = loadJSON()
    if "tasks" in data and task_id in data["tasks"]:
        data["tasks"][task_id].update(task_info)
        saveJSON(data)
    else:
        print(f"Task with ID '{task_id}' does not exist.")


def deleteTask(task_id):
    """Delete a task from the JSON file."""
    data = loadJSON()
    if "tasks" in data and task_id in data["tasks"]:
        del data["tasks"][task_id]
        saveJSON(data)
    else:
        print(f"Task with ID '{task_id}' does not exist.")


def getTask(task_id):
    """Retrieve a task by ID from the JSON file."""
    data = loadJSON()
    return data.get("tasks", {}).get(task_id, None)


def listTasks():
    """List all tasks from the JSON file."""
    data = loadJSON()
    return data.get("tasks", {})


# Example Usage
if __name__ == "__main__":
    # Add tasks
    addTask("1", {"name": "Buy milk", "status": "todo"})
    addTask("2", {"name": "Write code", "status": "in-progress"})

    # Update a task
    updateTask("1", {"status": "done"})

    # List all tasks
    tasks = listTasks()
    print("All tasks:", tasks)

    # Get a specific task
    task = getTask("1")
    print("Task 1:", task)

    # Delete a task
    deleteTask("2")
    print("Remaining tasks after deletion:", listTasks())
