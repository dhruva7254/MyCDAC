#7. Write a Python function that accepts a string and counts the number of upper and lower case letters. 
#Sample String : 'The quick Brow Fox'
#Expected Output :
#No. of Upper case characters : 3
#No. of Lower case Characters : 12
def functionp7(s:str):
    cu=0
    cl=0
    for e in s:
        if e.isupper():
            cu=cu+1
        if e.islower():
            cl=cl+1
    print(f"No. of Upper case characters : {cu}")           
    print(f"No. of Lower case characters : {cl}")       
s='The quick Brow Fox'
functionp7(s)