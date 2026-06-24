Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=4;b=9
>>> print(a+b)
13
>>> a,b,c=10
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a,b,c=10
TypeError: cannot unpack non-iterable int object
>>> a=b=c=10
>>> print(a,b,c)
10 10 10
>>> a,b,c=2,3,4
>>> print(a,b,c)
2 3 4
>>> a,b,c=2,3,4,5,6,7,8,9
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a,b,c=2,3,4,5,6,7,8,9
ValueError: too many values to unpack (expected 3, got 8)
