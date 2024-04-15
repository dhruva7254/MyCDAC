a=2
b=3
print(a,b)
c=b
b=a
a=c
print(a,b)

a=4
b=5
print(a,b)
a=a+b
b=a-b
a=a-b
print(a,b)

a=6
b=7
b , a = a , b
print(a,b)
