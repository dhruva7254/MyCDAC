#5. Copy element 44 and 55 from the following tuple into a new tuple
tuple1 = (11, 22, 33, 44, 55, 66)
#Expected output:
#tuple2: (44, 55)
tp=()
for e in set(tuple1):
    if (e==44)|(e==55):
        tp=tp+(e,)
print(tp)        