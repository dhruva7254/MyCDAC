l1=[1,2,3]
l2=[100,200,300]
# expecte o/p
# 1  300
# 2  200
# 3  100
# l1=[1,2]
# l2=[67,78,90]
# l1=[1,2,3]
# l2=[45,56]
l3=l2[::-1] # reverse l2
#if(len(l2) < len(l1)):
# ....
#else:
for idx in range(len(l1)):
    print(l1[idx],l3[idx])

#zip function
l3=l2[::-1]
for e1,e2 in zip(l1,l3):
    print(e1,e2)
