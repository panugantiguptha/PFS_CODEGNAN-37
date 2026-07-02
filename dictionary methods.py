Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #dict{}
>>> a={"name":"Guptha","city":"vja"}
>>> print(a)
{'name': 'Guptha', 'city': 'vja'}
>>> type(a)
<class 'dict'>
>>> b={5,6,7,8,9,"name"}
>>> type(b)
<class 'set'>
>>> #dictionary methods
>>> a={"name":"Guptha","mailid":"panugantiguptha2004@gmail.com","mobileno":9346896609}
>>> a.keys()
dict_keys(['name', 'mailid', 'mobileno'])
>>> #keys will show only values
>>> a.values()
dict_values(['Guptha', 'panugantiguptha2004@gmail.com', 9346896609])
>>> #keys shows variablese
>>> a.items()
dict_items([('name', 'Guptha'), ('mailid', 'panugantiguptha2004@gmail.com'), ('mobileno', 9346896609)])
>>> #items will print all the data
>>> #in dictonary if we need to add data we have to use update(), and we can add one or more but it should be in single brackets
>>> a={"course":"python","institute":"codegnan","name":"Guptha"}
>>> a.update({"year":2026},{"month":7})
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a.update({"year":2026},{"month":7})
TypeError: update expected at most 1 argument, got 2
>>> a.update({"year":2026,"month":7})
>>> a
{'course': 'python', 'institute': 'codegnan', 'name': 'Guptha', 'year': 2026, 'month': 7}
>>> a.update({"place":"vja"})
>>> a
{'course': 'python', 'institute': 'codegnan', 'name': 'Guptha', 'year': 2026, 'month': 7, 'place': 'vja'}
>>> a=["year":2026,"month":"july"}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> a.setdefault("date",2)
2
>>> a
{'course': 'python', 'institute': 'codegnan', 'name': 'Guptha', 'year': 2026, 'month': 7, 'place': 'vja', 'date': 2}
>>> a={"year":2026,"month":"july"}
>>> a.setdefault("date",2)
2
>>> a
{'year': 2026, 'month': 'july', 'date': 2}
>>> #in setdefault it will take as dictinory format automatically
a={"time":12,"hour":1,"min":3}
a.pop()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("time")
12
a
{'hour': 1, 'min': 3}
a.popitem()
('min', 3)
a
{'hour': 1}
#in this pop we have to declare the purticular key and in popitem if we want to delete last item we need to use popitem()
a={"college":"klu","branch":"cse"}
a.get("college")
'klu'
a["branch"]
'cse'
a
{'college': 'klu', 'branch': 'cse'}
#get is used only for see the variable and if we need only value we need to use '[]' brackets then only value will be print if we need key we need to use get key word
a={"hour":12,"min":3,"sec":60}
a.copy()
{'hour': 12, 'min': 3, 'sec': 60}
#copy it will copy all the above one
a.clear()
a
{}
#clear means it will clear the data we have give n
#if we need to add the data we have to use setdefault or update
a.update({"name":"guptha"})
a
{'name': 'guptha'}
a={"name":"guptha","course":"python","year":2026}
len(a)
3
a.count("name")
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a.count("name")
AttributeError: 'dict' object has no attribute 'count'
a={"name":"guptha","city":"vja","name":"guptha"}
print(a)
{'name': 'guptha', 'city': 'vja'}
#in the above one it is name key so it print only one
a={"name":"guptha","city":"vja","name":"Trinadh"}
print(a)
{'name': 'Trinadh', 'city': 'vja'}
#in this it is same key so it will print only latest one
a={"name1":"guptha","city":"vja","name2":"guptha"}
print(a)
{'name1': 'guptha', 'city': 'vja', 'name2': 'guptha'}
#in this there is different key so it will print both
a={"idnos":[10,20,30],"names":["harsha","trinadh","sai"],"marks":[60,70,80]}
type(a)
<class 'dict'>
a.keys()
dict_keys(['idnos', 'names', 'marks'])
a.values()
dict_values([[10, 20, 30], ['harsha', 'trinadh', 'sai'], [60, 70, 80]])
a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['harsha', 'trinadh', 'sai']), ('marks', [60, 70, 80])])
