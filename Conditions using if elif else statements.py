#if-elif-else using comparision operator 
'''a=4
b=6
if a<b:
    print("less")
elif b>a:
    print("greater")'''
    

'''a=4
b=6
if a==b:
    print("less")
elif b<a:
    print("greater")
elif a!=b:
    print("not equal")'''



'''a=4
b=6
if a<b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''

'''a=4
b=6
if a==b:
    print("less")
elif b<a:
    print("greater")
else:
    print("true")'''


#if-elif-else by using logical operator

'''a=4
b=7
if a<b and b>a:
    print("true")
elif a>b or b<a:
    print("false")
else: 
    print("yes")'''

'''a=5
b=8
if a<b and b>a:
    print("yes")
elif a<b and not b!=a:
    print("true")'''

'''a=6
b=2
if a>b and b<a:
    print("yes")
elif not b==a:
    print("true")
else:
    print("false")'''

#if-elif-else by using identity operator

'''a=5
if type(a) is int:
    print("it is int")
elif type(a) is not int:
    print("false")'''

#if-elif-else by using membership operator

'''a=1,2,3,4,5,6,7,8,9,0
if 2 in a:
    print("yes")
elif 2 not in a:
    print("no")'''


#multiple-if  by using comparision operator

'''a=20
b=40
if a<b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("not equal")'''

'''a=20
b=40
if a==b:
    print("less")
if b>a:
    print("greater")
if a<b:
    print("true")'''

#multiple-if by using logical operator

'''a=20
b=40
if a<b and b>a:
    print("true")
if not a==b:
    print("false")
if a<=b or a!=b:
    print("yes")'''

#multiple-if by using identity operator

'''a=20
if type(a) is int:
    print("true")
if type(a) is float:
    print("yes")
if type(a) is not str:
    print("yess")'''

#multiple-if using membership operator

'''a=1,2,3,4,5,6,7,8,9,10
b=int(input())
if b in a:
    print("yes")
if b not in a:
    print("no")'''


#nested-if using comparision operator
#in this if first statement is false that it will be empty and won't go to next one
#if we use ifelse then it it will be print 

'''a=4
b=9
if a<b:
    print("less")
    if b>a:
        print("greater")'''

'''a=4
b=9
if a>b:
    print("less")
    if b>a:
        print("greater")'''


'''a=7
b=11
if a!=b:
    print("true")
    if b==a:
        print("greater")'''

'''a=7
b=11
if a!=b:
    print("true")
    if b==a:
        print("greater")
    else:
        print("false")'''

'''a=13
b=15
if a==b:
    print("true")
    if b>a:
        print("greater")
else:
    print("false")'''

'''a=7
b=11
if a!=b:
    print("true")
    if b==a:
        print("greater")
    else:
        print("false")
else:
    print("not true")'''

'''a=20
b=25
if a!=b:
    print("true")
    if b==a:
        print("greater")
    elif a<b:
        print("less")
    else:
        print("false")'''

'''a=int(input())
b=int(input())
if a!=b:
    print("true")
    if b==a:
        print("equal")
    elif b>a:
        print("greater")
    else:
        print("false")
else:
    print("program ends")'''

