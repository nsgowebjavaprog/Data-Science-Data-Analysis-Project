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


set sql_safe_updates = 0;

delete from student_data
where marks > 99;
select * from student_data;