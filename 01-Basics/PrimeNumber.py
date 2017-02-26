##num = int(input("Enter the number : "))
##
##
##if num > 1:
##    
##    for i in range(2,num):
##        if num%i == 0:
##            print("Not prime")
##            break
##    else:
##        print("Prime")

while True:
    
    min_range = int(input("Enter the lower range : "))
    max_range = int(input("Enter the upper range : "))

    for x in range(min_range,max_range+1):
        if x > 1:
            for i in range(2,x):
                if x%i == 0:
                    print("Not prime",x)
                    break
            else:
                print("Prime",x)
