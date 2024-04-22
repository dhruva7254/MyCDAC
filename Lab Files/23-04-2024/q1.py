
# WAP to print first 100 prime numbers

def prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

def no_prime(n):
    count = 0
    num = 2
    while count < n:
        if prime(num):
            print(num, end=" ")
            count += 1
        num += 1

no_prime(100)


