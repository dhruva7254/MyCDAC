y=int(input("enter year: "))
if (y%100==0) & (y%400):
    print(f"{y} is leap year")
elif y%4==0:
    print(f"{y} is leap year")
else:
    print(f"{y} is not leap year")

