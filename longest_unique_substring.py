r'''
Alex Yazdani
28 June 2025

longest_unique_substring.py
Write a function that takes a string and returns the length of the longest substring with no repeating characters.
'''


def longest_unique_substring(str):
    substr = ""
    length = 0
    for c in str:
        if c not in substr:
            substr += c
        else:
            length = longest_unique_substring(str[len(substr):])
            break
    return max(length, len(substr))


if __name__ == "__main__":
    test_cases = [
        "abcabcbb",    # 3 → "abc"
        "bbbbb",       # 1 → "b"
        "pwwkew",      # 3 → "wke"
        "",            # 0
        "abcdef",      # 6
        "abba"         # 2 → "ab" or "ba"
    ]

    for s in test_cases:
        print(longest_unique_substring(s))




