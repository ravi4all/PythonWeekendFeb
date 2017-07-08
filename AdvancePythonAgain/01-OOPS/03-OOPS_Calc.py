import calc_operations

class Calculator:

    def __init__(self):
        pass

    def display(self,user_choice,num_1,num_2,to_do):
        # print(to_do.get(user_choice)(num_1,num_2,user_choice))
        opr = to_do.get(user_choice)
        print(calc_operations.operations(num_1,num_2,opr))


    def menu(self):

        print("""
        1. Add
        2. Sub
        3. Mul
        4. Div
        """)

        user_choice = input("Enter your choice : ")

        num_1 = int(input("Enter first number : "))
        num_2 = int(input("Enter second number : "))

        # to_do = {
        #     "1" : calc_operations.operations,
        #     "2" : calc_operations.operations,
        #     "3" : calc_operations.operations,
        #     "4" : calc_operations.operations
        # }

        to_do = {
            "1" : "+",
            "2" : "-",
            "3" : "*",
            "4" : "/"
        }

        Calculator.display(self,user_choice,num_1,num_2,to_do)

obj = Calculator()
obj.menu()