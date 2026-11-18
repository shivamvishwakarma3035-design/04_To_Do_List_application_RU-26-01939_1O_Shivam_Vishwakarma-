# To-Do List Application

tasks = []



def load_tasks():

    try:
        with open("todo.txt", "r") as file:

            for line in file:
                line = line.strip()

                if line:
                    title, status = line.split("|", 1)

                    tasks.append({
                        "title": title,
                        "status": status
                    })

    except FileNotFoundError:
        pass


def save_tasks():

    with open("todo.txt", "w") as file:

        for task in tasks:
            file.write(
                task["title"] + "|" +
                task["status"] + "\n"
            )


def add_task():

    title = input("Enter task: ").strip()

    if title == "":
        print("Task cannot be empty!")
        return

    tasks.append({
        "title": title,
        "status": "Pending"
    })

    save_tasks()

    print("Task added successfully!")


def view_tasks():

    if len(tasks) == 0:
        print("No tasks found. Your to-do list is empty.")
        return

    print("\n===== YOUR TASKS =====")

    for i, task in enumerate(tasks, start=1):

        print(
            i, "|",
            task["title"], "|",
            task["status"]
        )


def complete_task():

    view_tasks()

    if len(tasks) == 0:
        return

    try:
        number = int(input("Enter task number: "))

        if number < 1 or number > len(tasks):
            print("Task number not found.")
            return

        tasks[number - 1]["status"] = "Done"

        save_tasks()

        print("Task marked as completed!")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():

    view_tasks()

    if len(tasks) == 0:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if number < 1 or number > len(tasks):
            print("Task number not found.")
            return

        tasks.pop(number - 1)

        save_tasks()

        print("Task deleted successfully!")

    except ValueError:
        print("Please enter a valid number.")

def main():

    load_tasks()

    while True:

        print("\n===== TO-DO LIST APPLICATION =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            print("Thank you for using To-Do List!")
            break

        else:
            print("Invalid choice! Please select 1 to 5.")


if __name__ == "__main__":
    main()