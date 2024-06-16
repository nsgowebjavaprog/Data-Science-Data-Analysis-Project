# Interpolate
# 1


import pandas as pd

var = pd.read_csv("C:\\path\\file name")

# data file by any value

var.interpolate


# 2.method:{'linear','time','index','values','nearest','zero','slinear','quadratic','cublic',
# 'barycentric', krogh, polynomial, spline, piecewise, \_polynomial, from_derivatives, pchip, akimaa

var.interpolate(method="linear")

var.interpolate(method="linear",axis=0)

var.interpolate(method="linear",axis=1)   # ROW

# Fill the random data to file limit=10 10 data item was filled

var.interpolate ( limit = 10 )

# direction
var.interpolate ( limit_direction="backword", limit = 10 )

var.interpolate ( limit_direction="forword", limit = 10 )

var.interpolate ( limit_direction="both", limit = 10 )


# Fill the data inside

var.interpolate(limit_area = "inside")

# Fill the data outside

var.interpolate(limit_area = "outside")
























