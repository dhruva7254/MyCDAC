
class Employee:
    Company_Name = "CDAC"
    def __init__(self,empid,name,designation,salary,project_ids_assigned,skills_list):
        self.empid = empid
        self.name = name
        self.designation = designation
        self.__salary = salary
        self.project_ids_assigned = project_ids_assigned
        self.skills_list = skills_list

    def display_projetids(self):
        print(self.project_ids_assigned)

    def display_identity(self):
        print(self.empid,self.name,self.designation)

    def check_relevant_skill(self):
        print(self.skills_list)
    
    def check_skill(self, skill):
        if skill in self.skills_list:
            return True
        else:
            return False

    @classmethod
    def display_company_details(cls):
        print(cls.Company_Name)
    
e1 = Employee(101,'James','Analyst',15000,'11,13,15','Cloud,Linux,Excel')
e2 = Employee(102,'Robert','Manager',30000,'11,12,14','Cloud,Tableau,MySQL,Python')
e3 = Employee(103,'John','Develeper',45000,'16,12,17','Cassandra,Tableau,MongoDB')

e1.display_identity()
e2.display_identity()
e3.display_identity()

e1.display_projetids()
e2.display_projetids()
e3.display_projetids()

e1.display_company_details()

print(e1.check_skill('Python'))
print(e2.check_skill('Python'))
print(e3.check_skill('Python'))



