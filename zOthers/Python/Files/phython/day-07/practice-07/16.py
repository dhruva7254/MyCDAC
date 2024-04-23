#16. Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30 (both included). 
def functionp16(a,b):
    l1=[]
    for e in range(a,b+1):
        l1.append(e**2)
    print(l1)    
functionp16(1,30)    