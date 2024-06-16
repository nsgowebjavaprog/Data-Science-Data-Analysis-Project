# matrix

mat1 = np.matrix([[1,2],[3,4]])
mat2 = np.matrix([[1,2],[3,4]])

print(mat1)

print(mat2)

print("MUL: ",mat1 * mat2)

# OUTPUT:
'''[[1 2]
 [3 4]]
[[1 2]
 [3 4]]
MUL:  [[ 7 10]
 [15 22]]'''







# 3*3

import numpy as np

mat1 = np.matrix([[1,2,3],[3,4,6],[1,2,3]])
mat2 = np.matrix([[1,2,3],[3,4,6],[1,2,3]])
mat3 = np.matrix([[1,2,3],[3,4,6],[1,2,3]])

print(mat1)

print(mat2)

print(mat3)

print("MUL: ",mat1 * mat2 * mat3)

#OUTPUT:
'''
[[1 2 3]
 [3 4 6]
 [1 2 3]]
[[1 2 3]
 [3 4 6]
 [1 2 3]]
[[1 2 3]
 [3 4 6]
 [1 2 3]]
MUL:  [[ 82 132 198]
 [174 280 420]
 [ 82 132 198]]'''