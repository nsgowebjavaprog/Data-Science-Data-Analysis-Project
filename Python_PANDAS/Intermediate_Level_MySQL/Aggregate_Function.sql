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

select distinct city from student_table;

# Aggrigate Functions
# 1

select marks
from student_table;

# MAX
select max(marks)
from student_table;  # 98

# MiN
select min(marks)
from student_table;  # 90

# AVG
select avg(marks)
from student_table;  # 95.0000

# COUNT
select count(marks)
from student_table;   # 5

# Group By
# Count number of students in each city

select city, count(name)
from student_table
group by city; 

1:34
