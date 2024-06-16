'''print("Wel-Come Nagaraj Loni For Algrbra With Python Course")
print("mathematics for AI DS ML")
print("Ratio, Proportions and conversions")'''
# Propotions

# 2/4 = 5/10 ---> Cross multi 20 = 20
# 3/6 = x/4 ---> 12 = 6x => /6 ---> {x=2}
# 1 mile / 1.6 km = 2 mile/ x ==> x = 3.2 km   { Cross multi }


# problem-1
'''n1 =1
d1 =2
n2 =0
d2= 16

if n2==0:
    ans = d2*n1/d1
    print("n2= ",ans)
    
if d2==0:
    ans=n2*d1/n1
    print("d2= ",ans)'''

# problem-2
# Extra Problems
# 1*2/3 + 3*4/5 -7  write in python like
'''print(1+2/3+3+4/5-7)  # -1.533333333333334

x=0.9999
print(9*x)
'''

# a/b = c/d
'''
a=1
b=1.29
c=0
d=1
if c==0:
    ans = d*a/b;
    print(ans)'''

# ----2
# solve foe "X"

''' (1). x+3=5-->{x=2} (2). x-2=10--->{12}  (3).3x=12-->{4}    (4).x/4=2-->{2*4=[8]} '''

''' (1). x+0.72 = 11.1-->{10.38}   '''

#Problem--2
'''import sympy
from sympy import symbols
from sympy.solvers import solve

x = symbols('x')
eq = 4*x-2  # x =  [1/2]

eq = x-2 ## x =  [2]

print("x = ",solve(eq,x))'''

# problem--3

'''import sympy
from sympy import symbols
from sympy.solvers import solve

x = symbols('x')
eq = 2*x + 1  # x =  [-1/2]

eq = 4*x + 1  # x =  [-1/4]

print("x = ",solve(eq,x))'''

# problem--3
'''import sympy
from sympy import symbols
from sympy.solvers import solve

x = symbols('x')
eq = input("Entr equation: ")

print("x = ",solve(eq,x))'''

'''output:
Entr equation: 3*x-6
x =  [2]'''


# problem--4
'''import sympy
from sympy import symbols
from sympy.solvers import solve

x = symbols('x')

eq = 2*x-4

solution = solve(eq,x)
print("x = ",solution[0])'''

# output: x =  2

#problem --5

'''import sympy
from sympy import symbols
from sympy.solvers import solve

x = symbols('x')

#eq = 2*x-4    # x :  2
eq = input("Entr equation: ") #Entr equation: (x-1)*(x+2)*(x-3)
                              #x :  -2
                              #x :  1
                              #x :  3

solution = solve(eq,x)
for s in solution:
    print("x : ",s)  '''
    
# problem----6

'''from sympy import*
var('x y')

# First eq set equal to zero, ready to solve
first = 2*x+10

# sympy for eq =0, ready to factor

eq1 = Eq(first,0)  # x= -5
eq1 = Eq(first,y)  # x= y/2 - 5

#sympy solve for x
sol = solve(eq1,x)

# show factored results
print("x=",sol[0]) '''


# problem--7
'''import sympy
from sympy import symbols

var('x y')

eq = 2*x + 10*y +4

sympy.factor(eq)'''

''' import sympy

x, y = sympy.symbols('x y')

eq = 2*x + 10*y + 4   # 2*x + 10*y + 3

eq = 2*x + 10*y + 3   # 2*(x + 5*y + 2)

eq = x**2-4   # (x - 2)*(x + 2)

print(sympy.factor(eq))  '''

'''print("converts STRING input (including fractions) TO FLOAT")

def string_frac(in_string):
    if"/" in in_string:
        nd = in_string.split("/")
        n = float(nd[0])
        d = float(nd[1])
        ans = n/d
        return ans
    else:
        ans = float(in_string)
        return ans

def one_step_add():
    import random
    a = random.randint(-4,10)
    b = random.randint(2,24)
    print("x + ",a,"=", b)
    ans = float(input("x :"))
    answer = b -a
    # test-input
    if ans== answer:
        print("Correct \n")
    else:
        print("Try again")
        print("The correct answer is ",answer,"\n")



def one_step_mult():
    import random
    a = random.randint(1,11)
    b = random.randint(2,24)
    print(a, "x : ",b)
    ans_in = (input("x : "))
    answer = b/a
    # test
    if string_frac(ans_in)== answer:
        print("Correct \n")
    else:
        print("Try again")
        print("The correct answer is ",answer,"\n")'''

# TOPIC---3

# print("Fractions and decimals")

# 1/10 = 0.1
# 1/100 = 0.01
# 1/1000 = 0.001

# 0.234 = 234/1000 => 0.234

# 0.4 = 4/10

# 1
'''
  10x = 4.4444
 -  x = 0.4444
  9x = 4
 x=4/9 = 0.4445 '''
 
 # 2
 
'''print(10**1)
print(10**2)
print(10**3)
print(10**0)
print(10**-1)
print(10**-2)
print(10**-3)
print(10**-4)
 # output:
 10
100
1000
1
0.1
0.01
0.001
0.0001'''


#problem-----1
'''text = input("Enter number:")
print(text)
print(len(text))'''
# 1.output:
'''Enter number:.123
.123
4'''
# 2.output:
'''Enter number:123
123
3'''

#problem-----2
'''text =input("Enter the number: ")
num = float(text)
print(num + 4)'''

# output:
'''Enter the number: 16
20.0'''

# output:
'''Enter the number: .123
4.123'''

#problem-----3

digits = input("Enter a decimal number to convert: ")

# dec--> in int
exponent = int(len(digits))-1

# convert exponent to float
n = float(digits)

# get numerator
numerator = int(n * 10**exponent)

# get denominator
denominator = 10**exponent

# present 1st 2 dec places
percent = n * 100

# OUTPUT
print("The decimal is",n)
print("The fraction is",numerator, "/", denominator)
print("The persent is",percent,"%")

# OUTPUT:
'''Enter a decimal number to convert: .125
The decimal is 0.125
The fraction is 125 / 1000
The persent is 12.5 %'''

# OUTPUT:
'''Enter a decimal number to convert: 123
The decimal is 123.0
The fraction is 12300 / 100
The persent is 12300.0 %'''

