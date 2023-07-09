def countOccurrencesOfKInSortedMatrix(matrix, r, c, k):
    countK = 0
    i = 0
    j = c - 1
    while j >= 0 and i < r:
        if matrix[i][j] == k:
            countK += 1
            i += 1
        elif matrix[i][j] > k:
            j -= 1
        else:
            i += 1

    return countK


arr = [[-4, -3, -1, 3, 5], [-3, -2, 2, 4, 6], [-1, 1, 3, 5, 8], [3, 4, 7, 8, 9]]
print(countOccurrencesOfKInSortedMatrix(arr, len(arr), len(arr[0]), 3))
