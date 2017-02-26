Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = [x*x for x in range(6)]
>>> a
[0, 1, 4, 9, 16, 25]
>>> a = [x*x for x in range(12) if x%2 == 0]
>>> a
[0, 4, 16, 36, 64, 100]
>>> 
