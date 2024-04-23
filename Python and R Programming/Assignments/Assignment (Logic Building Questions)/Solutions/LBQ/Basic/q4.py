
# WAP  to accept a number and check the number is even or not. Prints 1 if the number is even or 0 
# if the number is odd.

def check_even_or_odd(num):
    if num % 2 == 0:
        return 1  
    else:
        return 0  

num = int(input("Enter a number: "))

result = check_even_or_odd(num)

print(result)

