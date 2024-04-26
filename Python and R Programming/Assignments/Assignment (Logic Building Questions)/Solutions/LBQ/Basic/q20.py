

# 20) Check Palindrome string.

def is_palindrome_string(input_string):
    input_string = ''.join(char.lower() for char in input_string if char.isalnum())
    return input_string == input_string[::-1]

string1 = "A man, a plan, a canal, Panama!"
string2 = "Hello, world!"

print("String 1 is a palindrome:", is_palindrome_string(string1))
print("String 2 is a palindrome:", is_palindrome_string(string2))
