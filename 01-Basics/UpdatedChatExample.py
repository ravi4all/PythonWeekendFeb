import random

a = ['Hi', 'Greetings', 'Good Morning', 'Have a nice day']
b = random.choice(a)

user_name = input("Enter your name : ")
print(b,user_name)

def chatLoop():

    chat = False
    
    while not chat: # while True
        user_message = input("Enter your message :")
        print("User's Message",user_message)

        if user_message == 'Hi' or user_message == 'hi':
            print("Bot's Message",a[0])

        elif user_message == 'Bye' or user_message == 'bye':
            print('Byeeeee')
            chat = True

        else:
            print(random.choice(a))


chatLoop()
print("Out of loop")
