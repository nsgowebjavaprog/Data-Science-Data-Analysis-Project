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
(102,"GS",94,"A","Bijapur-1"),
(103,"SS",97,"A","Bijapur-2"),
(104,"AS",96,"A","Bijapur-3"),
(105,"SG",90,"A","Bijapur-4");
select * from student_table;