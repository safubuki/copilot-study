"""
このファイルはタスクマネージャーのメインエントリーポイントを提供します。
ユーザーにメニューを表示し、選択に応じてタスクを追加、表示、削除します。
"""
from task import TaskManager


def main():
    """
    タスクマネージャーのメインエントリーポイント。
    ユーザーにメニューを表示し、選択に応じてタスクを追加、表示、削除します。

    Args:
        なし

    Returns:
        なし
    """
    task_manager = TaskManager()
    print("タスクマネージャーへようこそ！")

    while True:
        # メニューを表示
        print("** メニュー:")
        print("1. タスクを追加")
        print("2. タスクを表示")
        print("3. タスクを削除")
        print("4. 終了")

        # ユーザーの選択を取得
        choice = input("選択肢を入力してください: ")
        print("-----")

        if choice == "1":
            # タスクを追加
            print("** タスクを追加:")
            task = input("タスクを入力してください: ")
            task_manager.add_task(task)
            print("タスクを追加しました。")
            print("-----")
        elif choice == "2":
            # タスクを表示
            print("** タスクを表示:")
            task_manager.display_tasks()
            print("-----")
        elif choice == "3":
            # タスクを削除
            print("** タスクを削除:")

            # 現在のタスクリストを表示
            task_manager.display_tasks()

            try:
                task_number = int(input("削除するタスクの番号を入力してください: "))
                task_manager.delete_task(task_number)
                print("タスクを削除しました。")
                print("-----")
            except ValueError:
                # 無効な入力の場合のエラーメッセージ
                print("無効な入力です。")
                print("-----")
        elif choice == "4":
            # プログラムを終了
            print("タスクマネージャーを終了します。")
            print("-----")
            break
        else:
            # 無効な選択肢
            print("無効な選択肢です。もう一度お試しください。")
            print("-----")

    # 終了メッセージ
    print("タスクマネージャーのご利用ありがとうございます！")


if __name__ == "__main__":
    main()
