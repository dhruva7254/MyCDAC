#4. set of all elements in either A or B, but not both
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
#Expected output:
#{20, 70, 10, 60}
s1=set1|set2
s2=set1&set2
print(s1-s2)
