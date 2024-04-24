

# Perfect sqaure WAP to check if a number is perfect square ot not.

def is_perfect_square(num):
    square_root = num ** 0.5
    
    return square_root == int(square_root)

number = 16
if is_perfect_square(number):
    print(number, "is a perfect square.")
else:
    print(number, "is not a perfect square.")
