
# WAP that accepts three integers from the user and return true if two or more of them (integers ) have 
# the same rightmost digit. The integers are non-negative

def same_rightmost_digit(num1, num2, num3):
    rightmost_digit_1 = num1 % 10
    rightmost_digit_2 = num2 % 10
    rightmost_digit_3 = num3 % 10
    
    if (rightmost_digit_1 == rightmost_digit_2 or
        rightmost_digit_1 == rightmost_digit_3 or
        rightmost_digit_2 == rightmost_digit_3):
        return True
    else:
        return False

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

result = same_rightmost_digit(num1, num2, num3)

print("Result:", result)
