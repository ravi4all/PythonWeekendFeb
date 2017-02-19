a = 30
b = 20

print("Sum is",a+b)
print("Divison is",a/b)
print("Multiplication is",a*b)
print(a%b)
print(a-b)
print(a//b)

if a > b:
    print("{} is greater than {}".format(a,b))
    print(a, "is greater than",b)
else:
    print("Not greater")


print(r'Hello world...This is \n "python"')

a = input("Enter the number:")
b = input("Enter the number:")
c = int(a) + int(b)
print(c)
