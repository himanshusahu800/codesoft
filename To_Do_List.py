def add_task(tasks):
    task_name = input("Enter the task you want to add: ")
    tasks.append(task_name)
    print(f"Task '{task_name}' has been successfully added.")

def update_task(tasks):
    update_val = input("Enter the task name you want to update: ")
    if update_val in tasks:
        new_task = input("Enter new task: ")
        ind = tasks.index(update_val)
        tasks[ind] = new_task
        print(f"Task '{update_val}' has been updated to '{new_task}'.")
    else:
        print(f"Task '{update_val}' not found.")

def delete_task(tasks):
    del_val = input("Enter the task name you want to delete: ")
    if del_val in tasks:
        tasks.remove(del_val)
        print(f"Task '{del_val}' has been deleted.")
    else:
        print(f"Task '{del_val}' not found.")

def view_tasks(tasks):
    if tasks:
        print(f"Total tasks: {tasks}")
    else:
        print("No tasks available.")

def task_management():
    tasks = [] 
    print("---WELCOME TO THE TASK MANAGEMENT APP---")
    total_task = int(input("Enter how many tasks you want to add: "))
    
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)
    
    print(f"Today's tasks are:\n{tasks}")
    
    while True:
        operation = int(input("Enter:\n1 - Add\n2 - Update\n3 - Delete\n4 - View\n5 - Exit\nYour choice: "))
        
        if operation == 1:
            add_task(tasks)
        
        elif operation == 2:
            update_task(tasks)
        
        elif operation == 3:
            delete_task(tasks)
        
        elif operation == 4:
            view_tasks(tasks)
        
        elif operation == 5:
            print("Closing the program...")
            break
        
        else:
            print("Invalid Input")

task_management()
