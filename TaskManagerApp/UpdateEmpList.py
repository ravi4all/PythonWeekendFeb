empData = {}

result = []

def fileOperations(e):
    file = open("EmpData.txt","a+")
    file.write(str(e).strip("{}")+"\n")
    file.close()

def addEmp():
    counter = 0
    
    emp_id = int(input("Enter emp id : "))
    emp_name = input("Enter emp name : ")
    emp_salary = float(input("Enter emp salary : "))

    empData['id'] = emp_id
    empData['Name'] = emp_name
    empData['Salary'] = emp_salary

    e_data = empData.copy()
    result.append(e_data)
    #print(result)
    print("Employee List...")
    for r in result:
        counter += 1
        print(counter,r)
        #print(r)
    fileOperations(r)

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

def loadEmp():
    file = open("EmpData.txt","r+")
    print(file.read())

def errHandler():
    print("You have entered something wrong....Try Again")


while True:
    
    print("""
    1. Add Emp
    2. Delete Emp
    3. Read Emp
    4. Update Emp
    5. Load Emp
    6. Search Emp
    7. Save Emp
    8. Sort Emp
    9. Exit
    """)

    toDo = {
        "1":addEmp,
        "2":delEmp,
        "3":readEmp,
        "4":updateEmp,
        "5":loadEmp,
        "9":quit
        }

    choice = input("Enter your choice : ")
    toDo.get(choice,errHandler)()
