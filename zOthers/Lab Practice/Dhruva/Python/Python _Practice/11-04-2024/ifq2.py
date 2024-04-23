# accept amount from user and find the minimum number notes required to get the amount amount =512  
# Notes: 2000,500,100,50,10,5,2,1

# 500-1 note  
# 10  - 1 note  
# 2-  1 coin  

# amount=20550  
# 2000 – 10 note  
# 500 – 1 note  
# 50 -1 note  

amt=int(input("Enter the Amount Needed: "))

# n2000,n500,n100,n50,n10,n5,n2,n1 = 0

n2000=amt//2000
n500=amt//500
n100=amt//100
n50=amt//50
n10=amt//10
n5=amt//5
n2=amt//2
n1=amt//1

if(amt>2000):
    print("2000 - ",n2000," note")
    print("500 - ",n500," note")
    print("100 - ",n100," note")
    print("50 - ",n50," note")
    print("10 - ",n10," note")
    print("5 - ",n5," coin")
    print("2 - ",n2," coin")
    print("1 - ",n1," coin")
elif(amt>500):
    print("500 - ",n500," note")
    print("100 - ",n100," note")
    print("50 - ",n50," note")
    print("10 - ",n10," note")
    print("5 - ",n5," coin")
    print("2 - ",n2," coin")
    print("1 - ",n1," coin")
elif(amt>100):
    print("100 - ",n100," note")
    print("50 - ",n50," note")
    print("10 - ",n10," note")
    print("5 - ",n5," coin")
    print("2 - ",n2," coin")
    print("1 - ",n1," coin")
elif(amt>50):
    print("50 - ",n50," note")
    print("10 - ",n10," note")
    print("5 - ",n5," coin")
    print("2 - ",n2," coin")
    print("1 - ",n1," coin")
elif(amt>10):
    print("10 - ",n10," note")
    print("5 - ",n5," coin")
    print("2 - ",n2," coin")
    print("1 - ",n1," coin")
elif(amt>5):
    print("5 - ",n5," coin")
    print("2 - ",n2," coin")
    print("1 - ",n1," coin")
elif(amt>2):
    print("2 - ",n2," coin")
    print("1 - ",n1," coin")
else:
    print("1 - ",n1," coin")
