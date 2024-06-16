# TOPIC-----1
# Eigenvectors and Eigenvalues

#PROBLEM--1

'''from numpy import array, diag
from numpy.linalg import eig, inv 
A = array([ 
    [1, 2], 
    [4, 5]
     ]) 
eigenvals, eigenvecs = eig(A) 
print("EIGENVALUES")
print(eigenvals)
print("\nEIGENVECTORS")
print(eigenvecs)'''

# OUTPUT
'''
EIGENVALUES
[-0.46410162  6.46410162]

EIGENVECTORS
[[-0.80689822 -0.34372377]
 [ 0.59069049 -0.9390708 ]]'''

# PROBLEM---2
'''from numpy import array, diag
from numpy.linalg import eig, inv 
A = array([ 
    [1, 2], 
    [4, 5]
     ]) 
eigenvals, eigenvecs = eig(A) 
print("EIGENVALUES")
print(eigenvals)
print("\nEIGENVECTORS")
print(eigenvecs) 
print("\nREBUILD MATRIX")
Q = eigenvecs
R = inv(Q) 
L = diag(eigenvals)
B = Q @ L @ R 
print(B)'''

# OUTPUT:
'''EIGENVALUES
[-0.46410162  6.46410162]

EIGENVECTORS
[[-0.80689822 -0.34372377]
 [ 0.59069049 -0.9390708 ]]

REBUILD MATRIX
[[1. 2.]
 [4. 5.]] '''

