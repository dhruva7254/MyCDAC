#l1=[1,4,9,16,25,36,49]
n=int(input("size of list: "))
l1=[]
for idx in range(n):
    elem=int(input(f"enter element {idx+1}: "))
    l1.append(elem)
print(l1)
print([e**0.5 for e in l1])    























