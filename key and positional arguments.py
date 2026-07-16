#key and positional arguments

'''def Details(id,name,mailid):
    id=10
    name="guppu"
    mailid="guppu@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''

'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id=20,name="manoj",mailid="m@gmmail.com")
Details(30,"harsha","h@gmail.com")
Details("t@gmail.com",40,"triandh")
Details(mailid="s@gmail.com",id="50",name="sai")'''

#default  arguments

'''def Grocery(item,price):
    print("item is %s"%item)
    print("price is %d"%price)
Grocery("sugar",200)'''

'''def Grocery(item="rice",price=1500):
    print("item is %s"%item)
    print("price is %d"%price)
Grocery()'''

'''def Grocery(item,price=200):
    print("item is %s"%item)
    print("price is %d"%price)
Grocery("dhal")'''

'''def Grocery(item="ghee",price):
    #it will be error beacause first one should be always empty.
    print("item is %s"%item)
    print("price is %d"%price)
Grocery(500)'''

#cake_name,price,qty

'''def party(cake_name,price,qty):
    print("cake is %s" %cake_name)
    print("price is %d" %price)
    print("qty is %d" %qty)
party("chocolate",1500,1)'''

'''def party(cake_name="chocolate",price=1500,qty=1):
    print("cake is %s" %cake_name)
    print("price is %d" %price)
    print("qty is %d" %qty)
party()'''

'''def party(cake_name,price=1500,qty=3):
    print("cake is %s" %cake_name)
    print("price is %d" %price)
    print("qty is %d" %qty)
party("chocolate")'''

#* arguments(* is used to unpack the elements)

#list
'''a=[2,3,4,5,6,7]
print(a)
print(*a)'''

#tuple
'''a=(2,3,4,5,6,7)
print(a)
print(*a)'''

#set
'''a={2,3,4,5,6,7}
print(a)
print(*a)'''

#dic
# in this it will print only keys
'''b={"name":"gupppu","city":"vja"}
print(b)
print(*b)'''

'''c="python"
print(c)
print(*c)'''

'''a,b,c=2,3,4,5,6,7,8,9,10
print(a)
print(b)
print(c)'''#error

'''a,b,c=2,3,4
print(a)
print(b)
print(c)'''

'''*a,b,c=2,3,4,5,6,7,8,9,10
print(*a)
print(b)
print(c)'''


'''a,b,c="codegnan"
print(a)
print(b)
print(c)'''#error

'''a,b,c="cod"
print(a)
print(b)
print(c)'''

'''a,*b,c="codegnan"
print(a)
print(*b)
print(c)'''













