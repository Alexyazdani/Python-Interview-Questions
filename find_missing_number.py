r'''
Alex Yazdani
22 November 2024

find_missing_number.py
Takes a list of integers from 1 to n with one number missing and returns the missing number.
The list will contain n-1 integers.
'''

def find_missing_number(lis):
    for i in range(1, len(lis)):
        if ((lis[i] - lis[i-1]) > 1):
            return (lis[i-1] + 1)
    return None

if __name__ == "__main__":
    print(find_missing_number([1,2,3,5]))          # 4   
    print(find_missing_number([1,2,3,4,5,6,8,9]))  # 7
    print(find_missing_number([1,2,3,4,5,6,7,9]))  # 8