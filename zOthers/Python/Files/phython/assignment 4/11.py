n=int(input("enter size of list: "))
l1=[]
for idx1 in range(n):
    elem=int(input(f"enter elem{idx1+1}: "))
    l1.append(elem)
print(l1)
l1.sort(reverse=True)
nmax=int("".join([str(i) for i in l1]))
print(f"maximun no: {nmax}")
l1.sort(reverse=False)
nmin=int("".join([str(e) for e in l1]))
print(f"minimum no: {nmin}")