"""4. Print two lists in the following order
list1 = [5, 6,7]
list2 = [0, 1]
output:
50,51,60,61,70,71"""

l1=[5, 6, 7]
l2=[0, 1]
l3=[str(l1[0])+str(l2[0]),]
print(str(l3))

l4=[]
for i in range(0,len(l1)):
    for j in range(0,len(l2)):
        l4.append(int(str(l1[i])+str(l2[j])))
print(l4)