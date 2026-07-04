#print(2+3)

'''a=5
b=7
print(a+b)'''

'''a=4
b=8
c=a+b
print(c)'''

#run_time input()
'''a=int(input("enter the a value "))
b=int(input("enter the b value "))
print(a+b)'''

'''a=float(input("enter the value"))
b=float(input("enter the value"))
print(a+b)'''

'''a=str(input("enter the value"))
b=str(input("enter the value"))
print(a+b)'''


'''a=bool(input("enter the value"))
b=bool(input("enter the value"))
c=bool(input("enter the value"))
print(a+b+c)'''

'''a=complex(input("enter the vaule"))
b=complex(input("enter the value"))
print(a+b)'''

'''fname=input("first name")
lname=input("last name")
print((fname+" "+lname).title())'''

'''a=int(input("a value"))
b=int(input("b value"))
option=int(input(choose the option
           add
           sub
           mul))
print(a+b)
print(a-b)
print(a*b)'''

'''a=input()
print(a)'''



#swapping of 2 varibles

#method 1
'''a=int(input())
b=int(input())
a,b=b,a
print(a,b)'''

#method 2
'''a=int(input())
b=int(input())
temp=a
a=b
b=temp
print(a,b)'''

#method 3
'''a=10
b=20
a=a+b
b=a-b
a=a-b
print(a,b)'''

#method 4
'''a=10
b=20
a=a+b
b=a-b
a=a-b
print("after swapping a=%d,b=%d" %(a,b))'''

# in float
'''a=float(input())
b=float(input())
a=a+b
b=a-b
a=a-b
print("after swapping a=%.2f,b=%.2f" %(a,b))'''

#in string
a=input()
b=input()
a,b=b,a
print("after swapping a=%s,b=%s" %(a,b))
