r'''
Alex Yazdani
21 November 2024
find_unique_char.py

Input: "swiss"
Output: "w"

Input: "level"
Output: "v"

Input: "aabbcc"
Output: None
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