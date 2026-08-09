'''Exception handling - 4 parts

try = Instructions from which we are expecting the exceptions

except = exceptions are raised in try block it will be handle by this block

else = optional (no exceptions)

finally = always it will display'''

'''while True:
    try:
        a=int(input('a value'))
        b=int(input('b value'))
        c=a//b
        print(c)
    except:
        print('exception is raised')
    else:
        print('no exceptions')
    finally:
        print('program ends...')'''


#regex (regular expression)
'''regular expressions are powerful tools (module) embedded in python,
which is mainly used to find a pattern within a given string or statements or files and we mainly used for text manipulation'''

# compile(), search(), findall(), split(), sub()
# sequence characters
'''\w = it matches alphanumeric
\W = it matches non-alphanumeric
\d = it matches any digit
\D = it matches non-digit
\s = it represents white spaces
\S = it represents non-white spaces'''

#compile()
'''import re
a='mat cat rat bat fat maths monkey cash cup coke cake'
b=re.compile(r'm\w')
#print(b)

#search()
c=b.search(a)
print(c)

#findall()
c=re.findall(r'c\w+',a)
print(*c)

#split()
d=re.split(r'm',a)
print(d)

e=re.split(r'\s',a)
print(e)

#sub()
f=re.sub('m','a',a)
print(f)'''

import re
a='year 2026 month 7 date 29'
b=re.findall(r'\d+',a)
print(b)
