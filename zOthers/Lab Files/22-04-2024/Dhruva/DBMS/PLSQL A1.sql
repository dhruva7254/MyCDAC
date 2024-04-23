
1. Write a function to compute the following. Function should take Emp_ num and return the cost to company. 
DA = 15% Salary, HRA= 20% of Salary, TA= 8% of Salary. 
Special Allowance will be decided based on the service in 
the company. 
< 1 Year Nil 
>=1 Year< 2 Year 10% of Salary 
>=2 Year< 4 Year 20% of Salary 
>4 Year 30% of Salary 

delimiter //
create function cost_company1(emp_num int) returns int
begin		
		declare cost int;
		declare exp int;
		declare csal int;
		declare chiredate date;
		select sal,hiredate into csal,chiredate from emp where empno=emp_num;
		
		set cost=(csal*0.15)+(csal*0.20)+(csal*0.08);
		set exp=datediff(curdate(),chiredate)/365;
		
		if exp<1 then
			set cost=csal;
		elseif exp>=1 and exp<2 then
			set cost=cost+(csal*0.10);
		elseif exp>=2 and exp<4 then
			set cost=cost+(csal*0.20);
		else
			set cost=cost+(csal*0.30);
		end if;
		return cost+csal;
end//
delimiter ;

----> select empno,ename,cost_company(empno) from emp;

2. Write a procedure that displays the following information of all emp 

Emp_Name Department Name Designation Salary Status 
Note: - Status will be (Greater, Lesser or Equal) respective 
to average salary of their own 
department. Display an error message Emp  table is ty if 
there is no matching 
record. 

---->	delimiter //
create procedure one()
begin
		declare vname varchar(10);
		declare vdname varchar(14);
		declare vsal int;
		declare vavgsal int;
		declare vdeptno int;
		declare vstatus varchar(14);
		declare vset int default 0;
		declare empcur cursor for select e.ename,d.dname,e.deptno,e.sal from emp e inner join dept d on e.deptno=d.deptno;
		declare continue  handler for not found set vset=1;
		open empcur;
		label:loop
				fetch empcur into vname,vdname,vdeptno,vsal;
				if vset=1 then
					leave label;
				end if;
				select avg(sal) into vavgsal from emp where deptno=vdeptno;
				if vsal>vavgsal then
				set vstatus='Greater';
				elseif vsal<vavgsal then
				set vstatus='Lesser';
				elseif vsal=vavgsal then
				set vstatus='Equal';
				else
				 set vstatus='Error';
				end if;
			select vname,vdname,vdeptno,vsal,vdeptno,vstatus;
		end loop;
		close empcur;
end//
delimiter ; 

3. Write a function to compute the following. Function 
should take Emp_num and return 

the cost to company. 
DA = 15% Salary, HRA= 20% of Salary, TA= 8% of Salary. 
Special Allowance will be decided based on the service in 
the company. 
< 1 Year Nil 
 



>=1 Year< 2 Year 10% of Salary 
>=2 Year< 4 Year 20% of Salary 
>4 Year 30% of Salary 
 

4. Write a procedure that displays the following 
information of all emp 

Emp_Name Department Name Designation Salary Status 
Note: - Status will be (Greater, Lesser or Equal) respective 
to average salary of their own 
department. Display an error message  table is  if there is 
no matching 
record. 
 
 

5. Write a procedure that accept Emp_num and update 
the salary and store the old salary 

details in Emp _Back (Emp _Back has the same structure 
without any 
constraint) table. 
Exp< 2 then no Update 
Exp> 2 and < 5 then 20% of salary 
Exp> 5 then 25% of salary 
 

6. Write a procedure and a function. 
Function: This function will return years of experience for a 
emp. This function will take the 
empid of the emp as an input parameter. The output will be 
rounded to the nearest year 
(1.4 year will be considered as 1 year and 1.5 year will be 
considered as 2 year). 



Procedure: Capture the value returned by the above 
function to calculate the additional 
allowance for the emp based on the experience. 
Additional Allowance = Year of experience x 3000 
Calculate the additional allowance and store Emp_num, 
Date of Joining, and Experience in 
years and additional allowance in Emp_Allowance table. 

 

 

Q2. Trigger 

1. Write a trigger which add entry in audit table when user 

tries to insert or delete records in employee table on sat 

or sun 

2. Create table order_history. Write a trigger to store old 

qty and old cost of order in history table before you 

update qty and cost of order. 

 

 

 


