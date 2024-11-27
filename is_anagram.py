r'''
Alex Yazdani
27 November 2024

is_anagram.py
Return True if two string are anagrams, ignoring spaces and capitalization.
'''

def is_anagram(str1, str2):
    return (sorted(str1.lower().replace(" ", "")) == sorted(str2.lower().replace(" ", "")))

if __name__ == "__main__":
    print(is_anagram("silent", "listen"))                   # True
    print(is_anagram("Hello", "Olelh"))                     # True (Tests Capitalization)
    print(is_anagram("Test", "Best"))                       # False
    print(is_anagram("Debit Card", "Bad Credit"))           # True
    print(is_anagram("Astronomer", "Moon Starer"))          # True
    print(is_anagram("Slot Machines", "Cash Lost in me"))   # True (Tests Extra Spaces)
    print(is_anagram("Python", "Java"))                     # False