#10. Write a Python program to print the even numbers from a given list. 
#Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Expected Result : [2, 4, 6, 8]
def functionp10(l:list):
    l1=[]
    for e in l:
        if e%2==0:
           l1.append(e)
    return l1
print(functionp10([1, 2, 3, 4, 5, 6, 7, 8, 9]))    