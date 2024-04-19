s=input("enter string with odd length>7: ")
if len(s)>7 & len(s)%2!=0:
 idexm=len(s)//2
 sm=s[idexm-1:idexm+2]
 print(sm)
else:
 print("invalid string") 