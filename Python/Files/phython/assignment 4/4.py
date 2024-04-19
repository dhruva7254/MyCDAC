l1=[5,6,7]
l2=[0,1]
l3=[]
for idx in range(0,len(l1),1):
    s1=str(l1[idx])
    print(s1)
    for idy in range(0,len(l2),1):
        s2=str(l2[idy])
        s3=int(s1+s2)
        l3.append(s3)
print(l3)



