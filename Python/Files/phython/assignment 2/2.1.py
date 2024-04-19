t=int(input("enter no of class held: "))
a=int(input("enter no of class attended: "))
x=a/t*100
print("persentage attendence: ",x)
if x>=75:
    print("allowed to sit in exam ")
else:
    print("not allowed to sit in exam ") 