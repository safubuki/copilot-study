class Task:
    def __init__(self, description):
        self.description = description

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def display_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks found.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task.description}")

    def delete_task(self, index):
        if index < 1 or index > len(self.tasks):
            print("Invalid task index.")
        else:
            del self.tasks[index - 1]
            print("Task deleted.")

# Example usage
task_manager = TaskManager()
task_manager.add_task("Task 1")
task_manager.add_task("Task 2")
task_manager.display_tasks()
task_manager.delete_task(1)
task_manager.display_tasks()