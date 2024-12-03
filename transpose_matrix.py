r'''
Alex Yazdani
2 December 2024

transpose_matrix.py
Transpose a Matrix
'''

def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

if __name__ == "__main__":
    print(transpose_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(transpose_matrix([[1, 2], [3, 4]]))
    print(transpose_matrix([[1]]))