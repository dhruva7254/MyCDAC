#Q Sort all the characters of given string using lambda function
s="ghjvbrueg"
l=sorted(s,key=lambda x:x)
s=""
for e in l:
  s=s+e
print(s)  