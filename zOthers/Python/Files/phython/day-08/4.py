#Q Given list of employees. This list may contain repetitions. Find all unique employee names and print them as 
#per order of second character in that name. Use lambda function and normal function both.

def functiona4(l:list):
    l1=[]
    for e in l:
        if e not in l1:
            l1.append(e)
    print(sorted(l1,key=lambda x:x[1]))        
functiona4(["yash","harsh","manthan","pranjal","sumedh","pranjal","sumedh","manthan"])