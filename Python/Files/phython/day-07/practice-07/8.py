#8. Write a Python function that takes a list and returns a new list with distinct elements from the first list. 
#Sample List : [1,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]
def functionp8(l:list):
    l1=[]
    for e in l:
        if e not in l1:
            l1.append(e)
    return l1       
print(functionp8([1,2,3,3,3,3,4,5]))    
