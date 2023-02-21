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
arr= array('i',[])
n = int(input("Enter the length of the array"))
for i in range(n):
    x = int(input("Enter the Values"))
    arr.append(x)
print(arr)

val = int(input('Enter the value for search'))
k=0
for e in arr:
    if e==val:
        print(k)
        break
    k+=1
