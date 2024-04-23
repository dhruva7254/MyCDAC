#1. Add a list of elements to a given set
#Given:
#sampleSet = {"Yellow", "Orange", "Black"}
#sampleList = ["Blue", "Green", "Red","Yellow","orange"]
l1=["Blue", "Green", "Red","Yellow","orange"]
s={"Yellow", "Orange", "Black"}
for e in l1:
    s.add(e)
print(s)
