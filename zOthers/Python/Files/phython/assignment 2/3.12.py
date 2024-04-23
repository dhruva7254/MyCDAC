n=int(input("enter no: "))
s=0
if n%2==0:
 for a in range(1,n,2):
    s=s+a
else:
  for a in range(1,n+1,2):
     s=s+a  
print(f"sum of odd no till {n} is {s}")    