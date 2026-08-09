#Abstraction:
#hiding unnessesary information from user is called abstaraction.

#Abstract class:
#In abtract class have one or more abstract methods is called abstract class.

#Abstract method:
#the method declared without implementation is called abstract method.

#abstaction

'''class A():
    def method1(self):
        pass
obj1=A()
obj1.method1()'''

#here the print statement is declared

'''class A():
    def method1(self):
        print("python")
obj1=A()
obj1.method1()'''


'''from abc import ABC,abstractmethod
class A():
    def method1(self):
        print("data")
obj1=A()
obj1.method1()'''

#in the above code it will be error next code it will be fixed beacause we have to use one or more abstract classes 

'''from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        print("codegnan")
obj1=A()
obj1.method1()'''

'''from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("python course")
    @abstractmethod
    def method3(self):
        pass
class B(A):
    def method1(self):
        print("data science")
    def method3(self):
        print("machine learning")
obj1=B()
obj1.method1()
obj1.method2()
obj1.method3()'''



