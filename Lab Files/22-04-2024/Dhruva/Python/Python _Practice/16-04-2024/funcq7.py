# Q WA function to take a dictionary as parameter. Print value of key "name" if key "rollno" is 
# having value 100.

def prival(a:dict):
    if a['rollno']==100:
        b=a['name']
    else:
        b=0
    return b
c={1:10,'name':'car',3:30,'rollno':100,5:50}
print(prival(c))
