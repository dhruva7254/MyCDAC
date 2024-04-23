#WA function to take string as parameter Check if string is palindrome or not
#If palindrome return 1
#if not palindrome return 0
def stringpalindrome(s):
    s1=s[::-1]
    if s1==s:
        return 1
    else:
        return 0
print(stringpalindrome("boo"))    
