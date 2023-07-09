def sumAllElementInSubMatrix(matrix, r, c, topLeft, bottomRight):
    prefixSumMatrix = [[0 for i in range(c)] for j in range(r)]
    # Entire first row
    prefixSumMatrix[0][0] = matrix[0][0]
    for i in range(1, c):
        prefixSumMatrix[0][i] = matrix[0][i] + prefixSumMatrix[0][i - 1]

    # Entire first column
    for i in range(1, r):
        prefixSumMatrix[i][0] = matrix[i][0] + prefixSumMatrix[i - 1][0]

    for i in range(1, r):
        for j in range(1, c):
            prefixSumMatrix[i][j] = matrix[i][j] + prefixSumMatrix[i - 1][j] + \
                                    prefixSumMatrix[i][j - 1] - prefixSumMatrix[i - 1][j - 1]
    print(prefixSumMatrix)

    # topLeft = (2, 1)
    # bottomRight = (3, 3)

    r1, c1 = topLeft
    r2, c2 = bottomRight

    subMatrixSum = 0
    subMatrixSum += prefixSumMatrix[r2][c2]
    if c1 > 0: subMatrixSum -= prefixSumMatrix[r2][c1 - 1]
    if r1 > 0: subMatrixSum -= prefixSumMatrix[r1 - 1][c2]
    if r1 > 0 and c1 > 0:
        subMatrixSum += prefixSumMatrix[r1 - 1][c1 - 1]

    return subMatrixSum


arr = [[3, 5, 2, 1],
       [3, 1, 1, 0],
       [5, 2, 3, 6],
       [1, 4, 4, 3]]

topLeft = (2, 1)
bottomRight = (3, 3)

print(sumAllElementInSubMatrix(arr, len(arr), len(arr[0]), topLeft, bottomRight))

# [[3, 8, 10, 11], [6, 12, 15, 16], [11, 19, 25, 32], [12, 24, 34, 44]]
# 22
