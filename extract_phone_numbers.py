r'''
Alex Yazdani
11 July 2025

extract_phone_numbers.py
Write a function extract_phone_numbers(text: str) -> list[str] that extracts all valid US phone numbers from a string. The valid formats are:
    (XXX) XXX-XXXX
    XXX-XXX-XXXX
    XXX.XXX.XXXX
    XXX XXX XXXX

    Where X is a digit (0–9), and:
    Area code cannot start with 0 or 1
    Prefix (second group) cannot start with 0 or 1
Return a list of all valid phone numbers in the order they appear.
'''

import re

def extract_phone_numbers(text: str) -> list[str]:
    numbers = re.findall(r'(?:[2-9]\d{2}(?:-|\.|\s)[2-9]\d{2}(?:-|\.|\s)\d{4}|\([2-9]\d{2}\)\s[2-9]\d{2}-\d{4})', text)
    return numbers

if __name__ == "__main__":
    print(extract_phone_numbers("Call me at (415) 555-1234 or 212-456-7890."))  
    # Expected: ['(415) 555-1234', '212-456-7890']

    print(extract_phone_numbers("Invalid: (015) 123-4567, 123-012-3456, 911.456.7890"))  
    # Expected: ['911.456.7890']

    print(extract_phone_numbers("Also valid: 415.555.1234 or 212 456 7890."))  
    # Expected: ['415.555.1234', '212 456 7890']
