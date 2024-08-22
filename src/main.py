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
    print("Welcome to the Task Manager!")

    while True:
        print("** Menu:")
        print("1. Add a task")
        print("2. Display tasks")
        print("3. Delete a task")
        print("4. Exit")

        choice = input("Enter your choice: ")
        print("-----")

        if choice == "1":
            print("** Add a task:")
            task = input("Enter the task: ")
            task_manager.add_task(task)
            print("Task added successfully.")
            print("-----")
        elif choice == "2":
            print("** Display tasks:")
            task_manager.display_tasks()
            print("Tasks displayed successfully.")
            print("-----")
        elif choice == "3":
            print("** Delete task:")
            try:
                task_number = int(input("Enter the task number to delete: "))
                task_manager.delete_task(task_number)
                print("Task deleted successfully.")
                print("-----")
            except ValueError:
                print("Invalid input. Please enter a number.")
                print("-----")
        elif choice == "4":
            print("Exiting the Task Manager. Goodbye!")
            print("-----")
            break
        else:
            print("Invalid choice. Please try again.")
            print("-----")

    print("Thank you for using the Task Manager!")


if __name__ == "__main__":
    main()
