#2. Write a Python function to sum all the numbers in a list. 
#Sample List : (8, 2, 3, 0, 7)
#Expected Output : 20
def functionp2(l:list):
    s=0
    for e in l:
        s=s+e
    return s    
print(functionp2([8, 2, 3, 0, 7]))