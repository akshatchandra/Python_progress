# def div(a,b):
#     print(a/b)
#
#
# def smart(func):
#     def inner(a,b):
#         if a<b:
#             a,b = b,a
#         return func(a,b)
#
#     return inner
#
# div = smart(div)
# div(2,4)


# Extra practice due to holi


# Python code 3.x to demonstrate star pattern

# Function to demonstrate printing pattern of alphabets

#
def contalpha(n):
    num = 65
    for i in range(0, n):
        for j in range(0, i+1):
            ch = chr(num)
            print(ch, end=" ")
            num = num + 1
        print("\r")
n = 5
contalpha(n)





