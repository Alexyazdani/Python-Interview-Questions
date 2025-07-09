r'''
Alex Yazdani
9 July 2025

first_duplicate.py
Write a function that returns the first duplicate element in a list of integers. If there are no duplicates, return None.
'''


def first_duplicate(lis):
    unique_elements = {}
    for item in lis:
        if item in unique_elements:
            return item
        unique_elements[item] = True
    return None


# Below is a functionally correct but slightly less efficient version - O(N)
def first_duplicate_v2(lis):
    unique_elements = {}
    for item in lis:
        unique_elements[item] = unique_elements.get(item, 0) + 1
        if unique_elements[item] > 1:
            return item
    return None


# Below is a functionally correct but significantly less efficient version - O(N^2)
def first_duplicate_v3(lis):
    unique_elements = []
    for item in lis:
        if item in unique_elements:
            return item
        unique_elements.append(item)
    return None


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 2, 4, 5],     # 2
        [5, 1, 5, 2, 3, 4],     # 5
        [1, 2, 3, 4],           # None
        [9, 8, 7, 9, 7],        # 9
        [1, 1, 2, 2, 1],        # 1
        [],                     # None
        [42],                   # None
    ]
    for nums in test_cases:
        print(first_duplicate(nums))
        print(first_duplicate_v2(nums))
        print(first_duplicate_v3(nums))
