Assignment 2 Employee MongoDB

name: Dhruva rakesh B 
roll no.: 243514
date: 07-04-2024

Create a Employee Collection add 5 documents:

Example: 

{emono:111,ename:”Deepali 
Vaidya”,sal:40000.00,dept:{deptno:12,dname:,”Hr”,dloc:”Mumbai},
Desg:”Analyst”,mgr:{name:”Satish”,num:111},project:[{name:”Project1”,Hrs:4},{name:”project- 2”,Hrs:4}]}

1. All Employee’s with the desg as ‘CLERK’ are now called as (AO) Administrative Officers. 
Update the Employee collection for this.

db.employee.update({Desg: 'CLERK'}, {$set: {desg: 'A0'}})
db.employee.find({Desg: 'CLERK'})

2. Change the number of hours for project-1 to 5 for all employees with designation analyst.

db.employee.find({Desg: 'Analyst', 'project.name': 'Project-1'})
db.employee.update({Desg: 'Analyst', 'project.name': 'Project-1'}, {$
set: {'project.$.Hrs':5}})
db.employee.find({Desg: 'Analyst', 'project.name': 'Project-1'})

3. Add 2 projects project-3 and project-4 for employee whose name starts with ”Deep” with 2 hrs

db.emp.update({name:/^Deep/},{$push:{project:{$each:[{name:'project-3',Hrs:2},{name:'project-4',Hrs:2}]}}},
{multi:true})
db.employee.find({Desg: 'Analyst', 'project.name': 'Project-1'})

4. Add bonus rs 2000 for all employees with salary > 50000 

db.employee.find({sal: {$gt:40000}})


5. add bonus 1500 if salary <50000 and > 30000 
6. add bonus 1000 if salary <=30000
7. Change manager name to Tushar for all employees whose manager is currently “satish”
And manager number to 3333
8. Increase salary of all employees from “purchase department” by 15000
9. Decrease number of hrs by 2 for all employees who are working on project-2
10. Delete project-2 from all employee document if they are working on the project for 4 
hrs.
db.emp.update({},{$pull:{“project.name”:”project2”,”project.Hrs”:4}},{multi:true})
or
db.Emp.update({},{$pull:{project:{name:'project-2',Hrs:4}}},{multi:true})
or
db.emp.update({},{$pull:{“project:{$elemMatch:{name:”project2”,”Hrs”:4}},{multi:true})
11. Change the salary of employees to 10000 only if their salary is < 10000
12. Increase bonus of all employees by 500 if the bonus is <2000 or their salary is < 
20000 or if employee belong to sales department
13. Add 2 new project at position 2 for all employees with designation analyst or salary is 
equal to either 30000 or 33000 or 35000
14. Delete last project of all employees with department name is “HR” and if the location 
is Mumbai 
15. Change designation of all employees to senior programmer if they are working on 
name:”Project-1” for 4 hrs
16. Add list of hobbies in all employees document whose manager is Rajan or Revati
17. Add list of skillset in all employee documents who are working on project-4 for 3 hrs 
or on project-3 for 4 hrs 
18. Add a new hobby as blogging at 3 position in hobbies array for all employess whose 
name starts with R or p and ends with j or s
19. Increase salary by 10000 for all employees who are working on project-2 or project-3 
or project-1
20. Decrease bonus by 1000 rs And increase salary by 1000rs for all employees whose 
department location is Mumbai
21. Remove all employees working on project-1
22. Replace document of employee with name “Deepak to some new document
23. Change skill python to python 3.8 for all employees if python is there in the skillset
24. Add 2 skills MongoDb and Perl at the end of skillset array for all employees who are 
working at Pune location
25. Delete first hobby from hobby array for all employees who are working on project-1 
or project-2
26. Delete last hobby from hobbies array for all employees who are working on project 
which is at 2 nd position in projects array for 4 hrs 
27. Add 2 new projects at the end of array for all employees whose skillset contains Perl 
or python 
28. Change hrs to 6 for project-1 for all employees if they working on the project-1 for < 
6 hrs. otherwise keep the existing value. 