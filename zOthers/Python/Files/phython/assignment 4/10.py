n=int(input("enter size of list: "))
l1=[]
for idx1 in range(n):
    elem=int(input(f"enter elem{idx1+1}: "))
    l1.append(elem)
print(l1) 
#l1=[5, 20, 15, 20, 25, 50, 20]
x=int(input("enter no to be replaced: "))
y=int(input("enter no to be replaced with: "))
for b in range(l1.count(x)):
    idx=l1.index(x)
    l1[idx]=y
print(l1)