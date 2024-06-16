# Handling Missing Data

#  Replace & Interpolate

import pandas as pd


# Access data from csv file

import pandas as pd

var = pd.read_csv("C:\\_________path__of-csv_______\\file-name{test.csv}")

print(var)



# Replace 

var.replace(to_replace=1,value=100)

var.replace(to_replace="NS",value="NSLONI")

var.replace([1,2,3,4,5,6,7,8,9,10],111)
