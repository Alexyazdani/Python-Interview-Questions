r'''
Alex Yazdani
9 July 2025

most_frequent_char.py
Write a function that returns the character that appears most frequently in a given string. If there's a tie, return any one of the most frequent characters.
'''


def most_frequent_char(str):
    chars = {}
    max_cnt = 0
    max_char = None
    for c in str:
        chars[c] = chars.get(c,0)+1
    for c in chars:
        if chars[c] > max_cnt:
            max_cnt = chars[c]
            max_char = c
    return max_char


if __name__ == "__main__":
    print(most_frequent_char("hello"))          # 'l'
    print(most_frequent_char("mississippi"))    # 'i' or 's'
    print(most_frequent_char("aabbbcccc"))      # 'c'
    print(most_frequent_char(""))               # None
    print(most_frequent_char("abcd"))           # 'a' or 'b' or 'c' or 'd'
