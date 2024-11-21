def panindrome(s):
    return (s[::-1] == s)

if __name__ == "__main__":
    print(panindrome("tacocat"))
    print(panindrome("racecar"))
    print(panindrome("hello"))