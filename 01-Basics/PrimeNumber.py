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

num = int(input("Enter the range : "))

for x in range(2,num):
    for i in range(2,x):
        if x%i == 0:
            print("Not prime",i)
            break
        else:
            print("Prime")
