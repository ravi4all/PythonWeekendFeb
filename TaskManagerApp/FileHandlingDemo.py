a = {}
c = []

def fileOpe(x):
    file = open("file.txt","w+")
    s = str(x).strip("{}")+"\n"
    file.write(s)
    file.close()

while True:
    e_id = int(input("Enter Id : "))
    e_name = input("Enter name : ")

    a["id"] = e_id
    a["name"] = e_name
    copy = a.copy()

    c.append(copy)

    for x in c:
        print(x)
    fileOpe(x)
        


