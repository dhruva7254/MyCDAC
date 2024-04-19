#2. Given a dictionary of students and their favourite colours:
people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}
#a. Find out how many students are in the list
#b. Change Lisa’s favourite colour
#c. Remove 'Jenny' and her favourite colour
#d.Sort and print students and their favourite colours alphabetically by name
print(F"no of students in list:{len(people)}")
people['Lisa']="orange"
print(people)
del people["Jenny"]
print(people)
people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}
lk=[]
for key in people:
   lk.append(key)
lk.sort(reverse=False)  
lv=[]
for e in lk:
   lv.append(people[e])
d=dict(zip(lk,lv))  
print(d)
