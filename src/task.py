"""
このファイルはタスクの追加、表示、削除を管理するTaskManagerクラスを提供します。
"""
from storage import TaskStorage


class TaskManager:
    """
    タスクの追加、表示、削除を管理するクラス。
    """

    def __init__(self, filename='tasks.json'):
        """
        TaskManagerのコンストラクタ。タスクリストを初期化し、ストレージからタスクを読み込みます。

        Args:
            filename (str): タスクを保存するファイルの名前。デフォルトは'tasks.json'。

        Returns:
            なし
        """
        self.storage = TaskStorage(filename)
        self.tasks = self.storage.load_tasks()

    def add_task(self, task):
        """
        タスクを追加します。

        Args:
            task (str): 追加するタスクの内容

        Returns:
            なし
        """
        self.tasks.append(task)
        self.storage.save_tasks(self.tasks)
        print(f"Task '{task}' added.")

    def display_tasks(self):
        """
        現在のタスクリストを表示します。

        Args:
            なし

        Returns:
            なし
        """
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def delete_task(self, task_number):
        """
        指定された番号のタスクを削除します。

        Args:
            task_number (int): 削除するタスクの番号

        Returns:
            なし
        """
        if task_number > 0 and task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            self.storage.save_tasks(self.tasks)
            print(f"Task '{removed_task}' deleted.")
        else:
            print("Invalid task number.")
