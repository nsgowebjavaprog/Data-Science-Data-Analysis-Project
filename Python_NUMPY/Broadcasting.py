# 1
import numpy as ns
a = ns.array([1,2,3,4,5])
print(a)


#2
var1 = ns.array([1,2,3,4,5])
var2 = ns.array([1,2,3,4,5])
print(var1 + var2)

# 3
var1 = ns.array([1,2,3,4,5])
var2 = ns.array([1,3,4,5])
print(var1 + var2)



# 4

var1 = ns.array([[1,2,3,4,5],[1,2,3,4,4]])
print(var1.shape)

var2 = ns.array([[1,2,3,5],[1,2,3,4]])
print(var2.shape)

print(var1 + var2)

# output:
'''(2, 5)
(2, 4)'''



# 6
import numpy as np

var1 = np.array([[1,2,3,4],[1,2,3,4]])
print(var1.shape)

var2 = np.array([[1,2,3,4],[1,2,3,4]])
print(var2.shape)

print(var1 + var2)

# output:

'''(2, 4)
(2, 4)
[[2 4 6 8]
 [2 4 6 8]]'''



