r'''
Alex Yazdani
9 July 2025

all_unique.py
Write a function that returns True if all characters in a string are unique (no repeats), False otherwise.
'''


def all_unique(str):
    chars = {}
    for c in str:
        if c in chars:
            return False
        chars[c] = True
    return True


if __name__ == "__main__":
    print(all_unique("abcdef"))     # True
    print(all_unique("hello"))      # False
    print(all_unique(""))           # True
    print(all_unique("AaBbCc"))     # True
    print(all_unique("Python!"))    # True
    print(all_unique("112233"))     # False
