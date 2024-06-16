import pandas as pd

csv_1 = pd.read_csv("C:\\user\\_____PATH OF CSV?XL FILE_____\\test.csv")
csv_1


# one row print

import pandas as pd

csv_2 = pd.read_csv("C:\\user\\folder _____PATH OF CSV?XL FILE_____\\test.csv",nrows=1)
print(csv_2)



# 10 row print

import pandas as pd

csv_2 = pd.read_csv("C:\\user\\folder _____PATH OF CSV?XL FILE_____\\test.csv",nrows=10)
print(csv_2)



#   print only column name u mention

import pandas as pd

csv_2 = pd.read_csv("C:\\user\\folder _____PATH OF CSV?XL FILE_____\\test.csv",usecol=["name of column"])
print(csv_2)



#   print only column name u mention {first col=idx == 0}

import pandas as pd

csv_2 = pd.read_csv("C:\\user\\folder _____PATH OF CSV?XL FILE_____\\test.csv",usecol=[0,3])
print(csv_2)


#  #  skip and print row

import pandas as pd

csv_2 = pd.read_csv("C:\\user\\folder _____PATH OF CSV?XL FILE_____\\test.csv",skiprows=[0])
print(csv_2)


# Add new name to col

#   print only column name u mention {first col=idx == 0}

import pandas as pd

csv_2 = pd.read_csv("C:\\user\\folder _____PATH OF CSV?XL FILE_____\\test.csv",header = None,prefix="col")
print(csv_2)


# no.of rows in sheet

csv_1.index

# OUTPUT  START=0,STOP=20

# HEADING NAME OF COLUMN

csv_1.columns


# result of count,mean,std,min,25%,50%

csv_1.describe()


# Print No.of Rows n to mention Num

csv_1.tail(2)

# output is a n and (n-1)th row


# print row on RANGE

csv_1[:10]


# Store in desending order

csv_1.sort_index(axis=0,ascending = False )  # axis=col/row===>0/1


# Change the name 0,0

csv_1.loc[0,"Name_of_col"]="Chaged_Name"

print(csv_1)


# Print col with 2 and 3ed row

csv_1.loc[2,3,["NAME_OF_!ST_COL","NAME_OF_2ND_COL"]]

csv_1.loc[2:10,["NAME_OF_!ST_COL","NAME_OF_2ND_COL"]]


# iloc

csv_1.iloc[0,1]

# o/p: sheet like matrix {0,1}



# DELETE/ DROP

csv_1.drop(0,axis=0)

# axis=0   ----> delete entair col of 0--idx
# 0 --> delete 0--idx row




