ammt=int(input("enter ammount: "))
n1=n2=n3=n4=n5=n6=n7=n8=0
if ammt>=2000:
    n1=ammt//2000
    ammt=ammt%2000
if ammt>=500:
    n2=ammt//500
    ammt=ammt%500
if ammt>=100:   
    n3=ammt//100
    ammt=ammt%100
if ammt>=50:   
    n4=ammt//50
    ammt=ammt%50
if ammt>=10:   
    n5=ammt//10
    ammt=ammt%10
if ammt>=5:   
    n6=ammt//5
    ammt=ammt%5
if ammt>=2:   
    n7=ammt//2
    ammt=ammt%2
if ammt>=1:   
    n8=ammt//1
    ammt=ammt%1
print("2000 Rs: ",n1,"500 Rs: ",n2,"100 Rs: ",n3, "50 Rs: ",n4,"10 Rs: ",n5 ,"5 Rs: ",n6 ,"2 Rs: ",n7 ,"1 Rs: ",n8) 