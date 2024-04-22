cursors - When you want to traverse through all rows one by one, and perform some action on each row, on by one, then use cursors

Cursors

Cursors are used to read the data from the table row by row, and process it

Step by step procedure to use cursor

1. Declare cursor.
2. declare continue handler to stop the loop
3. open the cursor.
4. fetch the row from the cursor.
5. check whether reached to last row leave the loop
6. process the row.
7. goto step 4
8. once come out of the loop then close the cursor.

delimiter //
create procedure displayallemp()
begin
    declare vset,vempno int default 0;
    declare vname varchar(20);
    declare empcur cursor for select empno,ename from emp;
    declare continue handler for NOT FOUND set vset=1;
    open empcur;
        lable1: loop
            fetch empcur into vempno,vname;
            if vset=1 then
                leave lable1;
            end if;
            select vempno,vname;
        end loop;
    close empcur;
end//
delimiter ;

2. write a procedure to display all the employees whose sal < avg sal of its own department

delimiter //
create procedure displayempbyavg()
begin
declare vset,vempno,vdeptno int default 0;
declare vename,vjob varchar(20);
declare vsal,vavgsal float(9,2);
declare empcur cursor for select empno,ename,job,sal,deptno from emp;
declare continue handler for NOT FOUND set vset=1;
open empcur;
label1:loop
fetch empcur into vempno,vename,vjob,vsal,vdeptno;
if vset=1 then
leave label1;
end if;
select avg(sal) into vavgsal
from emp
where deptno=vdeptno;
if vsal<vavgsal then
select vempno,vename,vjob,vsal,vdeptno,vavgsal;
end if;
end loop;
close empcur;
end//
delimiter ;
call displayempbyavg();

-- --


delimiter //
create procedure displayallemp()
begin
    declare vset,vempno int default 0;
    declare vname varchar(20);
    declare empcur cursor for select empno,ename from emp;
    declare continue handler for NOT FOUND set vset=1;
    open empcur;
        lable1: loop
            fetch empcur into vempno,vname;
            if vset=1 then
                leave lable1;
            end if;
            select vempno,vname;
        end loop;
    close empcur;
end//
delimiter ;
call displayallemp();



delimiter //

create procedure allemp()
begin
    declare vset,vempno int default 0;
    declare vname varchar(20);
    declare empcur curser for empno,ename from emp;
    declare continue handler for NOT FOUND vset=1;
    open empcur
    label1:loop
    if 
     
    end if
        select 
    end loop
    close empcur;
end //
delimiter ;

delimiter //
create procedure allemp()
begin

end //
delimiter ;
call allemp();

delimiter //
create procedure displayallemp()
begin
    declare vset,vempno int default 0;
    declare vname varchar(20);
    declare empcur cursor for select empno,ename from emp;
    declare continue handler for NOT FOUND set vset=1;
    open empcur;
        label1:loop
            fetch empcur into vempno,vname;
            if vset=1 then
                leave label1;
            end if;
            select vempno,vname;
        end loop;
    close empcur;
end //
delimiter ;
call displayallemp();

delimiter //
create procedure displayallemp()
begin
    declare vset,vempno int default 0;
    declare vname varchar(20);
    declare empcur cursor for select empno,ename from emp;
    declare continue handler for NOT FOUND set vset=1;
    open empcur;
        label1:loop
            fetch empcur into vempno,vname;
            if vset=1 then
                leave label1;
            end if;
            select vempno,vname;
        end loop;
    close empcur;
end //
delimiter ;
call displayallemp();















































































