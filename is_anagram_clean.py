r'''
Alex Yazdani
29 June 2024

is_anagram_clean.py
Return True if two string are anagrams, ignoring non-alphanumeric characters.
Like is_anagram.py but ignores all non-alphanumeric characters.
'''

def is_anagram_clean(str1, str2):
    str1_clean = "".join(c.lower() for c in str1 if c.isalnum())
    str2_clean = "".join(c.lower() for c in str2 if c.isalnum())
    return (sorted(str1_clean) == sorted(str2_clean))

if __name__ == "__main__":
    test_cases = [
        ("listen", "silent"),                # True
        ("triangle", "integral"),            # True
        ("Listen", "Silent"),                # True
        ("Dormitory", "dirty room"),         # True
        ("The eyes", "They see"),            # True
        ("Astronomer", "Moon starer"),       # True
        ("hello", "world"),                  # False
        ("aabb", "ab"),                      # False
        ("abc!", "cba"),                     # True
        ("a-b-c", "c!b@a"),                  # True
        ("123!", "321"),                     # True
        ("rat#", "tar$"),                    # True
        ("hello!", "o!lleh"),                # True
        ("not?same", "same...not"),          # True
    ]

    for a, b in test_cases:
        print(is_anagram_clean(a, b))
