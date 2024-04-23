#1. Write a Python function to find the maximum of three numbers. 
def functionp1(a,b,c):
    if a>b:
        if a>c:
            print(f"{a} is maximum")
        else:
            print(f"{c} is maximum")
    elif b>c:
        print(f"{b} is maximum")   
functionp1(1,5,1)