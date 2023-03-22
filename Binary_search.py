# pos = -1
# def search(list ,n):
#     # i = 0
#
#     # while i < len(list):
#     #     if list[i] == n:
#     #         globals()['pos'] = i
#     #         return True
#     #     i = i + 1
#
#     for i in range(len(list)):
#         if list[i] == n:
#             print("Found")
#             globals()['pos'] = i
#             return True
#         i = i +1
# list = [5,8,4,6,9,2]

# n = 9
# if search(list,n):
#     print("Found at",pos+1)
# else:
#     print("Not Found")


# Binary Search

# def search(list, n):
#     l = 0
#     u = len(list)-1
#
#     while l <= u:
#         mid  = (l+u) // 2
#
#         if list[mid]==n:
#             globals()['pos']=mid
#             return True
#         else:
#             if list[mid]<n:
#                 l = mid+1;
#             else:
#                 u = mid-1;
#     return False
# list = [4,7,8,12,45,99]
# # n = 4
# n=9
# if search(list,n):
#     print("Found at",pos+1)
# else:
#     print("Not Found")

# Bubble Sort:

# def sort(nums):
#     for i in range(len(nums)-1,0,-1):
#         for j in range(i):
#             if nums[j] > nums[j+1]:
#                 temp = nums[j]
#                 nums[j] = nums[j+1]
#                 nums[j+1] = temp
#
# nums = [5,3,8,6,7,2]
# sort(nums)
# print(nums)

# Selection Sort

def sort(nums):
    for i in range(5):
        minpos = i
        for j in range(i,6):
            if nums[j] < nums[minpos]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
nums = [5,3,8,6,7,2]
sort(nums)

print(nums)