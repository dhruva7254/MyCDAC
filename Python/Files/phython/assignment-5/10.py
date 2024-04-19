s=input("enter string: ")
ca=0
cs=0
cn=0
for idx in range(len(s)):
    if s[idx].isalpha():
        ca=ca+1
    if s[idx].isnumeric():
        cn=cn+1
    if s[idx].isspace():
        cs=cs+1
cp=len(s)-(ca+cs+cn)
print("spaces:",cs)
print("special characters:",cp)   
print("alphabetical:",ca)
print("numeric:",cn)
   