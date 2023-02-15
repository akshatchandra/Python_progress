# If and else
# if True:
#     print("Loops")
# if False:
# print("nothing")

# x = int(input())
# r = x % 2
# if r==0:
#     print("Even")
# else:
#     print("Odd")

# x=0
# if (x==1):
#     print("One")
# elif (x==2):
#     print("Two")
# elif(x==3):
#     print("Three")
# else :
#     print("Wrong Input")

# While Loop:>

# i=1
# while (i<=5):
#     print("While")
#     i=i+1

# i = 4
# while i >= 1:
#     print("hello")
#     i -= 1

# i = 1
# while i<=5:
#     print("Hello",end="")
#     j = 1
#     while j<=2:
#         print("Brother",end="")
#         j=j+1
#     i=i+1
#     print()

# For Loops

# x= ['xyz',2,2.3,4]
# # print(x)
# for i in x:
#     print(i)

# for i in range(1,10,1):
#     print(i)

# for i in range(20,10,-1):
#     print(i)

# for i in range(1,21):
#     if i%5!=0:
#         print(i)

# Break Continue and Pass

# av=4
# x=int(input())
# i=1
# while i<=x:
#     if i>av:
#         print("Out of stock")
#         break
#     print("we have candy")
#     i+=1
# print("no more candy")

# for i in range (1,101):
#     if (i%3==0):
#         continue
#     print(i)
# print("Finish")

for i in range(1,101):
    if i%2!=0:
        continue # Or pass
    else:
        print(i)
print("Finish")


