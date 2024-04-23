s=input("enter string: ")
cn=0
ci=0
ce=0
for idx in range(len(s)):
    if s[idx]==".":
        cn=cn+1
    if s[idx]=="?":
        ci=ci+1
    if s[idx]=="!":
        ce=ce+1
print("normal sentance:",cn)
print("intorgative sentence:",ci)   
print("exlametry sentance:",ce)
