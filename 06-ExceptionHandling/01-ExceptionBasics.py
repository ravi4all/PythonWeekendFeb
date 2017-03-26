a = 10

loop = False

for i in range(0,10):
    
    num = int(input("Enter the number : "))

    try:
        print(a/num)

    except:
        print("Cannot divide a number with zero")

    finally:
        print("I will always execute")


