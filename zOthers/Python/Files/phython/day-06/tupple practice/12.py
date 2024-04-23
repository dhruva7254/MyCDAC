t=(1,2,3)
t2=()
i=int(input("enter item to be removed: "))
for e in set(t):
    if e!=i:
        t2=t2+(e,)
t=t2
print(t)        