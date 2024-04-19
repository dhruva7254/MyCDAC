#1. Write a Python script to sort (ascending and descending) a 
#dictionary by value.

s={2:2,1:3,3:3}
l1=list(s.keys()) 
l1.sort(reverse=False)
s1={e:s[e] for e in l1}  
print(s1)