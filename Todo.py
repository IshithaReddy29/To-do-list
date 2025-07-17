todo_list = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("Your to-do list is empty!")
    else:
        for index, task in enumerate(todo_list):
            status = "✅" if task['done'] else "❌"
            print(f"{index + 1}. {task['task']} [{status}]")

def add_task():
    task = input("Enter your task: ")
    todo_list.append({"task": task, "done": False})
    print("Task added!")

def mark_done():
    view_tasks()
    try:
        num = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= num < len(todo_list):
            todo_list[num]['done'] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to delete: ")) - 1
        if 0 <= num < len(todo_list):
            deleted = todo_list.pop(num)
            print(f"Deleted task: {deleted['task']}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

# ✅ This is the loop that must be present!
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")

