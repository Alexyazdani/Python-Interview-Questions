r'''
Alex Yazdani
21 November 2024

remove_duplicates.py
Remove duplicate items in a list
Modify the list and return the new length
Assumes list is already sorted
'''

def remove_duplicates(nums):
    i = 0
    for j in range (1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1


if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(remove_duplicates(nums))  # Output: 5
    print(nums[:5])  # Output: [0,1,2,3,4]