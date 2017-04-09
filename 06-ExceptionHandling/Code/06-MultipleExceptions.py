try:
    file = open("demo3.txt",'r')
    f = file.read()
    print(f)

except (FileNotFoundError, IOError, ArithmeticError) as e:
    print(e)

else:
    print("File Found")
