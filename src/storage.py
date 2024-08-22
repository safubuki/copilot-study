import json

def save_tasks(tasks, filename):
    with open(filename, 'w') as file:
        json.dump(tasks, file)

def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            tasks = json.load(file)
            return tasks
    except FileNotFoundError:
        return []