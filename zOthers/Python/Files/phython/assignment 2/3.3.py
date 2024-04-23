n1=int(input("enter first non-negative no: "))
n2=int(input("enter second non_negative no: "))
hcf=1
if n1==0:
    hcf=n2
if n2==0:
    hcf=n1
else:    
 if n1<=n2:
    for a in range(1,n1+1):
        if(n1%a==0)&(n2%a==0):
            n1=n1//a
            n2=n2//a
            hcf=hcf*a
 if n1>n2:
    for a in range(1,n2+1):
        if(n1%a==0)&(n2%a==0):
            n1=n1//a
            n2=n2//a
            hcf=hcf*a            
print(f"HCF of input nos is {hcf}")

