import json


class TaskStorage:

    def __init__(self, filename='tasks.json'):
        self.filename = filename

    def save_tasks(self, tasks):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(tasks, file, ensure_ascii=False)

    def load_tasks(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                tasks = json.load(file)
                return tasks
        except FileNotFoundError:
            return []
