l1=[]
for e in range(150,251,2):
 l1.append(e)
print(l1)
print(len(l1))
l2=[a for a in l1 if a%4==0]
print(l2)