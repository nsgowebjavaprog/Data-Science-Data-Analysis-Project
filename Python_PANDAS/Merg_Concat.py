import pandas as pd
'''
var1 = pd.DataFrame({"A":[1,2,3,4],"B":[11,22,33,44]})
var2 = pd.DataFrame({"A":[1,2,3,4],"C":[11,22,33,44]})
# 1
pd.merge(var1,var2)
# 2
pd.merge(var1,var2, how = "left")
# 3
pd.merge(var1,var2, how = "left/outer/inner/rigth/", indicator = True)


# CONCAT
# 1
a1 = pd.Series([1,2,3,4])
a2 = pd.Series([11,22,33,44])
pd.concat([a1,a2])


# 2
var1 = pd.DataFrame({"A":[1,2,3,4],"B":[11,22,33,44]})
var2 = pd.DataFrame({"A":[1,2,3,4],"C":[11,22,33,44]})
pd.concat([var1,var2])

# 3

var1 = pd.DataFrame({"A":[1,2,3,4],"B":[11,22,33,44]})
var2 = pd.DataFrame({"C":[1,2,3,4],"D":[11,22,33,44]})
res = pd.concat([var1,var2])
print(res)'''

# OUTPUT:
'''
     A     B    C     D
0  1.0  11.0  NaN   NaN
1  2.0  22.0  NaN   NaN
2  3.0  33.0  NaN   NaN
3  4.0  44.0  NaN   NaN
0  NaN   NaN  1.0  11.0
1  NaN   NaN  2.0  22.0
2  NaN   NaN  3.0  33.0
3  NaN   NaN  4.0  44.0'''
'''

# 4
var1 = pd.DataFrame({"A":[1,2,3,4],"B":[11,22,33,44]})
var2 = pd.DataFrame({"C":[1,2,3,4],"D":[11,22,33,44]})
res = pd.concat([var1,var2],axis = 1)
print(res)'''


# OUTPUT:
'''
   A   B  C   D
0  1  11  1  11
1  2  22  2  22
2  3  33  3  33
3  4  44  4  44'''



# 5'''
'''
var1 = pd.DataFrame({"A":[1,2,3,4],"B":[11,22,33,44]})
var2 = pd.DataFrame({"C":[1,2,3,4],"D":[11,22,33,44]})

res = pd.concat([var1,var2],axis = 1,join = "inner")
print(res)
'''

# OUTPUT:
'''
   A   B  C   D
0  1  11  1  11
1  2  22  2  22
2  3  33  3  33
3  4  44  4  44'''''


# 6
'''
var1 = pd.DataFrame({"A":[1,2,3,4],"B":[11,22,33,44]})
var2 = pd.DataFrame({"C":[1,2,3,4],"D":[11,22,33,44]})

res = pd.concat([var1,var2],axis = 1,keys = ["Heading-1", "Heading-2"])
print(res)
'''
# output
'''
  Heading-1     Heading-2    
          A   B         C   D
0         1  11         1  11
1         2  22         2  22
2         3  33         3  33
3         4  44         4  44'''


# 7
'''
var1 = pd.DataFrame({"A":[1,2,3,4],"B":[11,22,33,44]})
var2 = pd.DataFrame({"C":[1,2,3,4],"D":[11,22,33,44]})

res = pd.concat([var1,var2],axis = 0,keys = ["Heading-1", "Heading-2"])
print(res)
'''
# output:
'''
               A     B    C     D
Heading-1 0  1.0  11.0  NaN   NaN
          1  2.0  22.0  NaN   NaN
          2  3.0  33.0  NaN   NaN
          3  4.0  44.0  NaN   NaN
Heading-2 0  NaN   NaN  1.0  11.0
          1  NaN   NaN  2.0  22.0
          2  NaN   NaN  3.0  33.0
          3  NaN   NaN  4.0  44.0'''


# 8








