Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatype conversions
#int
int(6)
6
int(True)
1
int(False)
0
int("code")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int("code")
ValueError: invalid literal for int() with base 10: 'code'
int(2+3j)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    int(2+3j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(2.3)
2
float(2.34)
2.34
flost(6.55)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    flost(6.55)
NameError: name 'flost' is not defined. Did you mean: 'float'?
>>> float(6.55)
6.55
>>> #in integer string and complex will not be considered
>>> string("code")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    string("code")
NameError: name 'string' is not defined. Did you forget to import 'string'?
>>> str("code")
'code'
>>> str('code')
'code'
>>> str("True")
'True'
>>> str(2+3j)
'(2+3j)'
>>> str(345)
'345'
>>> #complex
>>> complex(2+3j)
(2+3j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> complex(code)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    complex(code)
NameError: name 'code' is not defined. Did you forget to import 'code'?
>>> bool(True)
True
>>> bool(False)
False
>>> bool(code)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    bool(code)
NameError: name 'code' is not defined. Did you forget to import 'code'?
>>> bool(4.5)
True
>>> bool(1)
True
>>> bool(4+9j)
True
>>> #boolean can be convert to all except string
