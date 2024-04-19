m=int(input("enter marks: "))
g="n/a"
if m<25:
    g="F"
if 25<=m<45:
    g="E"
if 45<=m<50:
    g="D"
if 50<=m<60:
    g="C"
if 60<=m<80:
    g="B"
if 80<=m<100:
    g="A"
else:
    print("invalid marks")
print("grades:",g)