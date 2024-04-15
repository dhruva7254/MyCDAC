"""2. Given two strings, s1 and s2, create a new string by appending s2 in the middle of s1
Given:
s1 = "Ault"
s2 = "Kelly"
Expected Output:
AuKellylt"""

s1='Ault'
s2='Kelly'
l1=int(len(s1)//2)
s3=s1[:l1]+s2+s1[l1:]
print(s3)