# TOPIC-----1

# Function
#  y = 2x =3 {if x=0 ans=3} & {if x=1 ans=5} 
# input=x
# output=y
# problem--1

x = 5
y = 4*x + 3
print(x,",",y)
print("x \t y")
for x in range(11):
    y = 4*x +3
    print(x, "\t", y)
    
# OUTPUT:
'''5 , 23
x 	 y
0 	 3
1 	 7
2 	 11
3 	 15
4 	 19
5 	 23
6 	 27
7 	 31
8 	 35
9 	 39
10 	 43'''

# PROBLEM--2
def f(x):
    y = 4 * x +3
    return y
print(5,",",f(5))
for x in range(11):
    print(x,"\t",f(x))

# OUTPUT:'''
'''5 , 23
x 	 y
0 	 3
1 	 7
2 	 11
3 	 15
4 	 19
5 	 23
6 	 27
7 	 31
8 	 35
9 	 39
10 	 43'''

# TOPIC-----2
# Graphing Functions

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
plt.show()'''

'''import matplotlib.pyplot as plt
fig, ax = plt.subplots()
plt.axis([-10,10,-10,10])
plt.show()

# PROBLEM---1

from numpy import array
basic = array([[3,0],[0,2]])

v = array([1,1])
ans = basic.dot(v)
print(ans)          #OUTPUT: [3 2]

# PROBLEM---2

from numpy import array
i_hat = array([2,0])
j_hat = array([0,3])

basis = array([i_hat,j_hat]).transpose()
v = array([1,1])
ans = basis.dot(v)
print(ans)            # [2 3]

# PROBLEM---3
from numpy import array
i_hat = array([2,0])
j_hat = array([0,3])

basis = array([i_hat, j_hat]).transpose()

v=array([2,1])
ans=basis.dot(v)
print(ans)     # [4 3]

# PROBLEM---4
from numpy import array
i_hat = array([2,3])
j_hat = array([2,-1])

basis = array([i_hat, j_hat]).transpose()

v=array([2,1])
ans=basis.dot(v)
print(ans)            # [6 5]

# PROBLEM---5
# multiple transformations
#  Matrix Multiplication 

from numpy import array

i_hat = array([0,1])
j_hat = array([-1,0])
transform = array([i_hat, j_hat]).transpose()

i_hat1 = array([1,0])
j_hat1 = array([1,1])
transform1 = array([i_hat1, j_hat1]).transpose()

combined = transform @ transform1

print("COMBINED MATRIX :\n{}".format(combined))
v=array([1,2])
print(combined.dot(v))

'''
OUTPUT:
    COMBINED MATRIX :
[[ 0 -1]
 [ 1  1]]
[-2  3]'''


# PROBLEM---6
from numpy import array 
#  1
i_hat1 = array([0, 1])
j_hat1 = array([-1, 0])
transform1 = array([i_hat1, j_hat1]).transpose()
 
#  2
i_hat2 = array([1, 0])
j_hat2 = array([1, 1])
transform2 = array([i_hat2, j_hat2]).transpose() 
# Combine Transformations, apply sheer first and then rotation

combined = transform1 @ transform2 
# Test
print("COMBINED MATRIX:\n {}".format(combined)) 
v = array([1, 2])
print(combined.dot(v)) 

'''
OUTPUT:
    COMBINED MATRIX :
[[ 0 -1]
 [ 1  1]]
[-2  3]'''


# TOPIC--2
#  Determinants
# PROBLEM---1

# Calculating a determinant

from numpy.linalg import det
from numpy import array

i_hat = array([3,0])
j_hat = array([0,2])

basis = array([i_hat, j_hat]).transpose()  # output: 6.0

determinant = det(basis)
print(determinant)



# PROBLEM---2

 # A determinant for a shear
 
from numpy.linalg import det
from numpy import array 
i_hat = array([1, 0])
j_hat = array([1, 1]) 
basis = array([i_hat, j_hat]).transpose()  # output: 1.0
determinant = det(basis) 
print(determinant) 

# PROBLEM---3

from numpy.linalg import det
from numpy import array

i_hat = array([-2,1])
j_hat = array([1,2])

ans = array([i_hat,j_hat]).transpose()


determinant = det(ans)
print(ans)

'''
#OUTPUT:
[[-2  1]
 [ 1  2]]'''

# PROBLEM---4

from numpy.linalg import det
from numpy import array

i_hat = array([-2,1])
j_hat = array([3,-1.5])

result = array([i_hat, j_hat]).transpose()
determinant = det(result)
print(determinant)

'''
# OUTPUT:
0.0'''


# Systems of Equations and Inverse Matrices

# PROBLEM---1

from sympy import * 
# 4x + 2y + 4z = 44
 # 5x + 3y + 7z = 56
 # 9x + 3y + 6z = 72 
A = Matrix([ 
    [4, 2, 4], 
    [5, 3, 7], 
    [9, 3, 6]
     ]) 
# dot product between A and its inverse
 # will produce identity function
inverse = A.inv()
identity = inverse * A 
# prints Matrix([[-1/2, 0, 1/3], [11/2, -2, -4/3], [-2, 1, 1/3]])
print("INVERSE: {}".format(inverse)) 
# prints Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print("IDENTITY: {}".format(identity))

# OUTPUT:
INVERSE: Matrix([[-1/2, 0, 1/3], [11/2, -2, -4/3], [-2, 1, 1/3]])
IDENTITY: Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])



# PROBLEM---2

from numpy import array
from numpy.linalg import inv 
# 4x + 2y + 4z = 44
 # 5x + 3y + 7z = 56
 # 9x + 3y + 6z = 72 
A = array([ 
    [4, 2, 4], 
    [5, 3, 7], 
    [9, 3, 6]
     ]) 
B = array([ 
    44, 
    56, 
    72
     ]) 
X = inv(A).dot(B) 
print(X)

#OUTPUT:[ 2. 34. -8.]


# PROBLEM---3

from sympy import * 
# 4x + 2y + 4z = 44
 # 5x + 3y + 7z = 56
 # 9x + 3y + 6z = 72 
A = Matrix([ 
    [4, 2, 4], 
    [5, 3, 7], 
    [9, 3, 6]
     ]) 
B = Matrix([ 
    44, 
    56, 
    72
     ]) 
X = A.inv() * B 
print(X)

# output:
Matrix([[2], [34], [-8]])










































































































































































