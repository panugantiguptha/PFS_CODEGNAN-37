Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
>>> a='i am in class'
>>> a[8]+a[9]+a[10]+a[11]+a[12]
'class'
>>> a[5]+a[6]
'in'
>>> a[1]
' '
>>> a[2]+a[3]
'am'
>>> a[1]+a[4]+a[7]
'   '
>>> b='i am learning python course'
>>> a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
IndexError: string index out of range
>>> b[13]+b[14]+b[15]+b[16]+a[17]+a[18]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    b[13]+b[14]+b[15]+b[16]+a[17]+a[18]
IndexError: string index out of range
>>> b[13]+b[14]+b[15]+b[16]+b[17]+b[18]
' pytho'
>>> b[14]+b[15]+b[16]+b[17]+b[18]+b[19]
'python'
>>> b[5]+b[6]+b[7]+b[8]+b[9]
'learn'
>>> b[21]+b[22]+b[23]+b[24]+b[25]
'cours'
>>> b[21]+b[22]+b[23]+b[24]+b[25]+b[26]
'course'
>>> c='time is very precious'
>>> c[14]+c[15]+c[16]+c[17]+c[18]+c[19]+c[20]
'recious'
>>> c[13]+c[14]+c[15]+c[16]+c[17]+c[18]+c[19]+c[20]
'precious'
>>> c[9]+c[10]+c[11]+c[12]
'ery '
>>> KeyboardInterrupt
>>> c[8]+c[9]+c[10]+c[11]+c[12]
'very '
>>> a[0]+a[1]+a[2]+a[3]
'i am'
>>> c[0]+c[1]+c[2]+c[3]
'time'
