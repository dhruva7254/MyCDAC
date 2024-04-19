#WA function to check if number is prime or not. Return True if number is prime and false if number not prime.
def primenotest(n:int):
    count=0
    if (n==0)|(n==1)|(n<0):
       return False
    else:
     for a in range(1,n+1):
        if n%a==0:
            count=count+1
        if count>2:
            return False
        else:
            return True
print(primenotest(1))          