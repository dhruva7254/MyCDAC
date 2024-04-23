
# Factorial Program using Recursion
#     n! = n * (n-1) * (n-2) * ... *2*1

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter a number to calculate its factorial: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(number)
    print("Factorial of", number, "is:", result)
