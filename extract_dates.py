r'''
Alex Yazdani
11 July 2025

extract_dates.py
Write a function extract_dates(text: str) -> list[str] that extracts all valid dates in the format DD/MM/YYYY from a given string.
A valid date must match the following:
    Day: 01–31
    Month: 01–12
    Year: any 4-digit number (e.g., 1900–2099)
    Leading zeros are required (e.g., 3/7/2024 is not valid, but 03/07/2024 is).
The function should return a list of matching date strings in the order they appear.
'''

import re

def extract_dates(text: str) -> list[str]:
    dates = re.findall(r'(?:0[1-9]|1[0-9]|2[0-9]|3[0-1])/(?:0[1-9]|1[0-2])/\d{4}', text)
    return dates


if __name__ == "__main__":
    print(extract_dates("Today's date is 03/07/2024."))  # Expected: ['03/07/2024']
    print(extract_dates("Dates: 01/01/2000, 15/12/1999, and 31/04/2021."))  # Expected: ['01/01/2000', '15/12/1999', '31/04/2021']
    print(extract_dates("Bad: 3/07/2024, 15/13/2020, 00/10/2020."))  # Expected: []
    print(extract_dates("Mixed: 28/02/2020, 31/06/2020, 30/11/2099."))  # Expected: ['28/02/2020', '31/06/2020', '30/11/2099']
