"""
6. Remove empty strings from the list of strings
list1 = ["Ashish", "", "Atharva", "Amit", "", "Revati"]
output:
["Ashish", "Atharva", "Amit", "Revati"]
"""

l1=["Ashish", "", "Atharva", "Amit", "", "Revati"]
l2=[e for e in l1 if str(e)!=""]
print(l2)
