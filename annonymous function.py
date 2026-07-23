#annonymous functions(nameless function)
#annonymous functions are nameless functions and we use a keyword called lamda to create annonymous functions.
#write a function to calculate 2*x+5 where x=5

'''def cal(x):
    print(2*x+5)
cal(5)'''

#this using the run time 
'''def cal():
    x=int(input())
    print(2*x+5)
cal()'''

#syntax
#a=lamda arg:expr

'''a=lambda x:2*x+5
print(a(5))'''

#this is by using the runtime
'''a=int(input())
b=lambda x:2*x+5
print(b(a))'''

#task 
'''a=lambda x,y=x*y
print(a(x,y))'''

#task
'''a=int(input())
b=int(input())
c=lambda a,b:a*b
print(c(a,b))'''

#task
#codegnan ->CODEGNAN

'''a=input()
b=lambda a:a.upper()
print(b(a))'''

#task
#a=python course ->Python Course
'''a=input()
b=lambda a:a.title()
print(b(a))'''

#task
#first_name + last_name=fullname
'''fname=input("first name:")
lname=input("last name:")
fullname=lambda fname,lname:(fname+" "+lname).title()
print(fullname(fname,lname))'''

'''fname,lname=[x for x in input("enter the names:").split(",")]
fullname=lambda fname,lname:(fname+" "+lname).title()
print(fullname(fname,lname))'''

#filter()
'''a=[10,30,50,100,127,39,45,67,200]'''
'''for i in a:
    if i%2==0:
        print(i)'''

'''b=list(filter(lambda x:x%2==0,a))
print(b)'''

'''a=[[],(),set(),{}," ",None,5,8.9,"python",5+9j,True,False]
b=list(filter(None,a))
print(b)'''

