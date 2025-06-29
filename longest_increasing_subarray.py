r'''
Alex Yazdani
28 June 2025

longest_increasing_subarray.py
Write a function that takes a list of integers and returns the length of the longest contiguous subarray where the values are strictly increasing.
Empty lists return 0.
Non-empty, non-increasing lists return 1.
'''


def longest_increasing_subarray(ints):
    if len(ints) == 0:
        return 0
    max_len = 1
    cur_len = 1
    for i in range(len(ints)-1):
        if ints[i+1] > ints[i]:
            cur_len +=1
            if cur_len > max_len:
                max_len = cur_len
        else:
            cur_len = 1
    return max_len


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 2, 3, 4, 1],
        [5, 4, 3, 2, 1],
        [1, 2, 2, 3, 4],
        [],
        [10],
        [1, 3, 5, 4, 6, 8, 9],
    ]

    for nums in test_cases:
        print(longest_increasing_subarray(nums))
