Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[2,5.6."python",6+9j,True,False]
SyntaxError: invalid syntax
a=[2,5.6,"python",6+9j,True,False]
type(a)
<class 'list'>
b=5
type(b)
<class 'int'>
c=[5]
type(c)
<class 'list'>
a=["c","c++","Java","python"]
a.append("ml","dsa")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a.append("ml","dsa")
TypeError: list.append() takes exactly one argument (2 given)
a.append("ml")
print(a)
['c', 'c++', 'Java', 'python', 'ml']
#append can only add one variable only
#extend can add two variables
b=["c","java","python"]
b.extend("ml","dsa")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    b.extend("ml","dsa")
TypeError: list.extend() takes exactly one argument (2 given)
b.extend(["ml","dsa"])
print(b)
['c', 'java', 'python', 'ml', 'dsa']
#insert means it deside where the varible can be
c=["vij","vzg"]
c.insert(1,"hyd")
print(c)
['vij', 'hyd', 'vzg']
#index means it can say the number where the work is located
a=["black","white","red","pink"]
a.index("red")
2
a.copy()
['black', 'white', 'red', 'pink']
b=a.copy()
print(b)
['black', 'white', 'red', 'pink']
#copy means it can be copy into another one same
#count means it can count how any words are there
>>> b.count('white')
1
>>> #sort means print the values in perticular order
>>> a=["grapes","apple","mango","banana"]
>>> a.sort()
>>> print(a)
['apple', 'banana', 'grapes', 'mango']
>>> b=[8,7,1,6,2,0,4]
>>> b.sort()
>>> print(b)
[0, 1, 2, 4, 6, 7, 8]
>>> #reverse means printing from last
>>> a=[7,3,4,51,9,3,0]
>>> a.reverse()
>>> print(a)
[0, 3, 9, 51, 4, 3, 7]
>>> b=[7,1,9,2,0,4]
>>> b.reverse()
>>> print(b)
[4, 0, 2, 9, 1, 7]
>>> a=[0,1,7,2,9,4]
... a.reverse()
... print(a)
... [4, 9, 2, 7, 1, 0]
... #pop means delete the data
... #in pop we need to use index number and in remove we need to use data
... a=["c","c++","ml","ai"]
... a.pop(2)
... 'ml'
... a
... ['c', 'c++', 'ai']
... a.remove("c++")
... a
... ['c', 'ai']
... a=["pooja","priya","prince","surya"]
... len(a)
... 4
... b="surya"
... len(b)
... 5
... a.clear()
... a
... []
... a.append("Guppu")
... a
... ['Guppu']
