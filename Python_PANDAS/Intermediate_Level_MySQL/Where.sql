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
# where

select *
from student_table
where marks >= 90

select *
from student_table
where city="Bijapur";

select *
from student_table
where marks >= 90 or city="Bijapur";

# Operators
# 1 arithmetic

select *
from student_table
where marks-5 >= 90;

# 2 comparison

select *
from student_table
where marks >= 90;

# Logical

select *
from student_table
where marks >= 90 and name="NS";

# OPERATORS
# 1 BET-WINE

select *
from student_table
where marks between 80 and 90;

# insert
select *
from student_table
where city in("Bijapur", "Bijapur-1");

# NOT
select *
from student_table
where  city not in("Bijapur-1","Bijapur-2");

