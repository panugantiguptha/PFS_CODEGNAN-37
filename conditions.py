#conditions
#oif-condition by using comparision operators
#<,>,<=,>=,!=,==

'''a=10
b=20
if a<b:
    print("true")'''


'''a=10
b=20
if a>b:
    print("true")'''


'''a=5
b=7
if a<=b:
    print("yes")'''

'''a=10
b=20
if a>=b:
    print("true")'''

'''a=12
b=15
if a<=b:
   print("true")'''

'''a=10
b=10
if a==b:
    print("true")'''

'''a="python"
if a=="python":
    print("match")'''

'''a=int(input("a value"))
b=int(input("b value"))
if a<b:
    print("less")'''

'''a=int(input())
if a<=50:
    print("less")'''


#if- condition by using logical operator
#and,or,not

'''a=3
b=6
if a<b and b>a:
    print("true")'''

'''a=4
b=7
if a<=b and b>=a:
    print("true")'''

'''a=9
b=12
if a!=b and a==b:
    print("true")'''

'''a=2
b=4
if a<b or b>a:
    print("true")'''


'''a=14
b=16
if a<=b or b>=a:
    print("true")'''


'''a=3
b=6
if a!=b or a==b:
    print("true")'''

'''a=3
b=6
if not a<b:
    print("true")'''

'''a=3
b=6
if not a<b and b>a:
    print("true")'''

'''a=3
b=6
if not a<b or b>a:
    print("true")'''

#if- condition by using identify operators
#is, is not

'''a=4
if type(a) is int:
    print("it is int")'''

'''a=4
if type(a) is not int:
    print("it is int")'''

'''a=3.14
if type(a) is float:
    print("it is float")'''


'''a=3.14
if type(a) is not float:
    print("it is float")'''


'''a="Guppu"
if type(a) is str:
    print("it is string")'''


'''a="Guppu"
if type(a) is not str:
    print("it is string")'''

'''a=3+4j
if type(a) is complex:
    print("it is complex")'''


'''a=3+4j
if type(a) is not complex:
    print("it is complex")'''

'''a=True
if type(a) is bool:
    print("it is bool")'''


'''a=True
if type(a) is not bool:
    print("it is bool")'''

#if- condition using membership operator
#in, not in

'''a=2,3,4,5,6,7,8
if 8 in a:
    print("true")'''

'''a=2,3,4,5,6,7,8
if 20 in a:
    print("true")'''

'''a=int(input("a value"))
if 30 in a:
    print("true")''' #error because we need to declare values in seperate key

'''a=2,3,4,5,6,7,8,9,10
b=int(input("value"))
if b in a:
    print("true")'''

#if-else conditions by using comparision operators
'''a=4
b=8
if a<b:
    print("less")
else:
    print("more")'''

'''a=4
b=8
if a>b:
    print("less")
else:
    print("more")'''

'''a=4
b=8
if a<=b:
    print("less")
else:
    print("false")'''

'''a=4
b=8
if a>=b:
    print("less")
else:
    print("false")'''

'''a=5
b=6
if a!=b:
    print("yes")
else:
    print("no")'''

'''a=4
b=4
if a==b:
    print("yes")
else:
    print("no")'''

#if-else conditions by using logical operator
#and,or,not

'''a=5
b=7
if a>b and b<a:
    print("true")
else:
    print("false")'''

'''a=7
b=2
if a<b or b>a:
    print("true")
else:
    print("false")'''

'''a=3
b=7
if not a<b and a>b:
    print("true")
else:
    print("false")'''


#if-else condition by using identity operator
#is,is not
'''a=6
if type(a) is int:
    print("true")
else:
    print("false")'''


'''a=3
if type(a) is not int:
    print("true")
else:
    print("false")'''


'''a=3.14
if type(a) is float:
    print("true")
else:
    print("false")'''


'''a=3.14
if type(a) is not float:
    print("true")
else:
    print("false")'''

'''a="Guppu"
if type(a) is str:
    print("true")
else:
    print("false")'''


'''a="Guppu"
if type(a) is not str:
    print("true")
else:
    print("false")'''

'''a=3+9j
if type(a) is complex:
    print("true")
else:
    print("false")'''
    

'''a=3+9j
if type(a) is not complex:
    print("true")
else:
    print("false")'''

'''a=True
if type(a) is bool:
    print("true")
else:
    print("false")'''


'''a=True
if type(a) is not bool:
    print("true")
else:
    print("false")'''

#if-else condition by using membership operator
#in,not in
'''a=2,3,4,5,6,7,8,9,10
b=int(input())
if b in a:
    print("yes")
else:
    print("no")'''

'''a=2,3,4,5,6,7,8,9,10
b=int(input())
if b not in a:
    print("yes")
else:
    print("no")'''
