# Q WA function to check if number is prime or not. Return True if number is prime and false if 
# number not prime.

def numpri(a:int):
    idx=2
    while(idx < (int(a**0.5) + 1)):
        if(a % idx) == 0:
            b='False'
            break
        idx +=1
    else:
        b='True'
        return b
c=int(input('Enter a number: '))
print(numpri(c)) 


