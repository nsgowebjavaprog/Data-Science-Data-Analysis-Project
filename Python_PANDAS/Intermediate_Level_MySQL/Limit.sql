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
(102,"GS",94,"A","Bijapur"),
(103,"SS",97,"A","Bijapur"),
(104,"AS",96,"A","Bijapur"),
(106,"GS",78,"B","Bijapur-1"),
(107,"SS",45,"C","Bijapur-2"),
(108,"AS",45,"C","Bijapur-3"),
(105,"SG",90,"A","Bijapur");

select distinct city from student_table;

select *
from student_table

limit 2;
