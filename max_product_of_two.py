r'''
Alex Yazdani
28 June 2025

max_product_of_two.py
Write a function that takes a list of integers and returns the maximum product of any two distinct elements in the list.
'''


def max_product_of_two(lis):
    if len(lis) < 2:
        return None
    start = 1
    max = lis[0] * lis[1]
    for val1 in lis:
        for val2 in lis[start:]:
            prod = val1*val2
            if prod > max:
                max = prod
        start+=1
    return max


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4],          # 12 (3 * 4)
        [-10, -20, 1, 2],      # 200 (-10 * -20)
        [0, 5, 0],             # 0
        [-1, -2, -3],          # 6 (-2 * -3)
        [5, 5, 5],             # 25 (5 * 5)
        [-1000, 1000],         # -1000000
    ]

    for nums in test_cases:
        print(max_product_of_two(nums))
