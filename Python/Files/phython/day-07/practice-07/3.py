#3. Write a Python function to multiply all the numbers in a list. 
#Sample List : (8, 2, 3, -1, 7)
#Expected Output : -336
def functionp3(l:list):
    p=1
    for e in l:
        p=p*e
    return p    
print(functionp3([8, 2, 3, -1, 7]))