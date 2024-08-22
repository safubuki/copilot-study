# main.py

def main():
    # Program initialization
    print("Welcome to the Task Manager!")
    
    # Program execution
    while True:
        # Display menu options
        print("Menu:")
        print("1. Add a task")
        print("2. Display tasks")
        print("3. Delete a task")
        print("4. Exit")
        
        # Get user input
        choice = input("Enter your choice: ")
        
        # Process user input
        if choice == "1":
            # Add a task
            pass
        elif choice == "2":
            # Display tasks
            pass
        elif choice == "3":
            # Delete a task
            pass
        elif choice == "4":
            # Exit the program
            break
        else:
            print("Invalid choice. Please try again.")
    
    # Program termination
    print("Thank you for using the Task Manager!")

if __name__ == "__main__":
    main()