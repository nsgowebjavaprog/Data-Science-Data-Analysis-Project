import pandas as pd
'''
var1 = pd.DataFrame({"N":[1,2,3,4],"V":[12,13,14,15]})
var2 = pd.DataFrame({"N":[1,2,3,4],"S":[12,13,14,15]})

var1.join(var2)'''


# 2
'''
var1 = pd.DataFrame({"N":[1,2,3,4],"V":[12,13,14,15]})
var2 = pd.DataFrame({"A":[1,2,3,4],"S":[12,13,14,15]})

#var1.set_index('N', inplace=True)
#var2.set_index('N', inplace=True)

res = var1.join(var2)
print(res)

#output:


   N   V  A   S
0  1  12  1  12
1  2  13  2  13
2  3  14  3  14
3  4  15  4  15'''

# 3
'''var1 = pd.DataFrame({"N":[1,2,3,4],"V":[12,13,14,15]})
var2 = pd.DataFrame({"A":[1,2,3,4],"S":[12,13,14,15]})


res = var1.join(var2,how = "right")
print(res)'''



# 4
'''
var1 = pd.DataFrame({"N":[1,2,3,4],"V":[12,13,14,15]})
var2 = pd.DataFrame({"A":[1,2,3,4],"S":[12,13,14,15]})


res = var1.join(var2,how = "left")
print(res)'''

# output:
'''   N   V  A   S
0  1  12  1  12
1  2  13  2  13
2  3  14  3  14
3  4  15  4  15'''

# 5
'''
var1 = pd.DataFrame({"N":[1,2,3,4],"V":[12,13,14,15]})
var2 = pd.DataFrame({"A":[1,2,3,4],"S":[12,13,14,15]})


res = var1.join(var2,how = "inner")
print(res)'''



# output:
'''
   N   V  A   S
0  1  12  1  12
1  2  13  2  13
2  3  14  3  14
3  4  15  4  15'''

# Correct code
'''
import pandas as pd

var1 = pd.DataFrame({"N":[1,2,3,4],"V":[12,13,14,15]})
var2 = pd.DataFrame({"A":[1,2,3,4],"S":[12,13,14,15]})

var1.set_index('N', inplace=True)
var2.set_index('A', inplace=True)

res = var1.join(var2, on=None, how="inner")
print(res)

# output:
    V   S
N        
1  12  12
2  13  13
3  14  14
4  15  15'''



# append
'''

var1 = pd.DataFrame({"A":[1,2,3,4],"B":[12,13,14,15]})
var2 = pd.DataFrame({"A":[1,2,1,1],"B":[12,13,1,1]})

res = var1.append(var2)
print(res)'''





