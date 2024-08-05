def shiftMatrixbyOne(matrix, n: int):

    top, left, bottom, right = 0, 0, n - 1, n - 1
    direction = 0
    prev = matrix[0][0]

    while top <= bottom and left <= right:
        if direction == 0:
            for i in range(left, right + 1):
                temp = matrix[left][i]
                matrix[left][i] = prev
                prev = temp
            top += 1

        elif direction == 1:
            for i in range(top, bottom + 1):
                temp = matrix[i][right]
                matrix[i][right] = prev
                prev = temp
            right -= 1

        elif direction == 2:
            for i in range(right, left - 1, -1):
                temp = matrix[bottom][i]
                matrix[bottom][i] = prev
                prev = temp
            bottom -= 1

        else:
            for i in range(bottom, top - 1, -1):
                temp = matrix[i][left]
                matrix[i][left] = prev
                prev = temp
            left += 1

        direction = (direction + 1) % 4

    matrix[0][0] = prev

    return matrix

arr = [[1,  2,  3,  4], #top = 0
       [5,  6,  7,  8],
       [9,  10, 11, 12],
       [13, 14, 15, 16]] #bottom = len(arr)
    #left=0        #right = len(arr)

n = len(arr)
print(shiftMatrixbyOne(arr, n))

# [[10, 1, 2, 3],
#  [9, 5, 6, 4],
#  [13, 11, 7, 8],
#  [14, 15, 16, 12]]