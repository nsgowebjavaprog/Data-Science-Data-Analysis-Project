# update 
# SET

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


# safe mode
# SAVE MODE ON

set sql_safe_updates = 0;

update student_data
# 1
-- set marks = 100
-- where marks = 89;         # 107	SS	100	C	Hulbi
# 2
-- set grade = "O"
-- where grade = "A";
# 3
-- set grade = "A"
-- where marks between 80 and 90;
# 4
set marks = marks+1;

select * from student_data;
# OUTPUT:
#  101	NS	98	O	Bijapur
#  102	GS	94	O	Vijayapur
#  103	SS	97	O	Bangalore
#  104	AS	96	O	Mangalore
#  105	SG	90	O	Ballari
#  106	GS	98	B	Bagalakote
#  107	SS	89	C	Hulbi
#  108	AS	98	C	Dharwad


