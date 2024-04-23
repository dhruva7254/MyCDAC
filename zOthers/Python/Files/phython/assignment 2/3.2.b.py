n=int(input("enter size for pattern: "))
a=1
b=n//2
for x in range(n//2+1):
 print(" "*b,"*"*a," "*b,sep="")
 a=a+2
 b=b-1
b=1
a=n-2
for x in range(n//2):
 print(" "*b,"*"*a," "*b,sep="")
 a=a-2
 b=b+1