
# Q Given list of strings, sort all the strings by last character of that string.
# Use lambda function and normal function both.

words=["James","Robert","John","Michael","David"]
print(sorted(words, key = lambda s:s[-1]))

def sec_char(s):
    return s[-1]
words=["James","Robert","John","Michael","David"]
print(sorted(words, key = sec_char))

