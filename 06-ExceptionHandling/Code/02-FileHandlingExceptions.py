try:
    file = open("demo.txt",'r')
    f = file.read()
    print(f)

except FileNotFoundError as f:
    print(f)

else:
    print("File Found")
