#Q Given list of floating point numbers. Convert every number into string and 
#then join all the numbers such that they are separated by pipe(|)
l=[1.23,1.25,2.5,3.65]
l=list(map(lambda x:str(x),l))
print(l)
l="|".join(l)
print(l)