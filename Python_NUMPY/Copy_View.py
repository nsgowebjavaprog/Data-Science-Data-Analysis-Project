# Copy v/s  View

# COPY


import numpy as np

arr2 = np.array([ 1,2,3,4])

copy = arr2.copy()
view = arr2.view()
# Add new one
arr2[2] = 200;

print("Var : ",view)
print("Copy : ",copy)


# output:
'''Var :  [  1   2 200   4]
Copy :  [1 2 3 4]'''



# Join___ARRAY   and Split__ARRAY

import numpy as np

arr1 = np.array([1,2,3,4])
arr2 = np.array([9,8,7,6])

res_arr = np.concatenate((arr1,arr2))
print(res_arr)


 # output:
 '''[1 2 3 4 9 8 7 6]'''
 
 
 
 # Concatenate

arr3 = np.array([[1,2],[3,4]])
arr4 = np.array([[9,8],[7,6]])

res = np.concatenate((arr3,arr4),axis=1)
print(arr3)
print()
print(arr4)
print()
print(res)


# output:
'''[[1 2]
 [3 4]]

[[9 8]
 [7 6]]

[[1 2 9 8]
 [3 4 7 6]]'''
 
 
 
 # Using STACK

arr3 = np.array([1,2,3,4])
arr4 = np.array([5,6,7,8])

res = np.stack((arr3,arr4),axis=1)
print(arr3)
print()
print(arr4)
print()
print(res)


# output:
'''[1 2 3 4]

[5 6 7 8]

[[1 5]
 [2 6]
 [3 7]
 [4 8]]'''



# Using STACK----H-----ROW

arr3 = np.array([1,2,3,4])
arr4 = np.array([5,6,7,8])

res = np.hstack((arr3,arr4))
print(arr3)
print()
print(arr4)
print()
print(res)

# output:
'''[1 2 3 4]

[5 6 7 8]

[1 2 3 4 5 6 7 8]'''



# Using STACK----V------COLUMN

arr3 = np.array([1,2,3,4])
arr4 = np.array([5,6,7,8])

res = np.vstack((arr3,arr4))
print(arr3)
print()
print(arr4)
print()
print(res)


# output:
'''[1 2 3 4]

[5 6 7 8]

[[1 2 3 4]
 [5 6 7 8]]'''



# Using STACK----D-------HEIGHT

arr3 = np.array([1,2,3,4])
arr4 = np.array([5,6,7,8])

res = np.dstack((arr3,arr4))
print(arr3)
print()
print(arr4)
print()
print(res)


# output:
'''[1 2 3 4]

[5 6 7 8]

[[[1 5]
  [2 6]
  [3 7]
  [4 8]]]'''





