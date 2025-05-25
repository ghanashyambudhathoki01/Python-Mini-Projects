tasks = []

def user():
    print("Welcome to the TO-DO-List Of Ghanashyam\n")

    name = input("Please Enter Your Name Here: ")

    while True:
        print(f"\nWhat would you like to do, {name}?")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. View pending tasks")
        print("4. View completed tasks")
        print("5. Mark task as completed")
        print("6. Remove a task")
        print("7. Quit")

        try:
            choice = int(input("Enter your selection (1-7): "))
        except ValueError:
            print("Please enter a valid number between 1 and 7.")
            continue

        if choice == 1:
            task_name = input("Enter your task : ")
            due_date = input("Enter due date (e.g., 2025-06-01): ")
            task = {"name": task_name, "due": due_date, "status": "Pending"}
            tasks.append(task)
            print("Your task has been added successfully!")

        elif choice == 2:
            print("\nAll Tasks:")
            if tasks:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task['name']} | Due: {task['due']} | Status: {task['status']}")
            else:
                print("No tasks to show.")

        elif choice == 3:
            print("\nPending Tasks:")
            pending = [task for task in tasks if task['status'] == "Pending"]
            if pending:
                for i, task in enumerate(pending, 1):
                    print(f"{i}. {task['name']} | Due: {task['due']}")
            else:
                print("No pending tasks.")

        elif choice == 4:
            print("\nCompleted Tasks:")
            completed = [task for task in tasks if task['status'] == "Completed"]
            if completed:
                for i, task in enumerate(completed, 1):
                    print(f"{i}. {task['name']} | Completed")
            else:
                print("No completed tasks.")

        elif choice == 5:
            if tasks:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task['name']} | Status: {task['status']}")
                try:
                    mark_index = int(input("Enter the task number to mark as completed: "))
                    if 1 <= mark_index <= len(tasks):
                        tasks[mark_index - 1]['status'] = "Completed"
                        print("Task marked as completed.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No tasks available.")

        elif choice == 6:
            if tasks:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task['name']}")
                try:
                    remove_index = int(input("Enter the task number you wish to remove: "))
                    if 1 <= remove_index <= len(tasks):
                        removed = tasks.pop(remove_index - 1)
                        print(f"Removed Task: {removed['name']}")
                    else:
                        print("Invalid Task Number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No tasks to remove.")

        elif choice == 7:
            print(f"See you, {name}!")
            break

        else:
            print("Invalid choice. Please select from 1 to 7.")

user()
