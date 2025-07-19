import json
import os

FILENAME = "todo_data.json"

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file)

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {task['title']} [{status}]")

def add_task(tasks):
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})

def mark_done(tasks):
    show_tasks(tasks)
    idx = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= idx < len(tasks):
        tasks[idx]["done"] = True

def delete_task(tasks):
    show_tasks(tasks)
    idx = int(input("Enter task number to delete: ")) - 1
    if 0 <= idx < len(tasks):
        tasks.pop(idx)

def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List ---")
        print("1. View Tasks\n2. Add Task\n3. Mark Done\n4. Delete Task\n5. Exit")
        choice = input("Choose: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
