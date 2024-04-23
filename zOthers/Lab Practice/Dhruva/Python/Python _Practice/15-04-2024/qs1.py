# 1. Write a Python program to create a set.

s1=set('string')
print(s1)

# 2. Write a Python program to iterate over sets.

s2={4,5,6,7}
for i in s2:
    print(i)

# 3. Write a Python program to add member(s) to a set.

s3={1,2,3,4}
s3.add(5)
print(s3)

# 4. Write a Python program to remove item(s) from a given set.

s4={6,7,8,9}
s4.remove(9)
print(s4)

# 5. Write a Python program to remove an item from a set if it is present in the set.

s5={1,3,5,7,9}
s5.discard(2)
print(s5)
s5.discard(5)
print(s5)

# 6. Write a Python program to create an intersection of sets.

s6={1,2,3,4,5}
s7={1,3,5,7,9}
print(s6.intersection(s7))

# 7. Write a Python program to create a union of sets.

s8={1,3,5}
s9={2,4,6}
print(s8.union(s9))

# 8. Write a Python program to create set difference.

s10={2,3,4}
s11={2,4,5}
print(s10.difference(s11))

# 9. Write a Python program to create a symmetric difference.

s12={1,2,3}
s13={1,4,5}
print(s12.symmetric_difference(s13))

# 10. Write a Python program to check if a set is a subset of another set.

s14={1,3}
s15={1,2,3,4,5}
print(s14.issubset(s15))

# 11. Write a Python program to create a shallow copy of sets.

# Note : Shallow copy is a bit-wise copy of an object. A new object is created that has an exact copy of the values in the original object.

s16={1,3,5}
print(s16.copy())

# 12. Write a Python program to remove all elements from a given set.

s17={1,2,3,4,5}
print(s17.clear())

# 13. Write a Python program that uses frozensets.
# Note: Frozensets behave just like sets except they are immutable.

s18=frozenset([10,45,(22,55)])
print(s18)

# 14. Write a Python program to find the maximum and minimum values in a set.

s19={1,3,5,7,9}
print(max(s19))
print(min(s19))

# 15. Write a Python program to find the length of a set.

s20={1,2,3,4}
print(len(s20))

# 16. Write a Python program to check if a given value is present in a set or not.



# 17. Write a Python program to check if two given sets have no elements in common.



# 18. Write a Python program to check if a given set is a superset of itself and a superset of another given set.



# 19. Write a Python program to find elements in a given set that are not in another set.



# 20. Write a Python program to remove the intersection of a second set with a first set.