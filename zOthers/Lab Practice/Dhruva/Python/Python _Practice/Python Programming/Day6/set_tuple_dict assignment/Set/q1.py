"""1. Add a list of elements to a given set
Given:
sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red","Yellow","orange"]"""

sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red","Yellow","orange"]
sampleSet.update(sampleList)
print("Updated set:", sampleSet)
