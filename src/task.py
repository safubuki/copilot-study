from storage import TaskStorage


class TaskManager:

    def __init__(self, filename='tasks.json'):
        self.storage = TaskStorage(filename)
        self.tasks = self.storage.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        self.storage.save_tasks(self.tasks)
        print(f"Task '{task}' added.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def delete_task(self, task_number):
        if task_number > 0 and task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            self.storage.save_tasks(self.tasks)
            print(f"Task '{removed_task}' deleted.")
        else:
            print("Invalid task number.")
