r'''
Alex Yazdani
21 November 2024

unit_testing.py
Sample code for using unittest module, along with fibonacci.py
'''

import unittest
from fibonacci import fibonacci, fibonacci_recursive

class TestFibonacciFunctions(unittest.TestCase):
    def test_fibonacci_iterative(self):
        self.assertEqual(fibonacci(0), 0)               # Test base case
        self.assertEqual(fibonacci(5), 5)               # Test 5th Fibonacci number
        self.assertEqual(fibonacci(10), 55)             # Test 10th Fibonacci number
    
    def test_fibonacci_recursive(self):
        self.assertEqual(fibonacci_recursive(0), 0)     # Test base case
        self.assertEqual(fibonacci_recursive(5), 5)     # Test 5th Fibonacci number
        self.assertEqual(fibonacci_recursive(10), 55)   # Test 10th Fibonacci number

if __name__ == "__main__":
    unittest.main()
