r'''
Alex Yazdani
21 November 2024

find_unique_char.py
Write a Python function that takes a string as input and returns the first non-repeating character in the string. If all characters repeat, return None.
'''

def find_unique_char(str):
    char_count = {}
    for c in str:
        char_count[c] = char_count.get(c, 0) + 1
    for c in str:
        if char_count[c] == 1:
            return c
    return None

if __name__ == "__main__":
    print(find_unique_char("swiss")) # w
    print(find_unique_char("level")) # v
    print(find_unique_char("aabbcc")) # None