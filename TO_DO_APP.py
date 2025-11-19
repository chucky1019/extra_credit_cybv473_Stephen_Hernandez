# name = stephen Hernandez
# assignment = Extra credit
# date = 11/17/25


import json


TO_DO_FILE = "todos.json"

def task_list ():
    """Load task from json file"""
    try:
        with open(TO_DO_FILE) as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    """Save tasks to json file"""
    with open(TO_DO_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)


def add_task (tasks):
    """Add task to json file"""

    raw = input("enter task to add separte with comma to add multiple tasks")

    parts = raw.split(',')

    for part in parts:
       task_text = part.strip()
       if task_text:
            tasks.append({"task": task_text, "completed": False})
            print ("Task added")

    return tasks


def list_tasks (tasks):
    """List tasks saved in json file"""
    if not tasks:
        print ("No tasks saved")
        return

    for i , t in enumerate(tasks):
        status = t["completed"] if t["completed"] else False
        print (f"{i}. {t['task']}")


def mark_finshed(tasks):
    """Mark task as finished"""
    index_str = input("Enter task to mark as finished: ")
    try:
        index = int(index_str)
        tasks[index]["completed"] = True
        print ("Task marked as finished")
    except (ValueError, IndexError):
        print ("Invalid task")


def main():
    tasks = task_list()

    while True:
        print ("\nTask List")
        print ("[a] Add task")
        print ("[b] List tasks")
        print ("[d] Mark finished")
        print ("[e] Quit")
        print ("[s] Save tasks")



        choice = input("Enter choice: ")
        if choice == "a":
            add_task(tasks)
        elif choice == "b":
            list_tasks(tasks)
        elif choice == "d":
            mark_finshed(tasks)
        elif choice == "e":
            save_tasks(tasks)
        elif choice == "s":
            save_tasks(tasks)
            print("GoodJob!!")
            break
        else:
            print ("Invalid choice")


if __name__ == "__main__":
    main()




