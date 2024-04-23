"""6. Find all occurrences of “USA” from right to left in a given string ignoring the case. also display the
starting position
Given:
str1 = "Welcome to USA. usa awesome, isn't it?
Expected answer : 16, 11
" usa usa usa usa usa usa "
"""


str1=""
str1=str1.lower()
print(str1.rfind("usa",0,len(str1)))

for idx in range(len):