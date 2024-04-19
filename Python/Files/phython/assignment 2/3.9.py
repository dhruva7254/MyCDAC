x=int(input("enter vale of x: "))
n=int(input("enter no of terms: "))
s=0
for a in range(n):
 a1=x**a
 f=1
 for b in range(a):
      f=f*(b+1)
 t=a1/f
 s=s+t
 print(t,"+",end="")
print("\n",f"sum of first {n} terms: ",s)
