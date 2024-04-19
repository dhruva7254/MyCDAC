s1=input("enter first string: ")
s2=input("enter second string: ")
indm=len(s1)//2
s3=s1[0:indm]
s4=s1[indm:len(s1)]
s=s3+s2+s4
print(s)