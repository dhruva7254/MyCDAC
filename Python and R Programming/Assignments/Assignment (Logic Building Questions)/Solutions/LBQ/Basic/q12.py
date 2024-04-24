

# Factorial of a number using loop
#     n! = n * (n-1) * (n-2) * ... *2*1

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = 5
print("Factorial of", num, "is", factorial(num))

