l1=["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
n=int(input("enter size of list: "))
l2=[]
for idx in range(n):
    elem=input(f"enter element no {idx+1}: ")
    l2.append(elem)
print(l2)    
for idx1 in range(len(l2)):
   l1[2][1][2].append(l2[idx1])
print(l1)
