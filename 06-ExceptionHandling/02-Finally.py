a = 10
b = 0

try:
    print(a/b)

except ZeroDivisionError:
    print("Cannot divide")

finally:
    print("Execution will continue")


