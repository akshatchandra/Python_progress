# def greet():
#     print("Hello")
#     print("Sir/Madam")
#
# greet()

# def add(x,y):
#     c = x + y
#     # print(c)
#     return c
# add(3,2)
# result = add(4,2)
# print(result)

# def add_sub(x,y):
#     c = x + y
#     d = x - y
#     return c,d
# result1, result2 = add_sub(4,2)
# print(result1,result2)

# *************************
# Function Arguments
# *************************

# def update(x):
#     x = 3
#     print(x)
# # update(10)
# a = 2
# update(3)
# print("a ",a)

# def person(name,age=20):
#     print(name)
#     print(age-2)
# person('xyz',32)
# person(age=32,name='aks')
# person('Aks',)
# person('aks',31)
def sum(a,* b):
    # c = a + b
    # print(c)
    x = a
    for i in b:
        x = x + i
    print(x)
sum(1,3,2,1)