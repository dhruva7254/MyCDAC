
n=int(input("enter size of list: "))
l1=[]
for idx in range(n):
    elem=int(input(f"enter element no {idx+1}: "))
    l1.append(elem)
print(l1)
x=int(input("enter element to be replaced: "))
y=int(input("enter elemrnt to be replaced with: "))    
for a in range(len(l1)):
 idx1=l1.index(10)
 l1[idx1]=y
print(l1)