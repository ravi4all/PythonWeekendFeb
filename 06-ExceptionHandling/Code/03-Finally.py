try:
    file = open("demo1.txt",'r')
    f = file.read()
    print(f)

except FileNotFoundError as f:
    print(f)

finally:
    print("File Not Found")
    #file.close()


print("Let me execute")
