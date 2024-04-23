#Write a Python function to check whether a number falls within a given range. 
def functionp6(a,b,c):
    if b<=a<=c:
        print(f"{a} is in range of {b}&{c}")
    else:
        print(f"{a} is not in range of {b}&{c}")
functionp6(3,1,6)