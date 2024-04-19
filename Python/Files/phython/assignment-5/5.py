sa=input("enter first string: ")
sb=input("enter second string: ")
s=""
#for idx in range(0,len(sa)):
   # s=s+sa[idx]+sb[-(idx+1)]
#for idx1,idx2 in zip(range(0,len(sa)),range(len(sb)-1,-1,-1)):
 #   s=s+sa[idx1]+sb[idx2]
#print(s)
if len(sa)<=len(sb):
 for idx in range(len(sa)):
    s=s+sa[idx]+sb[-(idx+1)]
if len(sa)>len(sb):
 for idx in range(len(sb)):
    s=s+sa[idx]+sb[-(idx+1)]
print(s)