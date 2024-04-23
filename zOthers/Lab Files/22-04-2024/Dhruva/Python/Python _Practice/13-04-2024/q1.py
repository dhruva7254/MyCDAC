
"""1. Given a string of odd length greater than 7, return a new string made of the middle three characters
of a given String
Given:
str1 = "RakeshzipPetabb"
Output
zip
str2 = "JazzbonAyxx"
Output
bon"""

str1="RakeshzipPetabb"

# print(str1) 
# str2=str1[6:9:1]
# print(str2)

length1=int(len(str1)//2)
print(length1)
str3=str1[length1-1:length1+2:1]
print(str3)