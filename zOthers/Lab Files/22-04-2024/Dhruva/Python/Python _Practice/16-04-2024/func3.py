def fact(n:int):
    mul=1
    for i in range(2,n+1):
        mul*=i
    return mul
print(fact(100))
