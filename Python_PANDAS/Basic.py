# Instalation

import pandas as pd

# Syntax:

import pandas as pd
a = pd.Series()
print(a)


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







