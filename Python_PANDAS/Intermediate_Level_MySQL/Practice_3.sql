# student table:
 #  a. Change name of column {name to students name}
 #  b. Delete student score more than 80
 #  c. Delete the column for grades
 
create database practice_3;
use practice_3;

create table student_practice(                      
rollno int primary key,                         
name varchar(20),                               
marks int not null,                             
grade varchar(10),                              
city varchar(20)                                
);

insert into student_practice
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

select * from student_practice;

# ANS

alter table student_practice
change name student_name varchar(20);

# 2. DELETE

delete from student_practice
where marks < 80;

# 3/
alter table student_practice
drop column grade;

