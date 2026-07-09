#loops()
#for,while,range,break,continue,pass
#for loop is sequence iteration
#in loop use end to print in single line

'''a=[10,20,30,40,50]
for i in a:
    print(i)'''
#in the above code it will print one after another

'''a=[10,20,30,40,50]
for i in a:
    print(a)'''
#in the above one it will print entire array

'''a=[10,20,30,40,50]
for i in a:
    print(i,end=" ")'''

#in the above one if we need in one line we need to use "end".

'''a=[10,20,30,40,50]
for i in a:
    print(i)
print(type(a))
print(type(i))'''


'''a=(5,6,7,8,9)
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a={10,20,30,40,50}
for i in a:
    print(i)
print(type(a))
print(type(i))'''


'''b={"year":2026,"month":"july","date":9}
for i in b:
    print(i)
print(type(b))
print(type(i))
for i in b.keys():
    print(i)
for i in b.values():
    print(i)
for i in b.items():
    print(i)
    print(type(b))
    print(type(i))'''

'''a="codegnan"
for i in a:
    print(i,end="")'''

'''b=[4.5,6.7,8.9]
for i in b:
    print(i)
print(type(b))
print(type(i))'''

''''b=["python","java","c","c++"]
for i in b:
    print(i)
    print(type(b))
    print(type(i))'''

'''b=[4+9j,3+2j]
for i in b:
    print(i)
    print(type(b))
    print(type(i))'''

'''b=[True,False]
for i in b:
    print(i)
print(type(b))
print(type(i))'''

'''fruits=["apples","banana","mango"]
#["APPLE","BANANA","MANGO"]
b=[]
for i in fruits:
    b.append(i.upper())
print(b)'''

a=[1,3,5,7,9,"code"]
#[1,3,5,7,9,"c","o","d","e"]
a.extend("code")
print(a)
