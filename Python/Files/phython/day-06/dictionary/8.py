d1={1: 10, 2: 20, 3: 30, 4: 40}
d2={5: 10, 6: 20, 7: 30, 8: 40}
l=list(d1.items())+list(d2.items())
d=dict(l)
print(d)