# 1.INNER JOIN  {table-A inner join tavle-B}
# 2. LEFT JOIN 
# 3. RIGHT JOIN
# 4.FULL JOIN

# 1.inner join
create database in_join;
use in_join;
 
create table student_join(                      
id int primary key,
name varchar(20)                                
);

insert into student_join (id,name)
values
(101,"NS"),
(102,"GS"),
(103,"SS");

-- select * from student_join;
# output:
#  101	NS
#  102	GS
#  103	SS

create table course_join (                      
id int primary key,
course varchar(20)                                
);

insert into course_join (id,course)
values
(100,"english"),
(102,"maths"),
(104,"c++"),
(103,"phy");

-- select * from course_join;
# output:
#  100	english
#  102	maths
#  103	phy
#  104	c++


# 1. INNER JOIN----------INNER JOIN

# 1st way
-- select * from student_join
-- inner join course_join
-- on student_join.id = course_join.id;

# 2nd way
-- select * 
-- from student_join as a
-- inner join course_join as b
-- on a.id = b.id;

# output:
#  102	GS	102	maths
#  103	SS	103	phy

# 2.LEFT JOIN

-- select * 
-- from student_join as a
-- left join course_join as b
-- on a.id = b.id;

# OUTPUT:
#  101	NS  [101 NULL]	
#  102	GS	102	maths
#  103	SS	103	phy

# RIGTH JOIN

-- select * 
-- from student_join as a
-- right join course_join as b
-- on a.id = b.id;

# OUTPUT:
#  [null null]		100	english
#  102	GS	        102	maths
#  103	SS	        103	phy
#  [null null]		104	c++

# FULL JOIN

# left join {union} ||or|| [+] rigth join = full join
# 4.# FULL JOIN

-- select * 
-- from student_join as a
-- right join course_join as b
-- on a.id = b.id

-- union  # UNION

-- select * 
-- from student_join as a
-- left join course_join as b
-- on a.id = b.id;

# OUTPUT:
#  	-	100	english
#  102	GS	102	maths
#  103	SS	103	phy
#  	-	104	c++ -
#  101	NS	-	-

# 5. EXCLUSIVE 

# PROBLEM ON JOIN-----THINK and ANS
# 1

-- select * 
-- from student_join as a
-- left join course_join as b
-- on a.id = b.id
-- where b.id  is null;             # OUTPUT:  101	NS	-    -	

# 2

-- select * 
-- from student_join as a
-- right join course_join as b
-- on a.id = b.id
-- where a.id  is null;  

# OUTPUT: 
#  -   -		100	english
#  -   -		104	c++

# 6 SELF JOIN
# UNION
# RETURN UNIQUE RECORDS

-- select id from student_join
-- union
-- select id from course_join

#OUTPUT:
#101
#102
#103
#100
#104

# UNION ALL

select id from student_join
union ALL
select id from course_join

# OUTPUT:
#101
#02
#103
#100
#102
#103
#104