## List
a = [1, 3, 5, 2, 4, 6]
print(type(a))
a[2]
print(a[2])

## Tuple
x = (2,1,3,4,5)
print(type(x))
print(x[2])

##Dictionary
z = {1:3,2:6,4:5,3:4}
print(type(z))
print(z[2])

## Sets
k = {2,3,9,5,543,8}
print(type(k))

##Basic Arthemtic Operaiton
x = 98
y = 9
z = x**2 + 9**4j
score = (z/y**2)
print(z)
print(score)
print(type(score))

### Importing of Library
# import pandas
#
# Raw_Housing_Data = pandas.read_csv("1. Regression - Module - (Housing Prices).csv")
# print(Raw_Housing_Data)

## Conditional Statement
## If and else
i = 'late'
if (i == 'late'):
    print('order')
else:
    print('cook')

i = 'early'
if (i == 'late'):
    print('order')
else:
    print('cook')

num = 50
if num > 50:
    if num%2==0:
        print("number is even and greater than 50")
    else:
        print("number is not even and greater than 50")
else:
    if num%2 != 0:
        print("number is odd and less than 50")
    else:
        print("number is not odd and less than 50")

## Iterative Statement
for i in range(0,6,2):
    print("hello World")

##Calculation of factorial of 10:
fact = 1
for i in range(1,11):
    fact = fact * i
print(fact)

## Function
def square(a):
    sq = a*a
    return sq
print(square(2))

def factorial(value):
    fact = 1
    for i in range(1,value+1):
        fact = fact*i
    return fact
n = 10
r = 6
c = factorial(n)/(factorial(r) * factorial(n-r))
print(str (c))

#######################################################################################################################
import pandas

Raw_Housing_Data = pandas.read_csv("1. Regression - Module - (Housing Prices).csv")
print(Raw_Housing_Data)
print(Raw_Housing_Data.dtypes)

print(Raw_Housing_Data.head(10))
print(Raw_Housing_Data.tail(10))


# Descriptive statistics
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


# Numpy Library

import numpy as np
print(np.std(Raw_Housing_Data['Sale Price'])) #Std = standard Deviation
print(Raw_Housing_Data['Sale Price'].std()-np.std(Raw_Housing_Data['Sale Price']))

# S=_/E(x-x')^2/n-1
# E=sum of,x= each value in the data set,x'=Mean of all the values in the data set,n= number of the values in the data set
#
# c-=_/E(x-x')^2/n


print(np.std(Raw_Housing_Data['Sale Price'],ddof = 1)) #dd0f=degree of freedom
print(dir(np))

