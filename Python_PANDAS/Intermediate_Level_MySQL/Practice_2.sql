create database college_student;
use college_student;

create table student_data(
rollno int primary key,
name varchar(20),
marks int not null,
grade varchar(10),
city varchar(20)
);

insert into student_data
(rollno, name, marks, grade,city)
values
(101,"NS",98,"A","Bijapur"),
(102,"GS",94,"A","Vijayapur"),
(103,"SS",97,"A","Bangalore"),
(104,"AS",96,"A","Mangalore"),
(106,"GS",98,"B","Bagalakote"),
(107,"SS",89,"C","Hulbi"),
(108,"AS",98,"C","Dharwad"),
(105,"SG",90,"A","Ballari");

select * from student_data;

# avg marks

-- select city, avg(marks)
-- from student_data
-- group by city
-- order by city;

# 2
-- select name, avg(marks)
-- from student_data
-- group by name
-- order by name;

# count by grade

-- select grade, count(rollno)
-- from student_data
-- group by grade
-- order by grade;
# output:A	5
#        B	1
#        C	2