r'''
Alex Yazdani
11 July 2025

Write a function is_isomorphic(s: str, t: str) -> bool that determines if two strings s and t are isomorphic.
    Two strings are isomorphic if the characters in s can be replaced to get t, with a one-to-one mapping.
    No two characters may map to the same character, but a character can map to itself.'''


def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    chars_s = {}
    chars_t = {}
    counter_s = 0
    counter_t = 0
    list_s = []
    list_t = []
    for sc, tc in zip(s, t):
        if sc not in chars_s:
            chars_s[sc] = counter_s
            counter_s += 1
        if tc not in chars_t:
            chars_t[tc] = counter_t
            counter_t += 1
        list_s.append(chars_s[sc])
        list_t.append(chars_t[tc])
    return list_s == list_t

if __name__ == "__main__":
    print(is_isomorphic("egg", "add"))        # Expected: True
    print(is_isomorphic("foo", "bar"))        # Expected: False
    print(is_isomorphic("paper", "title"))    # Expected: True
    print(is_isomorphic("ab", "aa"))          # Expected: False
    print(is_isomorphic("a", "a"))            # Expected: True
