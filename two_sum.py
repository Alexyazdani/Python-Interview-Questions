r'''
Alex Yazdani
21 November 2024

two_sum.py
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''


# This is a brute force approach:
# def two_sum(lst, targ):
#     for i, num in enumerate(lst):
#         for j in range(i+1, len(lst)):
#             if num + lst[j] == targ:
#                 return [i, j]


# This is a better approach:
def two_sum(lst, targ):
    seen = {}
    for i, num in enumerate(lst):
        complement = targ - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i


if __name__ == "__main__":
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(two_sum(nums1, target1))  # Expected output: [0, 1]
    nums2 = [3, 2, 4]
    target2 = 6
    print(two_sum(nums2, target2))  # Expected output: [1, 2]
    nums3 = [3, 3]
    target3 = 6
    print(two_sum(nums3, target3))  # Expected output: [0, 1]
