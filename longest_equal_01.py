r'''
Alex Yazdani
9 July 2025

longest_equal_01.py
Write a function that takes a list of numbers and returns the length of the longest contiguous subarray with equal number of 0s and 1s.    The string alternates between messages from "You:" and "Ex:"
    The list only contains 0s and 1s.
    Subarray must be contiguous.
    Return the length — not the subarray.
'''


def longest_equal_01(nums):
    count_map = {}
    count_map[0] = -1
    max_len = 0
    running_sum = 0
    for i, num in enumerate(nums):
        if num == 1:
            running_sum += 1
        else:
            running_sum -= 1
        if running_sum in count_map:
            length = i - count_map[running_sum]
            if length > max_len:
                max_len = length
        else:
            count_map[running_sum] = i
    return max_len


if __name__ == "__main__":
    test_cases = [
        [0, 1],                      # 2
        [0, 1, 0],                   # 2
        [0, 0, 1, 0, 0, 0, 1, 1],    # 6
        [0, 0, 1, 1, 0],             # 4
        [1, 1, 1, 0, 0, 1, 0],       # 6
        [1, 1, 1, 1],                # 0
    ]

    for nums in test_cases:
        print(longest_equal_01(nums))
