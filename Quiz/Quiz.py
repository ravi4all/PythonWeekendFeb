counter = 1
file = open("ques.txt","r+")
def fileHandling():
    str = file.readline()
    print(str)
    answer()


def answer():
    ans = ['Delhi','Kohli','Modi','Jawaharlal Nehru']
    user_ans = input("Enter your answer : ")

    if counter == 1 and user_ans == ans[0]:
        print("Correct")
    if counter == 2 and user_ans == ans[1]:
        print("Correct")
    if counter == 3 and user_ans == ans[2]:
        print("Correct")
    if counter == 4 and user_ans == ans[3]:
        print("Correct")
    else:
        print("Wrong")

while True:
    choice = int(input("Press 1 to see ques : "))
    if choice == 1:
        fileHandling()
    counter += 1

