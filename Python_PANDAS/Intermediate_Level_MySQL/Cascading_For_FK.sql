use key_table;

create table student_data(                      
rollno int primary key,                   
name varchar(20),                      
marks int not null,                       
grade varchar(10),                           
city varchar(20)                                           
);


create table dept_data(                         
id int primary key,   
name varchar(20)                             
);
insert into dept_data
values
(1001,"asasas"),
(1002,"dsdsdsd");
select * from dept_data;



create table teacher_data(  
id int primary key,   
name varchar(20),   
dept_data_id int,
foreign key (dept_data_id) references dept_data(id)
       # cascading
on update cascade
on delete cascade
);
insert into teacher_data
values
(1001,"ASasasas",1001),
(1002,"sdsdsds",1002);
select * from teacher_data;



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