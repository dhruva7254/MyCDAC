a=abs(int(input("enter no: ")))
if (a%5==0) & (a%11==0) & (a>0):
    print("no is divisible by 5 and 11")
elif (a%5==0) & (a>0):
   print("no is divisible by 5") 
elif (a%11==0) & (a>0):
   print("no is divisible by 11") 
else:
   print("no is not divisible by 11 and 5") 