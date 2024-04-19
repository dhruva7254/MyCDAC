#Q Sort all the numbers in a list in descending order using lambda function
#sorted(l1, key=(lambda x:-x))
l=[1,3,4,5,6,1,2,3,5,8]
print(sorted(l,key=lambda x:-x))