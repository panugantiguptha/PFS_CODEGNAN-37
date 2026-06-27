Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #negative indexing
>>> a='simple is better than complex'
>>> a[-23]+a[-22]+a[-21]+a[-20]+a[-19]+a[-18]
' is be'
>>> a[-30]+a[-29]+[-28]+a[-27]+a[-26]+a[-25]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a[-30]+a[-29]+[-28]+a[-27]+a[-26]+a[-25]
IndexError: string index out of range
>>> a[-21]+a[-20]+a[-19]+a[-18]+a[-17]+a[-16]
's bett'
>>> a[-29]+[-28]+a[-27]+a[-26]+a[-25]+a[-24]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a[-29]+[-28]+a[-27]+a[-26]+a[-25]+a[-24]
TypeError: can only concatenate str (not "list") to str
>>> a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'complex'
>>> a[-29]+a[-28]+a[-27]+a[-26]+a[-25]+a[-24]
'simple'
>>> b='i love python'
>>> a[-12]+a[-11]+a[-10]+a[-9]
'than'
>>> a[-19]+a[-18]+a[-17]+a[-16]+a[-15]+a[-14]
'better'
>>> b[-11]+b[-10]+b[-9]+b[-8]
'love'
>>> b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'python'
