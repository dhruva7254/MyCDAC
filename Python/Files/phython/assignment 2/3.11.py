n=int(input("enter no: "))
count=0
if n>1:
    for a in range(1,n+1):
        if n%a==0:
            count=count+1
    if count>2:
        print(f"{n} is not prime no")
    else:
        print(f"{n} is prime no")         
else:
    print(f"{n} is not prime no")    