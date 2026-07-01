Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#tuple means immutable
in tuple we use () round bractes
SyntaxError: invalid syntax
#in tuple we use () round brackets
a=(4,5.6,"code",2+9j,True,False)
print(a)
(4, 5.6, 'code', (2+9j), True, False)
type(a)
<class 'tuple'>
a.count(2+9j)
1
a.index(True)
4
len(a)
6
#sets
#it always represents in {} brackets

#sets{}
#in sets there is no order it will print in unorder
a={5,8.9,"pooja",5+9j,True,False}
print(a)
{False, True, (5+9j), 5, 8.9, 'pooja'}
type(a)
<class 'set'>
#subset means values in one set it should be in another set
a={2,3,4,5,6,7,8}
b={5,6,7,8]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
b={5,6,7,8}
a.issubset(b)
False
b.issubset(a)
True
a.issuperset(b)
True
b.issuperset(a)
False
#union means mearging of two cells
a={3,5,6,7,8}
b=4,5,6,7,8}
SyntaxError: unmatched '}'
b={4,5,6,7,8}
a.union(b)
{3, 4, 5, 6, 7, 8}
c={3,4,5,6,5,6,7,8,9,0,9}
print(c)
{0, 3, 4, 5, 6, 7, 8, 9}
#intersection means it will print common values in the set
a={3,4,5,6,7,8,9}
b={5,6,7,8,9}
a.intersection(b)
{5, 6, 7, 8, 9}
#update() it will udate from previous sets and update
a={10,20,30,40,50}
b={40,50,60,70,80}
a
{50, 20, 40, 10, 30}
a.update(b)
a
{70, 40, 10, 80, 50, 20, 60, 30}
a
{70, 40, 10, 80, 50, 20, 60, 30}
b.update(a)
b
{70, 40, 10, 80, 50, 20, 60, 30}
b
{70, 40, 10, 80, 50, 20, 60, 30}
#difference means a values that are not in b
a={4,5,6,7,8,9}
b=(8,9,2,6,7}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
b={8,9,2,6,7}
a.difference(b)
{4, 5}
b.difference(a)
{2}
#symmetric difference means it will eliminate common values from both sets and give remaining values
a={3,4,5,6,7,8,9}
b={1,3,5,7,8,11,13}
a.symmetric_difference(b)
{1, 4, 6, 9, 11, 13}
a={1,3,5,7,9,11,13}
b={2,3,4,6,7,9,11,12}
a.intersection_update(b)
a
{11, 9, 3, 7}
b
{2, 3, 4, 6, 7, 9, 11, 12}
b.intersection_update(a)
b
{3, 9, 11, 7}
#intersection update means it will update only different values from a
a{2,3,4,5,6,7}
SyntaxError: invalid syntax
a={2,3,4,5,6,7}
b={9,8,7,5,6,4,2}
a.difference_update(b)
a
{3}
b.difference_update(a)
b
{2, 4, 5, 6, 7, 8, 9}
a={11,12,13,14,15,16,17}
b={13,14,15,16,17,18}
a.symmetric_difference_update(b)
#in symmetric difference update means it will print different from a
a
{18, 11, 12}
b.symmetric_difference_update(a)
>>> b
{16, 17, 11, 12, 13, 14, 15}
>>> b
{16, 17, 11, 12, 13, 14, 15}
>>> a={4,5,6,7,,8,9,10}
SyntaxError: invalid syntax
>>> a={4,5,6,7,8,9,10}
>>> a.pop()
4
>>> a.remove(5)
>>> a
{6, 7, 8, 9, 10}
>>> a={3,4,5,6,7,8,9}
>>> a.discard(7)
>>> a
{3, 4, 5, 6, 8, 9}
>>> a.clear()
>>> a
set()
>>> b=set(20)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    b=set(20)
TypeError: 'int' object is not iterable
>>> b=set()
>>> b.add(20)
>>> b
{20}
>>> a=(3,4,5,6,7}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
>>> len(a)
0
>>> a={3,4,5,6,7}
>>> len(a)
5
>>> a.count(6)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    a.count(6)
AttributeError: 'set' object has no attribute 'count'
>>> #in sets there are no sets and index will be there
>>> #disjoint means there should be not equal in two sets
>>> a={3,4,5,6,7,9}
>>> b={22,67,34,57}
>>> a.isdisjoint(b)
True
