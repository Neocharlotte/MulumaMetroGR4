# Task list initialization
tasks = []

# Display the menu options
def show_menu():
    print("\n====== TO-DO LIST MENU ======")
    print("1. Add a task")
    print("2. List tasks")
    print("3. Mark task as completed")
    print("4. Exit")

# Add a task to the list
def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added.")
    else:
        print("No task entered. Try again.")

# Display all tasks in the list
def list_tasks(tasks):
    if not tasks:
        print("No tasks.")
    else:
        print("\nCurrent Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

# Mark a task as completed (removes it)
def complete_task(tasks):
    list_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter task number to mark as completed: "))
        if 1 <= index <= len(tasks):
            completed = tasks.pop(index - 1)
            print(f"Task '{completed}' completed and removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program loop
def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            list_tasks(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            print("Goodbye! All tasks cleared from memory.")
            break
        else:
            print("Invalid choice. Please choose from 1 to 4.")

# Run the program
if __name__ == "__main__":
    main()
