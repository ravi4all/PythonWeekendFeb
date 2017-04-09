def div():
    a = int(input("Enter the number "))
    try:
        b = a/2
        assert(b >= 0), "You have entered a wrong number"
        print(b)
    except AssertionError as a:
        print(a)

div()
    
