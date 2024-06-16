create database company;
use company;

create table employee(
id int primary key,
name varchar(10),
salary int
);

insert into employee
(id, name, salary)
values
(1,"Nagaraj Loni",12000000),
(2,"Gururaj Loni",18000000),
(3,"NS Loni",15000000);

select * from employee;