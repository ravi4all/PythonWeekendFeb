#!C:/Python36-32/python.exe

import cgi
import pymysql

connection = pymysql.connect(host='localhost', port = 3306, user='root', passwd='',
                             db = 'e_commerce', autocommit = True)

cursor = connection.cursor()

form = cgi.FieldStorage()
u_mail = form.getvalue("mail")
u_pwd = form.getvalue("pwd")

# u_mail = "ravi@gmail.com"
# u_pwd = "raviravi"

def print_html(data):
    print("""
    <!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style>
        body {
            background-color: darkgray;
        }
    </style>
</head>
<body>

<h1>Hello %s</h1>

</body>
</html>
    """%(data))

def failure():
    print("""
    <!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style>
        body {
            background-color: darkgray;
        }
    </style>
</head>
<body>

<h1>You are a fraud</h1>

</body>
</html>
    """)

def success():

    query = "SELECT Name FROM users WHERE email = %s AND password = %s "
    cursor.execute(query, (u_mail, u_pwd))

    for data in cursor:
        pass

    print_html(data)


def check_user():

    query = "SELECT * FROM users"
    cursor.execute(query)

    for data in cursor:
        # print(data)
        pass

    if u_mail in data and u_pwd in data:
        # print("User Exist")
        # print(data)
        success()
    else:
        failure()
        # print("Not Exist")


# register_user()

check_user()