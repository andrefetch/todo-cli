from functions.greet import ask_questions

TODO_FILE = "files/todo.txt"


def specifics():
    choice = ask_questions()

    if choice == 1:
        task = input("Input the task you want to add.\nInput: ")
        with open(TODO_FILE, "a") as f:
            f.write(task + "\n")
        print(f"Added: {task}")

    elif choice == 2:
        with open(TODO_FILE, "r") as f:
            tasks = [line.rstrip("\n") for line in f]
        if not tasks:
            print("Your to-do list is empty.")
        else:
            print("All items in the to-do list:")
            for i, task in enumerate(tasks):
                print(f"  {i}. {task}")

    elif choice == 3:
        with open(TODO_FILE, "r") as f:
            tasks = [line.rstrip("\n") for line in f]
        if not tasks:
            print("Your to-do list is empty, nothing to remove.")
            return
        for i, task in enumerate(tasks):
            print(f"  {i}. {task}")
        index = int(input("Select the index you want to remove.\nInput: "))
        removed = tasks.pop(index)
        with open(TODO_FILE, "w") as f:
            f.write("\n".join(tasks) + ("\n" if tasks else ""))
        print(f"Removed: {removed}")

    else:
        print(f"Your input {choice} is invalid. Choose 1, 2, or 3.")
