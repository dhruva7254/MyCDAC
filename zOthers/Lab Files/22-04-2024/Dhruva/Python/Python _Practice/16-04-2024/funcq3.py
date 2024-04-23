# Q WA function to take string as parameter
# Check if string is palindrome or not
# If palindrome return 1
# if not palindrome return 0

def strpal(a:str):
    if a==a[::-1]:
        b=1
    else:
        b=0
    return b
c=str(input('Enter a string: '))
print(strpal(c))

