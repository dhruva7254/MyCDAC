"""""""""3. Given a Python list of numbers. Turn every item of a list into its square root
aList = [1, 4, 9, 16, 25, 36, 49] 
output:
[1, 2, 3, 4, 5, 6, 7]"""
""""""
l1=[1, 4, 9, 16, 25, 36, 49]
l2=[int(e**0.5) for e in l1]
print(l2)