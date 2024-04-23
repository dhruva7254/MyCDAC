#Q. Take Employee id and Employee name of 5 employees from user. Store it in dictionary. 
#Print all employees in increasing order of employee Id . Also print all employees in alphabetical order by name.
d={1:"yash",3:"harsh",2:"manthan",6:"pranjal",5:"sumedh",4:"pranjal"}
def functiona5(d:dict):
   lkak=sorted(d,key=lambda x:x)
   lkav=sorted(d,key=lambda x:d[x])
   lvak=[]
   for e in lkak:
       lvak.append(d[e])
   print(dict(zip(lkak,lvak)))
   lvav=[]
   for e in lkav:
       lvav.append(d[e])
   print(dict(zip(lkav,lvav)))
functiona5(d)   
print(dict(sorted(d.items(),key=lambda x:x[0]))) # d.items is going to give list of tupples so x[0] index will be key
print(dict(sorted(d.items(),key=lambda x:x[1]))) # d.items is going to give list of tupples so x[1] index will be name
