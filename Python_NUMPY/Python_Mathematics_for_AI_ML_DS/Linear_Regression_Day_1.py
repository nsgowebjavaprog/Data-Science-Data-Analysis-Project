'''import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 
# Import points
df = pd.read_csv('https://bit.ly/3goOAnt', delimiter=",") 
# Extract input variables (all rows, all columns but last column)
X = df.values[:, :-1] 
# Extract output column (all rows, last column)
Y = df.values[:, -1] 
# Fit a line to the points
fit = LinearRegression().fit(X, Y) 
# m = 1.7867224, b = -16.51923513
m = fit.coef_.flatten()
b = fit.intercept_.flatten()
print("m = {0}".format(m))
print("b = {0}".format(b)) 
# show in chart
plt.plot(X, Y, 'o') # scatterplot
plt.plot(X, m*X+b) # line
plt.show()'''

# 2   Calculating the residuals for a given line and data

'''import pandas as pd 
# Import points
points = pd.read_csv('https://bit.ly/3goOAnt', 
delimiter=",").itertuples() 
# Test with a given line
m = 1.93939
b = 4.73333 
# Calculate the residuals
for p in points: 
    y_actual = p.y 
    y_predict = m*p.x + b 
    residual = y_actual - y_predict 
    print(residual)'''
# output:
'''-1.67272
1.3878900000000005
-0.5515000000000008
2.5091099999999997
-0.4302799999999998
-1.3696699999999993
0.6909400000000012
-2.2484499999999983
2.812160000000002
-1.1272299999999973'''


# 3  Using inverse and transposed matrices to fit a linear regression
'''
import pandas as pd
from numpy.linalg import inv
import numpy as np 
# Import points
df = pd.read_csv('https://bit.ly/3goOAnt', delimiter=",") 
# Extract input variables (all rows, all columns but last column)
X = df.values[:, :-1].flatten() 
# Add placeholder "1" column to generate intercept
X_1 = np.vstack([X, np.ones(len(X))]).T 
# Extract output column (all rows, last column)
Y = df.values[:, -1] 
# Calculate coefficents for slope and intercept
b = inv(X_1.transpose() @ X_1) @ (X_1.transpose() @ Y)
print(b) # [1.93939394, 4.73333333] 
# Predict against the y-values
y_predict = X_1.dot(b)'''

# OUTPUT: [1.93939394 4.73333333]

# 4 Using QR decomposition to perform a linear regression
'''
import pandas as pd
from numpy.linalg import qr, inv
import numpy as np 
# Import points
df = pd.read_csv('https://bit.ly/3goOAnt', delimiter=",") 
# Extract input variables (all rows, all columns but last column)
X = df.values[:, :-1].flatten() 
# Add placeholder "1" column to generate intercept
X_1 = np.vstack([X, np.ones(len(X))]).transpose() 
# Extract output column (all rows, last column)
Y = df.values[:, -1] 
# calculate coefficents for slope and intercept
 # using QR decomposition
Q, R = qr(X_1)
b = inv(R).dot(Q.transpose()).dot(Y) 
print(b)'''

# OUTPUT :  [1.93939394 4.73333333]


# 5  Using gradient descent to find the minimum of a parabola
''' 
import random 
def f(x): 
    return (x - 3) ** 2 + 4 
def dx_f(x): 
    return 2*(x - 3) 
# The learning rate
L = 0.001   

iterations = 100_000 
# start at a random x
x = random.randint(-15,15) 
for i in range(iterations): 
# get slope 
    d_x = dx_f(x) 
# update x by subtracting the (learning rate) * (slope) 
    x -= L * d_x 
print(x, f(x))'''

# OUTPUT: 2.999999999999889 4.0


# 6

# Plotting the loss function for linear regression
 
from sympy import *
from sympy.plotting import plot
import pandas as pd
import numpy as np

points = list(pd.read_csv("https://bit.ly/2KF29Bd").itertuples())
m, b, i, n = symbols('m b i n')
x, y = symbols('x y', cls=Function)
sum_of_squares = Sum((m*x(i) + b - y(i)) ** 2, (i, 0, n)).subs(n, len(points) - 1).doit()
sum_of_squares = sum_of_squares.replace(x, lambda i: points[i].x).replace(y, lambda i: points[i].y)

# Compute the minimum of the sum of squares
min_sum_of_squares = Min(sum_of_squares, m, b)

# Extract the values of m and b that minimize the sum of squares
m_min, b_min = min_sum_of_squares.args[1:]

# Generate x values for the regression line
x_values = np.linspace(min(points, key=lambda x: x.x).x, max(points, key=lambda x: x.x).x, 100)

# Generate y values for the regression line
y_values = [m_min * x + b_min for x in x_values]

# Plot the data points and the regression line
plot(x_values, y_values, (points, 'bo'), title='Linear Regression', xlabel='x', ylabel='y', show=True)