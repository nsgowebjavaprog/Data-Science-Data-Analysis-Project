#  Functions

#  Shuffle

import numpy as np

arr = np.array([1,2,3,4])

np.random.shuffle(arr)
print(arr)

# OUTPUT:
'''[3 4 2 1]'''


# Unique

import numpy as np

arr = np.array([1,1,2,2,3,3,3,2,3,4])

x = np.unique(arr, return_index=True, return_counts=True)
print(x)

# OUTPUT:
'''(array([1, 2, 3, 4]), array([0, 2, 4, 9], dtype=int64), array([2, 3, 4, 1], dtype=int64))'''


# Resize

arr1 = np.array([1,2,3,4,5,6])

a = np.resize(arr1,(2,3))
c = np.resize(arr1,(3,2))

print("---->",a)
print("---->",c)

# OUTPUT:
'''----> [[1 2 3]
 [4 5 6]]
----> [[1 2]
 [3 4]
 [5 6]]'''



# Flatten

arr1 = np.array([1,2,3,4,5,6])

a = np.resize(arr1,(2,3))

print(a)

# return Same size

print(a.flatten())

# OUTPUT:
'''[[1 2 3]
 [4 5 6]]
[1 2 3 4 5 6]'''


