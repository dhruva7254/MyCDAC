n1=int(input("enter 1st no: "))
n2=int(input("enter 1st no: "))
print("chose options","\n","a. add","\n","b. subtract","\n","c. divide","\n","d. multiply","\n","e. integer division",
      "\n","f. mod operation","\n","g. check if both numbers are same","\n","h. power operation","\n",
      "i. square root of both numbers","\n","j. log of both numbers","\n","k. gcd","\n","l. lcm")
c=input("enter choice: ")
if c=="a":
    print(f"addition of {n1}&{n2}:{n1+n2}")
if c=="b":
    print(f"subtraction of {n1}&{n2}:{n1-n2}")
if c=="c":
    print(f"division of {n1}&{n2}:{n1/n2}")
if c=="d":
    print(f"multiplication of {n1}&{n2}:{n1*n2}")
if c=="e":
    print(f"integer division of {n1}&{n2}:{n1//n2}")
if c=="f":
    print(f"mod of {n1}&{n2}:{n1%n2}")
if c=="g":
    if n1==n2:
        print(f"{n1}&{n2} are same")
    else:
        print(f"{n1}&{n2} are not same")    
if c=="h":
    p=int(input("enter power of both no: "))
    print(f"{n1} to the power {p}:{n1**p}")
    print(f"{n2} to the power {p}:{n2**p}")
if c=="i":
    print(f"squre root of {n1}:{n1**0.5}")
    print(f"squre root of {n2}:{n2**0.5}")
if c=="j":
    print(f"log of {n1}:{math.log10(n1)}")
    print(f"log of {n2}:{math.log10(n2)}")
if c=="k":
 gcf=1
 if n1==0:
     hcf=n2
 if n2==0:
     hcf=n1
 else:   
   if n1<=n2:
      for a in range(1,n1+1):
         if (n1%a==0)&(n2%a==0):
             n1=n1/a
             n2=n2/a
             gcf=gcf*a
   if n1>n2:
      for a in range(1,n2+1):
         if (n1%a==0)&(n2%a==0):
             n1=n1/a
             n2=n2/a
             gcf=gcf*a     
 print(f"gcf of {n1}&{n2}: {gcf}")         
if c=="l":
 gcf=1
 if n1==0:
     hcf=n2
 if n2==0:
     hcf=n1
 else:   
   if n1<=n2:
      for a in range(1,n1+1):
         if (n1%a==0)&(n2%a==0):
             n1=n1/a
             n2=n2/a
             gcf=gcf*a
   if n1>n2:
      for a in range(1,n2+1):
         if (n1%a==0)&(n2%a==0):
             n1=n1/a
             n2=n2/a
             gcf=gcf*a     
 n1=n1*gcf
 n2=n2*gcf
 lcm=(n1*n2)/gcf
 print(f"lcm of {n1}&{n2}: {lcm}")      
    