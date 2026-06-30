Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
#len()

a="python"
len(a)
6
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
#len() represents number of characters in a string.
#count()
b="twinkle twinkle little star"
b.count("twinkle")
2
b.count("t")
5
b.count("le")
3
b.count("k")
2
b.count(" ")
3
b.count("")
28
#find a string
#in this it will the position of the letter
a="code"
a.find("d")
2
a.find("e")
3
b="hello"
b.find("l")
2
#in the above one it will find only first "l" only
#if we want to find second one also we need to use slicing method
b[2:4]
'll'
#escape sequences
#\n->new line
#\t->tab space
a="name\nmobile/tmailid\nclg"
print(a)
name
mobile/tmailid
clg]
a="name\nmobile\tmailid\nclg"
print(a)
name
mobile	mailid
clg
b="name:Guppu/nmobile no:9346896609/tmailid:panugantiguptha2004@gmail.com/nclg:KLU
SyntaxError: unterminated string literal (detected at line 1)
b="name:Guppu/nmobile no:9346896609/tmailid:panugantiguptha2004@gmail.com/nclg:KLU"
print(b)
name:Guppu/nmobile no:9346896609/tmailid:panugantiguptha2004@gmail.com/nclg:KLU
b="name:Guppu\nmobile no:9346896609\tmailid:panugantiguptha2004@gmail.com\nclg:KLU"
print(b)
name:Guppu
mobile no:9346896609	mailid:panugantiguptha2004@gmail.com
clg:KLU
#replace
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
#\->back slash used in coding
#/->forwardd hash used in url
a
'wait until you succeed'
b="wait wait until you succeed"
b.replace("wait","work")
'work work until you succeed'
#upper case upper()
#it is used to print in capital
a="hello"
a.upper()
'HELLO'
#lower case lower()
#it is used to print in small
a.lower()
'hello'
#if we need capital letter in first letter we need to use "capitalize()"
b="python"
b.capitalize()
'Python'
b.upper()
'PYTHON'
b.lower()
'python'
b.capitalize()
'Python'
c="guppu"
c.capitalize()
'Guppu'
#if we need capital letter in first letter we need to use "title()"
d="python course"
d.title()
'Python Course'
a="java"
a.isupper()
False
a.islower()
True
a.isdigit()
False
a.isalpha()
True
b="python course"
b.isalpha()
False
b="pythoncourse"
b.isalpha()
True
c="guppu123"
c.isalnum()
True
d="Panugantiguptha200@gmail.com"
c.isalnum()
True
d.isalnum()
False
d="Panuganti"
d.isalnum()
True
d.isnum()
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    d.isnum()
AttributeError: 'str' object has no attribute 'isnum'. Did you mean: 'isalnum'?
d.isalpha()
True
e="123456"
e.isdigit()
True
e.isalnum()
True
#startswith() in the give string starting word is correct is true other wise false
a="hello python"
a.startswith("h")
True
a.endswith("n")
True
#strip()
#lstrip(),rstrip()
a="      guppu"
a.lstrip()
'guppu'
a.rstrip()
'      guppu'
a.strip()
'guppu'
a="     guppu      "
a.lstrip()
'guppu      '
a.strip()
'guppu'
a.rstrip()
'     guppu'
a.strip()
'guppu'
#split() means separating group of words
a="python c java c++"
a.split()
['python', 'c', 'java', 'c++']
b="i am in vja"
b.split()
['i', 'am', 'in', 'vja']
#join() means it joins group of words
a="vja hyd vzg"
a.join()
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    a.join()
TypeError: str.join() takes exactly one argument (0 given)
"".join(a)
'vja hyd vzg'
" ".join(a)
'v j a   h y d   v z g'
b="vja","hyd","vzg"
"".join(b)
'vjahydvzg'
" ".join(b)
'vja hyd vzg'
"k"" ".join(b)
'vjak hydk vzg'
#concatination() means adding all the string in on line
a="hello"
b="world"
print(a+b)
helloworld
print(a+" "+b)
hello world
print((a+" "+b).title())
Hello World
#formatting
a=4
b=8
print(a+4)
8
print("the sum is",a+b)
the sum is 12
x=vja
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    x=vja
NameError: name 'vja' is not defined
x="vja"
print("the city",x)
the city vja
#.format method means we can add easy any string
a="motu"
b='patlu'
print("Hello {} {},.format(a+b))
      
SyntaxError: unterminated string literal (detected at line 1)
print("Hello {} {}",.format(a+b))
      
SyntaxError: invalid syntax
print("Hello {} {}".format(a+b))
      
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    print("Hello {} {}".format(a+b))
IndexError: Replacement index 1 out of range for positional args tuple
>>> print("Hello",a+b)
...       
Hello motupatlu
>>> print("Hello {} {}
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print("Hello {}{}".format(a+b))
...       
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    print("Hello {}{}".format(a+b))
IndexError: Replacement index 1 out of range for positional args tuple
>>> c="motu"
...       
>>> d="patlu"
...       
>>> a="sita"
...       
>>> b="ram"
...       
>>> print(f"hello {a}{b}")
...       
hello sitaram
>>> a=4
...       
>>> b=5
...       
>>> print("The product is".format(a*b))
...       
The product is
>>> print("The product is",a*b)
...       
The product is 20
>>> c=a+b
...       
>>> print("the product is {}".format(c))
...       
the product is 9
>>> print("The product is {}".format(a*b))
...       
The product is 20
>>> print(f"the product is {a*b}")
...       
the product is 20
