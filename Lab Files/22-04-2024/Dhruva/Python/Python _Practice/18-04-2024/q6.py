
# Q. Take comma separated numbers as input from the user. Split it in list of strings. 
# Now convert every string in this list to float using map function


# a=int(input("enter length: "))
# b=[]
# for i in range(1,a+1):
#     b.append(int(input("enter values: ")))
# print(b)
# c=b.split()
# print(c)


itsr="1,34,55.5,77.8,23.345"
ltnosr=itsr.split(",")
res=map(float, ltnosr)
print(res)
l=[]
for num in res:
    print(num)
    l.append(num)
print(l)

print([ num for num in map(float, ltnosr)])

print([ num for num in map(float, itsr.split(","))])

