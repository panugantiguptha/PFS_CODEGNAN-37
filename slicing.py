Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #slicing
>>> a='codegnan'
>>> a[0:4]
'code'
>>> a[:4]
'code'
>>> a[4:8]
'gnan'
>>> a[4:]
'gnan'
>>> b='work until you succeed'
>>> b[5:10]
'until'
>>> b[11:14]
'you'
>>> b[:4]
'work'
>>> b[15:]
'succeed'
>>> c='codegnan it solutions'
>>> c[9:11]
'it'
>>> c[:8]
'codegnan'
>>> c[12:]
'solutions'
>>> #over is positive slicing
>>> #neagative slicing
>>> d='vijayawada is a royal city'
>>> d[-6:-11]
''
>>> d[-5:-12]
''
>>> d[-1:-5]
''
>>> d[-11:-6]
' roya'
>>> d[-10:-5]
'royal'
>>> d[-25:-16]
'ijayawada'
>>> d[-26:-16]
'vijayawada'
>>> d[-4:]
'city'
e='vizag is city of destiny'
e[-15:-11]
'city'
e[:-19]
'vizag'
e[-7:]
'destiny'
#striding means jumble words we need to find
#in this increment will be there if any numeber
a='data science'
a[::1]
'data science'
a[::2]
'dt cec'
a[::3]
'dacn'
b='cloud computing'
b[2:]
'oud computing'
b[:9]
'cloud com'
b[3:11]
'ud compu'
b[::2]
'codcmuig'
b[::6]
'cci'
a[::5]
'dsc'
b[::5]
'c u'
a="machine learning"
a[3:15:4]
'h r'
a[3:14:2]
'hn eri'
a[5:15:4]
'nei'
a[2:12:3]
'cnlr'
a[0:10:1]
'machine le'
#neagative striding
a="python course"
a[-1:-10:-2]
'ero o'
