#!C:/Python36-32/python.exe

import cgi

form = cgi.FieldStorage()

mail_id = form.getvalue('mail')
pwd = form.getvalue('pwd')

def success():

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
    """%(mail_id))

def failure():

    print("""
    <!DOCTYPE html>
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>

    <h1>Login Failed</h1>

    </body>
    </html>
    """)

if mail_id == 'ram@gmail.com' and pwd == 'ram12345':
    success()
else:
    failure()