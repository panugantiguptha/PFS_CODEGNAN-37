#module - math

'''import math
print(math.pi)
print(math.pi*4)
print(math.sqrt(2))
print(math.log(2))
print(math.tan(45))
print(math.cos(60))
print(math.sin(30))
print(math.pow(2,4))
print(math.ceil(6.9))
print(math.floor(3.11))'''

'''from math import pi,sqrt,log,tan
print(pi)
print(sqrt(4))
print(log(6))
print(tan(45))'''

#sys module

'''import sys
print(sys.version)
print(sys.path)'''

#os module

'''import os
print(os.path)
print(os.getcwd)
print(os.listdir)
print(os.chdir("C:\\Users\LENOVO\Downloads"))
print(os.listdir())'''

# random module = random module is used to generate a random numbers in python, randint function is used and this function is defined in random module. 

'''import random
a=random.sample(range(10,40),5)
print(a)


#randint()
import random
a=random.randint(50,60)
print(a)

#choice()
import random
a=[30,40,50,60,70]
b=random.choice(a)
print(b)'''

# ludo
'''import random
while True:
    input('enter the roll of dice:')
    a=random.randint(1,6)
    print(a)

    option=input('roll again?  (y/n) ')
    if option=='y':
        continue
    elif option=='n':
        break
    else:
        print('Invalid option')'''


