# import array as arr
from array import *
vals = array('i',[5,4,7,8,2,1])
# print(vals.buffer_info())
# print(vals.typecode)
# vals.reverse()
# print(vals[])
# for i in range(len(vals)):
#     print(vals[i])

# vals=array('u',['a','e','o'])
# for e in vals:
#     print(e)

# newArr = array(vals.typecode,(a for a in vals))
# i=0
# while i<len(newArr):
#     print(newArr[i])
#     i+=1

# SORTING IN ARRAY
# import numpy as np
# arr = np.array(vals)
# print(np.sort(vals))

# Array from the User
# arr= array('i',[])
# n = int(input("Enter the length of the array"))
# for i in range(n):
#     x = int(input("Enter the Values"))
#     arr.append(x)
# print(arr)
#
# val = int(input('Enter the value for search'))
# k=0
# for e in arr:
#     if e==val:
#         print(k)
#         break
#     k+=1

# NUMPY
from array import *
# import numpy as np
from numpy import *
# arr = array('i',[1,2,3],[3,2,1])
# print(arr)

# 6 ways to creating an array
# array
# linspace()
# logspace()
# arange()
# zeros()
# ones()

# arr = array([1,2,3,4,5])
# print(arr.dtype)
# print(arr)

# LINESPACE
# arr = linspace(0,15) #if last element is not present then it take 50 parts as default
# arr = linespace(0,15,16)
# print(arr)

# ARANGE
# arr = arange(1,16,2)
# print(arr)

# LOGSPACE
# arr = logspace(1,2,40,3)
# print('%.2f' %arr[3])

# ZEROS
# arr = zeros(5)
# print(arr)

# ONES
# arr = ones(4,int)
# print(arr)

# arr = array([1,2,3,4,5],int)
# for i in arr:
#     print(i+5)

# arr = array([1,2,4,5,6])
# arr2 = arr + 5
# print(arr2)

# arr1 = array([1,2,3])
# arr2 = array([3,2,1])
# arr3 = arr1 + arr2
# print(arr3)

arr = array([1,3,4,5,2])
# arr1 = array([2,3,4,6,7])
# print(sin(arr))
# print(cos(arr))
# print(log(arr))
# print(sqrt(arr))
# print(sum(arr))
# print(min(arr))
# print(sort(arr))
# print(concatenate([arr,arr1]))
# arr1 = array([12,3,4,5,3])
# arr1 = arr.copy()
# print(arr)
# print(arr1)
# print(id(arr))
# print(id(arr1))

arr = array([
    [1,2,3],
    [3,2,1]
])
# print(arr)
# print(arr.dtype)
# print(arr.shape)
# print(arr.ndim)
# arr2 = arr.flatten()
# arr3 = arr.reshape(2,3)
# print(arr3)
# print(arr2)
# print(arr.size)

# **********
# Matrices
# **********

m1= matrix('1 2 3 ;4 5 4; 3 2 6')
# print(m)
# print(m.diagonal())
# print(m.min())
# print(m.max())

# m2 = matrix('1 3 2 ;4 5 5; 3 1 6')
# m3 = m1 * m2;
# print(m3)

