d={1:3,2:2}
lk=sorted(d,key=lambda e:d[e])
lv=[]
for e in lk:
    lv.append(d[e])
d1=dict(zip(lk,lv))    
print(d1)
