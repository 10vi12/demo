import json
import os

TODO_FILE = "tasks.json"

# Load existing tasks or create file
def load_tasks():
    if not os.path.exists(TODO_FILE):
        with open(TODO_FILE, "w") as f:
            json.dump([], f)
    with open(TODO_FILE, "r") as f:
        return json.load(f)

# Save tasks back to file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def strike(text):
    # Render a visual strikethrough by combining characters with U+0336
    return ''.join(ch + '\u0336' for ch in text)

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found! Add something :)")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "✔️" if task["done"] else "❌"
        name = strike(task["task"]) if task.get("done") else task["task"]
        print(f"{i}. {name} [{status}]")

def add_task(tasks):
    task_name = input("\nEnter task: ")
    tasks.append({"task": task_name, "done": False})
    save_tasks(tasks)
    print("Task added!")

def complete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("\nEnter task number to mark complete: "))
        tasks[num - 1]["done"] = True
        save_tasks(tasks)
        print("Marked as complete!")
    except:
        print("Invalid input!")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("\nEnter task number to delete: "))
        tasks.pop(num - 1)
        save_tasks(tasks)
        print("Task deleted!")
    except:
        print("Invalid input!")

def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

