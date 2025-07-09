r'''
Alex Yazdani
9 July 2025

missing_number.py
Write a function that returns the missing number from an unsorted list containing all integers from 0 to n, except one.
    The list contains n unique numbers in the range 0 to n, missing one number.
    The input list may be unsorted.
    Return the missing number.
'''


# O(N) Solution
def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


# O(N^2) Solution
# def missing_number(nums):
#     for i in range(len(nums)+1):
#         if i not in nums:
#             return i
#     return None


if __name__ == "__main__":
    test_cases = [
        [3, 0, 1],        # 2
        [0, 1],           # 2
        [9,6,4,2,3,5,7,0,1],  # 8
        [0],              # 1
        [1],              # 0
    ]
    for nums in test_cases:
        print(missing_number(nums))
