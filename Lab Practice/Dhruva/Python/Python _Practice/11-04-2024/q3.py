"""
n=int(input("Enter a num: "))
for m in range(1,n):
    print("*"*m)
"""

n=int(input("Enter no of lines: "))
count=0
stars=1
spaces=n//2
while(count<(n//2 +1)):
    print(" "*spaces,"*"*stars,sep="")
    spaces-=1
    stars+=2
    count+=1
