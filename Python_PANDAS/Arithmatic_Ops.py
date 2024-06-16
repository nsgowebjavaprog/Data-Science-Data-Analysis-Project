# Arithmatic Operation in PANDAS

import pandas as ps

arr = ps.DataFrame({"A":[1,2,3,4,5],"B":[6,7,8,9,0]})


arr["Add"] = arr["A"] * arr["B"]
print(arr)

# output:
'''   A  B  Add
0  1  6    6
1  2  7   14
2  3  8   24
3  4  9   36
4  5  0    0'''

arr["res"] = arr["Add"] > 10
print(arr)

# output:
'''   A  B   Add    res
0  1  6  True  False
1  2  7  True  False
2  3  8  True  False
3  4  9  True  False
4  5  0  True  False'''



#  insert & Delete Data in pandas python

import pandas as pd

var = pd.DataFrame({"A":[1,2,3,4,5],"B":[9,8,7,6,5]})
var

var.insert(1,"Python",var["A"])
var


# output:
'''

A	Python	B
0	1	1	9
1	2	2	8
2	3	3	7
3	4	4	6
4	5	5	5
'''