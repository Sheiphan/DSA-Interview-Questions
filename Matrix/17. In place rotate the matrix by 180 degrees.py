def rotate180(matrix, r, c):
    assert r == c
    for i in range(r // 2):
        for j in range(r):
            matrix[i][j], matrix[r - i - 1][r - j - 1] = matrix[r - i - 1][r - j - 1], matrix[i][j]
    # Edge case when old, if r % 2 == 1
    if r % 2 == 1:  # reverse the middle segment
        for i in range(r // 2):
            matrix[r // 2][i], matrix[r // 2][r - i - 1] = matrix[r // 2][r - i - 1], matrix[r // 2][i]

    return matrix


arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]

print(rotate180(arr, len(arr), len(arr[0])))


# [[16, 15, 14, 13],
#  [12, 11, 10, 9],
#  [8, 7, 6, 5],
#  [4, 3, 2, 1]]