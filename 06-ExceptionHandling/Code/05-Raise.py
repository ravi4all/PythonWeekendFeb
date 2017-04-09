def division():
    a = int(input("Enter the number: "))
    b = 2
    try:
        if(a < 0):
            raise ValueError("Enter the integer")
        print(b/a)
    except ValueError as v:
        print(v)
        print("Exception Occured")


division()
