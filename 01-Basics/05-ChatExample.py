import random

a = ['Hi', 'Greetings', 'Good Morning', 'Have a nice day']
b = random.choice(a)

user_name = input("Enter your name : ")
print(b,user_name)


while True:
    user_message = input("Enter your message :")
    print("User's Message",user_message)

    if user_message == 'Hi':
        print("Bot's Message",a[0])

    elif user_message == 'Bye':
        print('Byeeeee')

    else:
        print(random.choice(a))
