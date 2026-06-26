Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#operations
#arithematic opearion
a=2
b=4
print(a+b)
6
print(a-b)
-2
print(a*b)
8
print(a//b)
0
print(a/b)
0.5
print(a**b)
16
print(a%b)
2
#assignment operator
a=4
b=5
a+b
9
a+=b
a
9
a-=b
a
4
a//=b
a
0
a/=b
a
0.0
a**=b
a
0.0
b+=a
b
5.0
b-=a
b
5.0
b//=a
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    b//=a
ZeroDivisionError: division by zero
#comparison operators
a=4
b=9
a<b
True
a>b
False
b>a
True
b<a
False
a!=b
True
a==b
False
b==a
False
a=b
a==b
True
b==a
True
#logical operators
a=3
b=6
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a<b or b>a
True
a!=b or a==b
True
a<=b or b<=a
True
not True
False
not False
True
#Identify Operator
>>> a=4
>>> type(a) is int
True
>>> type(a) is not int
False
>>> b=6.5
>>> type(b) is float
True
>>> type(b) is not float
False
>>> c=code
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    c=code
NameError: name 'code' is not defined. Did you forget to import 'code'?
>>> c="code"
>>> type(c) is str
True
>>> type(c) is not str
False
>>> type(c) is int
False
>>> d=2+3j
>>> type(d) is complex
True
>>> type(d) is not complex
False
>>> type(d) is not int
True
>>> e=True
>>> type(e) is bool
True
>>> type(e) is not int
True
>>> #membership operator
>>> a=2,4,5,6,10,7
>>> 2 in a
True
>>> 24 in a
False
>>> 22 not in a
True
>>> 6 not in a
False
>>> 7 in a
True
