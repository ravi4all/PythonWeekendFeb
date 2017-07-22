import re

while True:

    pwd = input("Enter password : ")

    if re.search(r'[a-z]{5}[A-Z]{2}', pwd):
        print("Match")
    else:
        print("Do not match")