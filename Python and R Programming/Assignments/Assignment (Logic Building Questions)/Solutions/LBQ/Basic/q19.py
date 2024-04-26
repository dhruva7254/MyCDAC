

# 19) Check Palindrome number

def is_palindrome_number(num):
    return str(num) == str(num)[::-1]

number1 = 12321
number2 = 12345

print(number1, "is a palindrome number:", is_palindrome_number(number1))
print(number2, "is a palindrome number:", is_palindrome_number(number2))
