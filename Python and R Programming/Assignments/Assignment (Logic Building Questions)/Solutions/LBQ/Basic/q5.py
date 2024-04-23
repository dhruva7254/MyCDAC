
# WAP to print numbers between 1 to 100 which are divisible by 3, 5 and by both
# ( total 3 list of numbers to be printed)

divisible_by_3 = []

divisible_by_5 = []

divisible_by_3_and_5 = []

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        divisible_by_3_and_5.append(num)
    elif num % 3 == 0:
        divisible_by_3.append(num)
    elif num % 5 == 0:
        divisible_by_5.append(num)

print("Numbers divisible by 3:", divisible_by_3)

print("Numbers divisible by 5:", divisible_by_5)

print("Numbers divisible by both 3 and 5:", divisible_by_3_and_5)

