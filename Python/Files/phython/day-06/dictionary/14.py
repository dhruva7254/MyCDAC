def multi(x,y):
    p=1
    for n in range(x,y+1,2):
        p=p*n
    return p
print(multi(1,100))    

def factorial(a):
    p=1
    for n in range(1,a+1):
        p=p*n
    return p
print(factorial(5)) 