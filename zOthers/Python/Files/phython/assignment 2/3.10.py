x=int(input("enter vale of x: "))
n=int(input("enter no of terms: "))
s=0
p=1
for a in range(n):
    num=x**p
    p=p+2
    if a%2!=0:
        num=-num
    s=s+num
    print(num)
print("\n",f"sum of first {n} terms: ",s)

