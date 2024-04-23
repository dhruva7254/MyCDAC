#Q1
t1=(1,2,3)
t2=("ghgh",)

#Q3
t1=(1,2,3)
print(t1[1],t1[0:2],t1[:3])

#Q4
v1,v2 = (1,2) # error
print(v1,v2)
#v1,v2 = (1) 
#print(v1,v2)

#Q5
# t1=(5,7,8)
# t1.add(45) #error

#Q6
t1=(2,3,4)
str=((2,3,4))

t2=('I','A','C','S','D')
"".join(t2)

# t1=(2,3,4)
# s1=""
# for e1 in t1:
#     s1+=str(e1)
# print(s1,int(s1))
# s1= "".join(t1)
# print(s1)


t1=(9,9,9,9,9,23,45,67,67,10)
t1.count(9)
# using set
for e1 in set(t1):
    if t1.count(e1) > 1:
        print("repeated elem",e1)


repeated_set=set()
for e1 in t1:
    for e2 in t1:
        if (e1 == e2) and (e1 not in repeated_set):
            repeated_set.add(e1)
print(repeated_set)


repeated_set=set()
for idx1 in range(len(t1)):
    for idx2 in range(len(t1)):
        if (idx1 != idx2) and (t1[idx1] == t1[idx2]) and (t1[idx1] not in repeated_set):
            repeated_set.add(t1[idx1])
print(repeated_set)


#Q17


# t1=(1,2,3,4)
# print(t1[::-1], tuple(reversed(t1)))


l_t=[(1,2),(4,5)]
dict(l_t)
print(dict(l_t))


# t10=(1,2,3)
# print("This is a tuple", str(t10))


t=(1,2,3)
print(tuple((*t[:2],4)))


"""23. Write a Python program to sort a tuple by its float element.
Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]"""

l=[('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
l1=[t[1] for t in l]
l1.sort(reverse=True)
print(l1)
#l1.sort()
l2=[()]*len(l1)
for tup in l:
    idx = l1.index(tup[1])
    if idx< len(l2):
        l2.insert(idx,tup)
    else:
        l2.append(tup)
print(l2)

#bibble sort
