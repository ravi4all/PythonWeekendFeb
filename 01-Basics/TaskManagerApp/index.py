taskList = []

def addTask():
    counter = 0
    #print("Add Task")
    task = input("Enter your task : ")
    taskList.append(task)
    print("Task List")
    for t in taskList:
        counter += 1
        print(counter,t)
    

def delTask():
    #print("Delete Task")
    to_delete = int(input("Enter task ID : "))
    del taskList[to_delete-1]
    print(taskList)

def readTask():
    for t in taskList:
        print(t)


while True:
    print("""
    1. Add Task
    2. Delete Task
    3. Read Task
    4. Update Task
    5. Sort Task
    6. Search Task
    7. Save Task
    8. Load Task
    9. Exit
    """)

    choice = int(input("Enter your choice : "))

    if choice == 1:
        addTask()
    elif choice == 2:
        delTask()
    elif choice == 9:
        quit()

