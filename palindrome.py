r'''
Alex Yazdani
21 November 2024

palindrome.py
Return True if input string is a palindrome.
'''

def palindrome(s):
    return (s[::-1] == s)

if __name__ == "__main__":
    print(palindrome("tacocat"))
    print(palindrome("racecar"))
    print(palindrome("hello"))