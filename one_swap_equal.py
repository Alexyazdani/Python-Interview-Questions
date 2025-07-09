r'''
Alex Yazdani
9 July 2025

one_swap_equal.py
Write a function that checks whether two strings are one swap away from being equal.
    Strings must be the same length.
    Return True if they are one swap away (or already equal), else False.
'''


def one_swap_equal(a,b):
    if a == b:
        return True
    elif len(a) != len(b):
        return False
    else:
        diff = [(x,y) for (x,y) in zip(a,b) if x != y]
        if len(diff) != 2:
            return False
        x1, y1 = diff[0]
        x2, y2 = diff[1]
        return x1 == y2 and x2 == y1

if __name__ == "__main__":
    test_cases = [
        ("converse", "conserve"),    # True (swap 'r' and 'v')
        ("abcd", "abdc"),            # True (swap 'c' and 'd')
        ("abcd", "abcd"),            # True (already equal)
        ("abcd", "abcc"),            # False
        ("aabb", "bbaa"),            # False
        ("ab", "ba"),                # True
        ("abc", "def"),              # False
    ]

    for a, b in test_cases:
        print(one_swap_equal(a, b))
