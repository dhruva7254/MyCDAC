n=int(input("enter no of terms: "))
s=0
t=""
for a in range(n):
    t=t+"9"
    s=s+int(t)
    print(t,",",end="")
print("\n",f"sum of {n} terms : ",s)    