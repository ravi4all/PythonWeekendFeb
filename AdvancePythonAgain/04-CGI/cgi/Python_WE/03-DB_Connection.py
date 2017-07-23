import pymysql

connection = pymysql.connect(host='localhost', port = 3306, user='root', passwd='',
                             db = 'e_commerce')

cursor = connection.cursor()

cursor.execute("SELECT * FROM users WHERE email = 'ram@gmail.com' AND password = 'ram12345'")

for data in cursor:
    print(data)