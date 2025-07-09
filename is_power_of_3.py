r'''
Alex Yazdani
9 July 2025

is_power_of_3.py
Write a function that determines whether a given integer is a power of 3.
    Input is a non-negative integer.
    Return True if it is a power of 3 (i.e. 1, 3, 9, 27, ...), otherwise False.
    1 is considered a power of 3 (3⁰ = 1).
'''


def is_power_of_3(itg):
    if itg == 0:
        return False
    while itg % 3 == 0:
        itg = itg // 3
    return itg == 1


if __name__ == "__main__":
    test_cases = [
        1,        # True
        3,        # True
        9,        # True
        27,       # True
        0,        # False
        45,       # False
        81,       # True
        10,       # False
        243,      # True
        59049,    # True
        59048     # False
    ]
    for n in test_cases:
        print(is_power_of_3(n))
