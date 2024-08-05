def rotateBy90Degree(matrix, r, c):
    # Transpose the matrix
    for i in range(r):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]

    # Swap the 1st col element with the last col elements
    # swap the jth col element with (c-j-1)th col from end
    for i in range(r):
        for j in range(r//2):
            matrix[i][j], matrix[i][c-j-1] = matrix[i][c-j-1], matrix[i][j]

    return matrix


arr = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,16,]]

print(rotateBy90Degree(arr, len(arr), len(arr[0])))

# [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]

