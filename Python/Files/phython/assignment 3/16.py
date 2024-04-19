n=int(input("enter no: "))
a=n**0.5
s=str(a)
if s[len(s)-1]=="0":
  print(f"{n} is perfect squre of {a}")
else:
  print(f"{n} is inperfect squre of {a}")
