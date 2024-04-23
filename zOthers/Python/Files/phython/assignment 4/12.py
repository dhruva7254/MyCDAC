n=int(input("enter size of list: "))
l1=[]
for idx1 in range(n):
    elem=input(f"enter elem{idx1+1}: ")
    l1.append(elem)
print(l1)    
l2=[]
for idx1 in range(len(l1)):
    n=int(l1[idx1])    
    if n%2!=0:
        l2.append(n)
    for idx2 in range(len(l1)):
      if l1[idx1]!=l1[idx2]: 
        n=int(l1[idx1]+l1[idx2])    
        if n%2!=0:
         l2.append(n) 
      for idx3 in range(len(l1)):
        if l1[idx1]!=l1[idx2]!=l1[idx3]: 
         n=int(l1[idx1]+l1[idx2]+l1[idx3])    
         if n%2!=0:
          l2.append(n)
        for idx4 in range(len(l1)):
         if l1[idx1]!=l1[idx2]!=l1[idx3]!=l1[idx4]: 
          n=int(l1[idx1]+l1[idx2]+l1[idx3]+l1[idx4])    
          if n%2!=0:
           l2.append(n) 
l2.sort(reverse=False)
print(l2)        