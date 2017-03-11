empId = {}
empName = {}
empSalary = {}

result = []

def addEmp():
    counter = 0
    
    emp_id = int(input("Enter emp id : "))
    emp_name = input("Enter emp name : ")
    emp_salary = float(input("Enter emp salary : "))

    empId['id'] = emp_id
    empName['Name'] = emp_name
    empSalary['Salary'] = emp_salary

    e_id = empId.copy()
    e_name = empName.copy()
    e_sal = empSalary.copy()

    empList = [e_id, e_name, e_sal]

    result.append(empList)
    #print(result)
    print("Employee List...")
    for r in result:
        counter += 1
        print(counter,r)
        #print(r)

    #print(empData)


def delEmp():
    e_num = int(input("Enter emp number to delete : "))
    del result[e_num-1]
    for r in result:
        print(r)
        

def readEmp():
    pass

def updateEmp():
    pass

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
        "1":addEmp,
        "2":delEmp,
        "3":readEmp,
        "4":updateEmp,
        "9":quit
        }

    choice = input("Enter your choice : ")
    toDo.get(choice,errHandler)()
