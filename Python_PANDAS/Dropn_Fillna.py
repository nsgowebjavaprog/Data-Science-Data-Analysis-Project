# HANDLING MISSIMG DATA/VALUES

# dropna , fillna



import pandas as pd

var = pd.read_csv("C:\\_________path__of-csv_______\\file-name{test.csv}")

print(var)


# if NaN then delete that row axis=0 ======> row

var.dropna()  # by Default row axis=0

var.dropna(axix=1)  # Delete all NaN col


var.dropna(how = "all")  # when all values are empty that row only not printed


# Delete null all values of that col

var.dropna(subset = ["NAME_OF_COL"])


# Delete null all values for all col

var.dropna(inplace =True)

# IF 1 null value then only not print if more than 1 then print

var.dropna(thresh = 1)


# IF 2 null value then only not print if more than 2 then print

var.dropna(thresh = 2)


# FILLNA

# if any empty space then it fill into name you provide in code

var.fillna("New_Name")

# if mention 2 col_names in that col NaN values then fill into new_name into all same in a same column

var.fillna({"1st_Col":"1st_New_Name", "2nd_Col":"2nd_New_Name" })


# o/p is if any row is empty then all values of above roww same as NaN row TOP-BOTTOM

var.fillna(method= "ffill")


# o/p is if any row is empty then all values of BELOW roww same as NaN row BOTTOM-TOP

var.fillna(method= "bfill")


