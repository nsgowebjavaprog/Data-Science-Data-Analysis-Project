# insert and Delete

import numpy as np

a = np.array([1,2,3,4])

print(a)
added = np.insert(a, 2,2200)

print(added)

#OUTPUT:
'''1 2 3 4]
[   1    2 2200    3    4]
'''



# insert

import numpy as np

a = np.array([1,2,3,4])

print(a)
added = np.insert(a, (2,4),2200)

print(added)

#OUTPUT:
'''[1 2 3 4]
[   1    2 2200    3    4 2200]'''



# Delete

import numpy as np

a = np.array([1,2,3,4])

print(a)
delete = np.delete(a, 3)
delete1 = np.delete(a, 1)
delete2 = np.delete(a, 2)

print(delete)
print(delete1)
print(delete2)

# OUTPUT:
'''
[1 2 3 4]
[1 2 3]
[1 3 4]
[1 2 4]'''