#Q Given list of strings, sort all the strings by last character of that string. . 
#Use lambda function and normal function both.
l=["yash","kunjir","dbda","iacsd","cdac"]
print(sorted(l,key=lambda x:x[len(x)-1]))
def functiona3(s):
    return s[len(s)-1]
print(sorted(l,key=functiona3))
