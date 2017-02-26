Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = ['hi',1,2,3,'Bye']
>>> a
['hi', 1, 2, 3, 'Bye']
>>> a.append(0)
>>> a
['hi', 1, 2, 3, 'Bye', 0]
>>> for i in a:
	print(i)

hi
1
2
3
Bye
0
>>> i
0
>>> i = []
>>> for j in a:
	i.append(j)
	print(i)

['hi']
['hi', 1]
['hi', 1, 2]
['hi', 1, 2, 3]
['hi', 1, 2, 3, 'Bye']
['hi', 1, 2, 3, 'Bye', 0]
>>> i
['hi', 1, 2, 3, 'Bye', 0]
>>> for j in a:
	i.append(j)

>>> print(i)
['hi', 1, 2, 3, 'Bye', 0, 'hi', 1, 2, 3, 'Bye', 0]
>>> a
['hi', 1, 2, 3, 'Bye', 0]
>>> del a[2]
>>> a
['hi', 1, 3, 'Bye', 0]
>>> a.pop()
0
>>> a
['hi', 1, 3, 'Bye']
>>> a.pop(3)
'Bye'
>>> a
['hi', 1, 3]
>>> a.remove(0)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a.remove(0)
ValueError: list.remove(x): x not in list
>>> a.remove(1)
>>> a
['hi', 3]
>>> a = {'id':1001,'name':'Ram','salary':10000}
>>> for i in a:
	print(i)

id
salary
name
>>> for i in a.items():
	print(i)

('id', 1001)
('salary', 10000)
('name', 'Ram')
>>> i
('name', 'Ram')
>>> a.keys()
dict_keys(['id', 'salary', 'name'])
>>> a.values()
dict_values([1001, 10000, 'Ram'])
>>> a['designation'] = 'Emp'
>>> a
{'designation': 'Emp', 'id': 1001, 'salary': 10000, 'name': 'Ram'}
>>> a
{'designation': 'Emp', 'id': 1001, 'salary': 10000, 'name': 'Ram'}
>>> a
{'designation': 'Emp', 'id': 1001, 'salary': 10000, 'name': 'Ram'}
>>> a['salary'] = 20000
>>> a
{'designation': 'Emp', 'id': 1001, 'salary': 20000, 'name': 'Ram'}
>>> del a['id']
>>> a
{'designation': 'Emp', 'salary': 20000, 'name': 'Ram'}
>>> 
