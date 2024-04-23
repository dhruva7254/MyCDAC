s=int(input("enter size of tupple: "))
t=()
for a in range(s):
    e=int(input(f"enter element{a}: "))
    t=t+(e,)
print(t)    
d={}
for idx in range(len(t)):
    d[t[idx]]=t[idx]
print(d)    