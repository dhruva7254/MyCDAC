#1. Reverse the following tuple
#aTuple = (10, 20, 30, 40, 50,60)
#Expected output:
#(60,50, 40, 30, 20, 10)
t=(10, 20, 30, 40, 50,60)
l1=[]
for idx in range(0,len(t)):
    l1.append(t[idx])
l1=l1[::-1]    
t1=()
for e in l1:
    t1=t1+(e,)
print(t1)