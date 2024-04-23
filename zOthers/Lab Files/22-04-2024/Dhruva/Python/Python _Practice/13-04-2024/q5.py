"""5. create a third-string made of the first char of s1 then the last char of s2, Next, the second char of s1
and second last char of s2, and so on. Any leftover chars go at the end of the result.
Given:
s1 = "Abc"
s2 = "Xyz"
Expected Output:
AzbycX"""


"""s1='Abc'
s2='Xyz'
l1=int(len(s1)//2)
l2=int(len(s2)//2)
s3=s1[0]+s2[len(s2)-1]+s1[1]+s2[len(s2)-2]
s4=''
s6=s2[::-1]
print(s6)
#a=index(s1)
for i in range(len(s1)):
    s5=s1[i]+s6[i]
    #for j in range(1,len(s2)-1):
        #s4=s1[i]+s2[len(s2)-j]
#s3=s1[0]+s2[len(s2)-1]
print(s3)
#print(s4)
print(s5)"""

s1='Abcdef'
s2='Xyz'
s3=s2[::-1]
s4=''
for i in range(int(len(s1))):
    s4=s4+s1[i]+s3[i]
print(s4)

------------------------
s1=''
s2=''
s3=s2[::-1]
s4=''
s5=''
for e1,e3 in zip(s1,s3):
    s4=s4+e1+e3
if len(s1)==len(s2):
    print(s4)
elif len(s1)>len(s2):
    s5=s4+s1[len(s2):]
    print(s5)
    

