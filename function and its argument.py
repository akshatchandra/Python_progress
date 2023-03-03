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

a =10
def something():
    a=14
    # global a

    # a=90
    x = globals()['a']
    # a=21
    print("in the function",a)
    globals()['a'] = 90
something()
print("outside the function",a)


