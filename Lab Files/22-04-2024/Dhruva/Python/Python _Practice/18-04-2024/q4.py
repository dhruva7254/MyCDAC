
# Q Given list of employees. This list may contain repetitions. Find all unique employee names and 
# print them as per order of second character in that name. Use lambda function and normal function both.

words=["James","Robert","John","Michael","David","James"]
print(sorted(set(words), key = lambda s:s[1]))

def sec_char(s):
    return s[1]
words=["James","Robert","John","Michael","David","James"]
print(sorted(set(words), key = sec_char))

