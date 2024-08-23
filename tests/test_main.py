"""
このファイルは、main.pyの機能をテストするためのpytestテストケースを含んでいます。
各テストケースは、ユーザー入力をモックし、TaskManagerクラスのメソッドが正しく呼び出されることを確認します。
"""

from unittest.mock import MagicMock, patch

import pytest

from src.main import main


@pytest.fixture
def mock_task_manager():
    with patch('src.main.TaskManager') as MockTaskManager:
        mock_instance = MockTaskManager.return_value
        yield mock_instance


def test_main_add_task(mock_task_manager):
    """
    ユーザーがタスクを追加するシナリオをテストします。
    ユーザー入力をモックし、タスクが正しく追加されることを確認します。
    """
    user_inputs = iter(["1", "Test Task", "4"])
    with patch('builtins.input', lambda _: next(user_inputs)):
        with patch('builtins.print'):
            main()
    mock_task_manager.add_task.assert_called_once_with("Test Task")


def test_main_display_tasks(mock_task_manager):
    """
    ユーザーがタスクを表示するシナリオをテストします。
    ユーザー入力をモックし、タスクが正しく表示されることを確認します。
    """
    user_inputs = iter(["2", "4"])
    with patch('builtins.input', lambda _: next(user_inputs)):
        with patch('builtins.print'):
            main()
    mock_task_manager.display_tasks.assert_called_once()


def test_main_delete_task(mock_task_manager):
    """
    ユーザーがタスクを削除するシナリオをテストします。
    ユーザー入力をモックし、タスクが正しく削除されることを確認します。
    """
    user_inputs = iter(["3", "1", "4"])
    mock_task_manager.display_tasks.return_value = None
    with patch('builtins.input', lambda _: next(user_inputs)):
        with patch('builtins.print'):
            main()
    mock_task_manager.delete_task.assert_called_once_with(1)


def test_main_invalid_choice(mock_task_manager):
    """
    無効な選択肢を入力した場合のシナリオをテストします。
    ユーザー入力をモックし、何も操作が行われないことを確認します。
    """
    user_inputs = iter(["invalid", "4"])
    with patch('builtins.input', lambda _: next(user_inputs)):
        with patch('builtins.print'):
            main()
    mock_task_manager.add_task.assert_not_called()
    mock_task_manager.display_tasks.assert_not_called()
    mock_task_manager.delete_task.assert_not_called()


def test_main_exit(mock_task_manager):
    """
    プログラムを終了するシナリオをテストします。
    ユーザー入力をモックし、終了メッセージが表示されることを確認します。
    """
    user_inputs = iter(["4"])
    with patch('builtins.input', lambda _: next(user_inputs)):
        with patch('builtins.print') as mock_print:
            main()
    mock_print.assert_any_call("タスクマネージャーを終了します。")
