r'''
Alex Yazdani
28 June 2025

palindrome_clean.py
Write a function that returns True if the input string is a valid palindrome, ignoring all non-alphanumeric characters and case. Return False otherwise.
Similar to palindrom.py but ignores punctuation and spaces.
'''


def palindrome_clean(s):
    cleaned_s = ''.join(c.lower() for c in s if c.isalnum())
    return (cleaned_s == cleaned_s[::-1])

if __name__ == "__main__":
    test_cases = [
        "A man, a plan, a canal: Panama",     # True
        "racecar",                            # True
        "hello",                              # False
        "Was it a car or a cat I saw?",       # True
        "No 'x' in Nixon",                    # True
        "",                                   # True
        "12321",                              # True
        "123abccba321",                       # True
        "1a2"                                 # False
    ]

    for s in test_cases:
        print(palindrome_clean(s))


