r'''
Alex Yazdani
29 November 2024

merge_sorted_lists.py
Merge 2 sorted lists
'''

# # This version has worse time complexity but is simple: O((n+m)log(n+m))
# def merge_sorted_lists(l1, l2):
#     return(sorted(l1+l2))

# This version has time complexity: O(n+m)
def merge_sorted_lists(l1, l2):
    # Initialize pointers for both lists
    i, j = 0, 0
    merged_list = []
    # Traverse both lists and append smaller element from either list
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            merged_list.append(l1[i])
            i += 1
        else:
            merged_list.append(l2[j])
            j += 1
    # If l1 has leftovers
    while i < len(l1):
        merged_list.append(l1[i])
        i += 1
    # If l2 has leftovers
    while j < len(l2):
        merged_list.append(l2[j])
        j += 1
    return merged_list


if __name__ == "__main__":
    print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))          # Output: [1, 2, 3, 4, 5, 6]
    print(merge_sorted_lists([0, 10, 20], [15, 25, 30]))     # Output: [0, 10, 15, 20, 25, 30]
    print(merge_sorted_lists([i for i in range(0, 100, 3)], [i for i in range(0, 100, 5)]))
