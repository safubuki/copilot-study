"""
このファイルはタスクを外部ファイルに保存および読み込むためのTaskStorageクラスを提供します。
"""
import json


class TaskStorage:
    """
    タスクを外部ファイルに保存および読み込むクラス。
    """

    def __init__(self, filename='tasks.json'):
        """
        TaskStorageのコンストラクタ。ファイル名を設定します。

        Args:
            filename (str): タスクを保存するファイルの名前。デフォルトは'tasks.json'。

        Returns:
            なし
        """
        self.filename = filename

    def save_tasks(self, tasks):
        """
        タスクリストをファイルに保存します。

        Args:
            tasks (list): 保存するタスクリスト

        Returns:
            なし
        """
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(tasks, file, ensure_ascii=False)

    def load_tasks(self):
        """
        ファイルからタスクリストを読み込みます。

        Args:
            なし

        Returns:
            list: 読み込んだタスクリスト。ファイルが存在しない場合は空のリストを返します。
        """
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                tasks = json.load(file)
                return tasks
        except FileNotFoundError:
            return []
