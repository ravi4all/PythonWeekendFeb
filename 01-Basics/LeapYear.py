a = int(input("Enter the year : "))

if a%4 == 0 and a%400 == 0:
    if a%400 == 0:
        print("Leap Year")
else:
    print("Not a leap year")




