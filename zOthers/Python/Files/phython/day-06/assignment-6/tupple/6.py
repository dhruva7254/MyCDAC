#6. Modify the first item (22) of a list inside a following tuple to 200
t=(11, [22, 33], 44, 55)
#Expected output:
#tuple1: (11, [200, 33], 44, 55)
l=[]
for e in t:
    l.append(e)
l[1][0]=200
t=()
for e in l:
    t=t+(e,)    
print(t)