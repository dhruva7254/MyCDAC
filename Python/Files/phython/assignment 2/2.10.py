p=int(input("enter price of bike: "))
if p<=50000:
    t=p+p*0.05+p*0.05
if 50000<p<=100000:
    t=p+p*0.1+p*0.08 
else:
    t=p+p*0.15+p*0.2
print(f"total ammount to be paid: {t} ")      