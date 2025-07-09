r'''
Alex Yazdani
9 July 2025

first_unique_index.py
Write a function that returns the index of the first character in a string that does not repeat. If all characters repeat, return -1.
'''


def first_unique_index(str):
    chars = {}
    for c in str:
        chars[c] = chars.get(c,0)+1
    for i,c in enumerate(str):
        if chars[c] == 1:
            return i
    return -1


if __name__ == "__main__":
    test_cases = [
        "leetcode",         # 0 ('l')
        "loveleetcode",     # 2 ('v')
        "aabb",             # -1
        "abcabcde",         # 6 ('d')
        "xxyz",             # 2 ('y')
        "a",                # 0
    ]
    for s in test_cases:
        print(first_unique_index(s))
