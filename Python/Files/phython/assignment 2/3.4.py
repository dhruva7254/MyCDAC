p=1
s=0
count=0
for x in range(100):
    n=input("enter no or enter q to quit: ")
    if n=="q":
       break
    else:
        n1=int(n)
        p=p*n1
        s=s+n1
        count=count+1
if s==0:
 avg=0
 p=0
else:
 avg=s/count
print(f"product of given nos:{p}")
print(f"average of given nos:{avg}")         