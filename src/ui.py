class UI:
    def __init__(self):
        pass

    def show_menu(self):
        print("Welcome to the Task Manager!")
        print("1. Add a task")
        print("2. Display tasks")
        print("3. Delete a task")
        print("4. Exit")

    def get_user_choice(self):
        choice = input("Enter your choice: ")
        return choice

    def show_task_added(self):
        print("Task added successfully!")

    def show_task_deleted(self):
        print("Task deleted successfully!")

    def show_task_list(self, tasks):
        print("Task List:")
        for task in tasks:
            print(task)

    def show_invalid_choice(self):
        print("Invalid choice. Please try again.")

    def show_exit_message(self):
        print("Exiting Task Manager. Goodbye!")