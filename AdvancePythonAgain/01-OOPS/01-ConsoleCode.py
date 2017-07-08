Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 20
>>> type(a)
<class 'int'>
>>> class My_Cls:
	print("Hello")

	
Hello
>>> class My_Cls:
	x = 10
	y = 20
	c = x + y
	print(c)

30
>>> obj = My_Cls()
>>> obj
<__main__.My_Cls object at 0x03180AD0>
>>> obj_1 = My_Cls()
>>> obj_1
<__main__.My_Cls object at 0x031C1FD0>
>>> My_Cls.x
10
>>> obj.x
10
>>> obj_1.x = 12
>>> My_Cls.x
10
>>> obj.x
10
>>> My_Cls.x = "Hello"
>>> obj.x
'Hello'
>>> obj_1.x
12
>>> class Emp():

	def name(e_name):
		print("Name is",e_name)
	def salary(e_sal):
		print("Salary is",e_sal)

	
>>> name("Ram")
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    name("Ram")
NameError: name 'name' is not defined
>>> Emp.name("Ram")
Name is Ram
>>> x = Emp.name("Ram")
Name is Ram
>>> x
>>> type(x)
<class 'NoneType'>
>>> obj = Emp()
>>> type(obj)
<class '__main__.Emp'>
>>> obj_1 = Emp()
>>> obj_2 = Emp()
>>> obj_1.name("John")
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    obj_1.name("John")
TypeError: name() takes 1 positional argument but 2 were given
>>> class Emp():

	def name(this,e_name):
		print("Name is",e_name)
	def salary(this,e_sal):
		print("Salary is",e_sal)

	
>>> obj_1.name("John")
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    obj_1.name("John")
TypeError: name() takes 1 positional argument but 2 were given
>>> obj_1 = Emp()
>>> obj_1.name("John")
Name is John
>>> obj_1.salary(15000)
Salary is 15000
>>> class Emp():
	id = 10
	def name(this,e_name):
		print("Name is",e_name)
	def salary(this,e_sal):
		print("Salary is",e_sal)

		
>>> class Emp():
	id = 10
	def name(this,e_name):
		print("Name is",e_name)
	def salary(this,e_sal):
		print("Salary is",e_sal)
	def display_Emp(this):
		id += 1
		print("ID : {},Name : {}, Salary : {}".format(id,e_name,e_sal))

		
>>> obj = Emp()
>>> obj.name("Ram")
Name is Ram
>>> obj.sal(15000)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    obj.sal(15000)
AttributeError: 'Emp' object has no attribute 'sal'
>>> obj.salary(15000)
Salary is 15000
>>> obj.display_Emp()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    obj.display_Emp()
  File "<pyshell#55>", line 8, in display_Emp
    id += 1
UnboundLocalError: local variable 'id' referenced before assignment
>>> class Emp():
	id = 10
	def name(this,e_name):
		Emp.e_name = e_name
		print("Name is",e_name)
	def salary(this,e_sal):
		Emp.e_sal = e_sal
		print("Salary is",e_sal)
	def display_Emp(this):
		Emp.id += 1
		print("ID : {},Name : {}, Salary : {}".format(Emp.id,Emp,e_name,Emp.e_sal))

		
>>> obj = Emp()
>>> obj.name("Ram")
Name is Ram
>>> obj.salary(12000)
Salary is 12000
>>> obj.display_Emp()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    obj.display_Emp()
  File "<pyshell#62>", line 11, in display_Emp
    print("ID : {},Name : {}, Salary : {}".format(Emp.id,Emp,e_name,Emp.e_sal))
NameError: name 'e_name' is not defined
>>> class Emp():
	id = 10
	def name(this,e_name):
		Emp.e_name = e_name
		print("Name is",e_name)
	def salary(this,e_sal):
		Emp.e_sal = e_sal
		print("Salary is",e_sal)
	def display_Emp(this):
		Emp.id += 1
		print("ID : {},Name : {}, Salary : {}".format(Emp.id,Emp.e_name,Emp.e_sal))

		
>>> obj = Emp()
>>> obj.name("Ram")
Name is Ram
>>> obj.salary(12000)
Salary is 12000
>>> obj.display_Emp()
ID : 11,Name : Ram, Salary : 12000
>>> obj.display_Emp()
ID : 12,Name : Ram, Salary : 12000
>>> obj.display_Emp()
ID : 13,Name : Ram, Salary : 12000
>>> obj.display_Emp()
ID : 14,Name : Ram, Salary : 12000
>>> obj_1 = Emp()
>>> obj_2 = Emp()
>>> obj_1.name("John")
Name is John
>>> obj_1.salary(12000)
Salary is 12000
>>> obj_1.display_Emp()
ID : 15,Name : John, Salary : 12000
>>> obj_2.name("Mike")
Name is Mike
>>> obj_1.salary(12000)
Salary is 12000
>>> obj_1.display_Emp()
ID : 16,Name : Mike, Salary : 12000
>>> 
