"""
このファイルはタスクの追加、表示、削除を管理するTaskManagerクラスを提供します。
"""
from typing import List

from storage import TaskStorage


class TaskManager:
    """
    タスクの追加、表示、削除を管理するクラス。
    """

    def __init__(self, filename: str = 'tasks.json') -> None:
        """
        TaskManagerのコンストラクタ。タスクリストを初期化し、ストレージからタスクを読み込みます。

        Args:
            filename (str): タスクを保存するファイルの名前。デフォルトは'tasks.json'。

        Returns:
            なし
        """
        # ストレージオブジェクトを初期化
        self.storage = TaskStorage(filename)
        # ストレージからタスクリストを読み込み
        self.tasks: List[str] = self.storage.load_tasks()

    def add_task(self, task: str) -> None:
        """
        タスクを追加します。

        Args:
            task (str): 追加するタスクの内容

        Returns:
            なし
        """
        # タスクリストに新しいタスクを追加
        self.tasks.append(task)
        # 更新されたタスクリストをストレージに保存
        self.storage.save_tasks(self.tasks)
        print(f"Task '{task}' added.")

    def display_tasks(self) -> None:
        """
        現在のタスクリストを表示します。

        Args:
            なし

        Returns:
            なし
        """
        # タスクリストが空の場合の処理
        if not self.tasks:
            print("No tasks available.")
        else:
            # タスクリストを表示
            print("Tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def delete_task(self, task_number: int) -> None:
        """
        指定された番号のタスクを削除します。

        Args:
            task_number (int): 削除するタスクの番号

        Returns:
            なし
        """
        # 有効なタスク番号かどうかを確認
        if task_number > 0 and task_number <= len(self.tasks):
            # 指定されたタスクを削除
            removed_task = self.tasks.pop(task_number - 1)
            # 更新されたタスクリストをストレージに保存
            self.storage.save_tasks(self.tasks)
            print(f"Task '{removed_task}' deleted.")
        else:
            print("Invalid task number.")
