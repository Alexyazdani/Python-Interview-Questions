r'''
Alex Yazdani
11 July 2025

first_unique_char.py
Write a function first_unique_char(s: str) -> int that takes a string s and returns the index of the first non-repeating character in the string. If no such character exists, return -1.
'''


def first_unique_char(s: str) -> int:
    chars = {}
    for c in s:
        chars[c] = chars.get(c,0)+1
    for i,c in enumerate(s):
        if chars[c] == 1:
            return i
    return -1

if __name__ == "__main__":
    print(first_unique_char("leetcode"))        # Expected: 0
    print(first_unique_char("loveleetcode"))    # Expected: 2
    print(first_unique_char("aabb"))            # Expected: -1
    print(first_unique_char("aabbccdde"))       # Expected: 8
    print(first_unique_char("abcabc"))          # Expected: -1
    print(first_unique_char("z"))               # Expected: 0
