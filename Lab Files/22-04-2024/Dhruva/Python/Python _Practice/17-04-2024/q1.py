
# WAP to print first 100 prime numbers

def numpri(a:int):
    idx=2
    while(idx < (int(a**0.5) + 1)):
        if(a % idx) == 0:
            b='False'
            break
        idx +=1
    else:
        b=a
        return b
c=int(input('Enter a number: '))
for i in range(2,c+1):
    print(numpri(i)) 