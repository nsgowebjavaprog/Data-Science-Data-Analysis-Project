# 1
'''
import pandas as pd

var = pd.DataFrame({ "name" : ["n","s","l","o","n","i"],
                     "sub_id_1":[10,20,30,40,50,60],
                     "sub_id_2":[11,22,33,44,55,66]})
print(var)


# output:
 name  sub_id_1  sub_id_2
0    n        10        11
1    s        20        22
2    l        30        33
3    o        40        44
4    n        50        55
5    i        60        66

var_new = var.groupby("name")
print(var_new)

# output:<pandas.core.groupby.generic.DataFrameGroupBy object at 0x00000244D00A9C90>

for x,y in var_new:
    print(x)
    print(y)
    
# output:

  name  sub_id_1  sub_id_2
0    n        10        11
1    s        20        22
2    l        30        33
3    o        40        44
4    n        50        55
5    i        60        66
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x00000242066D9C90>
i
  name  sub_id_1  sub_id_2
5    i        60        66
l
  name  sub_id_1  sub_id_2
2    l        30        33
n
  name  sub_id_1  sub_id_2
0    n        10        11
4    n        50        55
o
  name  sub_id_1  sub_id_2
3    o        40        44
s
  name  sub_id_1  sub_id_2
1    s        20        22'''

# 1
'''
import pandas as pd

var = pd.DataFrame({ "name" : ["n","s","l","o","n","i"],
                     "sub_id_1":[10,20,30,40,50,60],
                     "sub_id_2":[11,22,33,44,55,66]})
print(var)

var_new = var.groupby("name")
print(var_new)

for x,y in var_new:
    print(x)
    print(y)
    print()'''

# 2

import pandas as pd

var = pd.DataFrame({ "name" : ["n","s","l","o","n","i"],
                     "sub_id_1":[10,20,30,40,50,60],
                     "sub_id_2":[11,22,33,44,55,66]})
print(var)

var_new = var.groupby("name")
print(var_new)

for x,y in var_new:
    print(x)
    print(y)
    print()
    print()
    print()
    
a=var_new.get_group("n")
print(a)
# output:
'''
  name  sub_id_1  sub_id_2
0    n        10        11
4    n        50        55
'''
b = var_new.min()
print(b)
# output:
'''
      sub_id_1  sub_id_2
name                    
i           60        66
l           30        33
n           10        11
o           40        44
s           20        22
'''


b = var_new.mean()
print(b)

# output:
'''      sub_id_1  sub_id_2
name                    
i         60.0      66.0
l         30.0      33.0
n         30.0      33.0
o         40.0      44.0
s         20.0      22.0
'''

















