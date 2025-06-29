r'''
Alex Yazdani
29 June 2024

parens_balanced.py
Write a function that returns True if a string contains balanced parentheses, and False otherwise.
'''

def parens_balanced(str):
    balance = 0
    for c in str:
        if c == "(": balance += 1
        elif c == ")": balance -= 1
        if (balance < 0): return False
    return (balance == 0)

if __name__ == "__main__":
    test_cases = [
        "(a + b) * (c + d)",        # True
        "((())())",                 # True
        "(()",                      # False
        "())(",                     # False
        "",                         # True
        "())",                      # False
        "(()(()))",                 # True
        "abc(def(ghi))",            # True
    ]

    for s in test_cases:
        print(parens_balanced(s))
