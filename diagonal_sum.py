r'''
Alex Yazdani
2 December 2024

diagonal_sum.py
Calculate the sum of the diagonals in a square matrix. 
Only includes each element once even if it's shared by both diagonals (which occurs in the center of the matrix if it has an odd size).
'''

def diagonal_sum(matrix):
    sum = 0
    width = len(matrix[0])
    for i in range(width):
        sum += matrix[i][i]
        if (width-1-i) != i:
            sum += matrix[width-1-i][i]
    return sum

if __name__ == "__main__":
    print(diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # Output 25
    print(diagonal_sum([[1, 2], [3, 4]]))                   # Output 10
    print(diagonal_sum([[1]]))                              # Output 1
