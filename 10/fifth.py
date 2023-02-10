import pandas

Raw_Housing_Data = pandas.read_csv("1. Regression - Module - (Housing Prices).csv")
print(Raw_Housing_Data)
print(Raw_Housing_Data.dtypes)

print(Raw_Housing_Data.head(10))
print(Raw_Housing_Data.tail(10))


## Descriptive statistics
# -> Count of values for a variable
# -> Mean
# ->Standard Deviation
# ->Minimum value
# ->Maximum Value
# -> Three paercentiles -First,second and third

print(Raw_Housing_Data.describe())
print(Raw_Housing_Data.describe(include='all'))

print(Raw_Housing_Data['Sale Price'].min())
print(Raw_Housing_Data['Sale Price'].max())
print(Raw_Housing_Data['Sale Price'].mean())
print(Raw_Housing_Data['Sale Price'].std())
print(Raw_Housing_Data['Sale Price'].quantile(.50))
print(Raw_Housing_Data['Condition of the House'].unique())


#Numpy Library

import numpy as np
print(np.std(Raw_Housing_Data['Sale Price']))# Std = standard Deviation
print(Raw_Housing_Data['Sale Price'].std()-np.std(Raw_Housing_Data['Sale Price']))

#S=_/E(x-x')^2/n-1
# E=sum of,x= each value in the data set,x'=Mean of all the values in the data set,n= number of the values in the data set

#c-=_/E(x-x')^2/n


print(np.std(Raw_Housing_Data['Sale Price'],ddof = 1)) #dd0f=degree of freedom
print(dir(np))

