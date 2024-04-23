n=int(input("enter integer: "))
b=bin(n)
c1=0
c0=0
for idx in range(2,len(b)):
  if b[idx]=="1":
     c1=c1+1
  if b[idx]=="0":
     c0=c0+1
print("no of 1ns:",c1)    
print("no of 0ns:",c0)  