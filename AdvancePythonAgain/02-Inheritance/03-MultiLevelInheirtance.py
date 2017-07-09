class Bank:

    def __init__(self,id,name,acc_bal):
        self.id = id
        self.name = name
        self.acc_bal = acc_bal

    def authentication(self):
        pin = int(input("Enter PIN : "))
        if pin == 1234:
            print("Welcome")
            print("ID : {}, Name : {}, Balance : {}".format(self.id,self.name,self.acc_bal))

        else:
            print("Try Again")

    def check_availability(self):
        if self.acc_bal > 12000:
            print("Loan Available")
        elif self.acc_bal < 12000:
            print("Not Eligible")
        else:
            print("Try Next Year...")


class Customer(Bank):

    def __init__(self,id,name,acc_bal):
        self.id = id
        self.name = name
        self.acc_bal = acc_bal
        super().__init__(id,name,acc_bal)

    def withdraw(self):
        self.amount = int(input("Enter amount to withdraw : "))
        self.acc_bal = self.acc_bal - self.amount
        return self.acc_bal

    def deposit(self):
        self.amount = int(input("Enter amount to deposit : "))
        self.acc_bal = self.acc_bal + self.amount
        return self.acc_bal


class Show(Customer):

    main_bal = 25000

    def __init__(self,id,name,acc_bal):
        self.id = id
        self.name = name
        self.acc_bal = acc_bal
        super().__init__(id,name,acc_bal)

    def menu(self):
        print("""
        1. Withdraw
        2. Deposit
        """)
        user_choice = input("Enter your choice : ")
        todo = {
            "1" : super().withdraw,
            "2" : super().deposit
        }
        todo.get(user_choice)()

    def display(self):
        print("Available Balance",self.acc_bal)


class Cibil(Show):

    def __init__(self,id,name,acc_bal):
        self.id = id
        self.name = name
        self.acc_bal = acc_bal
        super().__init__(self.id,self.name,self.acc_bal)

    def check_cibil(self):
        cibil = 700
        print("Main Balance",Show.main_bal)

        if self.acc_bal >= 12000 and cibil >= 700:
            print("Status is green")
        elif self.acc_bal <= 11999 and cibil <= 699:
            print("Status is red")
        else:
            print("Get Lost")


obj_1 = Show(1,"Ram",23000)
obj_1.authentication()
obj_1.menu()
obj_1.display()
obj_1.check_availability()

obj_2 = Cibil(obj_1.id,obj_1.name,obj_1.acc_bal)
obj_2.check_cibil()