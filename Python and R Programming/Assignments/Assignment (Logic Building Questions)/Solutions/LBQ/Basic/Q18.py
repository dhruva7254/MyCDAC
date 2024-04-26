

# 18) Reverse a number.

def reverse_number(num):
    reversed_num = int(str(num)[::-1])
    return reversed_num

original_number = 123456
reversed_number = reverse_number(original_number)
print("Original number:", original_number)
print("Reversed number:", reversed_number)

