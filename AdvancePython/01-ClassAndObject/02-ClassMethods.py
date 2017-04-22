class Demo:
    "This is a demo class"
    "This is another docstring"

    a = 10
    b = 20
    c = 0
    
    def add():
        Demo.c = Demo.a + Demo.b
        Demo.display()

    def sub():
        Demo.c = Demo.a - Demo.b
        Demo.display()

    def mul():
        Demo.c = Demo.a * Demo.b
        Demo.display()

    def div():
        Demo.c = Demo.a // Demo.b
        Demo.display()

    def display():
        print("Hello World")
        print("Result is",Demo.c)

    #display()

Demo.add()
Demo.sub()
Demo.mul()
Demo.div()
