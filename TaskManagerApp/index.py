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

def updateTask():
    taskName = input("Enter task name to update : ")
    updatedTask = input("Enter Updated task : ")

    if taskName in taskList:
        indexOfTask = taskList.index(taskName)
        taskList[indexOfTask] = updatedTask
        print("Updated TaskList",taskList)

def errHandler():
    print("You have entered something wrong....Try Again")


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

    toDo = {
        "1":addTask,
        "2":delTask,
        "3":readTask,
        "4":updateTask,
        "9":quit
        }

    choice = input("Enter your choice : ")
    toDo.get(choice,errHandler)()

##    if choice == 1:
##        addTask()
##    elif choice == 2:
##        delTask()
##    elif choice == 9:
##        quit()

