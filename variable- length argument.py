#Topic:varible length arguments
#variable length arguments are automatically stores in tuple and we use star arguments
'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7,8)
b=[2,3,4,5,6,7,8]
check(*b)
c={4,5,6,7,7,8,9}
check(*c)
d={"name":"guppu","age":22,"place":"vja"}
check(*d)#in dic it wil print only keys'''



#task
'''def check1(*a):
    d=1#checking a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
check1()
check1(2,3,4,5,6)
check1(1,3,5,2.3,4.3)
check1(4,3,6,2,3.4,2.3,"python")'''

#**(kwargs)
'''def check2(**a):
    print(a)
    print(type(a))
check2()
details={"names":["sweety","cuty","hearty"],
         "marks":[60,70,80],
         "status":["p","a","p"]}
check2(**details)'''

'''def check2(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
check2()
details={"names":["sweety","cuty","hearty"],
         "marks":[60,70,80],
         "status":["p","a","p"]}
check2(**details)'''


#both * and ** usuage
'''def final(*a,**b):
    d=1
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+1
        print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is",j)
final()
data=(2,3,4,5,6,2.3,4.5)
final(*data)
details={"year":[2024,2025,2026],
         "month":["june","july","aug"]}
final(**details)
final(*data,**details)'''

#Railway Ticket
'''Railway ticket we need to take gender male and female
divide male into 2 catagiries and female into two categiries
male >60 falt 30and <60 flat 100 in female >60 flat 50 and <60 flat 30'''

def railway(gender,age):
    ticket_price=1000
    if gender=="male":
        if age>60:
            discount=30
            final_price=ticket_price-(ticket_print*discont/100)
        else:
            final_price=ticket_price
    elif gender=="female":
        if age>60:
            final_prince=ticket_price-500
        else:
            final_price=ticket_price-700
    else:
        print("Not Valid")



