no=int(input("Enter a no"))
idx=2
while(idx<(no//2 + 1)):
    if(no % idx) == 0:
        print("not a prime")
        break
    idx +=1
else:
    print("prime")     

#while(idx < (int(no**0.5) + 1)):
