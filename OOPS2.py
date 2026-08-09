#oops
#syntax
'''class classname():
    #attributes
    name="trinadh"
    age=22
    place="ong"
    def fname(method_name):
        print("statements.......")
a=classname()
a.fname()'''

#class declaration
'''class Details():
    name="trinadh"
    age=22
    place="ong"
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.display()'''

#object instatination
'''class Details():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.data("trinadh",22,"ong")
a.display()
b=Details()
b.data("harsha",22,"vja")
b.display()'''

#object initialization
'''class Details():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details("satish",50,"ong")
print(dir(a))
a.display()'''

#object runtime
'''class Details():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
name=input("Enter the name:")
age=int(input("Enter the age:"))
place=input("Enter the place:")
a=Details(name,age,place)
print(dir(a))
a.display()'''

#Another method 

'''class Details():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details(input("name:"),int(input("age:")),input("place:"))
print(dir(a))
a.display()'''

#Another method 

'''class Details():
    def __init__(self):
        self.name=input("name:")
        self.age=int(input("age:"))
        self.place=input("place:")
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.display()'''

#diff blw _ and __

'''class employee():
    def __init__(self):
        self.name="trinadh"
        self._mailid="panugantiguptha2004@gmail.com"
        self.__salary=10000
a=employee()
print(dir(a))
print(a.name)
print(a._mailid)
print(a._employee__salary)'''
#print(a.__salary) it will be error beacuse it should declare with the class name and the attribute

#task

'''class employee1():
    def __init__(self):
        self.name="trinadh"
        self._mailid="panugantiguptha2004@gmail.com"
        self.__salary=10000
class employee2():
    def __init__(self):
        self.name="satish"
        self._mailid="spsatishbabu@gmail.com"
        self.__salary=50000
class employee3():
    def __init__(self):
        self.name="padmaja"
        self._mailid="padmajapanuganti@gmail.com"
        self.__salary=20000
        
a=employee1()
print(a.name)
print(a._mailid)
print(a._employee1__salary)

a=employee2()
print(a.name)
print(a._mailid)
print(a._employee2__salary)

a=employee3()
print(a.name)
print(a._mailid)
print(a._employee3__salary)'''

#operator overloading

'''a=2;b=4
print(a+b)
print(a.__add__(b))
print(a.__add__(5))
print(a.__sub__(1))
print(a.__mul__(10))
#print(a.__div__(2)) it will show the error beacause it doesn't have the div variable.
print(a.__pow__(2))
print(a.__ge__(7))
print(a.__le__(10))
print(a.__eq__(2))
a=[2,3,4,5,6,7,8];b=[4,5,6,7,8,9,10]
print(a+b)
print(a.__add__(b))
print(a.__getitem__(2))
print(b.__getitem__(5))
a="code";b="gnan"
print(a+b)
print(a.__add__(b))
a="python";b="course"
print(a.__add__(" "+b).title())
print("trinadh".__add__(" "+"p"))'''

#operator overriding

'''class A():
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
x=A(5)
y=B(4)
#x=5
#y=4
print(x+y)'''


#Method Overloading

'''class new():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("the sum is",a+b+c)
        elif a!=None and b!=None:
            print("the product is",a*b)
        else:
            print("program ends")
a=new()
a.sum()
a.sum(2,4,6)
a.sum(6,3)'''

#Method Overriding

'''class Animal():
    def speak(self):
        print("animals can make sounds")
class Dog():
    def speak(self):
        print("dog barks")
a=Animal()
b=Dog()
a.speak()
b.speak()'''

#task

'''class Car():
    def vehicle(self):
        print("Hyundai")
class Bike():
    def vehicle(self):
        print("Pulsar")
b=Car()
b.vehicle()
c=Bike()
c.vehicle()'''
