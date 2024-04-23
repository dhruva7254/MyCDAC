#9. Write a Python function that takes a number as a parameter and checks whether the number is prime or not. 
#Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.
def functionp9(n:int):
    count=0
    if (n==0)|(n==1)|(n<0):
       print(f"{n} is not prime no")
    else:
     for a in range(1,n+1):
        if n%a==0:
            count=count+1
     if count>2:
            print(f"{n} is not prime no")
     else:
            print(f"{n} is prime no")
print(functionp9(237))