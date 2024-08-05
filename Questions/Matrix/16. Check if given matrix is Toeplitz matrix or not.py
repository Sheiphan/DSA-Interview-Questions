def checkMatrixIsToeplitz(matrix, r, c):
    for i in range(r-1):
        for j in range(c-1):
            if matrix[i][j] != matrix[i + 1][j + 1]:
                return False
    return True


arr = [[5, 2, 1, 9, 10],
       [3, 5, 2, 1, 9],
       [6, 3, 5, 2, 1],
       [7, 6, 3, 5, 2],
       [8, 7, 6, 3, 5]]

print(checkMatrixIsToeplitz(arr, len(arr), len(arr[0])))

# True