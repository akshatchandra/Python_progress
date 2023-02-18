# Square Patter
# for i in range(0,4):
#     for j in range(0,4):
#         print("# ",end="")
#     print()

# Traingle Patter
# for i in range(0,4):
#     for j in range(i+1):
#         print("# ",end="")
#         j-=1
#     print()

# Reverse Triangle PAtter
# for i in range(4):
#     for j in range(4-i):
#         print("# ", end="")
#     print()

################################
# For Else
################################

# a=[12,13,14,1,2,29]
# for i in a:
#     if i % 5== 0:
#         print(i)
#         break
# else:
#     print("No number Found")

# Prime Number
# n=4
# for i in range (2,n):
#     if n%i==0:
#         print("Not Prime")
#         break
# else:
#     print("Prime Number")


# n = int(input())
# for i in range(0,n):
#     for j in range(0,i+1):
#         print("* ",end="")
#     print("\r")
#     # print("\n")
# for i in range(n,0,-1):
#     for j in range(0,i+1):
#         print("* ",end="")
#     print("\r")

# n=int(input())
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             print("* ",end="")
#         else: print("  ",end="")
#     print()

# n = int(input())
# for i in range(n):
#     for j in range(i,n-1):
#         print("  ",end="")
#     for k in range(0,i+1):
#         print("* ",end="")
#     print()

## RIGHT DOWNWARD TRIANGLE PATTERN

# n = int(input())
# for i in range(n):
#     for j in range(i):
#         print(" ",end="")
#     for j in range(n, i,-1):
#         print("*",end="")
#     print()

# HOLLOW TRIANGLE STAR PATTERN
# n=int(input())
# for i in range (1,n+1):
#     for j in range(i):
#         if j == 0 or j == i-1:
#             print("* ",end="")
#         else:
#             if i!=n:
#                 print("  ",end="")
#             else:
#                 print("* ",end="")
#     print()

# PYRAMID STAR PATTERN
n=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end='')
    for k in range(2*i-1):
        print("*",end='')
    print()

