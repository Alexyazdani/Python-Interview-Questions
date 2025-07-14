r'''
Alex Yazdani
14 July 2025

longest_common_prefix.py
Write a function longest_common_prefix(strs: list[str]) -> str that returns the longest common prefix among all strings in the list strs.
If there is no common prefix, return an empty string "".
'''


def longest_common_prefix(strs: list[str]) -> str:
    if not strs:
        return ""
    prefix = ""
    for i in range(len(strs[0])):
        char = strs[0][i]
        for s in strs:
            if i >= len(s) or s[i] != char:
                return prefix
        prefix += char
    return prefix


if __name__ == "__main__":
    print(longest_common_prefix(["flower", "flow", "flight"]))      # Expected: "fl"
    print(longest_common_prefix(["dog", "racecar", "car"]))         # Expected: ""
    print(longest_common_prefix(["interspecies", "interstellar", "interstate"]))  # Expected: "inters"
    print(longest_common_prefix(["a"]))                             # Expected: "a"
    print(longest_common_prefix(["", "b"]))                         # Expected: ""
    print(longest_common_prefix([]))                                # Expected: ""
