# a vector is an arrow in space with a specific direction and
# length, often representing a piece of data. It is the central building block of
# linear algebra, including matrices and linear transformations.

#s tail starts at the origin of a Cartesian plane (0,0).

'''v =[3,2]
print(v)'''  # output: [3,2]

#SymPy to perform linear algebra operations

# 2-D
'''import numpy as np
v = np.array([3,2])
print(v)'''
# [3 2]

#  3-D
'''import numpy as np
v = np.array([2,1,4])  # we use numpy-array{np.array}
print(v)'''

#output = [2 1 4]

# n-D
'''import numpy as np
v =np.array([12,3,44,5,66,776,334])
print(v)

# output :
[ 12   3  44   5  66 776 334]'''

# Adding and Combining Vectors
'''from numpy import array

v1 = array([3,2])
v2 = array([2,-1])

add_v1_and_v2 = v1+v2
print(add_v1_and_v2) '''   # output : [5 1]

#  Scaling Vectors
#  Scaling is growing or shrinking a vector’s length.
# add in front of one vector only one direction in 2 vectors

'''from numpy import array

v = array([3,1])

scaled = 2*v

print(scaled)'''   # [6 2]


# Span and Linear Dependence

#  These vectors →vand →w, fixed in two different directions, canbe scaled and added to create any new vector −−−−→ v +w
 

