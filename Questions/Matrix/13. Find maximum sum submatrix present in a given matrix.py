def maximumSumSubMatrix(matrix, r, c):
    prefixSumMatrix = [[0 for i in range(c)] for j in range(r)]
    prefixSumMatrix[0][0] = matrix[0][0]

    for i in range(1, c):
        prefixSumMatrix[0][i] = matrix[0][i] + prefixSumMatrix[0][i - 1]
    for i in range(1, r):
        prefixSumMatrix[i][0] = matrix[i][0] + prefixSumMatrix[i - 1][0]

    for i in range(1, r):
        for j in range(1, c):
            prefixSumMatrix[i][j] = matrix[i][j] + prefixSumMatrix[i - 1][j] + \
                                    prefixSumMatrix[i][j - 1] - prefixSumMatrix[i - 1][j - 1]
    maxSum = float("-inf")
    for r2 in range(r):
        for r1 in range(r2, r):
            for c2 in range(c):
                for c1 in range(c2, c):
                    subMatrixSum = 0
                    subMatrixSum += prefixSumMatrix[r2][c2]
                    if c1 > 0: subMatrixSum -= prefixSumMatrix[r2][c1 - 1]
                    if r1 > 0: subMatrixSum -= prefixSumMatrix[r1 - 1][c2]
                    if r1 > 0 and c1 > 0:
                        subMatrixSum += prefixSumMatrix[r1 - 1][c1 - 1]
                    maxSum = max(maxSum, subMatrixSum)
    return maxSum


arr = [[-5, -3, -2, 100],
       [10, 11, -5, 5],
       [100, 200, -500, 30],
       [-50, -20, -10, -11],
       [1, 2, 3, 4]]
print(maximumSumSubMatrix(arr, len(arr), len(arr[0])))
