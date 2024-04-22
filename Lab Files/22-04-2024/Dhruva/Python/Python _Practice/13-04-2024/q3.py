"""3. two strings, s1, and s2 return a new string made of the first, middle, and last characters each input
string
Given:
s1 = "America"
s2 = "Japan"
Expected Output:
AJrpan
"""


s1='America'
s2='Japan'
l1=int(len(s1)//2)
l2=int(len(s2)//2)
s3=s1[:1]+s2[:1]+s1[l1:l1+1]+s2[l1-1:l1]+s1[len(s1)-1:len(s1)]+s2[len(s2)-1:len(s2)]
print(s3)
