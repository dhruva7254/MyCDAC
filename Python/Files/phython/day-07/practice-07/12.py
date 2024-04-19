#12. Write a Python function that checks whether a passed string is a palindrome or not. 
#Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
def functionp12(s:str):
    s1=s[::-1]
    if s==s1:
        print("given string is palindrome ")
    else:
        print("given string is not palindrome ")
functionp12("madam")