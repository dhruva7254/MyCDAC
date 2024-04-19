s=int(input("enter size of tupple: "))
t=()
for a in range(s):
    e=int(input(f"enter element{a}: "))
    t=t+(e,)
print(t)    
e1=int(input("enter element: "))
for idx in range(0,len(t)):
    if t[idx]==e1:
       print(f"index of {e1}:{idx}")
    elif e1 not in set(t):
       print(f"element {e1} is not part of tupple")