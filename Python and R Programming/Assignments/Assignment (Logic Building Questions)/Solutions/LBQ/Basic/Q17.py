

# 17) Reverse a string.

def reverse_string(input_string):
    reversed_str = ""
    for char in input_string:
        reversed_str = char + reversed_str
    return reversed_str

original_string = "Hello, world!"
reversed_string = reverse_string(original_string)
print("Original:", original_string)
print("Reversed:", reversed_string)
