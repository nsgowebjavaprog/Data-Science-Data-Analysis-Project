create database col_stu;
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
(106,"GS",78,"B","Bagalakote"),
(107,"SS",45,"C","Hulbi"),
(108,"AS",45,"C","Dharwad"),
(105,"SG",90,"A","Bijapur-1");

select distinct city from student_table;

-- select *
-- from student_table
-- order by marks asc;

select *
from student_table
order by marks desc;