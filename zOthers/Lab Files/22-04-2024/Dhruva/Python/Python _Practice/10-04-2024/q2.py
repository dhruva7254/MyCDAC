inc=int(input("enter income:"))
if(inc>100000):
    print("Platinum Card")
elif(50000<inc<=100000):
    print("Gold Card")
elif(25000<inc<=50000):
    print("Silver Card")
else:
    print("Bronze")
