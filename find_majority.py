r'''
Alex Yazdani
14 July 2025

find_majority.py
Write a function called find_majority(nums: list[int]) -> int that returns the element that appears more than n // 2 times in the list. 
You can assume such an element always exists.
'''


def find_majority(nums: list[int]) -> int:
    # Your code here
    pass


if __name__ == "__main__":
    print(find_majority([3, 2, 3]))                # Expected: 3
    print(find_majority([2, 2, 1, 1, 1, 2, 2]))     # Expected: 2
    print(find_majority([1, 1, 1, 2, 3, 1]))        # Expected: 1
