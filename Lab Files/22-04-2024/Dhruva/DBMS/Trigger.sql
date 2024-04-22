--------------------------------------------------------------------
Triggers 

any block of code , which has business logic, and gets called on some users action automatically, then it is called as trigger

To write trigger

Triggers are used for data analysis purpose or for security purpose.

1. create table to store trigger data

create table dept_audit(
    did int,
    dname varchar(20),
    old_dname varchar(20),
    newloc varchar(20),
    oldloc varchar(20),
    username varchar(20), 
    chang_date date,
    action varchar(20));

delimiter //
create trigger updatedepttr before update on dept
for each row
 insert into dept_audit values(old.deptno,new.dname,
old.dname,new.loc,old.loc,user(),curdate(),’update’);
end//
delimiter ;

create trigger insertdepttr before insert
on dept
for each row
 insert into dept_audit values(new.deptno,new.dname,
null,new.loc,null,user(),curdate(),'insert');

create trigger deletedepttr after delete
on dept
for each row
 insert into dept_audit values(old.deptno,null,
old.dname,null,old.loc,user(),curdate(),'delete');

In trigger we get 2 special variables old and new

     insert  delete  update
old  null    data    existing data in the table
new  data    null    the record after changes are done

----------------------------------------------------------

-- --
drop trigger insertdepttr;
-- --

delimiter //
 create trigger insertdepttr before update
    -> on dept
    -> for each row
    ->     insert into dept_audit values(old.deptno,new.dname,
    -> old.dname,new.loc,old.loc,user,curdate());
    -> //
delimiter ;

--- ---
drop trigger insertdepttr;

delimiter //
create trigger insertdepttr before update
on dept
for each row
insert into dept_audit values(old.deptno,new.dname,
old.dname,new.loc,old.loc,user(),curdate());
//
delimiter ;

update dept set loc='xxx' where deptno=20;

select * from dept_audit;
--- ---

alter table dept_audit add action varchar(20);

desc dept_audit;

drop table dept_audit;

select * from dept;

mysql> select * from dept_audit;
+------+----------+------------+--------+---------+----------------+------------+--------+
| did  | dname    | old_dname  | newloc | oldloc  | username       | chang_date | action |
+------+----------+------------+--------+---------+----------------+------------+--------+
|   20 | RESEARCH | RESEARCH   | xxx    | DALLAS  | root@localhost | 2024-03-31 | update |
|   30 | a        | SALES      | b      | CHICAGO | root@localhost | 2024-03-31 | update |
|   60 | sss      | NULL       | pune   | NULL    | root@localhost | 2024-03-31 | insert |
|   30 | NULL     | a          | NULL   | b       | root@localhost | 2024-03-31 | delete |
|   40 | NULL     | OPERATIONS | NULL   | BOSTON  | root@localhost | 2024-03-31 | delete |
+------+----------+------------+--------+---------+----------------+------------+--------+
5 rows in set (0.00 sec)

mysql> drop table dept_audit;
Query OK, 0 rows affected (0.03 sec)


mysql> create trigger deletedepttr after delete
    -> on dept
    -> for each row
    ->     insert into dept_audit values(old.deptno,null,
    -> old.dname,null,old.loc,user(),curdate(),'delete');
Query OK, 0 rows affected (0.02 sec)

delete from dept
    -> where deptno between 30 and 50;

mysql> create trigger updatedepttr before update
    -> on dept
    -> for each row
    ->     insert into dept_audit values(old.deptno,new.dname,
    -> old.dname,new.loc,old.loc,user(),curdate(),'update');
    ->
    -> //
Query OK, 0 rows affected (0.02 sec)

mysql> create trigger insertdepttr before insert
    -> on dept
    -> for each row
    ->     insert into dept_audit values(new.deptno,new.dname,
    -> null,new.loc,null,user(),curdate(),'insert');
    -> //
Query OK, 0 rows affected (0.02 sec)

mysql> insert into dept values(60,'sss','pune');
    -> //
Query OK, 1 row affected (0.01 sec)

alter table dept_audit
    -> add action varchar(20);

update dept_audit
    -> set action='update';

---------------------------
create table dept_audit(
    did int,
    new_dname varchar(20),
    old_dname varchar(20),
    new_loc varchar(20),
    old_loc varchar(20),
    username varchar(20),
    change_date date,
    daction varchar(20)
);

create trigger updatedepttr before update
on dept
for each row
    insert into dept_audit values(old.deptno,new.dname,old.dname,new.loc,old.loc,user(),curdate(),'update');

update dept set loc='abc' where deptno=40;

mysql> select * from dept;
+--------+------------+----------+
| DEPTNO | DNAME      | LOC      |
+--------+------------+----------+
|     10 | ACCOUNTING | NEW YORK |
|     20 | RESEARCH   | DALLAS   |
|     30 | SALES      | CHICAGO  |
|     40 | OPERATIONS | BOSTON   |
+--------+------------+----------+
4 rows in set (0.03 sec)

create trigger insertdepttr before insert
on dept
for each row
    insert into dept_audit values(new.deptno,new.dname,null,new.loc,null,user(),curdate(),'insert');

insert into dept values(50,'qwe','rty');

create trigger deletedepttr before delete
on dept
for each row
    insert into dept_audit values(old.deptno,null,old.dname,null,old.loc,user(),curdate(),'delete');

delete from dept where deptno between 40 and 60;
