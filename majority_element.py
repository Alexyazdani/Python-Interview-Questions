r'''
Alex Yazdani
28 June 2025

majority_element.py
Write a function that takes a list of integers and returns the majority element — the element that appears more than half the time. If no such element exists, return None.
'''


def majority_element(nums):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    for num, count in counts.items():
        if count > len(nums) // 2:
            return num
    return None


if __name__ == "__main__":
    test_cases = [
        [3, 3, 4, 2, 3, 3, 3],      # 3
        [1, 2, 3, 4],               # None
        [2, 2, 1, 1, 2, 2],         # 2
        [5],                        # 5
        [1, 1, 1, 2, 2],            # 1
        [1, 2, 3, 1, 2, 3]          # None
    ]

    for nums in test_cases:
        print(majority_element(nums))



