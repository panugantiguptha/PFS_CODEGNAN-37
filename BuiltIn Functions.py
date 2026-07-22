#Built-In Functions 
#directory dir() means collection of files.
#print(dir())

#print(dir("_builtin_"))

#fromkeys()

'''a="codegnan"
print(a)
print(list(a))
print(tuple(a))
print(set(a))'''
#print(dict(a)) #dic won't print, to print this we are using fromkeys().

'''b=dict.fromkeys(a)
print(b)

c=dict.fromkeys(a,"Guppu")
print(c)

c["d"]="python"
print(c)'''


#eval()
'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)'''
    
'''while True:
    a=float(input("a value"))
    b=float(input("b value"))
    print(a+b)'''

'''while True:
    a=eval(input("a value"))
    b=eval(input("b value"))
    print(a+b)'''

#zip()->we can combine multiple collecions into one connection.
'''a=[10,20,30,40,50,60]
names=["khushal","manoj","harsha","sumanh","gopi"]
print(a+names)'''

'''b=zip(a,names)
print(b)'''

'''c=list(zip(a,names))
print(c)

c=tuple(zip(a,names))
print(c)

c=set(zip(a,names))
print(c)

c=dict(zip(a,names))
print(c)'''

#enumerate()-> we can give counter to the collection

'''names=["nikitha","taruni","siri","kalyani","prameela"]'''
'''for i in range(len(names)):
    print(i,names[i])'''

'''b=list(enumerate(names))
print(b)

b=list(enumerate(names,10))
print(b)

b=list(enumerate(names,100))
print(b)'''

#ASCII (American standard code for information interchange)

#char()
#ord()

'''print(chr(65))

print(chr(90))

#The ascii values from capital letters are from 65 to 90 other than that it will print some other values

print(chr(92))

print(ord("a"))

print(ord("z"))

print(chr("y"))''' #it will show error so we need to use only integer in chr.

#task1
#ASCII

'''for i in range(65,91):
    print(chr(i),end=" ")
print()
for i in range(97,123):
    print(chr(i),end=" ")'''

#task2
'''n=input("Enter the name:")
for i in n:
    print(i,"-",ord(i))'''

#task3
#BMI
while True:
    w=eval(input("Enter the Weight:"))
    h=eval(input("Enter the Height:"))
    bmi=w/h**2
    if bmi<18.5:
        print("Under Weight")
    elif bmi>18.5 and bmi<=24.5:
        print("Healty Weight")
    elif bmi>24.5 and bmi<29.5:
        print("Over Weight")
    else:
        print("Obesity")

