class Parent:

    def __init__(self,name):
        self.name = "Shyam"

    def display(self):
        print("Parent Function call by...",self.name)

    def show_me(self):
        print("My child will call me...")


class Child(Parent):

    def __init__(self,name):
        self.name = name
        # Parent.__init__(self,name)
        super().__init__(self,name)

    def display(self):
        print("Child Function call by...",self.name)


obj_1 = Child("Ram")
obj_1.display()
obj_1.show_me()

obj_2 = Child("Ram")
obj_2.display()
obj_2.show_me()