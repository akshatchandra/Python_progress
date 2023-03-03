# def sum( a,b):
#     c=a+b
#     print(c)
#
# sum(3,2)

# def sum(a,*b):
def sum(*b):
    # c = a
    c=0
    for i in b:
        c=c+i
    print(c)

sum(4,3,2,1)