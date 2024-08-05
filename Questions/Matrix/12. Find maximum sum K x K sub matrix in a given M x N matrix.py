def maxSumOfKSubMatrix(matrix, r, c, k):
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

    maxSum = float("-inf")
    print(prefixSumMatrix)
    for r2 in range(k-1, r):
        for c2 in range(k-1, c):
            r1 = r2 - k + 1
            c1 = c2 - k + 1
            subMatrixSum = 0
            subMatrixSum += prefixSumMatrix[r2][c2]
            if c1 > 0: subMatrixSum -= prefixSumMatrix[r2][c1 - 1]
            if r1 > 0: subMatrixSum -= prefixSumMatrix[r1 - 1][c2]
            if r1 > 0 and c1 > 0:
                subMatrixSum += prefixSumMatrix[r1 - 1][c1 - 1]
            maxSum = max(maxSum, subMatrixSum)
    return maxSum


arr = [[-5, 4, 3, -10, 6],
       [10, -100, -20, -50, -30],
       [15, 100, 100, 50, 20],
       [-10, -3, 100, 30, -50],
       [3, 80, 20, 100, -200],
       [1, 1, 6, 10, 100]]

print(maxSumOfKSubMatrix(arr, len(arr), len(arr[0]), 3))

# [[-5, -1, 2, -8, -2], [5, -91, -108, -168, -192], [20, 24, 107, 97, 93], [10, 11, 194, 214, 160], [13, 94, 297, 417, 163], [14, 96, 305, 435, 281]]
# 577