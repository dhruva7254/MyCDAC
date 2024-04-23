#s=input("enter string: ")
#l="".join(e for e in s if e.islower())
#u="".join(e for e in s if e.isupper())
#s1=l+u
#print(s1)

s=input("enter string: ")
s1=""
s2=""
for idx in range(len(s)):
    if s[idx].islower():
       s1=s1+s[idx]
    else:
       s2=s2+s[idx]  
s3=s1+s2
print(s3)