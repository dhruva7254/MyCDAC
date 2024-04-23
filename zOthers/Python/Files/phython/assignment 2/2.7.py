u=int(input('enter units:'))
a1=a2=a3=0
if u<=100:
    a1=u*0
    print("ammount: ",a1)
if 200>=u>100:
    a2=(u-100)*5+100*0
    print("ammount: ",a2)
if u>200:
    a3=(u-200)*10+100*5+100*0
    print("ammount: ",a3)
