n1=int(input("enter size of first list: "))
l1=[]
for idx1 in range(n1):
  a1=int(input("enter no: "))
  l1.append(a1)
print(l1)
n2=int(input("enter size of second list: "))
l2=[]
for idx2 in range(n2):
  a2=int(input("enter no: "))
  l2.append(a2)
print(l2)
l3=l2[::-1]
if len(l1)>len(l3):
  for e1 in range(len(l3)):
    print(l1[e1],l3[e1])
else:
  for e1 in range(len(l1)):
    print(l1[e1],l3[e1])
