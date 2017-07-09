class Student:

    def __init__(self):
        self.average = 0
        self.grade_a = 'A'
        self.grade_b = 'B'
        self.grade_c = 'C'

    def name(self,s_name):
        self.s_name = s_name
        return self.s_name

    def marks(self,p,c,m):
        self.average = (p+c+m)//3
        return self.average

    def grades(self):

        if self.average > 90:
            print("Average : {}, Grade : {}".format(self.average,self.grade_a))
        elif self.average < 90 and self.average > 75:
            print("Average : {}, Grade : {}".format(self.average,self.grade_b))
        else:
            print("Average : {}, Grade : {}".format(self.average,self.grade_c))

ram = Student()
print(ram.name("Ram"))
ram.marks(56,67,78)
ram.grades()

shyam = Student()
print(shyam.name("Shyam"))
shyam.marks(78,98,99)
shyam.grades()