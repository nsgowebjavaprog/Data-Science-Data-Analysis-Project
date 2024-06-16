

# Start Arrray

import pandas as pd

a = [1,2,3,4,5]

res = pd.Series(a)
print(res)
print(type(res))

#OUTPUT:
'''
Trusted

Code

JupyterLab

Python 3 (ipykernel)'''

# Syntax:

import pandas as pd
a = pd.Series()
print(a)
Series([], dtype: object)
Selection deleted'''


# Start Arrray

import pandas as pd

a = [1,2,3,4,5]

res = pd.Series(a)
print(res)
print(type(res))
0    1
1    2
2    3
3    4
4    5
dtype: int64
<class 'pandas.core.series.Series'>'''


# Tables Like row & col

dic = {"name":['nagaraj','ns','loni'], "age":[12,12,23,345], "rank" : [1,2,3,4]}

res = pd.Series(dic)
print(res)

# OUTPUT:
'''name    [nagaraj, ns, loni]
age       [12, 12, 23, 345]
rank           [1, 2, 3, 4]
dtype: object'''


# Same value but Different Index

arar = pd.Series(12,index=[1,2,3,4,5,6,7,8,9])
print(arar)

# OUTPUT:
'''1    12
2    12
3    12
4    12
5    12
6    12
7    12
8    12
9    12
dtype: int64'''



# Ading two arrray 

arr1 = pd.Series(10,index=[1,2,3,4,5,6,7])
arr2 = pd.Series(11,index=[1,2,3,4])

print(arr1+arr2)

# OUTPUT:
'''
1    21.0
2    21.0
3    21.0
4    21.0
5     NaN
6     NaN
7     NaN
dtype: float64'''


# DataFrame in List

import pandas as ps

l = [1,2,3,4,5]
res = ps.DataFrame(l)
print(res)

# OUTPUT:
'''
   0
0  1
1  2
2  3
3  4
4  5'''



# Data Frame in Dictionary

import pandas as ps

dic = {"arr1":[1,2,3,4,5],"arr2":[6,7,8,9,10]}
res = ps.DataFrame(dic)
print(res)

# OUTPUT:
'''   arr1  arr2
0     1     6
1     2     7
2     3     8
3     4     9
4     5    10'''


# Data Frame in Dictionary      acces only i or more col

import pandas as ps

dic = {"arr1":[1,2,3,4,5],"arr2":[6,7,8,9,10]}
res = ps.DataFrame(dic,columns=["arr1"])
print(res)


# OUTPUT:
'''   arr1
0     1
1     2
2     3
3     4
4     5'''


# no.of list

list_1 = [[1,1,1,1,1],[11,22,33,44,55,66]]

res = ps.DataFrame(list_1)
print(res)

# OUTPUT:
'''
   0   1   2   3   4     5
0   1   1   1   1   1   NaN
1  11  22  33  44  55  66.0'''

