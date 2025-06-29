r'''
Alex Yazdani
28 June 2025

one_edit_apart.py
Write a function that checks if two strings are one edit apart (insert, delete, or replace a character).
Note: cannot be 0 edits apart.
'''


def one_edit_apart(str1, str2):
    if abs(len(str1)-len(str2)) > 1:
        return False
    if len(str1) == len(str2):
        mistakes = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                mistakes+=1
        return (mistakes == 1)
    else:
        if len(str1) > len(str2):
            long_str = str1
            short_str = str2
        else:
            long_str = str2
            short_str = str1
        for i in range(len(short_str)):
            if long_str[i] != short_str[i]:
                short_str = short_str[:i] + long_str[i] + short_str[i:]
                return (short_str == long_str)
        return True    


if __name__ == "__main__":
    test_cases = [
        ("pale", "ple"),     # True (delete 'a')
        ("pales", "pale"),   # True (delete 's')
        ("pale", "bale"),    # True (replace 'p' with 'b')
        ("pale", "bake"),    # False (2 edits)
        ("a", "a"),          # False (0 edits)
        ("", "a"),           # True (insert 'a')
        ("cad", "ab"),       # False (2 edits)
    ]

    for a, b in test_cases:
        print(one_edit_apart(a, b))
