r'''
Alex Yazdani
27 November 2024

find_duplicates.py
Returns all duplicate elements
'''

def find_duplicates(lis):
    element_count = {}
    output_list = []
    for i in lis:
        element_count[i] = element_count.get(i, 0) + 1
    for j in element_count:
        if element_count[j] >= 2:
            output_list.append(j)
    return output_list


if __name__ == "__main__":
    print(find_duplicates([1, 2, 3, 4, 5, 3, 2, 1]))  # Output: [1, 2, 3]
    print(find_duplicates([10, 20, 20, 30, 40, 50, 30, 10]))  # Output: [10, 20, 30]
    print(find_duplicates([1, 2, 3, 4, 5]))  # Output: []
