def countNegativeElementInSortedMatrix(matrix, r, c):
    negativeCount = 0
    # for i in range(r):
    #     for j in range(c):
    #         if matrix[i][j] == 0:
    #             negativeCount += 1
    i = 0
    j = c - 1
    while j >= 0:
        if matrix[i][j] >= 0:
            j -= 1
        else:
            i += 1
            negativeCount += j + 1

    return negativeCount


arr = [[-7, -3, -1, 3, 5], [-3, -2, 2, 4, 6], [-1, 1, 3, 5, 8], [3, 4, 7, 8, 9]]
print(countNegativeElementInSortedMatrix(arr, len(arr), len(arr[0])))
