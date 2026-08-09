#Inheritance
#single inheritance

'''class RBI():#parent class
    cash=100000
    def available_cash(cls):
        #print("available_cash is",cls.cash)
        print("available_cash is",RBI.cash)
class SBI(RBI):
    pass
class HDFC(RBI):
    cash=50000
    def new_cash(cls):
        #print("new cash is",cls.cash+cls.cash)
        print("new cash is",cls.cash+RBI.cash)
a=HDFC()
a.available_cash()
a.new_cash()'''

#multiple inheritance

#this is without inheritance
'''class father():
    def height(cls):
        print("height is 5.5 inches")
class mother():
    def weight(cls):
        print("weight is 60kgs")
class kid():
    def dob(cls):
        print("just born.....")

a=father()
b=mother()
c=kid()
a.height()
b.weight()
c.dob()'''

#by using the inheritance

'''class father():
    def height(cls):
        print("height is 5.5 inches")
class mother():
    def weight(cls):
        print("weight is 60kgs")
class kid(father,mother):
    def dob(cls):
        print("just born.....")

c=kid()
c.height()
c.weight()
c.dob()'''

#multi-level inheritance

'''class grandparent():
    def acres(self):
        print("10 acres")
class parent(grandparent):
    def house(self):
        print("i have house")
class child(parent):
    def car(self):
        print("i have car")
a=child()
a.acres()
a.house()
a.car()'''

#hierarical inheritance
#hierarical inheritance means where one parent class is inherited by multiple child classes.

class employee():
    def company(self):
        print("codegnan it solutions")
class Trainer(employee): #child-1
    def Trainee(self):
        print("I will teach the code")
class developer(employee):#child-2
    def develop(self):
        print("I will develops the code")
a=Trainer()
a.Trainee()
a.company()
b=developer()
b.develop()
b.company()
