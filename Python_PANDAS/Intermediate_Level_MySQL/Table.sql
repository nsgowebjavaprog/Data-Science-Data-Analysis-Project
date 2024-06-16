create database college;
use college;

create table student(
rollno int primary key,
name varchar(20)
);

select * from student;
insert into student
(rollno, name)
values
(100,"Nagaraj"),
(101,"Gururaj");

insert into student values(111,"Ram");