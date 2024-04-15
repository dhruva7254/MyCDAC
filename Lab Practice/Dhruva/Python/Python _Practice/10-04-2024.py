totlec=int(input("Enter total lectures:"))
attlec=int(input("Enter attended lectures:"))
print(attlec,totlec)
peratt=attlec/totlec*100
if(peratt>75):
    print("Allowed for exam")
elif(peratt>50):
    print("allowed with 40% reduction in marks")
else:
    print("Not Allowed")
