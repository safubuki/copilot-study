from task import TaskManager


def main():
    task_manager = TaskManager()
    print("Welcome to the Task Manager!")

    while True:
        print("Menu:")
        print("1. Add a task")
        print("2. Display tasks")
        print("3. Delete a task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            task_manager.add_task(task)
            print("Task added successfully.")
        elif choice == "2":
            task_manager.display_tasks()
            print("Tasks displayed successfully.")
        elif choice == "3":
            try:
                task_number = int(input("Enter the task number to delete: "))
                task_manager.delete_task(task_number)
                print("Task deleted successfully.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "4":
            print("Exiting the Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

    print("Thank you for using the Task Manager!")


if __name__ == "__main__":
    main()
