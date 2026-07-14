#list Comprehension
a=["codegnan","python","course"]
#["CODEGNAN","PYTHON","COURSE"]
#print(a.upper())

'''b=str(a)
print(b.upper())'''

'''for i in a:
    print(i.upper(),end=",")'''

'''b=[]
for i in a:
    b.append(i.upper())
print(b)''' # this is without list comprehension

#by using list comprehension
#a=[exp for var in collection/range]
'''a=[i.upper() for i in a]
print(a)'''


#tasks
'''a=["vja","hyd","vzg"]
#["Vja","Hyd",Vzg"]
a=[i.title() for i in a]
print(a)'''

#task -2
'''a=[1,2,3,5,8,12,13]
#[1,4,9,25,64,144,169]
a=[i**2 for i in a]
a=[i*2 for i in a]
a=[pow(i,2) for i in a] #we can use any methods in there three
print(a)'''

#task -3

#if-usuage in list comprehention
'''a=[i for i in range(16)]
print(a)'''

#to print for even
'''a=[i for i in range(16) if i%2==0]
print(a)'''

#to print for odd
'''a=[i for i in range(16) if i%2!=0]
print(a)'''

#to print even and it should be square
'''a=[i**2 for i in range(21) if i%2==0]
print(a)'''

#to print "a" letter fruits

'''a=["apple","banana","grape","mango","kiwi","dragon","berry"]
b=[i for i in a if "a" in i]
print(b)'''

#to print not "a" letter fruits

'''a=["apple","banana","grape","mango","kiwi","dragon","berry"]
b=[i for i in a if "a" not in i]
print(b)'''

#no elif usuage in list comprehension

#if-else usuage in list comprehension
'''a=[i**2 if i%2==0 else i*5 for i in range(31)]
print(a)'''

a=[1,2,3,4,5]
b=[5,4,3,2,1]
#[6,6,6,6,6]
'''c=[a[i] +b[i] for i in range(len(a))]
print(c)'''#by uing length

c=[a[i] +b[i] for i in range(5)]
print(c)



