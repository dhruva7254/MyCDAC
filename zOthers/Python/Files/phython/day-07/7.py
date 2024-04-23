#WA function to take a dictionary as parameter. Print value of key "name" if key "rollno" is having value 100.
def functionrollno(d):
    if d["roll_no"]==100:
      print(d["name"])
d={"name":"abc","roll_no":100}      
functionrollno(d)