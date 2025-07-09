r'''
Alex Yazdani
9 July 2025

word_pattern.py
Write a function that takes a pattern string and a list of words, and returns True if the pattern matches the words one-to-one, otherwise False.
Each letter in the pattern should uniquely map to one word, and vice versa.
'''


def word_pattern(str, lis):
    if len(str) != len(lis):
        return False
    chars = {}
    word_to_char = {}
    for i, c in enumerate(str):
        if c not in chars:
            if lis[i] in word_to_char and word_to_char[lis[i]] != c:
                return False
            chars[c] = lis[i]
            word_to_char[lis[i]] = c
        if lis[i] != chars.get(c, lis[i]):
            return False
    return True



if __name__ == "__main__":
    print(word_pattern("abba", ["dog", "cat", "cat", "dog"]))   # True
    print(word_pattern("abba", ["dog", "cat", "cat", "fish"]))  # False
    print(word_pattern("aaaa", ["dog", "dog", "dog", "dog"]))   # True
    print(word_pattern("abca", ["dog", "cat", "fish", "dog"]))  # True
    print(word_pattern("abca", ["dog", "cat", "fish", "cat"]))  # False
    print(word_pattern("abc", ["dog", "cat"]))                  # False (length mismatch)
    print(word_pattern("", []))                                 # True
    print(word_pattern("ab", ["dog", "dog"]))                   # False
