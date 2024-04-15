n=int(input("Enter no of lines: "))
count=0
stars=1
spaces=n//2
while(count<(n//2 +1)):
    print("*"*spaces," "*stars,"*"*spaces,sep="")
    spaces-=1
    stars+=2
    count+=1
count=0
stars=n-2
spaces=1
while(count<(n//2)):
    print("*"*spaces," "*stars,"*"*spaces,sep="")
    spaces+=1
    stars-=2
    count+=1