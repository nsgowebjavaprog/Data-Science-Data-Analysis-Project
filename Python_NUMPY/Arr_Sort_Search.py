# Array ROW/COL/HET


arr3 = np.array([1,2,3,4])
arr4 = np.array([5,6,7,8])

res = np.dstack((arr3,arr4))
res1 = np.vstack((arr3,arr4))
res2 = np.vstack((arr3,arr4))


print(res)
print(res1)
print(res2)

# output:
'''[[[1 5]
  [2 6]
  [3 7]
  [4 8]]]
[[1 2 3 4]
 [5 6 7 8]]
[[1 2 3 4]
 [5 6 7 8]]'''


# Split Array

# 1-D

import numpy as np

arr = np.array([1,2,3,4,5,6])

print(arr)

res = np.array_split(arr,3)
print(res)
print(type(res))


# output:
'''[1 2 3 4 5 6]
[array([1, 2]), array([3, 4]), array([5, 6])]
<class 'list'>'''


# Split Array

# 2-D

import numpy as np

arr1 = np.array([[1,2],[3,4],[5,6]])

print(arr1)

res = np.array_split(arr1,3)
print(res)
print(type(res))

# output;
'''[[1 2]
 [3 4]
 [5 6]]
[array([[1, 2]]), array([[3, 4]]), array([[5, 6]])]
<class 'list'>
'''




# Search

import numpy as ns

arr = ns.array([1,2,3,4,5,6,7,8,9,12,4,56,3453,565])

x = np.where(arr == 56)
even = np.where((arr%2) != 0)  # print IDX
print(x)
print("even: ",even)


# output:
'''(array([11], dtype=int64),)
even:  (array([ 0,  2,  4,  6,  8, 12, 13], dtype=int64),)'''


# Search Sorted Array

import numpy as ns

arr1 = ns.array([1,2,3,3,3,3,3,4,5,6,7,8,9,12,565])

x1 = np.searchsorted(arr1,5)  # Where inert for inc order
print(x1)
print(arr1)

# output:
'''8
[  1   2   3   3   3   3   3   4   5   6   7   8   9  12 565]'''



# Sortded ------Incresing Order

arr10 = np.array([9,7,4,2,4,6,7,4,35,6,4,3,55,3,464,54,234])

print(arr10)

print(np.sort(arr10))

# output:
'''[  9   7   4   2   4   6   7   4  35   6   4   3  55   3 464  54 234]
[  2   3   3   4   4   4   4   6   6   7   7   9  35  54  55 234 464]'''




# Sortded ------Incresing Order  ----ChAR

arr10 = np.array(["a","E","I","o","U"])

print(arr10)

print(np.sort(arr10))


# output:
'''['a' 'E' 'I' 'o' 'U']
['E' 'I' 'U' 'a' 'o']'''



# Sortded ------Incresing Order----2-D _________ARRAY

arr10 = np.array([[9,7,4,2],[3,7,3,67]])

print(arr10)

print(np.sort(arr10))

# output:
'''[[ 9  7  4  2]
 [ 3  7  3 67]]
[[ 2  4  7  9]
 [ 3  3  7 67]]'''



