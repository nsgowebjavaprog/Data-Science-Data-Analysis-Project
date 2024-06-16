use college_student;

create table student_data(                      # select
rollno int primary key,                         # from
name varchar(20),                               # where
marks int not null,                             # group by
grade varchar(10),                              # having
city varchar(20)                                # order by () asc/desc;
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

# count no.of student in each city where max marks cross 90

--  select city, count(rollno)
--  from student_data
--  group by city
--  having max(marks) > 90;

# general order

select city
from student_data
where grade = "A"
group by city
having max(marks) >= 96
order by city asc;
 # OUTPUT:
 
# Bangalore
# Bijapur
# Mangalore


