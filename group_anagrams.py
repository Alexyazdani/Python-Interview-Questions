r'''
Alex Yazdani
28 June 2025

group_anagrams.py
Write a Python function that takes a list of strings and groups anagrams together. The function should return a list of lists, with each inner list containing words that are anagrams of each other.
'''


def group_anagrams(lis):
    lists = {}
    for item in lis:
        sorted_str = "".join(sorted(item))
        if sorted_str not in lists:
            lists[sorted_str] = []
        lists[sorted_str].append(item)
    return list(lists.values())


if __name__ == "__main__":
    test_cases = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [""],
        ["a"],
        ["abc", "cab", "bca", "xyz", "zyx", "yxz"],
    ]
    for case in test_cases:
        print(group_anagrams(case))
