#14. Write a Python function to check whether a string is a pangram or not. 
#Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
#For example : "The quick brown fox jumps over the lazy dog"
def functionp14(s:str):
    s=s.lower()
    s1=""
    for e in s:
        if (e not in s1)&(e.isalpha()):
            s1=s1+e
    if len(s1)==26:
        print("given string is panagram")        
    else:
        print("given string is not panagram")
functionp14("Go, lazy fat vixen; be shrewd, jump quick.")