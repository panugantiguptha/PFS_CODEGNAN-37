#hybrid inheritance
#hybrid inheritance means combining more than one type of inheritance for example hierarical and multiple inheritance.
'''class person():
    def Detail(self):
        print("Trinadh")
class Trainer(person):
    def Teaching(self):
        print("trainer teach the subject")
class Student(person):
    def Study(self):
        print("preparing for exams")
class program_manager(Trainer,Student):
    def manager(self):
        print("assign the classes")
c=program_manager()
c.Detail()
c.Teaching()
c.Study()'''


#super function

'''class parent():
    def __init__(self,name):
        self.name=name
        print("parent constructor")
class child(parent):
    def __init__(self,name,age):
        self.age=age
        super().__init__(name)
        print("child constructor")
a=child("trinadh",22)
print(dir(a))
print(a.name)
print(a.age)'''


#encapsulation 
#publicdata()

'''class parent():
    publicdata=100
    def method1(self):
        print(self.publicdata)
class child(parent):
    def method2(self):
        print(self.publicdata)
obj1=child()
obj1.method1()
obj1.method2()'''

#_protecteddata()

'''class parent():
    _protecteddata=10
    def method1(self):
        print(self._protecteddata)
class child(parent):
    def method2(self):
        print(self._protecteddata)
obj1=child()
obj1.method1()
obj1.method2()
print(obj1._protecteddata)'''

#privatedata()

class parent():
    __privatedata="trinadh"
    def method1(self):
        print(self.__privatedata)
class child(parent):
    def method2(self):
        print(self._parent__privatedata)
obj1=child()
obj1.method1()
obj1.method2()
