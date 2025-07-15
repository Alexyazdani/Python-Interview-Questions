r'''
Alex Yazdani
15 July 2025

reverse_words.py
Write a function reverse_words(sentence: str) -> str that takes a string containing words separated by spaces and returns a new string with the word order reversed.
    Words are separated by a single space
    There are no leading/trailing spaces
'''


def reverse_words(sentence: str) -> str:
    # return " ".join(sentence.split()[::-1])   # Too obvious
    words = sentence.split()
    n = len(words)
    for i in range(n // 2):
        words[i], words[n - 1 - i] = words[n - 1 - i], words[i]
    return " ".join(words)

if __name__ == "__main__":
    print(reverse_words("the sky is blue"))     # Expected: "blue is sky the"
    print(reverse_words("hello world"))         # Expected: "world hello"
    print(reverse_words("a b c d"))             # Expected: "d c b a"
    print(reverse_words("word"))                # Expected: "word"
