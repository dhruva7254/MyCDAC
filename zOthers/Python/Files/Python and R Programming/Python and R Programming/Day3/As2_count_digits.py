"""
5.	Given a number count the total number 
of digits in a number and also find sum 
of digits of the number. 
"""
count=0
num=int(input("Enter an int"))
while(num>0):
    d=num%10
    print("next digit is ",d)
    count+=1
    d=d//10

num=input("Enter an int")
print("count of digits =",len(num))
print("last digit", num[len(num) -1])
print("first digit", num[0])