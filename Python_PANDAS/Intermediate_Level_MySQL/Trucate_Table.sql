# delete table {data}

use querys;

create table related_query(                      
rollno int primary key,                         
name varchar(20),                               
marks int not null,                             
grade varchar(10),                              
city varchar(20)                                
);

insert into related_query
(rollno, name, marks, grade,city)
values
(101,"NS",98,"A","Bijapur"),
(102,"GS",89,"B","Vijayapur"),
(103,"SS",87,"B","Bangalore"),
(104,"AS",96,"A","Mangalore"),
(106,"GS",98,"A","Bagalakote"),
(107,"SS",79,"C","Hulbi"),
(108,"AS",75,"C","Dharwad"),
(105,"SG",91,"A","Ballari");

select * from related_query;

# Trucating data alll data will be deleted 

truncate table related_query;