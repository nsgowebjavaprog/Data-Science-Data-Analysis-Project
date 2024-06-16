# NumPy Array Iterating

# for  loop
#  Iteration

# 1-D

import numpy as ns

arr = ns.array([1,2,3,4,54,566,7,7,8,8,9])
print(arr)
print(arr.size)

for i in arr:
    print(i)
    
    
# output:
    '''[  1   2   3   4  54 566   7   7   8   8   9]
11
1
2
3
4
54
566
7
7
8
8
9'''
    


# 2-D

#  Iterration

arr1 = ns.array([[1,2,3,4],[5,6,7,8]])
print(arr1)

print()

for  j in arr1:
    for k in j:
        print(k)
        
        
# output:
'''[[1 2 3 4]
 [5 6 7 8]]

1
2
3
4
5
6
7
8'''
 
 
 
 # 3-D

#  Iterration
import numpy as np

arr2 = np.array([[[1,2,3,4],[6,7,8,9]]])
print(arr2)

for i in arr2:
    for j in i:
        for k in j:
            print(k)


# output:
'''[[[1 2 3 4]
  [6 7 8 9]]]
1
2
3
4
6
7
8
9'''


# Enumerater   idx's

import numpy as np

arr2 = np.array([[[1,2,3,4],[6,7,8,9]]])
print(arr2)

for i, d in np.ndenumerate(arr2):
    print(i,d)
    
    # output:
    '''[[[1 2 3 4]
  [6 7 8 9]]]
(0, 0, 0) 1
(0, 0, 1) 2
(0, 0, 2) 3
(0, 0, 3) 4
(0, 1, 0) 6
(0, 1, 1) 7
(0, 1, 2) 8
(0, 1, 3) 9'''



