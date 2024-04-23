"""4. Given an input string with the combination of the lower and upper case arrange characters in such a
way that all lowercase letters should come first."""


s1=str(input("Enter a String: "))
print(s1)

s2=''
s3=''
s4=''

for i in s1:
    if i.islower():
        s2=s2+i
for i in s1:
    if i.isupper():
        s3=s3+i

s4=s2+s3

#print(s2)
#print(s3)
print(s4)

# QwertYuiop
# s5="".join(sorted(s1))
# print(s5)