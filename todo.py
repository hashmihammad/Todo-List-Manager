FILENAME = "tasks.txt"

def load_tasks():
    tasks = []
    file = open(FILENAME, "a+")
    file.seek(0)
    for line in file:
        line = line.strip()
        if line:
            tasks.append(line)
    file.close()
    return tasks

def save_tasks(tasks):
    file = open(FILENAME, "w")
    for task in tasks:
        file.write(task + "\n")
    file.close()

def show_menu():
    print("\n===== To-Do List Manager =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("\n--- Your Tasks ---")
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")

def add_task(tasks):
    task = input("Enter the new task: ")
    if task.strip() != "":
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task '{task}' added successfully.")
    else:
        print("Task cannot be empty.")

def delete_task(tasks):
    view_tasks(tasks)
    if len(tasks) == 0:
        return

    number = input("Enter task number to delete: ")
    if number.isdigit():
        number = int(number)
        if number >= 1 and number <= len(tasks):
            removed = tasks.pop(number - 1)
            save_tasks(tasks)
            print(f"Task '{removed}' deleted.")
        else:
            print("Invalid task number.")
    else:
        print("Please enter a valid number.")

tasks = load_tasks()

while True:
    show_menu()
    choice = input("What would you like to do (1-4): ")

    if choice == "1":
        view_tasks(tasks)
    elif choice == "2":
        add_task(tasks)
    elif choice == "3":
        delete_task(tasks)
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
