d1={1:10, 2:20}
d2={3:30, 4:40}
d3={5:50,6:60}
l1=list(d1.items())+list(d2.items())+list(d2.items())
print(l1)
d=dict(l1)
print(d)