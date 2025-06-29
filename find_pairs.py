r'''
Alex Yazdani
28 June 2025

find_pairs.py
Write a function that takes a list of integers and returns all pairs of numbers that sum to a target value.
'''


def find_pairs(nums, targ):
    seen = set()
    output = set()
    for num in nums:
        complement = targ - num
        if complement in seen:
            output.add(tuple(sorted((num, complement))))
        seen.add(num)
    return list(output)


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 6),
        ([0, -1, 2, -3, 1], -2),
        ([2, 4, 6, 8], 10),
    ]

    for nums, target in test_cases:
        print(find_pairs(nums, target))
