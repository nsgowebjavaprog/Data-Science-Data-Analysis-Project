# coversion from INT to FLOAT

a = np.array([12,34,45,56],dtype="f")
print("Data Type: ",a.dtype)
print(a)

print("_________________________________________")

c = np.array([12,34,45,56])
print("Data Type: ",c.dtype)
print(c)

print("OR_________________OR_______________________OR")

x = np.array([1,2,3,4])

new = np.float32(x)

print("Data Type:",x.dtype)
print("Data Type: ",new.dtype)

print(x)
print(new)
'''
Data Type:  float32
[12. 34. 45. 56.]
_________________________________________
Data Type:  int32
[12 34 45 56]
OR_________________OR_______________________OR
Data Type: int32
Data Type:  float32
[1 2 3 4]
[1. 2. 3. 4.]'''

#
x = np.array([1,2,3,4])

new = np.float32(x)

new_agian = np.int_(new)

print("Data Type:",x.dtype)
print("Data Type: ",new.dtype)
print("Data Type: ",new_agian.dtype)


print(x)
print(new)
print(new_agian)

# SHAPE and RESHAPING

# 1.Shape

import numpy as ns

var = ns.array([[1,2],[3,4]])
print(var)

#
var = ns.array([[1,2,3,4],[3,4,5,6],[1,2,3,4],[3,4,5,6]])
print(var)
print(var.shape)

#
var = ns.array([[1,2,3,4],[3,4,5,6]])
print(var)
print(var.shape)

#  ReShape

var1= ns.array([1,2,3,4,5,6,7,8,9])

x = var1.reshape(3,3)
print(x)

#2-D

var1= ns.array([1,2,3,4,5,6,7,8,9])
print(var1)
print(var1.ndim)

x = var1.reshape(3,3)
print(x)
print(x.ndim)

# 3-D

var2 = ns.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(var2)
print(var2.ndim)

x = var2.reshape(2,3,2)
print(x)
print(x.ndim)

var2 = ns.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(var2)
print(var2.ndim)

x = var2.reshape(2,3,2)
print(x)
print(x.ndim)

one = x.reshape(-1)
print(one)

#  Arithmatic operation

import numpy as np

var = np.array([1,2,3,4])

var_add = var +3

print(var_add)

#

var = np.array([1,2,3,4])

var_add = var * 3

print(var_add)

# 1.ADDITION

var1 = np.array([1,2,3,4])
var2 = np.array([5,6,7,8])

var_add = var1 + var2

print(var_add)

# 2.sub

var1 = np.array([1,2,3,4])
var2 = np.array([5,6,7,8])

var_add = var1 - var2

print(var_add)

# 3.mul

var1 = np.array([1,2,3,4])
var2 = np.array([5,6,7,8])

var_add = var1 * var2

print(var_add)

# 4.Division

var1 = np.array([1,2,3,4])
var2 = np.array([5,6,7,8])

var_add = var1 / var2

print(var_add)

# 5.Mod

var1 = np.array([1,2,3,4])
var2 = np.array([5,6,7,8])

var_add = var1 % var2

print(var_add)

# 6.Power

var1 = np.array([1,2,3,4])
var2 = np.array([5,6,7,8])

var_add = var1 ** var2

print(var_add)

# 7.reciprocal

var1 = np.array([1,2,3,4])
var2 = np.array([5,6,7,8])

var_add = 1/var1 

print(var_add)

# 1 Sum

var1 = np.array([1,2,3,4])
var2 = np.array([5,6,7,8])
sum = np.add(var1,var2)
print(sum)

# 3
var1 = np.array([1,2,3,4])
var2 = np.array([5,6,7,8])
sum = np.add(var1,var2)
print(sum)

sub = np.subtract(var1,var2)
print(sub)

mul = np.multiply(var1,var2)
print(mul)

div = np.divide(var1,var2)
print(div)

mod = np.mod(var1,var2)
print(mod)

power = np.power(var1,var2)
print(power)

reciprocal1 = np.reciprocal(var1)
reciprocal2 = np.reciprocal(var2)
print(reciprocal1)
print(reciprocal2)

# 2
mat1 = np.array([[1,2,3,4],[1,2,3,4]])
mat2 = np.array([[1,2,3,4],[1,2,3,4]])

print(mat1)
print()
print(mat2)
print()

matrix_add = mat1 + mat2
print("Add:")
print(matrix_add)

matrix_add = mat1 * mat2
print("Mul:")
print(matrix_add)

#1

x = np.array([1,2,3,4,5,6,7,8,9])

print(np.min(x))
print(np.max(x))
print(np.argmin(x))
print(np.sqrt(x))
print(np.sin(x))
print(np.cos(x))
print(np.cumsum(x))