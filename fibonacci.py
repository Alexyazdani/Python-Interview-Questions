r'''
Alex Yazdani
21 November 2024

fibonacci.py
Return the nth term of the fibonacci sequence, recursively and non-recursively.
'''

def fibonacci(n):
    if n < 2:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_recursive(n):
    if n < 2:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
        