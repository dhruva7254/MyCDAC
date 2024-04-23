#5. Write a Python function to calculate the factorial of a number (a non-negative integer). 
#The function accepts the number as an argument. 
def function5(n):
    if n>=0:
       f=1
       for x in range(1,n+1):
          f=f*x
    else:
        f=None
        print("invalid no")  
    return f     
print(function5(-1))