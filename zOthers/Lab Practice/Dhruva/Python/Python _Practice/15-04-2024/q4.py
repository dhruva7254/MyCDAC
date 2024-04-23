"""33. Write a Python program to convert a given list of tuples to a list of lists.
Original list of tuples: [(1, 2), (2, 3), (3, 4)]
Convert the said list of tuples to a list of lists: [[1, 2], [2, 3], [3, 4]]
Original list of tuples: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
Convert the said list of tuples to a list of lists: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]"""

t1=(1,2)
t2=(2,3)
t3=(3,4)
l1=[t1,t2,t3]
print(l1)
l2=[t1]
l3=[t2]
l4=[t3]
l5=[l2,l3,l4]
#print[l5]

# l1=[]
# print(l1)
# l2=[t1.0]

"""7. Write a Python program to get the 4th element from the last element of a tuple."""

t1=(1,2,3,4,5,6,7,8,9)
print(t1[-4])

