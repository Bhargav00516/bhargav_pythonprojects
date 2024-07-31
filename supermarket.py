name=input("enter your name:")
#list of items
lists='''
rice - 20Rs/kg
sugar - 30Rs/kg
salt - 20Rs/kg
oil - 80Rs/lit
paneer - 110Rs/kg
maggi - 50Rs/kg
boost - 90Rs/each
collgate - 85Rs/each
'''
# we will define in predefine 
#intially we define just like a declaration
price=0
pricelist=[]
totalprice=0
finalfinalprice=0
ilist=[] # items ki list
qlist=[] #quantity list
plist=[] #price list
 
#rates which give life to above display data
items={'rice':20,
       'sugar':30,
       'salt':20,'oil':80,
       'paneer':110,
       'maggi':50,
       'boost':90,
       'collgate':85}

option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
# if i want to buy we will write forloop
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or press 2 for exit :"))
    if inp1==2:
        break
    if inp1==1:
        item=input("enter your items:")
        quantity=int(input("enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
         print("sorry you entered item is not available")
    
        inp=input("can i bill the items yes or no :")
if inp=="yes":
        pass
        if finalamount!=0:
           print(25*"=","supermarket",25*"=")
           print(28*" ","")
           print("Name:",name,30*" ","Date:")
           print(75*"-")
           print("sno",8*" ",'items',8*" ",'Quantity',3*" ",'price')
           for i in range(len(pricelist)):
            print(i,8*' ',5*' ',ilist[i],3*' ',qlist[i],8*" ",plist[i])
            print(75*"-")
            print(50*" ",'Totalamount:','Rs',totalprice)
            print("gst amount",40*" ",'Rs',gst)
            print(75*"-")
            print(50*"-",'finalamount:','Rs',finalamount)
            print(75*"-")
            print(50*" ",'finalamount:','Rs',finalamount)
            print(75*"-")
            print(20*" ","Thanks for visiting")
            print(75*"-")

            
