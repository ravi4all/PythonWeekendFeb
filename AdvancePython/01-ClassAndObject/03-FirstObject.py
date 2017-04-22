import os

class MyFirstObj:
    "My First Object"

    def disp(self):
        print("Hello World")


obj = MyFirstObj()
#MyFirstObj.disp()
obj.disp()
print(type(obj))
print(obj.__doc__)
#print(os.__dict__)
print(obj.__dict__)
print(obj.__module__)
print(MyFirstObj.__bases__)
print(MyFirstObj.__name__)

##print(3 + 4)
##
##a = 3
##b = 4
##c = a+b
##print(c)
