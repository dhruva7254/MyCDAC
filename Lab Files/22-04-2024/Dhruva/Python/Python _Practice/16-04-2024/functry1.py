def numdiv11(d:list):
    f=[e for e in d if e%11==0]
    return f
g=[11,25,35,66,99,100]
h=[]
num=int(input('enter length of list: '))
for i in range(1,num+1):
    h.append(int(input('enter list values : ')))
print(h)
print(numdiv11(h))