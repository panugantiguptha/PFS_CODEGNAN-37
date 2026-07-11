#difference between break,continue and pass.
#Break is used to terminate the entire loop.
#continue is used to skip the current iteration and rest of the code will continue
#pass is a null statement it does nothing but systamatically we need.

#Break

'''a=10
while a>1:
    print(a)
    a=a-1'''

'''a=10
while a>1:
    print(a)
    a=a-1
    if a==6:
        break'''

'''a=10
while a>1:
    a=a-1
    if a==6:
        break
    print(a)'''

'''for i in range(20):
    if i==13:
        break
    print(i)'''

'''a="python"
if a=="h": 
    break
print(a)''' #error

'''a="python"
for i in a:
    if i=="h":
        break
    print(i)'''


#continue

'''a=20
while a>5:
    print(a)
    a-=1'''

'''a=20
while a>5:
    print(a)
    a-=1
    if a==10:
        continue''' # in this it will print entire code because print should be after continue

'''a=20
while a>5:
    a=a-1
    if a==10:
        continue
    print(a)'''

'''for i in range(15):
    if i==7:
        continue
    print(i)'''

'''a="python"
for i in a:
    if i=="y":
        continue
    print(i)'''

#pass

'''a=30
while a>10:
    print(a)
    a=a-1
    if a==20:
        pass'''

'''for i in range(40):
    if i==10:
        pass
    print(i)'''

#ATM APPLICATION

balance=100000
card=str(input("enter the card name: "))
password=int(input("enter the password: "))
if card=="c":
    if password=="1234":
        print("welcome")
        print("1.withdrawal")
        print("2.balance")
        option=input("enter the option: ")
        if option=="1":
            print("enter the amount: ")
            


    

                  
