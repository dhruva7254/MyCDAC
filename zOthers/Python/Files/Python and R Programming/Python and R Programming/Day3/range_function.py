#range function
# returns an iterator
#range(start, end, step)
#start is included, default of start = 0
# end is excluded, compulsory
# step is increment / decrement value
# default value of step =1
#
# ex. range(1,5,1) -> 1,2,3,4
#range(2,10,2) -> 2,4,6,8
#range(1,16,2) ->1,3,5,7,9,11,13,15
#range(1,100000000000000000,1)
#range(5) -> range(0,5,1) ->0,1,2,3,4

#1. WaP to take n as input from user
# print all odd nos till n
n=100
print(list(range(1,n,2)))
for num in range(1,n,2):
    print(num)
# print all even nos till n
#2. WAP to print table of 3,7,13,17,19,23
print(list(range(3,3*11,3)))




