s=int(input("enter size of set: "))
s1=set()
for a in range(s):
    e=int(input(f"enter element{a}: "))
    s1.add(e)
print(s1) 
s=int(input("enter size of set: "))
s2=set()
for a in range(s):
    e=int(input(f"enter element{a}: "))
    s2.add(e)
print(s2) 
print(s1|s2)