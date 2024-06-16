# 1. melt

'''
import pandas as pd

var = pd.DataFrame({"Days":[1,2,3,4,5],"Eng":[10,20,30,40,50],"Maths":[11,22,33,44,55]})
print(var)

# OUTPUT:
  Days  Eng  Maths
0     1   10     11
1     2   20     22
2     3   30     33
3     4   40     44
4     5   50     55


var1 = pd.melt(var)
print(var1)

# output:
   variable  value
0      Days      1
1      Days      2
2      Days      3
3      Days      4
4      Days      5
5       Eng     10
6       Eng     20
7       Eng     30
8       Eng     40
9       Eng     50
10    Maths     11
11    Maths     22
12    Maths     33
13    Maths     44
14    Maths     55



var1 = pd.melt(var, id_vars=["Days"])
print(var1)

# o/p==

   Days variable  value
0     1      Eng     10
1     2      Eng     20
2     3      Eng     30
3     4      Eng     40
4     5      Eng     50
5     1    Maths     11
6     2    Maths     22
7     3    Maths     33
8     4    Maths     44
9     5    Maths     55



var1 = pd.melt(var,id_vars=["Days"], var_name="New_Name", value_name = "New_Value")
print()
print(var1)

# o/p:

   Days New_Name  New_Value
0     1      Eng         10
1     2      Eng         20
2     3      Eng         30
3     4      Eng         40
4     5      Eng         50
5     1    Maths         11
6     2    Maths         22
7     3    Maths         33
8     4    Maths         44
9     5    Maths         55
'''


# 2. pivot


import pandas as pd

var = pd.DataFrame({"Days":[1,1,1,2,2,2],
                    "Stu_name":["a","b","c","a","b","c"],
                    "Eng":[12,23,34,45,56,67],
                    "Maths":[11,22,33,44,55,66]})
                    
print(var)

# o/p:
'''
   days Stu_name  Eng  Maths
0     1        a   12     11
1     2        b   23     22
2     3        c   34     33
3     4        a   45     44
4     5        b   56     55
5     6        c   67     66
'''

var1 = var.pivot(index = "Days", columns = "Stu_name")
print(var1)


# o/p:
'''
           Eng             Maths            
Stu_name     a     b     c     a     b     c
days                                        
1         12.0   NaN   NaN  11.0   NaN   NaN
2          NaN  23.0   NaN   NaN  22.0   NaN
3          NaN   NaN  34.0   NaN   NaN  33.0
4         45.0   NaN   NaN  44.0   NaN   NaN
5          NaN  56.0   NaN   NaN  55.0   NaN
6          NaN   NaN  67.0   NaN   NaN  66.0
'''


# 4

var2 = var.pivot_table(index="Stu_name", columns="Days", aggfunc="mean")
print(var2)

# o/p:
'''
           Eng       Maths      
Days         1     2     1     2
Stu_name                        
a         12.0  45.0  11.0  44.0
b         23.0  56.0  22.0  55.0
c         34.0  67.0  33.0  66.0
'''

# 5
var2 = var.pivot_table(index="Stu_name", columns="Days", aggfunc="avg")
print(var2)
