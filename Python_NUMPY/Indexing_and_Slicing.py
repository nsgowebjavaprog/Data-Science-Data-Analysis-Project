# Indexing and Slicing

# indexing
# 1-D

arr = np.array([9,8,7,6])
print(arr[1])
print(arr[-3])

# output:
'''8
8'''


# indexing
# 2-D

arr = np.array([[2,3,4],[6,7,8]])
print(arr)
print(arr.ndim)

print(arr[0,2])

# output:
'''[[2 3 4]
 [6 7 8]]
2
4'''


# 3-D

arr1 = np.array([[[2,3,4],[6,7,8]]])
print(arr1)
print(arr1.ndim)
print(arr1.shape)

print(arr1[0,1,1])

print(arr1[0,1,0])

# output:
'''[[[2 3 4]
  [6 7 8]]]
3
(1, 2, 3)
7
6'''



# Slicing

import numpy as nagaraj

arr1 = nagaraj.array([1,2,3,4,5,6,7,8])
print(" 2 To 5: ", arr1[2:5])
print(" upto To 5: ", arr1[:5])
print(" 2 To last: ", arr1[2:])
print("-Ve: ",arr1[-6:-1])
print(" sssssdsds ", arr1[::2])
print(" sssssdsds ", arr1[::-1])
print("Stop : ",arr1[1:6:2])


print(arr1)

# output:
''' 2 To 5:  [3 4 5]
 upto To 5:  [1 2 3 4 5]
 2 To last:  [3 4 5 6 7 8]
-Ve:  [3 4 5 6 7]
 sssssdsds  [1 3 5 7]
 sssssdsds  [8 7 6 5 4 3 2 1]
Stop :  [2 4 6]
[1 2 3 4 5 6 7 8]'''



arr2 = nagaraj.array([[1,2,3,4,5],[11,22,33,44,55],[111,222,333,444,555]])
print(arr2)

print("2-D indexing: ", arr2[1,1:])

print("2-D indexing: ", arr2[1,2:])

print("2-D indexing: ", arr2[2,1:])

# output:
'''[[  1   2   3   4   5]
 [ 11  22  33  44  55]
 [111 222 333 444 555]]
2-D indexing:  [22 33 44 55]
2-D indexing:  [33 44 55]
2-D indexing:  [222 333 444 555]'''


