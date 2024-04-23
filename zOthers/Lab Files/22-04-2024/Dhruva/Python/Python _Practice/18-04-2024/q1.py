
# Q Sort all the numbers in a list in descending order using lambda function
# sorted(l1, key=(lambda x:-x))

l=[1,5,4,8,2,10,7,6,9,3]
print(sorted(l, key=lambda x: -x))