# def sum( a,b):
#     c=a+b
#     print(c)
#
# sum(3,2)

# def sum(a,*b):
# def sum(*b):
#     # c = a
#     c=0
#     for i in b:
#         c=c+i
#     print(c)
#
# sum(4,3,2,1)

# KWARGGS Keyword Variable Length Argument

# def person(name,**data):
#     # print(data)
#     # print(name)
#     for i,j in data.items():
#         # i=i+data
#         print(i,j)
#         # print(i)
#         # print(j)
#
#
#
# person('aksh',age=23,city='delhi',mob=1234)


# Scope

# a =10
# def something():
#     a=14
#     # global a
#
#     # a=90
#     x = globals()['a']
#     # a=21
#     print("in the function",a)
#     globals()['a'] = 90
# something()
# print("outside the function",a)


# List to a Function
#
# def count(list):
#     even = 0
#     odd = 0
#
#     for i in list:
#         if i%2==0:
#             even+=1
#         else:
#             odd+=1
#     return even, odd
#
# list = [1,2,3,4,5,6,7,8,9,10]
#
# even, odd = count(list)
# print(even)
# print(odd)


# Fibinaxcii Series
# def fibo(n):
#     a=0
#     b=1
#     print(a)
#     print(b)
#     for i in range(2,n):
#         # n-=1
#         c=a+b
#         a=b
#         b=c
#         print(c)
# fibo(5)

# Factorial

# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f = f * i
#     return f
# x = int(input())
# # x=4
#
# result = fact(x)
# print(result)

# Recursion

# Factorial using recursion
#
# def fact(n):
#     if n==0:
#         return 1
#     return n * fact(n-1)
#
# result = fact(4)
# print(result)

# Anonymous Function or lambda function
# f=lambda a : a*a
# result = f(3)
# print(result)

def is_even
    return
nums = [2,3,4,1,5,6,]
evens = list(filter(is_even,nums))