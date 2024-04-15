"""7. Take two integer values in a & b. Swap their values using tuple, using temparary variable 
and without tuple and without temparary variable.
Ex. a=10 b=23
After swapping a=23 b=10"""

a, b = int(input("Enter value for a: ")), int(input("Enter value for b: "))
print("Original values: a =", a, ", b =", b)

# Using tuple
a, b = b, a
print("Swapped values using tuple: a =", a, ", b =", b)

# Using temporary variable
temp = a
a = b
b = temp
print("Swapped values using temporary variable: a =", a, ", b =", b)

# Without using tuple or temporary variable
a = a + b
b = a - b
a = a - b
print("Swapped values without tuple or temporary variable: a =", a, ", b =", b)
