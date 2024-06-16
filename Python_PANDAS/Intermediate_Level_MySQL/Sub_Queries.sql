# sub-queries-----> {[data]}
# sub {or} inner query {or} Nested query 

# select
# from
# where

# 1 find avg of class marks
# 2 find names of student with marks > avg

use col_stu;

create table student_table(
rollno int primary key,
name varchar(20),
marks int not null,
grade varchar(10),
city varchar(20)
);

insert into student_table
(rollno, name, marks, grade,city)
values
(101,"NS",98,"A","Bijapur"),
(102,"GS",94,"A","Vijayapur"),
(103,"SS",97,"A","Bangalore"),
(104,"AS",96,"A","Mangalore"),
(106,"GS",98,"B","Bagalakote"),
(107,"SS",89,"C","Hulbi"),
(108,"AS",98,"C","Dharwad"),
(105,"SG",90,"A","Bijapur-1");
select * from student_table;

# avg of marks of class
-- select avg(marks)
-- from student_table;        # OUTPUT: 95.0000

# find names of student with marks > avg

#SUB QUERY

-- select marks
-- from student_table
-- where marks > (select avg(marks) from student_table);  # 98 97 96


#  EVEN NUMBER OF ROLL_NUMBER 

select rollno
from student_table
where rollno % 2 = 0;     # 	OUTPUT : 102  104

select name,rollno
from student_table
where rollno IN(
	select rollno
	from student_table
    where rollno % 2 = 0);
    
# output:
#  GS	102
#  AS	104