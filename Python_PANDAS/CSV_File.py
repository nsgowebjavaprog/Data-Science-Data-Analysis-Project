# CSV FILE
'''
import pandas as pd

dis = {"A":[1,2,3,4,5],"B":[6,7,8,9,10],"C":[11,33,55,77,99]}

d = ps.DataFrame(dis)

print(d)

d.to_csv("Test_new.csv")'''

# output:
'''   A   B   C
0  1   6  11
1  2   7  33
2  3   8  55
3  4   9  77
4  5  10  99'''

import pandas as pd

# Create a DataFrame
dis = {"A":[1,2,3,4,5],"B":[6,7,8,9,10],"C":[11,33,55,77,99]}
d = pd.DataFrame(dis)

# Save the DataFrame to a CSV file
d.to_csv("Test_new.csv", index=False)

# Read the CSV file
df = pd.read_csv("Test_new.csv")

print(df)

# output:
'''

  A   B   C
0  1   6  11
1  2   7  33
2  3   8  55
3  4   9  77
4  5  10  99
'''