"""
2. take a list 'l1' of even nos between 150 to 250. Print its length.
Then create another list 'l2' using 'l1', containing only nos divisible by 4 from 'l1'.
"""

l1=[152,154,156,158]
print(len(l1))
l2=[e for e in l1 if e%4==0]
print(l2)



l3=[]
for i in range(152,250,2):
    l3.append(i)
    print(l3)
print(l3)
print(len(l3))
l4=[e for e in l3 if e%4==0]
print(l4)
print(len(l4))


