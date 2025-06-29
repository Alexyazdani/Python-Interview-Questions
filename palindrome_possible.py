r'''
Alex Yazdani
28 June 2025

palindrome_possible.py
Write a function that takes a string and returns True if it can be rearranged into a palindrome, otherwise False.
'''


def palindrome_possible(s):
    cleaned_s = "".join(c.lower() for c in s if c.isalnum())
    chars = {}
    odd_count = 0
    for c in cleaned_s:
        chars[c] = chars.get(c,0)+1
    for c in chars:
        if chars[c]%2 == 1:
            odd_count+=1
    return (odd_count <= 1)


if __name__ == "__main__":
    test_cases = [
        "civic",                        # True
        "ivicc",                        # True
        "civil",                        # False
        "livci",                        # False
        "A man a plan",                 # False
        "Rats live on no evil star",    # True
        "hello",                        # False
        "racecar",                      # True
        "",                             # True
    ]

    for s in test_cases:
        print(palindrome_possible(s))
