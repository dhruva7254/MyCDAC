

# Armstrong Number.
#     It is a number with 'n' digits. Here (sum of every digit ^ n) equal to ( number itself)
#     1) 1^3 5^3 3^3=153 ( here number of digits(n) is 3)
#     2) 1^1 = 1 ( here number of digits is 1)
#     3) 1634 = 1^4 + 6^4 + 3^4 + 4^4 ( here number of digits is 4)

def is_armstrong(num):
    num_digits = len(str(num))
    
    sum_of_digits = sum(int(digit) ** num_digits for digit in str(num))
    
    return sum_of_digits == num

number = 153
if is_armstrong(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")
