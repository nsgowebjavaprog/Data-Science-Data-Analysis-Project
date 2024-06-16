#  Number Theory
#  Irrational numbers-- certain numbers like √2
# 1
'''my_value = 2 * (3 + 2)**2 / 5 - 4 
 
print(my_value)  #  6.0

# 2
x = int(input("Please input a number\n")) 
product = 3 * x 
print(product)

# 3
def f(x): 
    return 2 * x + 1 
x_values = [0, 1, 2, 3] 
for x in x_values: 
    y = f(x) 
    print(y)'''

# OUTPUT:
'''
1
3
5
7'''

# 4
'''from sympy import * 
x = symbols('x')
f = 2*x + 1
plot(f)'''

# 5
'''from sympy import * 
x = symbols('x')
f = x**2 + 1
plot(f)'''

# 6
'''from sympy import *
from sympy.plotting import plot3d 
x, y = symbols('x y')
f = 2*x + 3*y
plot3d(f)'''

# 7
# Summations
'''summation = sum(2*i for i in range(1,6))
print(summation)'''
# 30


from sympy import * 
 
i,n = symbols('i n') 
 
# iterate each element i from 1 to n,
 # then multiply and sum
summation = Sum(2*i,(i,1,n)) 
 
# specify n as 5,
 # iterating the numbers 1 through 5
up_to_5 = summation.subs(n, 5)
print(up_to_5.doit())

# 30

#  Exponents


