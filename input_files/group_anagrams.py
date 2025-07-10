r'''
Alex Yazdani
10 July 2025

group_anagrams.py
Write a function called group_anagrams(words) that takes a list of strings and groups them into lists of anagrams.
    Two words are anagrams if they contain the same letters in different orders.
    Return the groups as a list of lists. The order of groups and words within each group does not matter.
'''


def group_anagrams(lis):
    anagrams_dict = {}
    anagrams = []
    for item in lis:
        sorted_item = "".join(sorted(item))
        if sorted_item in anagrams_dict:
            anagrams_dict[sorted_item].append(item)
        else:
            anagrams_dict[sorted_item] = [item]
    for item in anagrams_dict:
        anagrams.append(anagrams_dict[item])
    return anagrams



if __name__ == "__main__":
    test_input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(test_input)
    
    sorted_result = [sorted(group) for group in result]
    sorted_result.sort()
    
    expected = [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    expected = [sorted(group) for group in expected]
    expected.sort()
    
    print("PASS" if sorted_result == expected else "FAIL")
    print("Output:", result)
