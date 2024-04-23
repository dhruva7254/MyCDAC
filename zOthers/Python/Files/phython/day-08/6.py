#Q. Take comma separated numbers as input from the user. 
#Split it in list of strings. Now convert every string in this list to float using map function
l=[1,2,3,4]
print(list(map(lambda x:str(x),l)))
print(list(map(lambda x:float(x),l)))
print([str(e) for e in l])
print([float(e) for e in l])
for e in map(lambda x:str(x),l):
    print(e)
l1=map(lambda x:str(x),l)
print(next(l1))
print(next(l1))
print(next(l1))
print(next(l1))
