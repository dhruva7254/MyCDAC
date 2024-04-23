
# Q. Take Employee id and Employee name of 5 employees from user. Store it in dictionary. 
# Print all employees in increasing order of employee Id . Also print all employees in alphabetical 
# order by name.

# d=dict(input("enter emp id and emp name : "))
# d=dict()
# print(d)

"""num1=int(input('enter length of list A: '))
h1=[]
for i in range(1,num1+1):
    h1.append(int(input('enter list A values : ')))
print(h1)

num2=int(input('enter length of list B: '))
h2=[]
for i in range(1,num2+1):
    h2.append(str(input('enter list B values : ')))
print(h2)

d1=dict(zip(h1,h2))
print(d1)

print(sorted(d1, key= lambda s:s))
d2={101: 'James', 102: 'Robert', 103: 'John', 104: 'Michael', 105: 'David'}
# print(sorted(d1.keys()))"""


d2={101: 'James', 103: 'Robert', 105: 'John', 104: 'Michael', 102: 'David'}

a=sorted(d2.items(), key= lambda s:s[0]) 
#print(a1)

# print(sorted(d2, key= lambda s:s))
# a2=d2.values()
# print(a2)
# b1=d2.keys()
# print(b1)
# b2=sorted(d2.values(), key= lambda s:s)

#print(sorted(d2.items(), key= lambda s:s[1])) 

b=sorted(d2.items(), key= lambda s:s[1])

print(dict(a))
print(dict(b))

# d3=dict(zip(a1,a2))
# d4=dict(zip(b1,b2))
# print(d3)
# print(d4)


###########################


