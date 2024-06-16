# Matrix Function

# 1 Transpose

# 2. Swapaxes

# 3.Inverse

# 4.Power

# 5.Determinate

import numpy as mt

mat = mt.matrix([[1,2,3],[1,3,3]])
print(mat)

# OUTPUT:
'''[[1 2 3]
 [1 3 3]]'''

# 1 Transpose

import numpy as mt

mat = mt.matrix([[1,1,1],[2,2,2]])
print(mat)
print()

print(mt.transpose(mat))
print()

# OUTPUT:
'''[[1 1 1]
 [2 2 2]]

[[1 2]
 [1 2]
 [1 2]]'''

# 2. Swapaxes

import numpy as mt

mat = mt.matrix([[1,1,1],[2,2,2]])
print(mat)
print()

print(mt.swapaxes(mat,0,1))

# OUTPUT:
'''[[1 1 1]
 [2 2 2]]

[[1 2]
 [1 2]
 [1 2]]'''


# 3.Inverse

import numpy as np

mat = np.array([[1,0],[0,1]])
print(mat)
print()

print(np.linalg.inv(mat))
print()

# OUTPUT:
'''[[1 0]
 [0 1]]

[[1. 0.]
 [0. 1.]]'''


# 4.Power

import numpy as np

mat = np.array([[2,2],[2,1]])
print(mat)
print()

print(np.linalg.matrix_power(mat,2))  # mat ** 2 ===> mat * mat

# OUTPUT:
'''[[2 2]
 [2 1]]

[[8 6]
 [6 5]]'''


# 5.Determinate

import numpy as np

mat = np.array([[2,2],[2,1]])
print(mat)
print()

print(np.linalg.det(mat))    #  a(qw-er) - b(we-we) + c(we-rt)

# OUTPUT:
'''
[[2 2]
 [2 1]]

-2.0
'''


