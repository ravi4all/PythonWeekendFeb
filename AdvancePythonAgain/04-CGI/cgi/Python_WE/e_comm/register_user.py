#!C:/Python36-32/python.exe

import cgi
import pymysql

connection = pymysql.connect(host='localhost', port = 3306, user='root', passwd='',
                             db = 'e_commerce', autocommit = True)

cursor = connection.cursor()

form = cgi.FieldStorage()
u_name = form.getvalue("u_name")
u_mail = form.getvalue("mail")
u_pwd = form.getvalue("pwd")

# u_name = "Ravi"
# u_mail = "ravi@gmail.com"
# u_pwd = "raviravi"

def print_html():
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

<h1>Registered Successfully</h1>

</body>
</html>
    """)

def register_user():

    query = "INSERT INTO users (Name, email, password) VALUES (%s, %s, %s)"
    cursor.execute(query, (u_name, u_mail, u_pwd))

    print_html()

register_user()