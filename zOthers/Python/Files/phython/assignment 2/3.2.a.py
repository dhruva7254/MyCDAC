n=int(input("enter size for pattern: "))
a=1
b=n-1
for x in range(n):
 print("*"*a," "*b,sep="")
 a=a+1
 b=b-1