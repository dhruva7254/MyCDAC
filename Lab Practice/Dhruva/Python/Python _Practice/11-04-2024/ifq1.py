# A student will not be allowed to sit in exam if his/her attendence is less than 75%.  
# Take following input from user Number of classes held Number of classes attended. And print percentage of class attended  
# Is student is allowed to sit in exam or not. 

totlec=int(input("Enter total lectures:"))
attlec=int(input("Enter attended lectures:"))
print(attlec,totlec)
peratt=attlec/totlec*100
print(peratt)
if(peratt>75):
    print("Allowed for exam")
else:
    print("Not Allowed")
